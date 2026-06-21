# MCP 2026-07-28 Watchlist

Use this reference when MCP protocol 2026-07-28, release-candidate material, or future MCP v2 behavior could affect connector design.

As of 2026-06-21, treat the 2026-07-28 material as high-fragility and non-final for Connector Forge V1. Do not claim compliance until the final specification, SDK support, and host behavior are revalidated.

## Current Stance

Connector Forge OneMaster V1 integrates MCP procedure internally now. It does not wait for the future protocol release.

Baseline marker used by V1 spec-sensitive references: `[spec 2025-11-25 - revalidate]`.

Allowed claim:

```text
Connector Forge OneMaster V1 includes a self-contained MCP procedure and marks MCP 2026-07-28 as a high-fragility watchlist area to revalidate after final specification and host support.
```

Forbidden claims:

- "MCP 2 ready";
- "2026-07-28 compliant";
- "supports future Apps/Tasks";
- "stateless compliant";
- "all hosts support the new auth/transport behavior".

## Core-First / Carrier-After Rule

Protocol upgrades start in the shared core, not in host packaging.

For MCP 2026-07-28 or later material, update and revalidate the shared core first:

- `mcp-branch.md`;
- `mcp-procedure-track.md`;
- `mcp-remote-first-baseline.md`;
- `mcp-inspector-lab.md`;
- `assets/templates/MCP_TOOL_CATALOG.json`;
- `revalidation-matrix.md`;
- `security-mesh.md` when auth, scopes, approval, or write risk changes.

Only after the core is stable may host packs and carrier lanes be propagated. Each carrier keeps its existing state in `carrier-parity-matrix.md` until package evidence, install/reload proof, host discovery, smoke, and recovery evidence justify promotion.

## Watchlist Areas

| Area | Why it matters | Forge action |
|---|---|---|
| Protocol state | Future material may change session and initialization assumptions | keep app state explicit; do not hardcode session stickiness |
| State handles | App state may move to explicit handles | require owner, scope, TTL, risk class, cleanup, and audit for handles |
| Server-to-client input | Elicitation/confirmation patterns may change | bind human input to intent contract and original request |
| Routing and traceability | Future HTTP headers, cache metadata, and trace context may affect brokers | add to lifecycle/audit when final |
| Extensions | Apps, Tasks, and future features may be extension-negotiated | distinguish core MCP from extensions |
| Apps/UI | Server-rendered UI may create new consent and sandbox duties | route through security mesh and UX acceptance |
| Long-running tasks | Task handles may replace blocking calls | define task handle discipline and cancellation evidence |
| Authorization | OAuth/OIDC hardening may affect issuer/client registration behavior | revalidate issuer, client type, scopes, resource/audience, refresh |
| Deprecations | old Roots/Sampling/Logging/SSE assumptions may be deprecated or downgraded | avoid new designs built on deprecated assumptions |
| JSON Schema | richer schema support may affect catalog templates | bound schema depth/time and avoid unsafe external refs |
| Error codes | protocol errors may change | tests should assert class/meaning, not only old numeric codes |
| Host support | clients may adopt features at different speeds | host-capability matrix must remain dated and evidence-based |

## Revalidation Triggers

Revalidate when:

- final 2026-07-28 spec is published;
- MCP SDKs used by the project update;
- Codex, Claude/Cowork, ChatGPT Apps, Antigravity, Gemini, or target host changes MCP behavior;
- auth/client registration docs change;
- a connector uses future tasks/apps/extensions;
- a package claims public/GitHub-ready or production-ready status.

## Revalidation Checklist

- final spec read and source dated;
- current SDK support checked;
- host-specific behavior checked in real host;
- `MCP_TOOL_CATALOG.json` template reviewed;
- `mcp-branch.md` baseline updated;
- remote-first baseline and auth rules updated;
- Inspector/host smoke re-run;
- package integrity and carrier parity rechecked;
- changelog and claim audit updated.

## Quarantine Rule

Future-dated, release-candidate, draft, or contradictory information stays in `quarantine` in the Revalidation Matrix. It may guide design caution, but it is not release acceptance.

## Claim Limits

This file is a watchlist, not an implementation claim and not a compliance claim.
