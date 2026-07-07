# Current Pilot Limitations

The pilot proves an application-layer AXIS integration for a FastAPI and SQLAlchemy business backend. It does not prove native PostgreSQL wire compatibility, universal ORM interception, transparent driver-level deployment, or production readiness.

The sample stack is intentionally narrow:

- FastAPI backend
- SQLAlchemy ORM
- PostgreSQL
- AXIS HTTP `/query`
- Custom `AxisRoutingSession`
- Local Docker Compose services

Reviewers should treat the evidence as proof of this integration boundary only.
