# AXIS Public Claims Matrix

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

This public matrix is evidence-only. Private runnable scripts, source paths, and deployment files are intentionally withheld.

| # | Public claim | Public evidence | Boundary |
|---|---|---|---|
| 1 | AXIS routes protected ORM-generated writes through deterministic policy enforcement. | `demo/pre-generated-evidence/pilot-v1/selected-responses/safe-write-response.json`, `demo/pre-generated-evidence/pilot-v1/selected-audit-events/audit-sample-events.json` | Demonstrated for the captured pilot integration, not as a universal driver-level interception claim. |
| 2 | AXIS supports a safe read/write split in the pilot integration. | `demo/pre-generated-evidence/pilot-v1/selected-responses/safe-read-response.json` | Reads may go directly to PostgreSQL by design; this is not a direct-write bypass prevention claim. |
| 3 | AXIS returns structured outcomes instead of generic backend failure. | `approval-required-response.json`, `blocked-operation-response.json`, `approval-rejected-response.json` under `demo/pre-generated-evidence/pilot-v1/selected-responses/` | Response shape is shown through captured pilot evidence, not every application framework. |
| 4 | AXIS supports approval-required flows using rollback plus explicit retry. | `approval-required-response.json`, `approval-retry-success-response.json`, `demo/evidence/pilot-v1/limitations/approval-retry-model.md` | Approval is not executed while holding the original database transaction open. |
| 5 | AXIS avoids partial local workflow persistence around policy stops in the captured pilot. | `transaction-approval-rollback-response.json`, `transaction-blocked-rollback-response.json`, `demo/evidence/pilot-v1/limitations/transaction-model.md` | Demonstrated for selected pilot workflows only. |
| 6 | AXIS blocks destructive policy-covered operations in the captured pilot. | `blocked-operation-response.json`, `transaction-blocked-rollback-response.json`, audit samples | This does not claim all possible destructive SQL forms are covered. |
| 7 | AXIS emits auditable decision evidence. | `demo/pre-generated-evidence/pilot-v1/selected-audit-events/audit-sample-events.json`, `demo/pre-generated-evidence/pilot-v1/verification-output/audit-verification-output.json` | Public repo exposes selected evidence, not the private audit-chain implementation. |
| 8 | The public evidence package can be checked for consistency. | `python scripts\verify_pilot_evidence.py` | This verifies public evidence files only; it does not run AXIS. |

## Withheld From Public Repo

- Runtime source.
- Sample app source.
- Control Plane source.
- Policy fixtures.
- Test and benchmark scripts.
- Docker build/runtime files.
- Native wire implementation material.

See [../../PUBLIC_DEMO_NOTICE.md](../../PUBLIC_DEMO_NOTICE.md).
