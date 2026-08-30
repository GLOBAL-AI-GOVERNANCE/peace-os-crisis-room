from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RealWorldEvaluationKitTests(unittest.TestCase):
    def test_kit_preserves_unmet_human_gates(self):
        text = (ROOT / "docs/REAL-WORLD-EVALUATION-KIT.md").read_text(encoding="utf-8")
        for boundary in (
            "HUMAN UAT = NOT YET EVIDENCED",
            "ACCESSIBILITY HUMAN TESTING = NOT YET EVIDENCED",
            "PILOT USE = NOT YET EVIDENCED",
            "Automated and synthetic checks are machine evidence only",
        ):
            self.assertIn(boundary, text)

    def test_public_entrypoint_links_kit(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/REAL-WORLD-EVALUATION-KIT.md", readme)


if __name__ == "__main__":
    unittest.main()
