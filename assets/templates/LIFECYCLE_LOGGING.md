# LIFECYCLE_LOGGING

Project:
Connector:
Host:
Environment:
Date:
Owner:

## Log Contract

- Log path:
- Format: JSONL
- Encoding: UTF-8
- Logger mode: best-effort / blocking forbidden
- Stdout policy:
- Stderr policy:
- Redaction policy:

## Build / Runtime Identity

- Version:
- Build stamp:
- Built at:
- Source hash or revision:
- Mode (`live|mock|stub`):

## Required Events

| Event | Present (`yes|no|n/a`) | Required fields verified | Evidence |
|---|---|---|---|
| `process_start` | | pid, python, cwd, bridge_root, version, build_stamp, mode | |
| `transport_start` | | transport, host_hint if known | |
| `backend_probe` | | backend_url_redacted, ok, latency_ms, error_type | |
| `tool_requested` | | tool, request_id, bounded_args_summary | |
| `tool_completed` | | tool, request_id, elapsed_ms, result_count, has_more | |
| `tool_failed` | | tool, request_id, elapsed_ms, error_type, traceback_hash | |
| `process_error` | | error_type, traceback_redacted | |
| `process_end` | | pid, elapsed_ms, reason | |

## Redaction Check

- Tokens absent:
- Secrets absent:
- PII/full business payload absent:
- Large raw output absent:
- Tracebacks scrubbed:

## Acceptance Decision

- Lifecycle observability status: verified / HOLD / BLOCKED / N/A with reason
- Blocking gaps:
- Next action:
