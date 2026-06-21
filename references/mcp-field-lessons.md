# MCP Field Lessons

Use this reference when a real MCP connector touches a desktop app, SDK wrapper, plugin/add-on, live host catalog, multi-bridge setup, or fast-moving integration surface.

This file preserves practical MCP lessons without turning the core procedure into a long case-study manual. Keep app-specific evidence in project case studies and `PROJECT-KNOWLEDGE.md`.

## Command Discovery

Docs are not enough for live command surfaces.

Use this loop:

1. read official docs;
2. inspect the installed app, add-on, plugin, or SDK version;
3. read source code or command registry when available;
4. probe one command at a time with minimal safe payload;
5. mine validation errors for real field names and wrappers;
6. write verified commands to `COMMANDS.md` and `WORKING_PAYLOADS.md`.

Do not promote doc-only command names, payload fields, aliases, or object IDs into stable tools.

## SDK Bypass Discipline

SDKs can have serialization or wrapper bugs. If the same payload works through a lower-level protocol but fails through the SDK:

- verify the SDK object serialization;
- keep SDK path for operations where it works;
- add raw protocol fallback only for verified gaps;
- document which path each command uses and why;
- keep both paths behind the adapter, not in the MCP server wrapper.

Do not call an SDK broken until a live comparison proves it.

## Domain Traps

Desktop and regulated systems often expose technical values that are not user-facing truth:

- display units may differ from storage/input/export units;
- IDs are safer than names;
- layer, story, selection, document, and active view affect writes;
- coordinate frames may be local, world, relative, or host-specific;
- derived outputs may require recompute, refresh, publish, schedule, or audit.

Use Forge references:

- `unit-calibration-gate.md`
- `resolver-freeze.md`
- `engine-respecting-write-path.md`
- `recompute-required.md`
- `risk-proportional-readback.md`

## API Incomplete: Seed vs Composite

When create primitives are missing, choose honestly:

| Pattern | Use when | Tool naming |
|---|---|---|
| Seed workflow | a real domain object must preserve native properties and an operator can provide a seed | name the dependency, such as `create_from_seed` |
| Composite operation | existing primitives can create an acceptable lower-fidelity result | declare proxy/limit in tool description |

Never satisfy a native-object request with a visual or metadata proxy unless the user explicitly accepts the downgrade.

## Host Refresh And Catalog Drift

After changes, verify all relevant layers:

- server process restarted or reloaded;
- host config/catalog refreshed;
- desktop app plugin/add-on loaded;
- bridge health/version reports expected build stamp;
- first live read succeeds.

Many "connector bugs" are stale catalog, stale process, or app-side plugin reload failures.

## Project Knowledge

Every real connector should keep durable knowledge:

- working payloads and command aliases;
- failed hypotheses;
- restart and refresh notes;
- known-good smoke steps;
- app version and host version;
- workaround limits and graduation path.

Chat history is not a project ledger.

## Batching, Timeouts, And Adapter Orchestration

Prefer one structured batch call over many tiny calls when the app surface supports batching.

Keep orchestration in the adapter or domain service, not by having one MCP tool call other MCP tools. Expose the final task-level operation as a bounded tool with progress, partial result, timeout expectations, and recovery notes when needed.

## Pagination And Adapter Signatures

Multi-bridge systems can diverge on pagination or method signatures.

Rules:

- define canonical pagination fields;
- support compatibility only deliberately;
- test canonical and fallback paths;
- verify whether an adapter uses `dispatch`, `execute`, or another method before wrapping it;
- do not assume every adapter exposes the same method signature.

## Windows And UTF-8

For Windows local bridges:

- set `PYTHONIOENCODING=utf-8` and `PYTHONUNBUFFERED=1` in host config;
- keep stdout protocol-clean;
- write diagnostics to UTF-8 files or controlled stderr;
- avoid secrets and large payloads in lifecycle logs;
- test rich text output before host acceptance.

Use `windows-utf8.md` and `transport-json-windows-cloudsync.md` for deeper Windows guidance.

## Stop Rules

Stop if:

- live command schema is unknown;
- an SDK bug is only guessed;
- workaround limitations are not declared;
- pagination parity is untested in a multi-bridge setup;
- a field lesson is app-specific but is being promoted into general Forge guidance without source limits.

## Claim Limits

This file preserves field-tested patterns. It does not prove capability for a new app, host, SDK, plugin, or package.
