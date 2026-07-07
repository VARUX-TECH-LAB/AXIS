# AXIS Pilot v1 Pre-Generated Evidence Summary

Capture timestamp: 2026-05-20T07:29:57.740426Z

Source commit hash: `0f6f8330c2e557ddb617aca8c9ddc1f5358550e6`

Working tree note: the pilot package files were present as local working-tree content during packaging. Reviewers should inspect source and run locally for stronger validation.

## Commands Used To Generate Evidence

```powershell
docker compose -f demo/docker-compose.pilot.yml down -v
docker compose -f demo/docker-compose.pilot.yml up -d --build
python scripts\pilot_smoke_tests.py
python scripts\run_pilot_demo.py
python scripts\capture_pilot_evidence.py
python scripts\verify_pilot_evidence.py
```

## PASS/FAIL State

Current pilot evidence verification state: PASS.

The source evidence README reported:

`Verification status: PASS (last verified at 2026-05-20T07:30:03.536802Z).`

## What Was Proven

- FastAPI sample backend health was captured.
- AXIS backend health was captured.
- Frontend reachability was captured.
- Safe read path used direct PostgreSQL in the pilot.
- ORM-generated protected write path used AXIS HTTP `/query`.
- Approval-required response, approval resolution, and explicit retry were captured.
- Rejected approval behavior was captured.
- Blocked destructive operation behavior was captured.
- Transaction rollback behavior was captured for approval-required and blocked workflows.
- Audit sample events and audit verification endpoint output were captured.

## What Was Not Proven

- Native PostgreSQL wire compatibility.
- Transparent enterprise drop-in proxy support.
- Production deployment readiness.
- Universal ORM coverage.
- Direct database write bypass prevention without deployment hardening.
- Local reproducibility in the reviewer's own environment.
- Enterprise-scale performance.
- Final compliance certification.

## Signed Or Unsigned Status

This pre-generated evidence is not cryptographically signed in this package version.

No signing keys, private keys, fabricated signatures, fake screenshots, or fake demo videos are included.
