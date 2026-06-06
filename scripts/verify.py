#!/usr/bin/env python3
"""Lightweight portfolio verification for repository structure and public metadata."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["README.md"]
STALE_TERMS = [
    "data-analytics-stuff",
    "Sales-Forecasting-Using-PyCaret",
    "Superstore-Dashboard",
    "AdventureWorks-Dashboard",
    "agentic-portfolio-site",
    "web tools",
    "practical web tools",
]
TEXT_EXTS = {".md", ".html", ".js", ".json", ".txt", ".yml", ".yaml"}
SKIP = {Path("scripts/verify.py")}

def text_files():
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if rel in SKIP or ".git" in path.parts or not path.is_file() or path.suffix.lower() not in TEXT_EXTS:
            continue
        yield path

def main() -> int:
    missing = [name for name in REQUIRED if not (ROOT / name).exists()]
    stale = []
    for path in text_files():
        text = path.read_text(errors="ignore")
        for term in STALE_TERMS:
            if term.lower() in text.lower():
                stale.append(f"{path.relative_to(ROOT)}: {term}")
    if missing or stale:
        for item in missing:
            print(f"missing_required={item}")
        for item in stale:
            print(f"stale_term={item}")
        return 1
    print(f"verify_ok project={ROOT.name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
