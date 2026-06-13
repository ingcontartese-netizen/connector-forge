# Hybrid Branch

Use Hybrid when neither pure CLI nor pure MCP is enough.

## Patterns

CLI first, MCP later:

- build local CLI adapter;
- smoke test it;
- wrap selected commands as MCP tools;
- keep CLI as fallback and diagnostic surface.

Local bridge plus remote broker:

- local bridge talks to desktop/proprietary app;
- remote broker exposes constrained MCP tools;
- broker never receives broad local credentials unless required and approved;
- audit the handoff boundary.

Desktop app to remote host:

- prefer official SDK/API/plugin/add-on;
- use file workflow if official and stable;
- use browser/computer automation only as fallback;
- stop if the workflow cannot be made stable and authorized.

## Required Artifacts

- local bridge contract;
- broker contract;
- auth boundary description;
- failure mode table;
- smoke test on local side;
- MCP validation on remote side;
- drift report.

## OneMaster Draft Addendum

For app-native connector evolution, prefer an API-first core when the app already exposes or can
support governed domain actions. CLI and MCP can be twin carriers over the same core, but parity
between carriers is a design target until the shared operations are implemented and tested.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-08, OMD-M-16; tags
BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
