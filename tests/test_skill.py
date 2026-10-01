from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


check_skill = load_module("check_skill", ROOT / "scripts" / "check_skill.py")
check_project = load_module("check_project", ROOT / "scripts" / "check_project.py")


class SkillTests(unittest.TestCase):
    def test_real_skill_passes(self):
        report = check_skill.validate(ROOT)
        self.assertEqual(report["status"], "PASS", report["errors"])
        self.assertGreater(report["checks"], 20)

    def test_missing_reference_fails(self):
        original = list(check_skill.REQUIRED)
        try:
            check_skill.REQUIRED.append("references/known-missing-mutation.md")
            report = check_skill.validate(ROOT)
            self.assertEqual(report["status"], "FAIL")
            self.assertTrue(any("known-missing-mutation" in item for item in report["errors"]))
        finally:
            check_skill.REQUIRED[:] = original


class ProjectGateTests(unittest.TestCase):
    def test_valid_project_passes(self):
        report = check_project.validate(FIXTURES / "valid_project")
        self.assertEqual(report["status"], "PASS", report["errors"])
        self.assertEqual(report["scanned"]["requirements"], 1)

    def test_empty_claims_fail(self):
        report = check_project.validate(FIXTURES / "invalid_empty_claims")
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("claims list is empty" in item for item in report["errors"]))


if __name__ == "__main__":
    unittest.main()
