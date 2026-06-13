# CLI Branch

Use this branch for agent-native CLIs, local adapters, FastAPI/OpenAPI wrappers, desktop bridges, repo workflows, and batch automation.

## Contract

Minimum commands:

- `doctor --format json`
- `list` or `search`
- `get ID`
- one read/export operation
- writes only after `--dry-run` exists
- dry-run output must be a structured JSON diff with a stable `plan_id`
- fail closed with exit `10` when scope, target, auth, idempotency, or recovery is unclear
- governed writes use proposal -> human approval -> audit, not direct mutation

Output discipline:

- stdout is machine-readable result;
- stderr is logs/progress;
- `--format json` must be valid JSON;
- exit codes must be documented;
- never print secrets.
- default read/search should support `--limit`, `--cursor`, and `--fields` to avoid large output dumps.

## Exit Codes

Canonical contract set:

- `0`: success.
- `2`: usage or invalid arguments.
- `3`: auth/config missing.
- `4`: permission or scope denied.
- `5`: object not found.
- `6`: conflict or lock.
- `7`: rate limit or remote unavailable.
- `8`: validation error.
- `10`: unsafe operation blocked.
- `70`: internal error.

`1` is tolerated only for legacy/unclassified failures; new CLIs should prefer the canonical set.

## Build Sequence

1. Implement `doctor`.
2. Implement one discovery/read command.
3. Add JSON output and fixtures.
4. Add `smoke_runner.py` manifest or command list.
5. Add dry-run for first write.
6. Only then wrap with MCP if needed.

## Script Helpers

- `surface_probe.py` for cautious API surface checks.
- `openapi_contract_stub.py` for OpenAPI/FastAPI draft contracts.
- `smoke_runner.py` for basic CLI confidence; pass the base command as separate arguments, for example `python scripts/smoke_runner.py python path/to/app_cli.py`.
- `drift_report.py` for snapshot comparison.

## OneMaster Draft Addendum

When CLI is the local control plane for a future MCP wrapper, define parity expectations early:
the same domain operation should have the same side-effect class, dry-run shape, readback, and
audit semantics in CLI and MCP. This is a target pattern until acceptance proves it.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atom OMD-M-16; tags BRIDGE / G1 /
G6 / G7 / LAB; claim limit: method/spec evidence only.
