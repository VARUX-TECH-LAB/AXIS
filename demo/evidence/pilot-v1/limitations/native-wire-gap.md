# Native Wire Gap

AXIS Pilot v1 does not expose a native PostgreSQL wire-compatible proxy path in this evidence package.

Protected writes are sent to AXIS over HTTP `/query`. The sample backend compiles SQLAlchemy operations into SQL text and sends that text to AXIS. This is not equivalent to accepting arbitrary PostgreSQL client protocol traffic.

Open work for a native wire path includes PostgreSQL protocol parsing, authentication, prepared statements, extended query flow, transaction affinity, connection pinning, driver compatibility, and operational hardening.
