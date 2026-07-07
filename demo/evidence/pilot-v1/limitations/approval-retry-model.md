# Approval Retry Model

The pilot uses rollback plus explicit retry.

Flow:

1. The business app submits an ORM-generated protected write to AXIS.
2. AXIS returns `REQUIRE_APPROVAL` with `approval_id`.
3. The business app rolls back local SQLAlchemy transaction state.
4. An operator approves or rejects through AXIS.
5. If approved, the same business operation is submitted again with `approval_id`.
6. AXIS validates the approval proof and executes the operation.

The model does not hold PostgreSQL transactions, locks, or connection state open while approval is pending.
