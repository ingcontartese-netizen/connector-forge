# MCP Branch

Use this branch when a connector must expose operations through MCP, a local MCP host, a remote broker, a remote MCP host, ChatGPT Apps, Claude/Cowork connectors, Antigravity/Gemini, or a cross-host tool catalog.

This is the Connector Forge MCP hub. It routes ordinary MCP design to the internal Forge references below.

## Branch Role

This file answers three questions:

1. Should the connector use MCP as the exposure layer?
2. Which MCP path applies: local-first, remote-first, or hybrid?
3. Which Forge references must be loaded next?

MCP is never the whole connector. The connector remains:

```text
official app surface -> domain adapter -> MCP server/broker -> host pack -> acceptance evidence
```

Start from the common Forge funnel before this branch:

```text
Gate 0.0 Domain Comprehension -> Gate 0 -> Source Registry -> Surface Map -> Capability Ledger -> Decision Engine -> MCP Branch
```

## Current Baseline

As of 2026-06-21, use MCP spec `2025-11-25` as the verified baseline for Connector Forge V1. Revalidate before release.

Spec-sensitive baseline marker: `[spec 2025-11-25 - revalidate]`.

Core baseline areas to check:

- transports: `stdio` and Streamable HTTP;
- remote endpoint commonly `/mcp`;
- `MCP-Session-Id` is optional but must be preserved after initialize when returned;
- HTTP requests after initialize must include `MCP-Protocol-Version`;
- resumability uses SSE event IDs / `Last-Event-ID` when supported;
- OAuth 2.1 or host-approved auth for production remote servers;
- protected resource metadata, client metadata / registration behavior, scopes, token audience/resource;
- `tools/list`, `tools/call`, input/output schema;
- structured output and protocol/tool error separation;
- annotations treated as hints, not trusted security facts.

Future MCP 2026-07-28 material is non-final for this V1 lane. Keep it in `mcp-2026-07-28-watchlist.md` and `revalidation-matrix.md`; do not claim future compliance.

## Internal Reference Map

| Need | Read |
|---|---|
| MCP procedure, Gate 0 dossier, pattern choice, build sequence, operating contract | `mcp-procedure-track.md` |
| Required artifacts by host family | `mcp-artifact-matrix.md` |
| Inspector / harness proof before host packaging | `mcp-inspector-lab.md` |
| Public endpoint, broker, auth, remote host, desktop bridge | `mcp-remote-first-baseline.md` |
| Carrier states, parity claims, package lag | `carrier-parity-matrix.md` |
| Field-tested lessons for live SDKs, desktop apps, refresh, UTF-8 | `mcp-field-lessons.md` |
| Future MCP protocol watchlist | `mcp-2026-07-28-watchlist.md` |
| Auth, secrets, tool catalog security, write policy | `security-mesh.md` |
| Host packaging rules | `host-packs.md` |
| Host capability screen | `host-capability-matrix.md` |
| Package/release integrity | `package-integrity.md` |
| Revalidation rows for fast-moving assumptions | `revalidation-matrix.md` |
| Readiness and go-live gates | `go-live-gates.md` |

## Branch Decision

Use MCP when the user needs tools surfaced inside an MCP-capable host, a remote connector, a host-packaged tool catalog, or a broker/bridge pattern.

Prefer another branch when:

- a local CLI is enough and no host tool catalog is needed;
- a direct API integration is the primary product and MCP would only wrap it prematurely;
- a file workflow or browser automation is the only authorized surface;
- there is no real host, test environment, auth owner, or MVP tool list.

For MCP:

1. choose one primary host for Sprint 1;
2. decide local-first, remote-first, or hybrid;
3. keep one domain adapter and vary transport/auth/packaging per host;
4. build the smallest read/state/export slice first;
5. add writes only after dry-run/proposal, approval, readback, audit, and rollback scope exist.

## Minimum Evidence

Before coding or packaging, capture:

- Gate 0 MCP dossier;
- official app surface and adapter contract;
- primary host and transport choice;
- auth model, scopes, secret location, and approval owner;
- MVP tool list, normally no more than five tools;
- `MCP_TOOL_CATALOG.json` or equivalent public tool contract;
- risk class and bounded-output controls for every tool;
- expected artifacts from `mcp-artifact-matrix.md`;
- acceptance evidence path.

Before calling a slice ready, capture:

- Inspector or host-equivalent proof;
- real host discovery and one read smoke;
- export/preview artifact when in scope;
- dry-run/proposal and audit when writes exist;
- recovery proof or explicit `N/A`;
- carrier state from `carrier-parity-matrix.md`;
- current revalidation status for high-fragility assumptions.

## Build Sequence

Do not maintain a second detailed procedure in this hub. Use `mcp-procedure-track.md` as the source of truth for the detailed Gate 0 dossier, build sequence, tool catalog discipline, write governance, and operating stop rules.

Hub-level routing sequence:

1. prove Gate 0, adapter contract, and primary host;
2. choose local-first, remote-first, or hybrid;
3. build the smallest bounded read/state/export slice;
4. validate discovery and one live read in Inspector or host-equivalent harness;
5. add governed writes only after proposal/dry-run, approval, readback, audit, and rollback scope;
6. package one primary host and record acceptance evidence.

## Local, Remote, And Hybrid Rules

Use `mcp-procedure-track.md` for pattern choice and `mcp-remote-first-baseline.md` for endpoint, broker, auth, and remote-host evidence.

Branch-level invariants:

- local-first keeps workstation apps, files, repos, and secrets local, normally through `stdio`;
- remote-first needs a reachable HTTPS endpoint, auth discovery, policy, audit, and host smoke;
- hybrid needs both sides: local bridge health plus remote broker reachability, policy, and lifecycle evidence.

Do not pretend a cloud host can reach a private desktop app directly. Do not pass target-app tokens through the client. Do not call a config snippet a host pack.

## Tool Catalog Discipline

Use `mcp-procedure-track.md` for the full tool catalog checklist and `security-mesh.md` for auth, secret, data, and write-risk review.

Branch-level invariant: every tool must be concrete, typed, risk-classed, bounded, auth-scoped, data-classed, and error-separated.

Avoid generic raw dispatch, unrestricted query, raw shell, arbitrary file, or broad API gateway tools as stable user-facing tools.

## Rev2 And Future-Feature Patterns

- Async Tasks are experimental in spec `2025-11-25`; use them only when the host and server declare support. Fall back to timeboxed synchronous calls.
- Elicitation/Form-style input is for structured missing data or confirmations; never use it for credentials. Prefer an auth URL or host-approved sensitive-auth path where supported.
- Roadmap, RC, future Apps/Tasks/extensions, or future protocol features stay in `mcp-2026-07-28-watchlist.md` and `revalidation-matrix.md`, not release acceptance.

## Stop Rules

Use `mcp-procedure-track.md` and `go-live-gates.md` for the full stop list. At the hub level, stop if:

- Gate 0 is incomplete;
- primary host is not chosen;
- target app surface is not official, authorized, or verified;
- auth, scopes, secret storage, or approval owner is theoretical;
- transport choice does not match host reachability;
- tool catalog is generic, unbounded, or schema-opaque;
- Inspector or host-equivalent harness cannot discover the catalog;
- host pack has no runtime entrypoint or host smoke;
- write path lacks dry-run/proposal, approval, readback, audit, or rollback scope;
- future protocol behavior is needed but still in watchlist/quarantine.

## OneMaster Draft Addendum

For domain apps with many specialist operations, prefer a small facade plus specialist tools:
read, simulate, propose, manage/apply as the user-facing mental model. Specialists can exist under that model only when capability state, side-effect class, and bounded output are explicit. MCP tool catalogs are contracts, not proof of implementation.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-15, OMD-M-16, OMD-M-25; tags BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.

## Claim Limits

This hub provides internal MCP routing for Connector Forge. It does not prove that an MCP server, broker, host pack, package, remote endpoint, or carrier lane exists, works, is installed, is host-loaded, is host-live, or is ready for public/GitHub release.
