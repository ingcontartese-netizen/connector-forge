# Changelog - connector-forge

## OneMaster V1 public working source - 2026-06-21

Integrated the MCP procedure into Connector Forge as an internal, self-contained method path for ordinary MCP connector design. This is the public GitHub working-source release, not a production/package/carrier-parity/host-live claim.

Added:

- MCP internal hub and procedure references for branch choice, Gate 0 to Sprint 1 flow, artifact matrix, Inspector checks, remote-first baseline, field lessons, carrier parity, and future protocol watchlist.
- Carrier parity governance with explicit source/package/installed/host-loaded/host-live layers and canonical carrier states.
- MCP 2026-07-28 watchlist with `[spec 2025-11-25 - revalidate]` markers and core-first / carrier-after upgrade rule.
- Merge deltas into security, host packs, host capability, package integrity, revalidation, and go-live gates.

Updated:

- `SKILL.md` now routes MCP work through internal Forge references instead of an external specialist dependency.
- `mcp-branch.md` is the self-contained MCP hub and uses `mcp-procedure-track.md` as the source of truth for detailed procedure.
- `claim-audit.md` scopes the self-contained MCP claim and keeps production, package, carrier parity, host-live, and future protocol claims gated.
- `SHA256SUMS_ONEMASTER_V1.txt` is regenerated outside the skill folder for the current OneMaster V1 working source; delivered/source manifests remain historical evidence.

Deferred:

- script/scaffold wave, including repository skeleton material;
- carrier package rebuild/import/install/reload smoke;
- MCP 2026-07-28 final-spec adoption until the final specification, SDKs, and host behavior are revalidated.

Claim limits:

- Earned: Connector Forge working source contains an internal MCP design method and no longer requires an external MCP specialist skill for ordinary MCP procedure.
- Earned: public GitHub working-source publication after no-secret audit, sanitized case studies, Apache-2.0 license/NOTICE, README/changelog reconciliation, install/test evidence, and Giuseppe sign-off.
- Not claimed: production-ready, package-ready, carrier parity, host-live parity, deployed endpoint, live connector, or MCP 2026-07-28 compliance.

## OneMaster Draft - Codex active lane - 2026-06-03

Promoted method/spec lessons from the ValuAziende learning bench, legacy bridge study, and MCP+CLI guide study into the Codex active skill lane.

Added:

- Engine-respecting read path reference.
- Generational connector evolution reference.
- Bridge Doctor target-pattern reference.
- Collaborative handoff reference.
- Old/new parity matrix template.
- ValuAziende OneMaster Draft sanitized case study, separate from the legacy ValuAziende MCP deployment case study.

Updated:

- Front-door claim state for OneMaster Draft.
- Release and claim-audit wording to keep Draft, Ready, Deployed, package, public, and carrier-parity claims separate.
- Host, packaging, lifecycle, governance, readback, and evidence references with ValuAziende-derived method lessons.

Claim limits:

- This is OneMaster Draft active in the Codex lane only.
- It is not OneMaster Ready, Deployed, package-ready, public/GitHub-ready, or Cowork parity evidence.
- ValuAziende Bridge V2 implementation, CLI/MCP parity, governed write smoke, no-secret audit, package/install/reload evidence, and Cowork package parity remain separate gates.

## 3.0.0-candidate R3 Codex active lane - 2026-06-02

Migrated the R3 write-path method into the active Codex skill lane after P6 Fascia B evidence and Giuseppe Pass A approval.

Added:

- ChangeSet Contract and Engine-Respecting Write Path references/templates.
- `recompute_required` derived-state gate.
- Field allowlist, protected rules, and required/writable field introspection.
- Host Actuator Layer, Actuator Trust Boundary, Actuator Contract, and Host Actuator Matrix.
- Risk-Proportional Readback with rollback-readiness proportional to actuator risk.
- Operating Knowledge Gate and Operating Manual for command semantics, units, progress/status methods, side effects, and recompute.
- Unit Calibration Gate for numeric/date/duration/percentage/rate/currency/quantity/progress writes.
- Live Capability Ladder / live co-operation discipline.
- Release Claim Audit and zero-drift claim rules.
- P6 Fascia B sanitized case-study evidence.
- Updated Codex host pack and `connector-toolsmith` helper skill instructions.

Claim limits:

- This is a Codex active migration candidate, not public/GitHub-ready.
- Cowork/plugin pack parity, package build, install/reload smoke, no-secret audit, and ValuAziende API-native bench remain separate gates.
- P6 evidence proves governed sandbox single-operation patterns only; no production P6 connector, no true bulk edit, and no generic P6 API on standalone SQLite are claimed.

## 2.3.0 field-tested Fascia A - 2026-06-01

Promoted the comprehension layer from Rev3 draft after the P6 cold-start lessons. This is an operational increment on top of 2.2, not full v3.

Added:

- Gate 0.0 Domain Comprehension.
- Domain-Semantic Validation for user-facing counts/lists/details.
- `DOMAIN_MODEL`, `FALSE_FRIENDS_REGISTER`, `ACCEPTANCE_EVIDENCE_EXTENDED`, and `COLD_START_MEASUREMENT_LEDGER` templates.
- References for resolver freeze, false friends, source-registry depth, live-vs-persisted, embedded DB/WAL safe reads, host-access asymmetry, acceptance evidence extension, packaging/deploy hardening, cold-start ledger, and case-study index.
- P6 cold-start case study as sanitized evidence of the comprehension gap.
- Codex `connector-verifier` checklist for v2.3 source/package checks.

Deferred:

- Fascia B write-path remains `needs-evidence` until the P6 bridge proves it in sandbox: changeset, engine-respecting write path, recompute, bulk-edit, field allowlist, and writable field introspection.
- `deployment-ready` / public GitHub-ready claim still requires later bridge evidence and final v3 consolidation.

## 2.2.0 field-tested - 2026-05-31

Joint freeze by Claude/Cowork and Codex. Field-tested on:

- Archicad: hybrid local bridge with native write, placement correction, readback, rollback scope, and cross-read.
- ValuAziende: MCP reuse, backend/frontend distinction, bounded output, lifecycle lessons, UI field mapping, and governed write flow.

Added:

- Gate 13 Write Intent Proof.
- Gate 14 Cold-Start Acceptance.
- `write-intent-proof`.
- `command-availability-matrix`.
- `command-schema-discovery`.
- `governance-write-ladder`.
- `rollback-strategies`.
- `host-busy-idle`.
- `relational-create`.
- `INTENT_CONTRACT`.
- Case studies: `ARCHICAD_HYBRID_REAL`, `VALUAZIENDE_MCP_DEPLOY`, `COLD_START_TEMPLATE`.
- `declared_limits` and native/proxy classes in capability evidence.
- Canonical operation risk classes and availability states.
- Security Mesh controls for v2.2 write paths.

Not yet:

- `deployment-ready` or public/GitHub-ready claim. Requires Gate 14 cold-start on an app not pre-studied in this project.
- Package regeneration. Repackage once after cold-start.

## 2.1.0 pre-deployment - 2026-05-30

Added host-live states, bounded-output Gate 11, lifecycle observability Gate 12, cache-bust/build-stamp, package integrity, UI field mapping, and natural user question acceptance.

## 2.0.0 Rev2

Added go-live gates, CLI/MCP/Hybrid decision engine, Security Mesh, anti-cutoff method, and revalidation matrix.
