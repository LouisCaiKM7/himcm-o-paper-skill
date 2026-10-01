#!/usr/bin/env python3
"""Check the minimum evidence chain of a HiMCM paper project.

This gate verifies presence, parseability, non-empty coverage, and selected
cross-artifact identities. It does not prove mathematical validity.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_JSON = {
    "paper_output/contest_profile.json": ("contest", "year", "problem", "rules"),
    "paper_output/input_manifest.json": ("files",),
    "paper_output/problem_analysis.json": ("problem", "requirements"),
    "paper_output/data/source_ledger.json": ("entries",),
    "paper_output/plan/model_cards.json": ("models",),
    "paper_output/results/result_contract.json": ("run_id", "model_id", "status", "results", "checks"),
    "paper_output/results/claim_ledger.json": ("claims",),
    "paper_output/results/run_manifest.json": ("run_id", "model_versions", "outputs", "exit_code"),
}


def load_json(root: Path, relative: str, required: tuple[str, ...], errors: list[str]) -> dict:
    path = root / relative
    if not path.is_file():
        errors.append(f"missing: {relative}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"invalid JSON {relative}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root is not an object: {relative}")
        return {}
    for key in required:
        if key not in value:
            errors.append(f"missing key {key!r}: {relative}")
    return value


def validate(root: Path, require_pdf: bool = True) -> dict[str, object]:
    errors: list[str] = []
    reports = {name: load_json(root, name, keys, errors) for name, keys in REQUIRED_JSON.items()}

    profile = reports["paper_output/contest_profile.json"]
    if not profile.get("rules"):
        errors.append("contest_profile rules list is empty")

    manifest = reports["paper_output/input_manifest.json"]
    if not manifest.get("files"):
        errors.append("input_manifest files list is empty")

    sources = reports["paper_output/data/source_ledger.json"].get("entries", [])
    if not sources:
        errors.append("source_ledger entries list is empty")

    analysis = reports["paper_output/problem_analysis.json"]
    requirements = analysis.get("requirements", [])
    if not requirements:
        errors.append("problem_analysis requirements list is empty")
    else:
        missing_answers = [r.get("id", "<unnamed>") for r in requirements if r.get("status") == "ANSWERED" and not r.get("answer")]
        if missing_answers:
            errors.append(f"requirements marked ANSWERED without answer: {missing_answers}")
        unfinished = [r.get("id", "<unnamed>") for r in requirements if r.get("status") != "ANSWERED"]
        if unfinished:
            errors.append(f"requirements not in final ANSWERED state: {unfinished}")

    cards = reports["paper_output/plan/model_cards.json"].get("models", [])
    if not cards:
        errors.append("model_cards models list is empty")
    model_ids = {card.get("model_id") for card in cards if card.get("model_id")}

    result_contract = reports["paper_output/results/result_contract.json"]
    if not result_contract.get("results"):
        errors.append("result_contract results list is empty")
    if not result_contract.get("checks"):
        errors.append("result_contract checks list is empty")
    if result_contract.get("status") != "VALID":
        errors.append(f"result_contract status is not VALID: {result_contract.get('status')}")
    if result_contract.get("model_id") and result_contract.get("model_id") not in model_ids:
        errors.append(f"result_contract references unknown model ID: {result_contract.get('model_id')}")

    claims = reports["paper_output/results/claim_ledger.json"].get("claims", [])
    if not claims:
        errors.append("claim_ledger claims list is empty")
    unknown_models = sorted({c.get("model_id") for c in claims if c.get("model_id") and c.get("model_id") not in model_ids})
    if unknown_models:
        errors.append(f"claims reference unknown model IDs: {unknown_models}")
    claims_without_evidence = [c.get("claim_id", "<unnamed>") for c in claims if not c.get("evidence")]
    if claims_without_evidence:
        errors.append(f"claims lack evidence references: {claims_without_evidence}")
    claims_without_verification = [c.get("claim_id", "<unnamed>") for c in claims if not c.get("verification")]
    if claims_without_verification:
        errors.append(f"claims lack verification references: {claims_without_verification}")

    manifest_run = reports["paper_output/results/run_manifest.json"]
    if manifest_run.get("exit_code") not in (0, None):
        errors.append(f"official run exit_code is not zero: {manifest_run.get('exit_code')}")
    if not manifest_run.get("outputs"):
        errors.append("run_manifest outputs list is empty")

    tex_root = root / "paper_output" / "tex"
    tex_files = sorted(tex_root.rglob("*.tex")) if tex_root.is_dir() else []
    if not tex_files:
        errors.append("no LaTeX source files found under paper_output/tex")
    tex_text = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in tex_files)
    for token in ("TODO", "FIXME", "PLACEHOLDER"):
        if re.search(rf"(?i)\b{token}\b", tex_text):
            errors.append(f"forbidden placeholder token in LaTeX: {token}")
    if re.search(r"(?i)\.docx?\b|Microsoft Word", tex_text):
        errors.append("Word/DOCX dependency mentioned in LaTeX source")

    pdf = root / "paper_output" / "final_paper.pdf"
    if require_pdf and (not pdf.is_file() or pdf.stat().st_size < 8):
        errors.append("missing or empty paper_output/final_paper.pdf")

    result_files = sorted((root / "paper_output" / "results").glob("*.json")) if (root / "paper_output" / "results").is_dir() else []
    if len(result_files) < 2:
        errors.append("fewer than two JSON result/contract files were scanned")

    scanned = {
        "required_json": len(REQUIRED_JSON),
        "requirements": len(requirements),
        "source_entries": len(sources),
        "model_cards": len(cards),
        "results": len(result_contract.get("results", [])),
        "result_checks": len(result_contract.get("checks", [])),
        "claims": len(claims),
        "tex_files": len(tex_files),
        "result_json_files": len(result_files),
        "pdf_files": int(pdf.is_file()),
    }
    return {"status": "PASS" if not errors else "FAIL", "project": str(root), "scanned": scanned, "errors": errors, "limitations": ["This structural gate does not establish mathematical, statistical, causal, or semantic validity."]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    parser.add_argument("--no-pdf", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = validate(Path(args.project).resolve(), require_pdf=not args.no_pdf)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"{report['status']}: {report['scanned']}")
        for error in report["errors"]:
            print(f"- {error}")
        print(f"LIMITATION: {report['limitations'][0]}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
