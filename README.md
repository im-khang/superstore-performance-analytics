# Superstore Performance Analytics

Which category, product, market, and profit patterns should retail stakeholders inspect first from a Superstore dashboard?

## Business question

Which category, product, market, and profit patterns should retail stakeholders inspect first from a Superstore dashboard?

## Reviewer guide

1. `dashboard/Superstore Report.pbit` — Power BI template artifact.
2. `reports/figures/Overview.png` — executive overview screenshot.
3. `reports/figures/MarketAnalysis.png` — market analysis screenshot.
4. `reports/figures/ProductAnalysis.png` — product analysis screenshot.
5. `docs/evaluation.md` and `reports/results.md` — verification notes.

## Data source

Superstore sample/reporting artifacts. No private business data is tracked.

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

```bash
python3 scripts/verify.py
```

## Public outputs

- Dashboard or public artifact: `Power BI template and exported dashboard screenshots.`
- Findings and evidence notes: `reports/`
- Evaluation notes: `docs/`
- Supporting references: `references/`

## Claim boundary

This repo demonstrates retail BI structure and dashboard evidence from sample artifacts. It does not claim production deployment, live data connection, or measured business impact.

## Data and security policy

- Credentials, environment files, local raw data, generated working data, databases, archives, and scratch outputs are ignored by `.gitignore`.
- Public repo keeps only shareable code, sample-safe artifacts, documentation, dashboard files, and evidence summaries.
- Claims stay bounded by available data and documented assumptions.
