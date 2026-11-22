import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "k-dari" / "scripts"))

from validate_report import validate_report  # noqa: E402


class StoredResearchArtifactTests(unittest.TestCase):
    """Validate committed artifacts; these tests do not execute a natural-language agent run."""

    def test_hong_kong_case_artifacts_are_structurally_valid(self):
        case_dir = ROOT / "examples/hong-kong-digital-green-bond"
        report = json.loads((case_dir / "report.json").read_text(encoding="utf-8"))
        errors, _ = validate_report(report, case_dir)
        self.assertEqual([], errors)
        self.assertNotIn("EIB", report["research_question"])
        self.assertTrue((case_dir / "report-ko.md").is_file())
        self.assertTrue((case_dir / "executive-summary-en.md").is_file())
        self.assertTrue((case_dir / "research-log.md").is_file())

    def test_all_new_case_sources_have_content_verification(self):
        path = ROOT / "examples/hong-kong-digital-green-bond/evidence.json"
        records = json.loads(path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(records), 6)
        self.assertTrue(all(item["verification"]["status"] == "CONTENT_VERIFIED" for item in records))
        self.assertTrue(all(item["verification"]["document_sha256"] for item in records))

    def test_reports_expose_unverified_limits(self):
        text = (ROOT / "examples/hong-kong-digital-green-bond/report-ko.md").read_text(encoding="utf-8")
        self.assertIn("한계", text)
        self.assertIn("입법예고", text)
        self.assertIn("추론", text)


if __name__ == "__main__":
    unittest.main()
