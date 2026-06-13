# Old/New Parity Matrix

Use this template when a new connector generation is built beside a working Legacy generation.

## Identity

| Field | Legacy | New Generation | Evidence |
|---|---|---|---|
| Connector name |  |  |  |
| Generation label | Legacy | OneMaster |  |
| Source root |  |  |  |
| Host plug |  |  |  |
| Version/build stamp |  |  |  |
| Installed or source-only |  |  |  |

## Golden Operations

| Operation | Legacy Result | New Result | Parity State | Evidence | Notes |
|---|---|---|---|---|---|
| health |  |  | not_run |  |  |
| bounded read |  |  | not_run |  |  |
| detail read |  |  | not_run |  |  |
| simulate / preview |  |  | not_run |  |  |
| proposal create |  |  | not_run |  |  |
| approval / apply |  |  | not_run |  |  |
| logs / lifecycle |  |  | not_run |  |  |
| negative test |  |  | not_run |  |  |

Suggested parity states:

- `same`
- `same_with_declared_difference`
- `new_better`
- `new_missing`
- `legacy_missing`
- `blocked`
- `not_run`

## Side-Effect Classification

| Operation | Legacy Class | New Class | Mismatch? | Resolution |
|---|---|---|---|---|
|  | read_only / simulate / proposal / governed_apply / maintenance_write |  |  |  |

## Host Parity

| Host | Source Hash | Package Hash | Installed Identity | Smoke Result | Declared Differences |
|---|---|---|---|---|---|
| Codex |  |  |  |  |  |
| Cowork |  |  |  |  |  |
| Antigravity |  |  |  |  |  |

## Decision

| Question | Answer | Evidence |
|---|---|---|
| Can the old generation remain active? |  |  |
| Can the new generation be used for test work? |  |  |
| Can the new generation replace the old one? |  |  |
| Can the old generation be archived? |  |  |

## Stop Rules

Do not replace or archive the Legacy generation when:

- golden operations were not baselined before refactor;
- side-effect classes differ without owner approval;
- a host package is stale or unverified;
- source and installed copy diverge without a drift row;
- the new generation has not proven the user-facing workflows needed by the owner.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Draft, 2026-06-03.
- Ledger atoms: OMD-M-12, OMD-M-13, OMD-M-16, OMD-M-21, OMD-M-29, OMD-M-30.
- Tags: BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB.
- Claim limit: This is method/spec evidence. It does not prove a deployed bridge, package parity,
  production readiness, or public/GitHub readiness.
