# AXIS Public Reviewer Quickstart

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

This public repository is source-redacted. The Docker-based reviewer runner is intentionally withheld.

## Purpose

Use this public repository to review:

- what AXIS claims;
- what AXIS explicitly does not claim;
- captured demo evidence;
- selected audit events and responses;
- known limitations; and
- the public license boundary.

## Review Steps

1. Read [../../PUBLIC_DEMO_NOTICE.md](../../PUBLIC_DEMO_NOTICE.md).
2. Read [../../demo/REVIEWER_START_HERE.md](../../demo/REVIEWER_START_HERE.md).
3. Inspect [../../demo/pre-generated-evidence/pilot-v1/evidence-summary.md](../../demo/pre-generated-evidence/pilot-v1/evidence-summary.md).
4. Inspect [../../demo/pre-generated-evidence/pilot-v1/selected-responses/](../../demo/pre-generated-evidence/pilot-v1/selected-responses/).
5. Inspect [../../demo/pre-generated-evidence/pilot-v1/selected-audit-events/](../../demo/pre-generated-evidence/pilot-v1/selected-audit-events/).
6. Read [AXIS_CLAIMS_MATRIX.md](AXIS_CLAIMS_MATRIX.md).
7. Read [AXIS_ANTI_CLAIMS.md](AXIS_ANTI_CLAIMS.md).

## Optional Evidence Check

From the repository root:

```powershell
python scripts\verify_pilot_evidence.py
```

Expected:

```text
PILOT_EVIDENCE_VERIFICATION: PASS
```

This check does not run AXIS. It verifies consistency of the public evidence package.

## Runnable Demo

Runnable AXIS source, Docker stacks, sample app source, reviewer automation, and production implementation details are not included in this public repository.

Request private review access from VARUX:

https://varuxcyber.com/
