# AXIS Public Evidence Package

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

This public repository includes selected evidence from a private AXIS pilot run.

## Public Evidence Contents

- Captured response JSON files.
- Selected audit events.
- Verification output.
- Health snapshots.
- Limitations notes.
- Benchmark result artifacts.

## What The Evidence Shows

The evidence shows selected allow, block, approval, approval retry, approval rejection, and rollback outcomes from the private pilot.

## What Is Withheld

- The private capture script.
- The private runtime stack.
- Runtime source code.
- Policy fixtures.
- Audit-chain implementation.
- Approval-store implementation.
- Sample app source.

## Public Verification

The only public check is evidence consistency:

```powershell
python scripts\verify_pilot_evidence.py
```

Expected:

```text
PILOT_EVIDENCE_VERIFICATION: PASS
```
