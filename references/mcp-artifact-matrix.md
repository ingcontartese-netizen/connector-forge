# MCP Artifact Matrix

Use this reference when deciding what must be delivered for an MCP connector in a real host.

The correct question is not "can we create an MCP server?" The correct question is "which artifacts make this connector installable, governable, testable, and useful in the selected host?"

Transport defaults, host artifact assumptions, and host certification evidence carry `[spec 2025-11-25 - revalidate]` when they depend on MCP protocol or host behavior.

## Minimum Artifact Family

Most serious MCP connector families need:

- domain adapter or native app plugin/add-on;
- optional local bridge or site agent;
- MCP server or remote broker;
- host-specific package;
- smoke tests and acceptance evidence;
- `PROJECT-KNOWLEDGE.md` or equivalent durable ledger;
- security and recovery runbook.

The host config file alone is never the connector.

## Local-First Hosts

| Host | Required artifacts | Zero tolerance |
|---|---|---|
| Codex | `AGENTS.md` when useful, adapter, MCP server, `config.toml`, tool allow/deny policy, smoke tests | missing adapter or runtime entrypoint |
| Claude Code | `CLAUDE.md`, adapter, MCP server, `.mcp.json` or settings, permissions, smoke tests | domain logic hidden only in prompts |
| Claude Desktop local | Desktop Extension `.mcpb` or local MCP package, adapter, installer/dependency path, local smoke | public endpoint used only to imitate local |
| Gemini CLI | `GEMINI.md`, `settings.json`, adapter, MCP server or extension, `/mcp list` smoke | config without policy and tool proof |

Local-first default transport is `stdio` unless an HTTP server is already justified.

## Remote-First Hosts

| Host | Required artifacts | Zero tolerance |
|---|---|---|
| Cowork | plugin or operating package, remote broker HTTPS, local site bridge for desktop apps, adapter, auth/approval/audit, Cowork smoke | pretending Cowork can reach a private desktop MCP directly |
| ChatGPT Apps | public HTTPS MCP/app server, protected resource metadata, tool metadata, security schemes, auth flow, Developer Mode/API smoke | missing public endpoint or auth metadata |
| Claude remote connectors | public/reachable endpoint, OAuth or documented auth, policy, host smoke | localhost-only server |
| Antigravity | rules/workflows or skill package, config/store entry, remote or local server as supported, auth-fit decision, client smoke | generic OAuth assumption without live validation |
| Google Cloud / Gemini remote | remote endpoint, IAM/ADC/OAuth profile, config, logs, smoke | unverified credential chain |

Remote-first default transport is Streamable HTTP over HTTPS.

## Cross-Host Certification

The same adapter or MCP server can support multiple hosts, but certification is per host.

For each host lane, verify:

- install or registration complete;
- discovery visible in that host;
- at least one read tool works;
- export/preview produces a verifiable artifact when in scope;
- dry-run or prepare/commit works before writes;
- auth and re-auth work end to end when required;
- recovery/runbook exists;
- evidence path is recorded.

## Artifact Placement

Default project skeleton:

```text
adapter/
bridge_local/          # only when needed
mcp_server/
host_packs/
acceptance/
docs/PROJECT-KNOWLEDGE.md
docs/ACCEPTANCE_EVIDENCE.md
```

Use Forge templates where possible:

- `assets/templates/MCP_TOOL_CATALOG.json`
- `assets/templates/ADAPTER_CONTRACT.yaml`
- `assets/templates/GATE_0_DOSSIER.md`
- `assets/templates/SPRINT1_READINESS.md`
- `assets/templates/ACCEPTANCE_EVIDENCE.md`
- `assets/templates/PROJECT-KNOWLEDGE.md`
- `assets/templates/LIFECYCLE_LOGGING.md`

## Definition Of Done

An MCP connector is not done until:

1. adapter or app package installs cleanly;
2. server starts and discovery works;
3. read/state path is live or explicitly mock-labeled;
4. export/preview path is verifiable when in scope;
5. write path has safety, approval, audit, readback, and rollback scope when in scope;
6. primary host smoke passes;
7. recovery and refresh behavior are documented.

## Stop Rules

Stop if:

- required host artifact is missing;
- host package carries divergent domain behavior;
- a host pack is called ready without host smoke;
- remote host depends on private localhost reachability;
- adapter is skipped and prompts carry domain logic;
- package evidence is stale relative to source.

## Claim Limits

This matrix defines required artifacts. It does not prove that any artifact exists, works, or is installable.
