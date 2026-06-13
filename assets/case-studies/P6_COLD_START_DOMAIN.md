# P6 Cold-Start Domain Case Study

Status: sanitized field evidence for connector-forge v2.3 Fascia A. This is not a P6 manual.

## What It Tested

P6 Professional 25 was used as a cold-start app to see whether connector-forge could choose a surface and produce useful doubts without being pre-loaded with the final answer.

## What Worked

- The method converged on hybrid/local control rather than blind MCP-only.
- Direct DB writes were treated as forbidden until an app engine/API proves safe write.
- Read-only inspection found real structure and produced a useful doubt list.
- Cross-agent work exposed host-access asymmetry.

## What Failed Or Needed Expert Input

- A technical count of `PROJECT` records was initially too easy to read as "projects".
- Domain structure had to distinguish EPS, projects, templates, and baselines.
- "Current/open project" is live state, not necessarily persisted DB truth.
- The deeper write surface required checking P6 Professional Integration API rather than stopping at no visible REST endpoint.

## Promoted Lessons

- Gate 0.0 Domain Comprehension.
- Domain-Semantic Validation.
- False-Friends Register.
- Source Registry Depth.
- Live State vs Persisted State.
- Embedded DB / WAL Safe-Read Pattern.
- Host Access Asymmetry.
- Cold-Start Measurement Ledger.

## Deferred

Write-path lessons remain draft/needs-evidence until a P6 bridge proves an engine-respecting write with sandbox, readback, and rollback/recovery.
