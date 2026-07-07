# AXIS Pilot Evidence Package v1

Captured at: 2026-05-20T07:29:57.740426Z

Verification status: PASS (last verified at 2026-07-07T22:42:59.603239Z).

## What Was Tested

- FastAPI sample backend health
- AXIS backend health
- Frontend reachability
- Direct PostgreSQL safe read path
- SQLAlchemy ORM write routed through AXIS HTTP `/query`
- Approval-required response, approval resolution, and explicit retry
- Rejected approval handling
- Blocked destructive operation handling
- All-safe transaction workflow
- Rollback behavior for approval-required and blocked transaction workflows
- Audit event capture and hash-chain verification endpoint output

## Reproduce

```powershell
docker compose -f demo/docker-compose.pilot.yml down -v
docker compose -f demo/docker-compose.pilot.yml up -d --build
python scripts\pilot_smoke_tests.py
python scripts\run_pilot_demo.py
python scripts\capture_pilot_evidence.py
python scripts\verify_pilot_evidence.py
```

## Known Limitations

This package documents the current HTTP adapter and SQLAlchemy routing model. It does not claim native PostgreSQL wire compatibility, transparent enterprise drop-in proxy behavior, or production deployment readiness.

## Reviewer Docs

- [Pilot Reviewer Demo Flow](../../../docs/demo/PILOT_REVIEWER_DEMO_FLOW.md)
- [Pilot Evidence Package](../../../docs/demo/PILOT_EVIDENCE_PACKAGE.md)
- [Pilot Limitations and Next Steps](../../../docs/demo/PILOT_LIMITATIONS_AND_NEXT_STEPS.md)
