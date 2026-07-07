# Audit Hash Chain Notes

Captured at: 2026-05-20T07:30:00.010209Z

## Source

Audit events are read from the AXIS backend endpoint `http://localhost:6654/audit/events?limit=100`.
The sample business backend sends ORM-generated protected writes to AXIS HTTP `/query`; AXIS evaluates policy, executes allowed SQL, and emits audit events.

## Hash Fields

- `event_hash` is the hash AXIS records for an audit event after canonicalizing the event payload.
- `previous_hash` links an event to the previous event in the audit chain.
- A continuous chain lets a reviewer detect missing, reordered, or modified audit entries when the verification endpoint is available.

## Verification Endpoint

The `/audit/verify` endpoint was available during capture and returned status `verified` after checking `208` events.

## Automatic Checks

`scripts/capture_pilot_evidence.py` saves recent audit events and the verification endpoint response.
`scripts/verify_pilot_evidence.py` checks that audit events exist, that representative events include decision and policy metadata, and that `/audit/verify` reports a verified chain for this captured package.

## Manual Or Future Work

The evidence package does not independently recompute every event hash outside AXIS. Reviewers should inspect `audit-sample-events.json` and `audit-verification-output.json`; independent offline recomputation can be added as a future evidence-package enhancement.
