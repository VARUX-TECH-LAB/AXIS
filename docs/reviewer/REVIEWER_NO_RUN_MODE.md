# AXIS No-Run Review Mode

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

No-run review is the default public path for this repository.

Review:

- `PUBLIC_DEMO_NOTICE.md`
- `demo/REVIEWER_START_HERE.md`
- `demo/pre-generated-evidence/pilot-v1/evidence-summary.md`
- `demo/pre-generated-evidence/pilot-v1/selected-responses/`
- `demo/pre-generated-evidence/pilot-v1/selected-audit-events/`
- `docs/reviewer/AXIS_CLAIMS_MATRIX.md`
- `docs/reviewer/AXIS_ANTI_CLAIMS.md`

Optional consistency check:

```powershell
python scripts\verify_pilot_evidence.py
```

This public path does not run AXIS and does not expose withheld implementation details.
