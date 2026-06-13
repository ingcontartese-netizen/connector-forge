# Lifecycle Logger

Use this reference for local MCP bridges, CLI-to-MCP wrappers, desktop bridges, and deployed connectors that can disconnect, exit early, or run stale code.

Goal: make runtime failures diagnosable without relying only on host logs. The logger is evidence for DEP-P0-001 and supports the host-live states in `go-live-gates.md`.

## Required properties

- JSONL format, one event per line.
- Append-only file such as `logs/mcp_bridge_lifecycle.jsonl`, or a configurable path documented in the host pack.
- Best-effort: logging failure must not break the bridge.
- Never write secrets, tokens, full business payloads, PII, or large raw outputs.
- Use UTF-8 when opening log files.
- Keep stdout clean for protocol/result data. Use file logging or controlled stderr, never free-form stdout chatter.
- Include `request_id` for tool calls when available.
- Include `build_stamp` in startup/health events when the connector has a build/version stamp.

## Minimum events

| Event | When | Required fields |
|---|---|---|
| `process_start` | process boot | pid, python, cwd, bridge_root, version, build_stamp, mode |
| `transport_start` | stdio/HTTP/WebSocket transport starts | transport, host_hint if known |
| `backend_probe` | backend/app reachability check | backend_url_redacted, ok, latency_ms, error_type |
| `tool_requested` | before tool execution | tool, request_id, bounded_args_summary |
| `tool_completed` | after success | tool, request_id, elapsed_ms, result_count, has_more |
| `tool_failed` | after handled failure | tool, request_id, elapsed_ms, error_type, traceback_hash |
| `process_error` | unhandled/fatal error | error_type, traceback_redacted |
| `process_end` | shutdown/finalizer | pid, elapsed_ms, reason |

## Redaction rules

- Log endpoint host/port only when useful; redact query strings and credentials.
- Replace token-like values with `[REDACTED]`.
- Summarize arguments instead of logging raw payloads.
- For large outputs, log shape: `result_count`, `has_more`, `next_cursor_present`, `artifact_path`, or `summary_len`.
- Tracebacks are allowed for diagnostics, but scrub environment variables, headers, tokens, passwords, cookies, and authorization values.

## Acceptance

To mark lifecycle logging `verified`, collect:

- one `process_start`;
- one transport start event;
- one successful read tool with requested/completed pair;
- one error or recovery event if the connector has a known failure path;
- proof that the log file uses UTF-8 and that stdout remains protocol-clean;
- a redaction check showing no secrets or full large payloads.

If a host provides an equivalent diagnostic channel, document it in `ACCEPTANCE_EVIDENCE.md`; otherwise a local/deployed bridge without lifecycle logging stays `HOLD`.
## OneMaster Draft Addendum

Record bridge generation, source root, host plug, version, loaded copy, and route catalog in the
lifecycle log. When old and new generations coexist, logs must make the generation visible so a
test cannot accidentally validate the wrong bridge.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atom OMD-M-18; tags BRIDGE / G1 /
G6 / G7 / LAB; claim limit: method/spec evidence only.
