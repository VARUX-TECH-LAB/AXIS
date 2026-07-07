# AXIS Public Pilot Reviewer Flow

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

The public pilot reviewer flow is no-run and evidence-only. The private runnable pilot stack, source code, policies, and reviewer automation are intentionally withheld.

## What The Captured Demo Shows

AXIS can protect selected ORM-generated PostgreSQL write paths in a realistic pilot by routing protected operations through deterministic policy evaluation, approval handling, rollback-safe retry behavior, and auditable evidence generation.

## What This Public Package Does Not Claim

- Native PostgreSQL wire compatibility.
- Transparent driver-level interception for arbitrary applications.
- Universal SQLAlchemy dialect behavior.
- Production deployment readiness.
- Public availability of the AXIS runtime source.

## Evidence Review Steps

1. Open [../../demo/pre-generated-evidence/pilot-v1/evidence-summary.md](../../demo/pre-generated-evidence/pilot-v1/evidence-summary.md).
2. Inspect selected responses under `demo/pre-generated-evidence/pilot-v1/selected-responses/`.
3. Inspect selected audit events under `demo/pre-generated-evidence/pilot-v1/selected-audit-events/`.
4. Inspect verification output under `demo/pre-generated-evidence/pilot-v1/verification-output/`.
5. Read limitations under `demo/evidence/pilot-v1/limitations/`.
6. Read [../reviewer/AXIS_CLAIMS_MATRIX.md](../reviewer/AXIS_CLAIMS_MATRIX.md).
7. Read [../reviewer/AXIS_ANTI_CLAIMS.md](../reviewer/AXIS_ANTI_CLAIMS.md).

## Expected Reviewer Conclusion

A reviewer should conclude that the captured pilot evidence supports a deterministic application-layer protection path for selected PostgreSQL write workflows.

A reviewer should not conclude that this public repository contains the full source, production deployment package, or enough implementation detail to rebuild AXIS.
