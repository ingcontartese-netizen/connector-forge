# Revalidation Matrix

Use this before release, before using a fast-moving host/protocol, or when a connector depends on current auth, transport, SDK, plugin, or host behavior.

## Purpose

Prevent stale assumptions from entering connector design.

## Minimum Columns

| Area | Assumption | Fragility | Revalidate when | Evidence/Test | Owner |
|---|---|---|---|---|---|
| MCP spec | | high/medium/low | | | |
| MCP auth/transport | | | | | |
| Host config | | | | | |
| App API/SDK | | | | | |
| CLI contract | | | | | |
| Security controls | | | | | |
| Acceptance tests | | | | | |

## MCP OneMaster Rows

When MCP is in scope, add rows for the assumptions below instead of relying on a generic release note.

Mark MCP spec-sensitive sections with `[spec 2025-11-25 - revalidate]` when transport, auth, session, discovery, schema, Inspector, or host behavior depends on the current baseline.

| Area | Assumption | Fragility | Revalidate when | Evidence/Test | Owner |
|---|---|---|---|---|---|
| MCP procedure | Core flow still matches current MCP host behavior | high | MCP spec, SDK, Inspector, or host behavior changes | `mcp-procedure-track.md` reviewed, Inspector/host smoke rerun | connector owner |
| MCP auth/transport | Selected auth, transport, endpoint, and registration model still work | high | remote host, OAuth/OIDC, protected-resource metadata, DCR/client metadata, SSE/Streamable HTTP behavior changes | auth discovery, re-auth, reachability, and negative auth test | security owner |
| Remote broker/bridge | Broker can reach host/client and local bridge can reach the app without leaking secrets | high | network path, desktop app version, bridge deploy, broker policy, or tenant boundary changes | health/version, lifecycle log, broker audit, first live read | bridge owner |
| Host catalog | Tool discovery, schema, permissions, and refresh behavior are current | high | tools change, package rebuilds, host config changes, or catalog appears stale | tools/list snapshot, build stamp, reload transcript | host owner |
| MCP 2026 watchlist | Future-dated MCP material is still non-final or has been finalized and integrated | high | final 2026-07-28 spec or official host support changes | `mcp-2026-07-28-watchlist.md` reviewed, `[spec 2025-11-25 - revalidate]` assumptions refreshed, and quarantine cleared or retained | release owner |
| Carrier parity | Package state still matches source and installed host behavior | medium/high | source edits, package rebuild, import/install, host reload, or smoke result changes | manifest, install proof, host smoke, `carrier-parity-matrix.md` state | package owner |

## Fragility Rules

- `high`: auth, transports, SDK versions, remote hosts, Apps/Cowork/Antigravity behavior, security guidance.
- `medium`: CLI grammar, adapter contract, OpenAPI shape, plugin packaging.
- `low`: stable local templates and project conventions.

## Release Rule

Do not release or rely on a connector if a high-fragility assumption is unverified and affects the MVP path.

Future-dated or non-final sources stay in quarantine until rechecked.

Revalidation status is separate from capability status: `verified` here means the assumption was refreshed, not that an operation is safe or implemented.
