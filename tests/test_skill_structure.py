import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "SKILL.md",
            "agents/openai.yaml",
            "references/research-methodology.md",
            "references/evidence-policy.md",
            "templates/research-report-ko.md",
            "schemas/evidence.schema.json",
            "scripts/validate_sources.py",
            "scripts/verify_evidence.py",
            "scripts/migrate_evidence_v1_to_v2.py",
            "scripts/route_question.py",
            "docs/HUMAN_REVIEW_GUIDE.md",
            "docs/RESEARCH_QUALITY_AUDIT.md",
            "docs/OPEN_QUESTIONS.md",
            "docs/ANALYST_REVIEW.md",
            "docs/PHASE_7_TEST_PLAN.md",
            "docs/QUESTION_ROUTING.md",
            "docs/RESEARCH_FRAMEWORKS.md",
            "docs/RESPONSE_MODES.md",
            "docs/GENERAL_USER_GUIDE.md",
            "docs/MIGRATION_KDAPI_TO_KDARI.md",
            "docs/PROJECT_STATUS_2026-11.md",
            "docs/PHASE_7.md",
            ".github/workflows/ci.yml",
        ]
        for relative in required:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_skill_frontmatter(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: k-digital-asset-research-intelligence", text)
        self.assertNotIn("TODO", text)

    def test_schemas_are_json(self):
        for path in (ROOT / "schemas").glob("*.json"):
            with self.subTest(path=path.name):
                self.assertIsInstance(json.loads(path.read_text(encoding="utf-8")), dict)


if __name__ == "__main__":
    unittest.main()

