#!/usr/bin/env python3
"""Dependency-free structural validator for the himcm-o-paper skill package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "agents/openai.yaml",
    ".github/workflows/validate.yml",
    "references/contest-and-problem-contracts.md",
    "references/workflow.md",
    "references/model-selection-and-families.md",
    "references/model-cards-and-provenance.md",
    "references/statistical-integrity.md",
    "references/verification-and-uncertainty.md",
    "references/failure-atlas.md",
    "references/writing-latex-and-pdf.md",
    "references/audit-and-repair.md",
    "references/outstanding-ready-standard.md",
    "templates/contest_profile.schema.json",
    "templates/input_manifest.schema.json",
    "templates/problem_analysis.schema.json",
    "templates/model_card.schema.json",
    "templates/source_ledger.schema.json",
    "templates/result_contract.schema.json",
    "templates/claim_ledger.schema.json",
    "templates/run_manifest.schema.json",
    "templates/final_handoff.md",
    "templates/UNIVERSAL_PROMPT.md",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate(root: Path) -> dict[str, object]:
    errors: list[str] = []
    checked = 0

    for relative in REQUIRED:
        checked += 1
        target = root / relative
        if not target.is_file() or target.stat().st_size == 0:
            fail(errors, f"missing or empty required file: {relative}")

    skill = root / "SKILL.md"
    text = skill.read_text(encoding="utf-8") if skill.is_file() else ""
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    checked += 1
    if not match:
        fail(errors, "SKILL.md has no valid YAML frontmatter fence")
    else:
        front = match.group(1)
        name_match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", front)
        description_match = re.search(r"(?m)^description:\s*(.+)$", front)
        if not name_match or name_match.group(1) != "himcm-o-paper":
            fail(errors, "frontmatter name must be himcm-o-paper")
        if not description_match or len(description_match.group(1).strip()) < 40:
            fail(errors, "frontmatter description is missing or nondiscriminating")

    for markdown in sorted(root.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        markdown_text = markdown.read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", markdown_text)
        for link in links:
            if "://" in link or link.startswith("#"):
                continue
            checked += 1
            target = (markdown.parent / link.split("#", 1)[0]).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                fail(errors, f"link escapes skill root in {markdown.relative_to(root)}: {link}")
                continue
            if not target.exists():
                fail(errors, f"broken local link in {markdown.relative_to(root)}: {link}")

    for schema in sorted((root / "templates").glob("*.schema.json")):
        checked += 1
        try:
            payload = json.loads(schema.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            fail(errors, f"invalid JSON schema {schema.name}: {exc}")
            continue
        if payload.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            fail(errors, f"schema draft missing or unexpected: {schema.name}")
        if payload.get("type") != "object":
            fail(errors, f"schema root must be an object: {schema.name}")

    for file in sorted(root.rglob("*")):
        if not file.is_file() or ".git" in file.parts:
            continue
        checked += 1
        if file.suffix.lower() in {".md", ".py", ".json", ".yaml", ".yml"}:
            content = file.read_text(encoding="utf-8")
            if re.search(r"(?im)^\s*\[?TODO(?::|\])", content):
                fail(errors, f"unfinished TODO in {file.relative_to(root)}")
            if re.search(r"(?i)C:\\Users\\[^\\]+", content):
                fail(errors, f"private absolute user path in {file.relative_to(root)}")

    status = "PASS" if not errors else "FAIL"
    return {"status": status, "files_scanned": sum(1 for p in root.rglob("*") if p.is_file()), "checks": checked, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = validate(Path(args.root).resolve())
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"{report['status']}: scanned {report['files_scanned']} files; ran {report['checks']} checks")
        for error in report["errors"]:
            print(f"- {error}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
