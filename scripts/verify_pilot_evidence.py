#!/usr/bin/env python3
"""Verify AXIS Pilot Evidence Package v1.

VARUX public demo signature: VARUX-AXIS-PUBLIC-DEMO-REDLINE-2026.
This script verifies public evidence consistency only; it does not include
AXIS runtime, policy engine, approval-store, or audit-chain internals.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ROOT = ROOT / "demo" / "evidence" / "pilot-v1"
CLEAN_RUN_DIR = EVIDENCE_ROOT / "clean-run"
HEALTH_DIR = EVIDENCE_ROOT / "health"
RESPONSES_DIR = EVIDENCE_ROOT / "responses"
AUDIT_DIR = EVIDENCE_ROOT / "audit"
LIMITATIONS_DIR = EVIDENCE_ROOT / "limitations"
DOCS_DIR = ROOT / "docs" / "demo"


REQUIRED_RESPONSE_FILES = [
    "safe-read-response.json",
    "safe-write-response.json",
    "approval-required-response.json",
    "approval-retry-success-response.json",
    "approval-rejected-response.json",
    "blocked-operation-response.json",
    "transaction-safe-response.json",
    "transaction-approval-rollback-response.json",
    "transaction-blocked-rollback-response.json",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_json(path: Path, failures: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        failures.append(f"missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        failures.append(f"invalid JSON: {path.relative_to(ROOT)} ({exc})")
    return None


def require_file(path: Path, failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"missing file: {path.relative_to(ROOT)}")


def body(response: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(response, dict):
        return {}
    value = response.get("body")
    return value if isinstance(value, dict) else response


def security(response: dict[str, Any] | None) -> dict[str, Any]:
    value = body(response).get("security")
    return value if isinstance(value, dict) else {}


def response_status(response: dict[str, Any] | None) -> str:
    return str(body(response).get("status") or "")


def http_status(response: dict[str, Any] | None) -> int | None:
    if isinstance(response, dict) and isinstance(response.get("http_status"), int):
        return int(response["http_status"])
    return None


def check(condition: bool, failures: list[str], message: str) -> None:
    if not condition:
        failures.append(message)


def check_required_structure(failures: list[str]) -> None:
    required_files = [
        EVIDENCE_ROOT / "README.md",
        CLEAN_RUN_DIR / "commands.md",
        CLEAN_RUN_DIR / "smoke-test-output.txt",
        CLEAN_RUN_DIR / "demo-run-output.txt",
        CLEAN_RUN_DIR / "compose-ps-output.txt",
        HEALTH_DIR / "axis-health.json",
        HEALTH_DIR / "backend-health.json",
        HEALTH_DIR / "frontend-health.txt",
        AUDIT_DIR / "audit-sample-events.json",
        AUDIT_DIR / "audit-verification-output.json",
        AUDIT_DIR / "audit-hash-chain-notes.md",
        EVIDENCE_ROOT / "screenshots" / "README.md",
        LIMITATIONS_DIR / "current-limitations.md",
        LIMITATIONS_DIR / "native-wire-gap.md",
        LIMITATIONS_DIR / "sql-alchemy-integration-notes.md",
        LIMITATIONS_DIR / "approval-retry-model.md",
        LIMITATIONS_DIR / "transaction-model.md",
        DOCS_DIR / "PILOT_REVIEWER_DEMO_FLOW.md",
        DOCS_DIR / "PILOT_EVIDENCE_PACKAGE.md",
        DOCS_DIR / "PILOT_LIMITATIONS_AND_NEXT_STEPS.md",
    ]
    required_files.extend(RESPONSES_DIR / name for name in REQUIRED_RESPONSE_FILES)
    for path in required_files:
        require_file(path, failures)
    if (EVIDENCE_ROOT / "PARTIAL_CAPTURE.txt").exists():
        failures.append("partial capture marker exists: demo/evidence/pilot-v1/PARTIAL_CAPTURE.txt")


def check_clean_run(failures: list[str]) -> None:
    commands = (CLEAN_RUN_DIR / "commands.md").read_text(encoding="utf-8") if (CLEAN_RUN_DIR / "commands.md").exists() else ""
    for expected in [
        "docker compose -f demo/docker-compose.pilot.yml down -v",
        "docker compose -f demo/docker-compose.pilot.yml up -d --build",
        "python scripts\\pilot_smoke_tests.py",
        "python scripts\\run_pilot_demo.py",
        "python scripts\\capture_pilot_evidence.py",
        "python scripts\\verify_pilot_evidence.py",
    ]:
        check(expected in commands, failures, f"commands.md missing clean-run command: {expected}")

    smoke = (CLEAN_RUN_DIR / "smoke-test-output.txt").read_text(encoding="utf-8") if (CLEAN_RUN_DIR / "smoke-test-output.txt").exists() else ""
    check("Exit code: 0" in smoke, failures, "smoke-test-output.txt does not show exit code 0")
    check(
        "AXIS real application pilot smoke tests passed" in smoke,
        failures,
        "smoke-test-output.txt missing smoke-test success line",
    )

    demo = (CLEAN_RUN_DIR / "demo-run-output.txt").read_text(encoding="utf-8") if (CLEAN_RUN_DIR / "demo-run-output.txt").exists() else ""
    check("Exit code: 0" in demo, failures, "demo-run-output.txt does not show exit code 0")
    check("Direct PostgreSQL read" in demo, failures, "demo-run-output.txt missing direct read step")
    check("Exact operation retry after approval" in demo, failures, "demo-run-output.txt missing approval retry step")

    compose_ps = (CLEAN_RUN_DIR / "compose-ps-output.txt").read_text(encoding="utf-8") if (CLEAN_RUN_DIR / "compose-ps-output.txt").exists() else ""
    check("Exit code: 0" in compose_ps, failures, "compose-ps-output.txt does not show exit code 0")
    for service in ["pilot-postgres", "axis-backend", "sample-business-backend", "sample-business-frontend"]:
        check(service in compose_ps, failures, f"compose-ps-output.txt missing service: {service}")


def check_health(failures: list[str]) -> None:
    axis = load_json(HEALTH_DIR / "axis-health.json", failures)
    backend = load_json(HEALTH_DIR / "backend-health.json", failures)
    check(isinstance(axis, dict) and axis.get("status") == "ok", failures, "axis-health.json does not report status ok")
    check(
        isinstance(backend, dict) and backend.get("status") == "ok",
        failures,
        "backend-health.json does not report status ok",
    )
    frontend = (HEALTH_DIR / "frontend-health.txt").read_text(encoding="utf-8") if (HEALTH_DIR / "frontend-health.txt").exists() else ""
    check("http_status: 200" in frontend and "result: reachable" in frontend, failures, "frontend health does not show reachable HTTP 200")


def load_responses(failures: list[str]) -> dict[str, dict[str, Any]]:
    responses: dict[str, dict[str, Any]] = {}
    for name in REQUIRED_RESPONSE_FILES:
        parsed = load_json(RESPONSES_DIR / name, failures)
        if isinstance(parsed, dict):
            responses[name] = parsed
        elif parsed is not None:
            failures.append(f"{name} is not a JSON object")
    return responses


def check_responses(failures: list[str]) -> None:
    responses = load_responses(failures)

    safe_read = responses.get("safe-read-response.json")
    check(response_status(safe_read) == "allowed", failures, "safe-read-response.json does not show allowed status")
    check(body(safe_read).get("path") == "direct_postgres", failures, "safe-read-response.json does not show direct PostgreSQL path")

    safe_write = responses.get("safe-write-response.json")
    check(response_status(safe_write) == "allowed", failures, "safe-write-response.json does not show allowed status")
    check(security(safe_write).get("decision") == "ALLOW", failures, "safe-write-response.json does not show AXIS ALLOW")
    check(bool(security(safe_write).get("audit_event_id")), failures, "safe-write-response.json missing audit_event_id")

    approval_required = responses.get("approval-required-response.json")
    check(
        response_status(approval_required) == "approval_required",
        failures,
        "approval-required-response.json does not show approval_required status",
    )
    check(http_status(approval_required) == 202, failures, "approval-required-response.json expected HTTP 202")
    check(bool(security(approval_required).get("approval_id")), failures, "approval-required-response.json missing approval_id")
    check(
        security(approval_required).get("decision") == "REQUIRE_APPROVAL",
        failures,
        "approval-required-response.json missing REQUIRE_APPROVAL decision",
    )

    retry_success = responses.get("approval-retry-success-response.json")
    check(response_status(retry_success) == "allowed", failures, "approval-retry-success-response.json does not show final success")
    check(http_status(retry_success) == 200, failures, "approval-retry-success-response.json expected HTTP 200")
    check(
        isinstance(retry_success, dict) and isinstance(retry_success.get("approval_resolution"), dict),
        failures,
        "approval-retry-success-response.json missing approval resolution evidence",
    )

    rejected = responses.get("approval-rejected-response.json")
    check(response_status(rejected) == "approval_rejected", failures, "approval-rejected-response.json does not show rejection")
    check(http_status(rejected) == 409, failures, "approval-rejected-response.json expected HTTP 409")
    check(
        isinstance(rejected, dict) and isinstance(rejected.get("rejection_resolution"), dict),
        failures,
        "approval-rejected-response.json missing rejection resolution evidence",
    )

    blocked = responses.get("blocked-operation-response.json")
    check(response_status(blocked) == "blocked", failures, "blocked-operation-response.json does not show blocked status")
    check(http_status(blocked) == 403, failures, "blocked-operation-response.json expected HTTP 403")
    check(security(blocked).get("decision") == "BLOCK", failures, "blocked-operation-response.json missing BLOCK decision")

    transaction_safe = responses.get("transaction-safe-response.json")
    safe_data = body(transaction_safe).get("data") if isinstance(body(transaction_safe).get("data"), dict) else {}
    check(response_status(transaction_safe) == "allowed", failures, "transaction-safe-response.json does not show allowed status")
    check(int(safe_data.get("axis_write_count") or 0) >= 3, failures, "transaction-safe-response.json does not show multiple AXIS writes")

    transaction_approval = responses.get("transaction-approval-rollback-response.json")
    check(
        response_status(transaction_approval) == "approval_required",
        failures,
        "transaction-approval-rollback-response.json does not show approval_required",
    )
    check(
        body(transaction_approval).get("marker_persisted") is False,
        failures,
        "transaction-approval-rollback-response.json indicates marker persisted",
    )
    check(
        isinstance(transaction_approval, dict)
        and isinstance(transaction_approval.get("state_check"), dict)
        and transaction_approval["state_check"].get("rollback_confirmed") is True,
        failures,
        "transaction-approval-rollback-response.json missing rollback state check",
    )

    transaction_blocked = responses.get("transaction-blocked-rollback-response.json")
    check(response_status(transaction_blocked) == "blocked", failures, "transaction-blocked-rollback-response.json does not show blocked")
    check(
        body(transaction_blocked).get("marker_persisted") is False,
        failures,
        "transaction-blocked-rollback-response.json indicates marker persisted",
    )
    check(
        isinstance(transaction_blocked, dict)
        and isinstance(transaction_blocked.get("state_check"), dict)
        and transaction_blocked["state_check"].get("rollback_confirmed") is True,
        failures,
        "transaction-blocked-rollback-response.json missing rollback state check",
    )


def check_audit(failures: list[str]) -> None:
    audit = load_json(AUDIT_DIR / "audit-sample-events.json", failures)
    if isinstance(audit, dict):
        recent = audit.get("recent_events")
        selected = audit.get("selected_events")
        events = selected if isinstance(selected, list) and selected else recent
        check(isinstance(events, list) and bool(events), failures, "audit-sample-events.json contains no audit events")
        if isinstance(events, list) and events:
            check(any(event.get("event_id") for event in events if isinstance(event, dict)), failures, "audit events missing event_id")
            check(any(event.get("decision") for event in events if isinstance(event, dict)), failures, "audit events missing decision")
            check(any(event.get("matched_rule") for event in events if isinstance(event, dict)), failures, "audit events missing matched_rule")
            check(any(event.get("sql_fingerprint") for event in events if isinstance(event, dict)), failures, "audit events missing sql_fingerprint")
            check(any(event.get("event_hash") for event in events if isinstance(event, dict)), failures, "audit events missing event_hash")
            check(any(event.get("previous_hash") for event in events if isinstance(event, dict)), failures, "audit events missing previous_hash")
            check(
                any(isinstance(event.get("policy"), dict) and event["policy"].get("policy_version") for event in events if isinstance(event, dict)),
                failures,
                "audit events missing policy metadata",
            )

    verification = load_json(AUDIT_DIR / "audit-verification-output.json", failures)
    if isinstance(verification, dict):
        check(verification.get("available") is True, failures, "audit verification endpoint was not available")
        verification_body = verification.get("body")
        check(
            isinstance(verification_body, dict) and verification_body.get("status") == "verified",
            failures,
            "audit-verification-output.json does not report verified status",
        )
        check(
            isinstance(verification_body, dict) and int(verification_body.get("events_checked") or 0) > 0,
            failures,
            "audit-verification-output.json did not check any events",
        )


def update_readme(status: str) -> None:
    path = EVIDENCE_ROOT / "README.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    replacement = f"Verification status: {status} (last verified at {utc_now()})."
    if re.search(r"Verification status: .+", text):
        text = re.sub(r"Verification status: .+", replacement, text, count=1)
    else:
        text = text + "\n" + replacement + "\n"
    path.write_text(text, encoding="utf-8")


def main() -> int:
    failures: list[str] = []
    check_required_structure(failures)
    check_clean_run(failures)
    check_health(failures)
    check_responses(failures)
    check_audit(failures)

    if failures:
        update_readme("FAIL")
        for failure in failures:
            print(f"- {failure}")
        print("PILOT_EVIDENCE_VERIFICATION: FAIL")
        return 1

    update_readme("PASS")
    print("PILOT_EVIDENCE_VERIFICATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
