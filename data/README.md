# Data Policy

## Source

Superstore sample/reporting artifacts. No private business data is tracked.

## Folder policy

- `raw/`: local-only raw files or explicitly public sample files.
- `interim/`: local-only working outputs.
- `processed/`: local-only generated datasets.

## Git policy

Raw/private data and generated outputs are ignored by `.gitignore`. Only `.gitkeep` placeholders or explicitly sample-safe files are tracked.

## Claim boundary

This repo demonstrates retail BI structure and dashboard evidence from sample artifacts. It does not claim production deployment, live data connection, or measured business impact.
