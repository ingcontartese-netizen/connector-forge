# Glossary And Canonical States

Use this reference to avoid drift between adapter, capability, operation, tool, bridge, broker, and wrapper.

Prose can be localized, but machine values stay in canonical English.

## Core Terms

| Term | Canonical meaning |
|---|---|
| App target | Real system to connect: SaaS, API, desktop tool, workflow, repo, database, proprietary app. |
| Host AI | Environment using the connector: Codex, Claude Code, Cowork, ChatGPT Apps, Antigravity, Gemini, custom agent. |
| Surface | Authorized way to talk to the app: API, SDK, CLI, plugin, file workflow, read-only DB/report, bridge, MCP, UI fallback. |
| Capability | User/domain-level ability such as read state, search, export, prepare, update. |
| Operation | Implementable contract action with input, output, risk, auth, errors, and tests. |
| Adapter | Reusable domain core translating app concepts into safe operations. |
| CLI | Local, scriptable control plane with commands and machine-readable output. |
| MCP wrapper | MCP exposure of selected adapter operations. |
| Bridge | Local process/plugin talking to a desktop or proprietary app. |
| Broker | Remote server reachable by cloud/remote hosts. |
| Hybrid | Bridge plus broker, or CLI first and MCP later. |
| Tool | Host-exposed callable function with schema and side-effect contract. |
| Host Pack | Host-specific install/use artifacts. |
| Claim Audit | Check against absolute or unproven promises. |

## Capability/Operation States

- `verified`: proven by primary source, code, authorized probe, transcript, fixture, or repeatable test.
- `hypothesis`: plausible but not proven; do not expose as stable capability.
- `forbidden`: disallowed by scope, auth, ToS, license, policy, or security.

## Risk Classes

- `read`: reads state only.
- `safe`: preview/export/local artifact.
- `write-safe`: reversible or prepared write.
- `write-governed`: regulated/business-significant write requiring proposal, human approval, audit trail, and usually an idempotency key; direct mutation is forbidden.
- `write`: changes app or remote state.
- `write-destructive`: delete/reset/deploy/irreversible or high-impact action.
- `open-world`: broad action needing strict schema, allowlist, and human approval.

## Native/Proxy Classes

- `native_verified`: the operation creates or changes the app's real native/domain object and readback proves it.
- `native_hypothesis`: likely native, but not yet proven by live readback.
- `visual_proxy`: visual representation only; not a domain object.
- `metadata_only`: metadata/comment/note only; not the requested domain entity.
- `unsafe_generic`: broad/raw/generic gateway not safe as a stable user-facing tool.
- `forbidden_proxy_for_native_request`: the user requested a native/domain object and a proxy is not acceptable.

## Declared Limits

`declared_limits` is the Capability Ledger field that states what the connector cannot yet do.

Examples:

- can read and simulate but cannot apply;
- can create native objects only for listed types;
- can dry-run but cannot read back live;
- can use visual proxy only when the user explicitly accepts the downgrade.

Claims, README text, and tool metadata must not promise beyond `declared_limits`.

## Gate States

- `READY`: gate complete; proceed.
- `HOLD`: missing recoverable input; stop and ask/research.
- `BLOCKED`: cannot proceed without external change.

## Host-Live States

- `source_validated`: source code, contracts, templates, and local checks are valid.
- `fresh_process_validated`: the connector process was restarted or reloaded after source changes, so stale code/cache is not the active process.
- `host_loaded`: the primary host sees the expected server/connector and current tool catalog.
- `host_live_validated`: the primary host executed a real live operation and, when relevant, a recovery/error path.

These are deployment/readiness states, not capability truth states and not Revalidation Matrix freshness states.

## Desktop / Local Host States

- `HOST_BUSY`: app is alive but not idle because of user input, modal dialog, active command, lock, or transaction. Use bounded retry or ask the user to complete/cancel the current action.

## Revalidation States

- `open`: assumption not yet refreshed.
- `verified`: assumption checked with dated source/test.
- `quarantine`: future-dated, non-final, weak, or contradictory source/claim.

`verified` in a Revalidation Matrix and `verified` in a Capability Ledger are different axes: freshness versus operational proof.
## OneMaster Draft Addendum

Use these additional states when bridge source, schema, and runtime are not aligned:

- `schema_stale`: the advertised contract is behind or ahead of implementation.
- `adapter_stub`: route exists but returns not-ready or placeholder behavior.
- `planned_contract_only`: documented for future use, not implemented.
- `active_needs_test_evidence`: code exists but has no acceptance proof.
- `evidence_gated`: concept is accepted as a target pattern, but runtime proof is missing.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atom OMD-M-14; tags BRIDGE / G1 /
G6 / G7 / LAB; claim limit: method/spec evidence only.
