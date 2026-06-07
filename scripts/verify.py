#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['README.md', 'LICENSE', '.gitignore', 'requirements.txt', 'data/raw/.gitkeep', 'data/interim/.gitkeep', 'data/processed/.gitkeep', 'docs', 'reports', 'references', 'dashboard', 'dashboard/Superstore Report.pbit', 'reports/figures/Overview.png', 'reports/figures/MarketAnalysis.png', 'reports/figures/ProductAnalysis.png', 'reports/CASE_RESULT.md', 'data/README.md']


def fail(msg: str) -> int:
    print(f"verify_failed project=superstore-performance-analytics reason={msg}")
    return 1


def main() -> int:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            return fail(f"missing:{rel}")
    readme = (ROOT / "README.md").read_text(errors="ignore")
    if "Reviewer guide" not in readme or "Claim boundary" not in readme:
        return fail("readme_missing_reviewer_or_claim_boundary")
    if "What decision can this analysis" in readme:
        return fail("generic_readme_placeholder")
    gitignore = (ROOT / ".gitignore").read_text(errors="ignore")
    for token in [".env", "secrets/", "credentials/", "data/raw/**", ".venv/"]:
        if token not in gitignore:
            return fail(f"gitignore_missing:{token}")
    data_dir = ROOT / "docs" / "assets" / "data"
    if data_dir.exists():
        for path in data_dir.glob("*.json"):
            try:
                json.loads(path.read_text())
            except Exception as exc:
                return fail(f"json_parse:{path.name}:{exc}")
    if "superstore-performance-analytics" == "olist-delivery-sla-risk-analytics":
        proc = subprocess.run([sys.executable, "notebooks/01_olist_delivery_risk_foundation.py"], cwd=ROOT, text=True, capture_output=True)
        if proc.returncode != 0:
            return fail("olist_notebook_setup_run_failed")
    print("verify_ok project=superstore-performance-analytics")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
