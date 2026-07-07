# AXIS Public Demo Workspace

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

This directory contains public demo-only and reviewer-facing assets. Runnable demo source code and containers are intentionally withheld from this public repository.

## Contents

- `REVIEWER_START_HERE.md` - Public no-run review entry point.
- `evidence/pilot-v1/` - Captured pilot evidence fixtures.
- `pre-generated-evidence/` - No-run reviewer evidence examples.
- `benchmark-results/` - Public benchmark output fixtures.
- `sample-business-app/` - Redaction placeholder for withheld sample app source.
- `reviewer/` - Redaction placeholder for withheld reviewer client source.

## Public Review

Inspect evidence:

```text
demo/pre-generated-evidence/pilot-v1/evidence-summary.md
demo/pre-generated-evidence/pilot-v1/selected-responses/
demo/pre-generated-evidence/pilot-v1/selected-audit-events/
demo/evidence/pilot-v1/limitations/
```

Optional consistency check from the repository root:

```powershell
python scripts\verify_pilot_evidence.py
```

## Runnable Demo

The runnable AXIS engine, Docker stacks, Control Plane, sample business application, and reviewer automation are not included in this public repository.

Request private access from VARUX:

https://varuxcyber.com/
