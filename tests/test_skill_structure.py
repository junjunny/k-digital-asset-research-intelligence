import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTests(unittest.TestCase):
    SKILL_ROOT = ROOT / "skills" / "k-dari"

    def test_required_files_exist(self):
        required = [
            "skills/k-dari/SKILL.md",
            "skills/k-dari/agents/openai.yaml",
            "skills/k-dari/references/research-methodology.md",
            "skills/k-dari/references/evidence-policy.md",
            "skills/k-dari/references/question-routing.md",
            "skills/k-dari/references/research-frameworks.md",
            "skills/k-dari/templates/research-report-ko.md",
            "skills/k-dari/schemas/evidence.schema.json",
            "skills/k-dari/scripts/validate_sources.py",
            "skills/k-dari/scripts/verify_evidence.py",
            "skills/k-dari/scripts/migrate_evidence_v1_to_v2.py",
            "skills/k-dari/scripts/route_question.py",
            "docs/HUMAN_REVIEW_GUIDE.md",
            "docs/RESEARCH_QUALITY_AUDIT.md",
            "docs/OPEN_QUESTIONS.md",
            "docs/ANALYST_REVIEW.md",
            "docs/archive/PHASE_7_TEST_PLAN.md",
            "docs/archive/PHASE_7.md",
            "docs/AI_ASSISTED_REVIEW_REPORT.md",
            "docs/PROJECT_STATUS_2026-11.md",
            "docs/SECURITY_AUDIT.md",
            "docs/MIGRATION_KDAPI_TO_KDARI.md",
            ".github/workflows/ci.yml",
        ]
        for relative in required:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_skill_frontmatter(self):
        text = (self.SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: k-dari", text)
        self.assertNotIn("TODO", text)

    def test_repository_root_is_not_a_second_skill(self):
        self.assertFalse((ROOT / "SKILL.md").exists())

    def test_deployable_skill_excludes_project_only_artifacts(self):
        for relative in ("evaluations", "tests", "docs", "human_review_ui", "portfolio"):
            self.assertFalse((self.SKILL_ROOT / relative).exists(), relative)

        total_bytes = sum(
            path.stat().st_size for path in self.SKILL_ROOT.rglob("*") if path.is_file()
        )
        self.assertLess(total_bytes, 1_000_000)

    def test_skill_markdown_local_links_resolve(self):
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        missing = []
        for markdown in self.SKILL_ROOT.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for target in link_pattern.findall(text):
                clean = target.split("#", 1)[0]
                if not clean or "://" in clean or clean.startswith("mailto:"):
                    continue
                if not (markdown.parent / clean).resolve().exists():
                    missing.append(f"{markdown.relative_to(ROOT)} -> {target}")
        self.assertEqual(missing, [])

    def test_schemas_are_json(self):
        schema_dirs = [ROOT / "schemas", ROOT / "skills" / "k-dari" / "schemas"]
        for path in (path for directory in schema_dirs for path in directory.glob("*.json")):
            with self.subTest(path=path.name):
                self.assertIsInstance(json.loads(path.read_text(encoding="utf-8")), dict)


if __name__ == "__main__":
    unittest.main()

