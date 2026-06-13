# Generational Evolution

Use this reference when a working connector, bridge, skill, host pack, or automation must evolve
without breaking the current generation.

## Core Rule

Do not overwrite a working connector generation to prove a new one. Build the next generation
side-by-side, compare it to the old generation, and retire the old one only after evidence and
owner approval.

## Pattern

1. Freeze the Legacy generation identity.
2. Baseline its golden operations before refactor or migration.
3. Create a clean new-generation nest with explicit identity and version.
4. Copy old code only as scaffold when useful, then relocate logic into the new structure.
5. Keep host plugs thin; shared domain logic belongs in one core.
6. Run old/new parity on read, simulate, propose, apply, logs, and failure paths that are in scope.
7. Keep both generations available until the owner approves archival or replacement.

## Required Artifacts

- generation manifest;
- old/new parity matrix;
- capability ledger per generation;
- drift report for host differences;
- release claim audit naming exactly which generation is active, installed, packaged, or only draft.

## Stop Rules

Stop the migration when:

- the old connector is still in real use and has no baseline;
- the new connector silently reuses the old identity;
- host-specific code contains domain logic;
- a case study merges two generations into one story and hides the claim boundary;
- the release wording says Ready or Deployed when only Draft evidence exists.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Draft, 2026-06-03.
- Ledger atoms: OMD-M-12, OMD-M-13, OMD-M-16, OMD-M-21, OMD-M-29, OMD-M-30.
- Tags: APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB.
- Claim limit: This is method/spec evidence. It does not prove a deployed bridge, package parity,
  production readiness, or public/GitHub readiness.
