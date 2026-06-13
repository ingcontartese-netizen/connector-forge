# Engine-Respecting Write Path

Status: active-v3-candidate / include-now
Class: decision rule

Use this before any persistent write to a source-of-truth application, project file, local database, schedule, model, ERP, CRM, finance system, or regulated workflow.

## Problem

Real applications are not just data containers. They have engines: validation, transactions, scheduling, geometry, permissions, audit, cache, object identity, and derived state.

Writing to the wrong store can appear to work while bypassing the engine that makes the state valid.

## Rule

Choose the write surface that respects the app engine for the actual data source and operation.

Preference order:

1. official API/SDK that applies validation and side effects;
2. native command, plugin, or add-on that creates real app objects;
3. official import/export workflow validated by the app;
4. vendor CLI or supported script;
5. DB/file write only if documented, supported, transactional, and recoverable for the actual data source;
6. UI/browser/computer-use actuator only when no better authorized surface exists and the workflow is stable, tokened, and testable.

Direct private datastore writes are forbidden unless the vendor explicitly authorizes that write path for the actual data source.

## Evidence Required

For the chosen write surface, record:

- which engine or validator is respected;
- which native validations/side effects run;
- which derived outputs may need recompute;
- why lower-authority alternatives were rejected;
- rollback/recovery route;
- readback path.

## Stop Rules

Stop if:

- the write bypasses the only engine that can validate the object;
- the surface supports another data source but not the actual one;
- success would be inferred from a raw table/file update;
- the app requires scheduling/recompute/audit and the bridge cannot trigger or record it;
- the claim says API-supported when only file/UI/human-assisted action was proven.
## OneMaster Draft Addendum

For proposal-governed apps, prefer the app's native proposal/action path or documented API path
over direct persistence. A bridge can prepare, preview, or propose changes, but apply belongs to
the app engine or an explicitly approved interim actuator with readback and rollback.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atom OMD-M-10; tags APP / BRIDGE /
G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
