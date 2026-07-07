# AXIS Pilot v1 Clean Run Commands

Captured at: 2026-05-20T07:29:57.740426Z

This evidence package is intended to be regenerated from a clean pilot stack with the exact flow below.

```powershell
docker compose -f demo/docker-compose.pilot.yml down -v
docker compose -f demo/docker-compose.pilot.yml up -d --build
python scripts\pilot_smoke_tests.py
python scripts\run_pilot_demo.py
python scripts\capture_pilot_evidence.py
python scripts\verify_pilot_evidence.py
```

The capture script archives reviewer evidence by invoking these Windows-compatible commands during capture:

```powershell
python scripts\pilot_smoke_tests.py
python scripts\run_pilot_demo.py
docker compose -f demo/docker-compose.pilot.yml ps --no-trunc
```

Service endpoints used by the capture:

- AXIS backend: `http://localhost:6654`
- Sample backend: `http://localhost:8000`
- Sample frontend: `http://localhost:8088`

Pass/fail interpretation:

- `smoke-test-output.txt` must show exit code `0` and the smoke-test success line.
- `demo-run-output.txt` must show exit code `0` and the demo walkthrough steps.
- `compose-ps-output.txt` must show the pilot compose services after the clean start.
- `python scripts\verify_pilot_evidence.py` must print `PILOT_EVIDENCE_VERIFICATION: PASS`.
