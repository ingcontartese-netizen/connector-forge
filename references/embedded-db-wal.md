# Embedded DB / WAL Safe-Read Pattern

Use this for SQLite, Access, local DBs, cache databases, project files, or other embedded stores.

## Problem

Reading an embedded DB while the app is open can create stale snapshots, lock conflicts, partial reads, or confusion between checkpointed data and WAL/live state.

## Rule

Default to read-only. Never use direct DB writes as the control surface unless the vendor explicitly authorizes it and the engine-respecting write path has evidence.

Checklist:

- path verified;
- read-only mode verified;
- journal/WAL mode detected;
- lock behavior tested;
- live-vs-persisted limit declared;
- backup/export/snapshot alternative considered;
- no write direct-to-store unless explicitly allowed.

## SQLite Example

Prefer a URI such as `file:C:/path/app.db?mode=ro` for inventory reads. If the answer depends on WAL/live state, test whether the read mode sees that state and document the limit.

## Stop Rule

If a direct DB write would bypass app rules, triggers, recalculation, audit, or locks, mark it `forbidden` and use the app engine/API/import workflow instead.
## OneMaster Draft Addendum

For app-owned SQLite, local DB, or cache files, raw read-only inspection can support discovery, but
it does not automatically prove semantic truth. Direct DB writes to source-of-truth app data remain
forbidden unless the app explicitly documents that surface as its supported write engine.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-08, OMD-M-09,
OMD-F-01; tags APP / BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
