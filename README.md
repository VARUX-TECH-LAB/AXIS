# AXIS Public Demo

AXIS is a deterministic database control layer built by VARUX to inspect SQL before execution, evaluate policy rules, record evidence, and decide whether a request should be allowed, blocked, or sent to approval.

> Control risky database writes before they reach production.

This repository is a public, source-redacted demo and reviewer surface. It is intentionally not the full AXIS product repository and it is not an open source release.

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

## Important License Notice

This repository is governed by the [VARUX AXIS Public Demonstration and Evaluation License v1.0](LICENSE).

The previous Apache-style public license has been replaced. This repository is now demo-only and proprietary. No open source, production, commercial, redistribution, sublicensing, reverse engineering, or competing-product use rights are granted.

For source access, commercial review, or a private runnable demo, contact VARUX:

https://varuxcyber.com/

## What This Public Repository Is

- A GitHub-visible AXIS demo surface.
- A reviewer evidence package.
- A public claims and limitations package.
- A redacted technical overview of the AXIS approach.

## What This Public Repository Is Not

- It is not the full AXIS source tree.
- It is not a runnable production build.
- It is not an open source release.
- It is not a license to clone and reuse AXIS in another product.
- It is not enough material to reconstruct the AXIS enforcement engine.

## Start Here

- Public redaction notice: [PUBLIC_DEMO_NOTICE.md](PUBLIC_DEMO_NOTICE.md)
- No-run reviewer path: [demo/REVIEWER_START_HERE.md](demo/REVIEWER_START_HERE.md)
- Demo workspace: [demo/README.md](demo/README.md)
- Pre-generated evidence: [demo/pre-generated-evidence/README.md](demo/pre-generated-evidence/README.md)
- Claims and boundaries: [docs/reviewer/AXIS_CLAIMS_MATRIX.md](docs/reviewer/AXIS_CLAIMS_MATRIX.md)
- Anti-claims: [docs/reviewer/AXIS_ANTI_CLAIMS.md](docs/reviewer/AXIS_ANTI_CLAIMS.md)
- Known limits: [docs/technical/LIMITATIONS.md](docs/technical/LIMITATIONS.md)

## Public Review Path

This public repository supports no-run review:

1. Read [PUBLIC_DEMO_NOTICE.md](PUBLIC_DEMO_NOTICE.md).
2. Read [demo/REVIEWER_START_HERE.md](demo/REVIEWER_START_HERE.md).
3. Inspect [demo/pre-generated-evidence/pilot-v1/evidence-summary.md](demo/pre-generated-evidence/pilot-v1/evidence-summary.md).
4. Inspect selected responses under [demo/pre-generated-evidence/pilot-v1/selected-responses/](demo/pre-generated-evidence/pilot-v1/selected-responses/).
5. Inspect selected audit events under [demo/pre-generated-evidence/pilot-v1/selected-audit-events/](demo/pre-generated-evidence/pilot-v1/selected-audit-events/).
6. Review limitations under [demo/evidence/pilot-v1/limitations/](demo/evidence/pilot-v1/limitations/).

The private runnable demo, runtime source, policy engine, approval store, audit chain, Control Plane implementation, sample business app source, and deployment artifacts are intentionally withheld.

## Optional Evidence Check

The public repository keeps a small verification helper for the captured evidence package:

```powershell
python scripts\verify_pilot_evidence.py
```

Expected result:

```text
PILOT_EVIDENCE_VERIFICATION: PASS
```

This check verifies public evidence consistency. It does not run the AXIS engine and does not include withheld source code.

## What AXIS Demonstrates

The demo evidence shows AXIS protecting ORM-generated PostgreSQL write paths with:

- deterministic policy decisions;
- allow, block, and approval outcomes;
- approval retry behavior;
- transaction rollback behavior around policy stops;
- audit and evidence records;
- evidence verification;
- operator visibility concepts; and
- a clear claims and limitations boundary.

## What Is Intentionally Withheld

- Runtime enforcement source code.
- Policy evaluator internals.
- SQL classifier and parser bypass internals.
- Approval-store implementation.
- Audit WAL/hash-chain implementation.
- Native PostgreSQL wire implementation notes and source.
- Control Plane application source.
- Sample business application source.
- Test, regression, stress, benchmark, and deployment scripts.
- Build files and Docker runtime artifacts.
- Production policy fixtures and private deployment material.

These omissions are intentional. They keep the demo visible without publishing enough implementation detail to copy or reconstruct AXIS.

## Repository Layout

- `demo/` - Public evidence, selected responses, and redacted demo notes.
- `docs/demo/` - Demo and pilot walkthrough material.
- `docs/reviewer/` - External reviewer claims, boundaries, and feedback material.
- `docs/technical/` - High-level technical, security, and limitation notes.
- `docs/presentation/` - Presentation-oriented demo material.
- `docs/explainers/` - Public explanatory material.
- `scripts/` - Public evidence verification helper.
- `src/`, `control-plane/`, `policies/` - Redaction placeholders.

## VARUX

AXIS is developed under VARUX.

- Website: [https://varuxcyber.com/](https://varuxcyber.com/)
- GitHub: [https://github.com/VARUX-TECH-LAB](https://github.com/VARUX-TECH-LAB)
- LinkedIn: [https://www.linkedin.com/company/varux/](https://www.linkedin.com/company/varux/)

## Legal

This public repository is proprietary and demo-only. See [LICENSE](LICENSE), [NOTICE](NOTICE), and [PUBLIC_DEMO_NOTICE.md](PUBLIC_DEMO_NOTICE.md).



<img width="6664" height="3750" alt="VARUX" src="https://github.com/user-attachments/assets/371a2d5f-ecd5-44b6-b95f-857942ce3113" />

