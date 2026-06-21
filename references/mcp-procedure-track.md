# MCP Procedure Track

Use this reference when the chosen connector branch must expose operations through MCP, a remote broker, a local MCP host, a remote MCP host, or another MCP-capable client.

This is the self-contained MCP procedure inside Connector Forge. Do not depend on a separate MCP specialist skill for ordinary MCP design.

## Core Rule

MCP is not the connector by itself. The reusable connector is:

1. official app surface;
2. domain adapter;
3. optional local bridge or site agent;
4. MCP server or broker;
5. host pack;
6. acceptance evidence.

Start from the common Forge funnel before this branch:

```text
Gate 0.0 Domain Comprehension -> Gate 0 -> Source Registry -> Surface Map -> Capability Ledger -> Decision Engine -> MCP Branch
```

If the app target, host, surface, auth, test environment, or MVP tool list is unknown, stop and fill the dossier before writing server code.

## Gate 0 MCP Dossier

Minimum required fields:

- app target, version, edition, and owner;
- operating systems and runtime environment;
- primary host for Sprint 1;
- local-first, remote-first, or hybrid mode;
- official app surface: API, SDK, plugin, add-on, CLI, file workflow, or supported automation layer;
- transport: `stdio`, Streamable HTTP, or host-specific remote endpoint;
- auth model, secret location, scopes, and approval owner;
- real test instance and sample data/file;
- MVP tool list, normally no more than five tools;
- human approver for governed or destructive writes;
- expected artifacts and evidence path.

If any item is generic, unverifiable, or ownerless, Gate 0 is `HOLD`.

## Host And Pattern Choice

Pick one primary host for Sprint 1.

| Pattern | Use when | Transport baseline | Extra requirement |
|---|---|---|---|
| Local-first | app, files, repo, or secrets stay on the workstation | `stdio` | local config and host smoke |
| Remote-first | cloud/client reaches a public endpoint | Streamable HTTP over HTTPS | auth discovery, audit, rate limits |
| Hybrid | app is local but host is remote-first | local bridge plus remote broker | bridge health, broker policy, reachability proof |

Do not let the first sprint target many hosts. Secondary hosts come after the primary host has real evidence.

## Gate 0 To Sprint 1 Walkthrough

For a custom financial analysis platform:

1. Gate 0 names the internal web app, staging instance, masked datasets, primary host, auth owner, and MVP tools.
2. Pattern choice is internal API/business service, read-first and export-first.
3. Minimum artifact family is adapter, MCP server, one host pack, and smoke evidence.
4. Strong Sprint 1 proves server start, discovery, state/context read, preview/simulate, export artifact, and one local host pack.
5. Acceptance captures Inspector transcript, sample output, exported artifact, host smoke, and recovery notes for missing auth, missing dataset, and stale context.

Do not use production credentials, direct database writes, generic query tools, multiple hosts, or approval-free persistence in Sprint 1.

## Build Sequence

1. Create or update `PROJECT-KNOWLEDGE.md`.
2. Confirm adapter contract: session, stable IDs, active context, lock state, export path, health, typed errors, audit payload.
3. Create `MCP_TOOL_CATALOG.json` or equivalent public tool contract.
4. Bring up minimal health/version.
5. Add state introspection.
6. Add one read tool with stable structured output and bounded payload.
7. Add one export or preview tool with verifiable artifact.
8. Add safety: `dry_run`, `prepare/commit`, or proposal governance before any meaningful write.
9. Validate in Inspector before relying on the final host UI.
10. Package one primary host.
11. Capture acceptance evidence and update project knowledge.

## Tool Catalog Discipline

Every tool must have:

- concrete "Use this when..." description;
- narrow input schema, enums where possible, and stable output shape;
- risk class: `read`, `write-safe`, `write-governed`, `write-destructive`, or `open-world`;
- bounded output fields: `limit`, `page_size`, `fields`, cursor, summary, or artifact path;
- declared auth/scopes and data class;
- error model that separates protocol/transport errors from tool execution errors.

Do not expose generic raw dispatch, unrestricted query, raw shell, arbitrary file, or broad API gateway tools as stable user-facing tools.

## Operating Contract

- Run discovery before action: initialize/discover, tools list, resources list when relevant.
- Do not invent tool names, object IDs, scopes, command names, or resource IDs.
- Treat host and app behavior as authoritative when it differs from the abstract spec.
- Keep one domain adapter and vary transport/auth/packaging per host.
- Use project knowledge for working payloads, command aliases, restart notes, and failed hypotheses.
- Share only public contracts across parallel bridge/agent work before convergence.
- In regulated systems, writes must be semantically equivalent to legitimate in-app user actions.
- If a domain brain or operating manual exists, load it before drafting governed narrative fields or judgment content.

## Write Governance

Default path:

```text
read -> simulate/preview -> propose or dry_run -> approve -> apply -> readback -> audit
```

Use Forge write references for source-of-truth operations:

- `security-mesh.md`
- `write-intent-proof.md`
- `governance-write-ladder.md`
- `engine-respecting-write-path.md`
- `recompute-required.md`
- `unit-calibration-gate.md`
- `risk-proportional-readback.md`

Dry-run and commit should be separate operations when the mutation is significant. A mutation result without readback and audit is not a readiness proof.

## Stop Rules

Stop if:

- Gate 0 is incomplete;
- primary host is not chosen;
- app reachability does not match host behavior;
- auth pattern is theoretical only;
- Inspector cannot discover the tool catalog;
- state introspection is missing;
- write path lacks dry-run, approval, rollback, or audit;
- tool output is unbounded;
- host pack is only a config snippet with no runtime entrypoint or host smoke;
- remote-first connector lacks HTTPS, auth discovery, policy, or audit story.

## Related References

- `mcp-artifact-matrix.md`
- `mcp-inspector-lab.md`
- `mcp-remote-first-baseline.md`
- `carrier-parity-matrix.md`
- `mcp-field-lessons.md`
- `mcp-2026-07-28-watchlist.md`
- `host-packs.md`
- `host-capability-matrix.md`
- `go-live-gates.md`

## Claim Limits

This reference is method guidance. It does not prove a deployed MCP server, host-loaded package, production readiness, package parity, or public/GitHub readiness.
