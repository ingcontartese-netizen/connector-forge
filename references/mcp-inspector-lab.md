# MCP Inspector Lab

Use this reference before relying on the final host UI or declaring MCP discovery, auth, schema, write safety, or recovery ready.

Inspector is where an MCP connector moves from architecture to verifiable behavior. Host smoke still matters later, but skipping Inspector makes host failures harder to diagnose.

## Core Rule

Do not proceed to final host packaging until Inspector or a host-equivalent harness proves the server can start, expose a stable catalog, run at least one read, and surface correctable errors.

Inspector invocation, initialize/discover behavior, capability negotiation, tool/resource/prompt discovery, protocol/tool error separation, and auth handshake checks carry `[spec 2025-11-25 - revalidate]`.

## Example Commands

Use the current official Inspector invocation for the runtime. Typical local shapes:

```bash
npx @modelcontextprotocol/inspector node path/to/server/index.js
npx -y @modelcontextprotocol/inspector uvx package-name
npx @modelcontextprotocol/inspector uv --directory path/to/server run package-name
```

Treat these as examples. Revalidate commands before release.

## Required Checks

| Check | Proof | Stop if |
|---|---|---|
| Handshake | initialize/discover and capability negotiation succeed for the baseline in use | startup hangs or transport fails |
| Discovery | tools list, resources list when relevant, prompt list when used | catalog empty, stale, or schema-opaque |
| Schema | readable input schemas and stable structured output | tool needs prose guessing to call safely |
| Correctable error | validation error returns tool execution error with guidance | validation appears as opaque protocol fault |
| Auth | missing/expired/scope-limited auth path tested when remote | re-auth story is unproven |
| Write safety | dry-run, prepare/commit, proposal, or approval path works before real write | write can apply without a gate |
| Recovery | app closed, bridge restart, stale context, or lock conflict tested where relevant | no runbook or recovery signal |
| Bounded output | variable-size tool proves `page_size=3` or equivalent | large raw payload can flood host |
| Lifecycle | local/deployed bridge logs startup and tool events without secrets | stdout is dirty or stale process cannot be ruled out |

## Host Refresh And Double Refresh

Desktop and hybrid connectors often need two refreshes:

1. host-side MCP reload: the AI host refreshes config and tool catalog;
2. app-side reload: the target app loads or reloads its plugin/add-on/project state.

Verify both. A server restart does not prove the desktop add-on is active. A visible host catalog does not prove the app-side bridge is fresh.

Record:

- authoritative config path;
- reload/restart command or manual step;
- process/build stamp;
- app-side plugin/add-on/version check;
- first live read after reload.

## Exit Checklist

Before leaving Inspector, collect:

- working read tool with stable structured output;
- export or preview artifact when in scope;
- one correctable validation error;
- dry-run, prepare, or proposal path when writes exist;
- transcript, screenshot, or log;
- discovery snapshot;
- auth/re-auth proof for remote connectors;
- recovery proof or explicit `N/A` reason.

## Link To Go-Live Gates

Inspector supports but does not replace `go-live-gates.md`.

- Inspector can support `source_validated` and local behavior.
- Host-loaded proof requires the real host.
- Go-live requires host live validation, recovery proof, and claim audit.

## Stop Rules

Stop if:

- Inspector cannot start or discover the catalog;
- output schemas are too broad or unbounded;
- write safety is only described but not callable;
- recovery is undocumented;
- host smoke is claimed based only on Inspector.

## Claim Limits

Passing Inspector does not prove final host UX, package parity, production readiness, or public release readiness.
