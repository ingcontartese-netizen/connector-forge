# Carrier Parity Matrix

Use this reference when Connector Forge source, packages, or installed copies must support more than one carrier: Codex, Claude Code, Cowork, ChatGPT Apps, Antigravity, Gemini, or another host.

Carrier parity does not mean identical files. It means equivalent method content, explicit host differences, and evidence for every readiness claim.

## Parity Layers

| Layer | Meaning | Evidence |
|---|---|---|
| Source parity | canonical source contains the shared method and host-specific lanes | source diff, reference map |
| Package parity | carrier package was regenerated from the canonical source | package manifest, checksum, changelog |
| Installed parity | package was installed or imported into the target host/carrier | install/import proof |
| Host-loaded parity | host sees the fresh server/package/catalog | config, launch, tools list, build stamp |
| Host-live parity | host executes a real operation and recovery/error path | host transcript, artifact, lifecycle log |

Do not claim a higher layer when only a lower layer has evidence.

## Carrier States

Use these states in package notes and release claims:

- `source_only`: source has guidance, no package proof;
- `package_lag`: package exists but is behind source;
- `package_built`: package generated, not installed;
- `installed_needs_smoke`: installed/imported, no host smoke;
- `host_loaded`: host sees current package/catalog;
- `host_live_validated`: real host operation and recovery proof exist;
- `research_live_verify`: behavior documented as possible but still needs live verification;
- `blocked`: cannot proceed without external change.

Current OneMaster V1 rule: Antigravity starts at `research_live_verify` until a real client/auth/discovery/smoke/recovery proof upgrades it. Use only the state names above in package notes, release claims, and cross-carrier summaries.

## Host Lane Matrix

| Carrier | Shared core | Host-specific lane | Evidence before parity claim |
|---|---|---|---|
| Codex | adapter, MCP server, method references | `AGENTS.md`, `config.toml`, tool policy | config loaded, discovery, read smoke |
| Claude Code | adapter, MCP server, method references | `CLAUDE.md`, `.mcp.json`, permissions | project config approved, tools list, read smoke |
| Claude Desktop | local adapter/server | Desktop Extension or local config | install proof, desktop discovery, local smoke |
| Cowork | adapter, broker, bridge when desktop | plugin package, remote connector, bridge notes | reachable broker, plugin state, Cowork smoke |
| ChatGPT Apps | remote MCP/app server | app metadata, auth/securitySchemes | Developer Mode/API test, auth, UX check |
| Gemini CLI | adapter/server | `GEMINI.md`, `settings.json`, `/mcp` commands | settings loaded, `/mcp list`, smoke |
| Antigravity | adapter/server | rules/workflows, store or raw config | auth fit verified, client smoke |

## Shared Contracts

For multi-agent or multi-host programs, freeze public contracts early:

- tool names;
- operation schemas;
- risk classes;
- bounded output rules;
- acceptance test cases;
- error taxonomy;
- version/build stamp.

Local brains, host prompts, and runtime assumptions may differ. The public contract must not drift silently.

## Package Lag Rule

Any source edit creates carrier drift until each intended package is rebuilt, installed/reloaded, and smoke-tested. If the work deliberately stops earlier, record package lag instead of hiding it.

MCP protocol upgrades follow the core-first / carrier-after rule in `mcp-2026-07-28-watchlist.md`: revalidate the shared core first, then rebuild and smoke-test each carrier lane before promoting its state.

## Stop Rules

Stop parity claims if:

- one host lane carries divergent domain behavior;
- a package was not regenerated after source changes;
- installed copy cannot be inspected;
- host-loaded state is inferred from config presence;
- Antigravity/Gemini are promoted beyond live evidence;
- old and new generations are not distinguishable by version/build stamp.

## Claim Limits

This matrix defines parity governance. It does not prove package parity, installed parity, host-loaded parity, or host-live parity.
