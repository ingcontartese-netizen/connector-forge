# MCP Branch

Use this branch when the target connector must be an MCP server, remote broker, ChatGPT App, Claude/Cowork connector, Antigravity/Gemini integration, or cross-host tool catalog.

## Current Baseline

As of 2026-05-30, use MCP spec `2025-11-25` as the verified baseline. Revalidate before release.

Core areas to check:

- transports: stdio and Streamable HTTP;
- remote endpoint commonly `/mcp`;
- `MCP-Session-Id` is optional but must be preserved after initialize when returned;
- HTTP requests after initialize must include `MCP-Protocol-Version`;
- resumability uses SSE event IDs / `Last-Event-ID` when supported;
- OAuth 2.1 for production remote servers;
- protected resource metadata, Client ID Metadata Documents when available, DCR fallback, scopes, token audience/resource;
- `tools/list`, `tools/call`, input/output schema;
- structured output and error separation;
- annotations treated as hints, not trusted security facts.

## Use Specialist Library

For detailed MCP design, read the installed skill:

`~/.codex/skills/mcp-connector-builder/SKILL.md`

Use its references for Gate 0 dossier, host-primary selection, Inspector, auth, broker/bridge, packaging, and field lessons.

## Build Sequence

1. Confirm the adapter contract.
2. Create `MCP_TOOL_CATALOG.json`.
3. Expose read-only tool first.
4. Validate with Inspector/API Playground or host-equivalent.
5. Add auth and scopes.
6. Add write tools only with confirmation and audit.
7. Package for the primary host.

## Remote MCP Safety

- Validate Origin for local HTTP.
- Bind local servers to localhost unless explicitly remote.
- Do not pass through raw upstream tokens.
- Use least privilege scopes.
- Keep session/auth assumptions in Source Registry.

## Rev2 Patterns

- Async Tasks are experimental in spec `2025-11-25`; use them only when `capabilities.tasks` declares support. Fall back to timeboxed synchronous calls.
- Elicitation Form mode is for structured missing data or confirmations; never use Form mode for credentials. Prefer URL mode for OAuth/sensitive auth flows where supported.
- Roadmap/RC/future features stay in the Revalidation Matrix as watchlist, not release acceptance.

## OneMaster Draft Addendum

For domain apps with many specialist operations, prefer a small facade plus specialist tools:
read, simulate, propose, manage/apply as the user-facing mental model; specialists can exist under
that model only when capability state, side-effect class, and bounded output are explicit. MCP
tool catalogs are contracts, not proof of implementation.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-15, OMD-M-16,
OMD-M-25; tags BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
