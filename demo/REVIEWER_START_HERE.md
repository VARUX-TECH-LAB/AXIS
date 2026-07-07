# AXIS Public Reviewer Start Here

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

This public repository is source-redacted. It is designed for no-run review of AXIS claims, limitations, and captured evidence.

## Choose Your Review Path

A. I only have 3 minutes

- Read the 30-second summary below.
- Skim [../PUBLIC_DEMO_NOTICE.md](../PUBLIC_DEMO_NOTICE.md).
- Skim [../docs/reviewer/AXIS_CLAIMS_MATRIX.md](../docs/reviewer/AXIS_CLAIMS_MATRIX.md).
- Skim [../docs/reviewer/AXIS_ANTI_CLAIMS.md](../docs/reviewer/AXIS_ANTI_CLAIMS.md).

B. I cannot or do not want to run code

- Open [pre-generated-evidence/README.md](pre-generated-evidence/README.md).
- Inspect selected responses and audit samples.
- Read [../docs/reviewer/BYPASS_BOUNDARY_AND_DEPLOYMENT_ASSUMPTIONS.md](../docs/reviewer/BYPASS_BOUNDARY_AND_DEPLOYMENT_ASSUMPTIONS.md).
- Send architecture feedback without running the demo.

C. I want a runnable demo

- The runnable demo is intentionally not included in this public repository.
- Request a private demo package or live walkthrough from VARUX.
- Website: https://varuxcyber.com/

## 30-Second Summary

AXIS is a deterministic control layer for protected PostgreSQL write paths.

The captured demo evidence shows AXIS routing protected ORM-generated write operations through policy enforcement, approval handling, rollback-safe retry behavior, and auditable evidence generation.

This public package does not include the runtime source, policy evaluator internals, audit-chain implementation, approval-store implementation, Control Plane source, sample business app source, or deployment/build files.

This package does not claim native PostgreSQL wire compatibility, transparent drop-in enterprise proxy support, production deployment readiness, or universal ORM coverage.

## Evidence To Inspect

- No-run review: [pre-generated-evidence/](pre-generated-evidence/)
- Captured evidence: [evidence/pilot-v1/](evidence/pilot-v1/)
- Selected responses: [pre-generated-evidence/pilot-v1/selected-responses/](pre-generated-evidence/pilot-v1/selected-responses/)
- Selected audit events: [pre-generated-evidence/pilot-v1/selected-audit-events/](pre-generated-evidence/pilot-v1/selected-audit-events/)
- Verification output: [pre-generated-evidence/pilot-v1/verification-output/](pre-generated-evidence/pilot-v1/verification-output/)
- Claims map: [../docs/reviewer/AXIS_CLAIMS_MATRIX.md](../docs/reviewer/AXIS_CLAIMS_MATRIX.md)
- Anti-claims: [../docs/reviewer/AXIS_ANTI_CLAIMS.md](../docs/reviewer/AXIS_ANTI_CLAIMS.md)

## Optional Evidence Consistency Check

From the repository root:

```powershell
python scripts\verify_pilot_evidence.py
```

Expected:

```text
PILOT_EVIDENCE_VERIFICATION: PASS
```

This verifies public evidence consistency only. It does not run AXIS.

## License Boundary

This repository is proprietary, demo-only, and source-redacted. See [../LICENSE](../LICENSE).
