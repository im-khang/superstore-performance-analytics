# Superstore Performance Analytics

Retail performance analysis dashboard focused on sales, profit, category, product, market, and regional insights.

## Business question

What decision can this analysis or workflow support, and what evidence should a reviewer inspect first?

## Data source

Superstore BI report artifacts and screenshots from original repo.

## Repository structure

```text
README.md
LICENSE
.gitignore
requirements.txt
data/
  raw/          # source/sample input files or local-only raw data
  interim/      # local-only transformed working files
  processed/    # local-only generated datasets
notebooks/      # ordered analysis notebooks/scripts
src/            # reusable project code
dashboard/      # BI/dashboard files or dashboard export code
docs/           # documentation and evaluation notes
reports/        # human-readable findings and figures
references/     # source notes, papers, dictionaries, original materials
scripts/        # verification or utility scripts
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run / verify

1. `python scripts/verify.py`

## Public outputs

- Dashboard or BI artifact: `dashboard/`
- Findings and evidence notes: `reports/`
- Evaluation notes: `docs/`
- Supporting references: `references/`

## Data and security policy

- Credentials, environment files, local raw data, generated working data, databases, archives, and scratch outputs are ignored by `.gitignore`.
- Public repo keeps only shareable code, sample-safe artifacts, documentation, dashboard files, and evidence summaries.
- Claims should stay bounded by available data and documented assumptions.
