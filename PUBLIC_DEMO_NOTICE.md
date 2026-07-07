# AXIS Public Demo Redaction Notice

This repository is a public demonstration surface for AXIS. It is not the full AXIS product repository and it is not an open source release.

Public demo signature:

```text
VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026
```

## What Is Included

- Public README and reviewer notes.
- Demo and reviewer documentation.
- Pre-generated evidence fixtures.
- Captured pilot evidence summaries and selected responses.
- A lightweight evidence verification script.
- High-level architecture, limitation, and presentation documents.

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

## Why These Parts Are Missing

AXIS must be visible for review, but the public repository must not expose enough implementation detail to reconstruct the product. Reviewers can inspect the public evidence and claims boundary here; runnable demos, deeper source review, and commercial evaluation require explicit written permission from VARUX.

## License Boundary

The repository is governed by [LICENSE](LICENSE). The license is proprietary, demo-only, and does not grant open source, commercial, redistribution, or production use rights.

For formal access:

https://varuxcyber.com/
