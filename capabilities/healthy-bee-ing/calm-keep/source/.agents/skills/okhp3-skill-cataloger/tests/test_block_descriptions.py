import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "gen-skills-readme.py"
spec = importlib.util.spec_from_file_location("gen_skills_readme_blocks", SCRIPT)
cataloger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cataloger)


class BlockDescriptionTests(unittest.TestCase):
    def test_block_markers_produce_catalog_description(self):
        for marker in (">", ">-", ">+", "|", "|-", "|+", ">- # summary"):
            with self.subTest(marker=marker), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                skill = root / "example"
                skill.mkdir()
                (skill / "SKILL.md").write_text(
                    f"---\nname: example\ndescription: {marker}\n"
                    "  First line of the description.\n"
                    "  Second line of the description.\n"
                    "metadata:\n  version: '1.0.0'\n  category: example\n---\n",
                    encoding="utf-8",
                )
                entries = cataloger.discover_skills(root, "project")
                self.assertEqual(entries[0]["description"],
                                 "First line of the description. Second line of the description.")
                self.assertEqual(cataloger.validate(entries)[0], [])
                self.assertIn(entries[0]["description"], cataloger._project_table(entries))

    def test_empty_block_description_fails_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "example"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: example\ndescription: >-\nmetadata:\n"
                "  version: '1.0.0'\n---\n", encoding="utf-8"
            )
            entries = cataloger.discover_skills(root, "project")
            errors, _ = cataloger.validate(entries)
            self.assertTrue(any("no description" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
