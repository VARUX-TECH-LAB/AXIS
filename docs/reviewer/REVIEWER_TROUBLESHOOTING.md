# AXIS Public Reviewer Troubleshooting

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

This public repository is source-redacted and does not include the runnable Docker demo, reviewer client, diagnostics collector, or setup scripts.

## Public Review Issues

If a link is missing:

- Start from [../../PUBLIC_DEMO_NOTICE.md](../../PUBLIC_DEMO_NOTICE.md).
- Inspect [../../demo/REVIEWER_START_HERE.md](../../demo/REVIEWER_START_HERE.md).
- Inspect [../../demo/pre-generated-evidence/README.md](../../demo/pre-generated-evidence/README.md).

If evidence verification fails:

- Run from the repository root: `python scripts\verify_pilot_evidence.py`.
- Confirm the repository was not partially downloaded.
- Confirm `demo/evidence/pilot-v1/` and `demo/pre-generated-evidence/` are present.

## Runnable Demo

The runnable demo is private. Request access from VARUX:

https://varuxcyber.com/
