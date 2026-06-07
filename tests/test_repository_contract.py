from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_standard_structure_exists():
    for rel in ["README.md", "LICENSE", ".gitignore", "requirements.txt", "data/raw", "data/interim", "data/processed", "notebooks", "src", "dashboard", "docs", "reports", "references"]:
        assert (ROOT / rel).exists(), rel


def test_readme_is_project_specific():
    text = (ROOT / "README.md").read_text(errors="ignore")
    assert "Reviewer guide" in text
    assert "Claim boundary" in text
    assert "What decision can this analysis" not in text


def test_gitignore_blocks_sensitive_and_local_data():
    text = (ROOT / ".gitignore").read_text(errors="ignore")
    for token in [".env", "secrets/", "credentials/", "data/raw/**", ".venv/"]:
        assert token in text


def test_case_result_exists():
    assert (ROOT / "reports" / "CASE_RESULT.md").exists()
