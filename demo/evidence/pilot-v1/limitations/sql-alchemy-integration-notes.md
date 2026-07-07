# SQLAlchemy Integration Notes

The sample backend uses `AxisRoutingSession` as a pilot v1 adapter.

Reads:

- ORM reads and SQLAlchemy `SELECT` statements execute directly against PostgreSQL.
- The backend records direct-read metrics.

Protected writes:

- ORM inserts, updates, and deletes in the sample app are compiled with SQLAlchemy's PostgreSQL dialect.
- Protected SQLAlchemy Core write statements are routed to AXIS.
- AXIS evaluates policy, executes allowed statements, and emits audit evidence.

Known boundaries:

- This is not a full SQLAlchemy dialect.
- Arbitrary relationship cascades, custom bind behavior, stored procedures, and all bulk operation modes are not proven.
- Literal SQL compilation is used because the current AXIS HTTP `/query` path executes SQL text rather than PostgreSQL wire-protocol bind parameters.
