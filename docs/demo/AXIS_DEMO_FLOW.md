# AXIS Public Demo Flow

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

This public flow is evidence-only. Runtime commands, Docker stacks, source code, and deployment artifacts are intentionally withheld.

## Objective

Show a reviewer what the captured AXIS demo proved without exposing the implementation.

## Review Flow

1. Read [../../PUBLIC_DEMO_NOTICE.md](../../PUBLIC_DEMO_NOTICE.md).
2. Read [../../demo/REVIEWER_START_HERE.md](../../demo/REVIEWER_START_HERE.md).
3. Inspect the evidence summary.
4. Inspect selected response JSON files:
   - safe read;
   - safe write;
   - approval required;
   - approval retry success;
   - approval rejected;
   - blocked operation;
   - transaction rollback outcomes.
5. Inspect selected audit events.
6. Read limitations.
7. Review claims and anti-claims.

## Optional Public Verification

From the repository root:

```powershell
python scripts\verify_pilot_evidence.py
```

Expected:

```text
PILOT_EVIDENCE_VERIFICATION: PASS
```

## Private Runnable Demo

The runnable demo is not included in this public repository. Request private access from VARUX:

https://varuxcyber.com/
