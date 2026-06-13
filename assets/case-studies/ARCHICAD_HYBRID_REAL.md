# Case Study: Archicad Hybrid Real

Date: 2026-05-31
Status: field-tested, sanitized
Purpose: record connector-forge lessons from a real desktop/native-write case without depending on private GUIDs or local paths.

## Scenario

Target app: Archicad 29 on Windows.

Goal: move beyond interrogation and create native app objects through an agent-controlled bridge, while proving intent and not just API success.

Branch selected: `hybrid`.

Reason: Archicad is a desktop app. The reliable surface was a local add-on/API bridge, exposed to agents through MCP tools. Direct remote MCP without the local app/add-on would not have reached the real project state.

## Surface Map Result

| Surface | Finding | Decision |
|---|---|---|
| Official/add-on API via Tapir Additional JSON Commands | Live add-on available after version check/upgrade to 1.4.0 | Primary write/read surface |
| MCP bridge | Useful host contract for Codex/Cowork | Wrapper around local bridge |
| CLI/Python local control | Useful diagnostic/control plane | Support layer |
| UI automation | Useful only for user-visible confirmation | Not primary |

## Field Sequence

1. Verified active project/app context.
2. Read live add-on status and version.
3. Discovered that dependency version matters: older add-on did not provide the required native write capability.
4. Upgraded dependency as a mini-deploy and revalidated live status.
5. Created a native Wall with dry-run first, then apply.
6. Read back GUID and geometry from the app.
7. Found a placement mismatch: length was correct, but location was not the user's intended reference.
8. Corrected by anchoring to the existing wall start point and reading real coordinates.
9. Closed a trapezoid by computing the final wall from real readback nodes, not by visual guess.
10. Cross-read from another bridge/host verified the same geometry.

## Lessons Promoted

- A native write must prove object class. A visual line/proxy is not a Wall.
- A write can pass length/dimension but fail placement intent.
- Gate 13 must include anchor/reference, orientation, relationship, context, readback, and visual/user-facing confirmation.
- Command availability has layers: documented, installed, live available, host exposed, dry-run verified, sandbox apply verified.
- Desktop apps can be busy with user input. `HOST_BUSY` is a real recovery state.
- Cross-host readback is strong evidence when multiple bridges exist.
- Dependency upgrades are mini-deploys: backup, restart, health/version, readback.

## Evidence Shape

Use this shape in future case-studies:

```text
intent -> surface decision -> command availability -> dry-run -> approval -> apply -> readback -> intent proof -> correction/rollback if needed -> cross-read when available
```

## Sanitization Rule

Do not publish:

- personal local paths;
- full private project names if sensitive;
- complete GUIDs unless test-only;
- screenshots containing private design data;
- proprietary bridge internals not meant for release.

## Connector-Forge Impact

This case supports:

- `write-intent-proof.md`;
- `command-availability-matrix.md`;
- `INTENT_CONTRACT.md`;
- Gate 13;
- `ACCEPTANCE_EVIDENCE.md` write intent section;
- `WORKING_PAYLOADS.md` write payload and recovery sections.
