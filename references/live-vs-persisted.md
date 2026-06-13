# Live State vs Persisted State

Use this when the question asks "what is open/current/running/selected/active now" or when a local app uses sessions, UI state, cache, locks, or WAL.

## Problem

Persistent stores describe saved state. Users often ask about live state. A DB/file query can be correct and still not describe what the app is showing now.

## Rule

For each capability, declare one of:

- `persisted`: file/DB/export/report state;
- `live`: process/session/UI/current document state;
- `hybrid`: persisted data plus live context.

State where live evidence comes from: app API, session API, window title, selected object, process probe, host tool, or typed error.

## Test

If a user asks for current/open/selected/active state, do not answer from persisted store alone unless the Domain Model says that store is authoritative for that live concept.
## OneMaster Draft Addendum

Before answering current, saved, generated, browser-local, runtime, or persisted questions, declare
the authoritative surface for the artifact. Durable database state, runtime process state,
browser-local drafts, generated reports, and UI-only selections are different truth surfaces.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atom OMD-M-05;
tags APP / BRIDGE / GIUSEPPE / LAB; claim limit: method/spec evidence only.
