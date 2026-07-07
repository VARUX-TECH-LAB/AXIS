# Transaction Model

The pilot demonstrates transaction behavior from the sample business app perspective.

Covered:

- All-safe workflow: multiple protected writes are routed through AXIS and complete.
- Approval-required workflow: a risky operation returns `approval_required`, and local pending state is rolled back.
- Blocked workflow: a destructive operation returns `blocked`, and local pending state is rolled back.

Important boundary:

AXIS HTTP `/query` is not a transaction coordinator. It does not expose native connection pinning, `BEGIN`/`COMMIT` affinity, or PostgreSQL wire session semantics in this pilot.

The rollback scenarios avoid partial local state by ordering risky statements before safe local markers are committed. Full atomic multi-statement AXIS-mediated transactions require future transaction-aware or wire-compatible integration work.
