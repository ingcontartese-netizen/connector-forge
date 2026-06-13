# Case Study: ValuAziende MCP Deploy

Status: field-tested, sanitized
Purpose: record connector-forge lessons from a proprietary web app with an existing MCP bridge.

## Scenario

Target: proprietary FastAPI/React app with existing MCP bridges.

Branch selected: `mcp`.

Reason: the bridge already existed and was authorized. The method chose reuse and hardening, not reinvention.

## Field Lessons

- Frontend availability is not backend availability. The connector talks to the backend surface, not the visual app alone.
- App closed or backend unreachable means `HOLD`/`BLOCKED`, not workaround.
- Host loaded does not prove fresh code. Use build stamp, process restart, and host-live evidence.
- Variable-size read/simulate/report operations need bounded output by default.
- Natural user questions require UI label to data-field mapping before answering.
- Lifecycle logs are necessary when a local bridge disconnects without traceback.
- Windows UTF-8 and synchronized folders can create real deployment bugs.
- Governed writes use read -> simulate -> propose -> approve -> apply -> audit.
- The agent must not touch the calculation engine or invent missing numbers.

## Promoted Artifacts

- `governance-write-ladder.md`
- `CAPABILITY_LEDGER.md` with `declared_limits`
- bounded-output Gate 11
- lifecycle Gate 12
- host-live states
- `UI_FIELD_MAP.md`
- `NATURAL_QUESTIONS.md`

## Non-Core Details

Do not publish personal paths, private data, endpoint internals, or domain-specific scoring details.
