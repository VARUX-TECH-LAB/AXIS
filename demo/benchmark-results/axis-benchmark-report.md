# AXIS Pilot Benchmark Report

Generated at: `2026-05-18T19:02:03.238984Z`

AXIS does not compete with raw database latency.
AXIS competes with uncontrolled production execution risk.

No combined average latency is reported across ALLOW, REQUIRE_APPROVAL, and BLOCK paths.
Direct PostgreSQL is compared only against the ALLOW-safe corpus.

## Configuration

- Total corpus: `100`
- Corpus split: `70/20/10`
- Seed: `42`
- Concurrency: `1`
- Warmup: `100`
- Tenant: `acme_corp`
- Environment: `production`

## Section 1 - Baseline Performance Comparison

This compares only Direct PostgreSQL ALLOW Path vs AXIS HTTP `/query` ALLOW Path.

| Performance & Capacity Metric | Direct PostgreSQL Path | AXIS HTTP /query Path | Delta |
| --- | --- | --- | --- |
| p50 latency | 0.664 ms | 59.630 ms | +58.966 ms (+8884.4%) |
| p95 latency | 2.747 ms | 82.436 ms | +79.689 ms (+2900.5%) |
| p99 latency | 17.857 ms | 99.201 ms | +81.345 ms (+455.5%) |
| min latency | 0.316 ms | 15.605 ms | +15.289 ms (+4836.8%) |
| max latency | 17.857 ms | 99.201 ms | +81.345 ms (+455.5%) |
| average latency | 1.246 ms | 59.280 ms | +58.035 ms (+4659.2%) |
| throughput QPS | 580.979 | 16.749 | -564.230 (-97.1%) |
| error rate | 0.00% | 0.00% | +0.00 pp |
| total queries | 70 | 70 | 0 |
| successful queries | 70 | 70 | 0 |
| failed queries | 0 | 0 | 0 |

## Section 2 - Enforcement Path Measurement

These are AXIS-only enforcement paths. They are not compared against Direct PostgreSQL latency.

| Enforcement Metric | APPROVAL_REQUIRED Path | BLOCK Path |
| --- | --- | --- |
| p50 decision latency | 68.346 ms | 56.754 ms |
| p95 decision latency | 81.183 ms | 72.789 ms |
| p99 decision latency | 82.255 ms | 72.789 ms |
| average decision latency | 66.811 ms | 55.949 ms |
| approval record creation success count | 20 | n/a |
| blocked count | n/a | 5 |
| structured error count | 0 | 10 |
| error rate | 0.00% | 0.00% |

## Section 3 - Security Outcome Summary

| Security Outcome | Count | Percentage |
| --- | --- | --- |
| total corpus size | 100 | 100.00% |
| ALLOW count | 70 | 70.00% |
| REQUIRE_APPROVAL count | 20 | 20.00% |
| BLOCK count | 10 | 10.00% |
| queries executed against DB | 70 | 70.00% |
| queries not executed | 30 | 30.00% |
| approval records created | 20 | 20.00% |
| blocked before DB | 10 | 10.00% |
| failed-closed count | 10 | 10.00% |

Policy:

- policy_id: `prod_safety_baseline`
- policy_version: `1.0.0`
- policy_sha256: `3b1c86af61be07f346c2a9c3cd057ab3eac3dc522203e61fd39db2d76acf2acd`

AXIS allowed 70 safe operations.
AXIS suspended 20 controlled-risk operations for approval.
AXIS blocked 10 dangerous or ambiguous operations before database execution.

## Native Wire Path

- None

## Warnings

- None

Latency is measured.
Risk reduction is demonstrated.
Evidence is verifiable.
