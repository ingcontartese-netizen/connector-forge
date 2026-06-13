# ChangeSet Contract

Status: active-v3-candidate / needs-evidence for bulk, evidenced for single-operation guarded writes
Class: principle + template

Use this reference before any write that creates, clones, imports, modifies, links, deletes, moves, bulk-edits, or changes dependent state.

## Problem

Moving directly from a natural-language request to a mutation hides the real plan: wrong target, wrong rows, unwritable fields, unintended side effects, derived state, and undefined rollback.

## Rule

Every non-trivial write becomes an explicit changeset before apply.

A changeset declares:

- requested intent;
- target identities and resolver evidence;
- operation type;
- fields to write;
- protected fields and invariants;
- expected before state;
- expected after state;
- side effects and recompute needs;
- readback plan;
- rollback or compensation plan;
- approval requirement;
- claim scope.

## Single Operation

Even one field update may need a changeset when the domain is non-trivial, the actuator is high-risk, derived state exists, or collateral changes are possible.

## Bulk Or Multi-Object Operations

Bulk edit is never inferred from single-operation evidence. Bulk remains `needs-evidence` until:

- row selection is bounded and previewed;
- identities are frozen per row;
- each row has before/after expectations;
- partial failure behavior is known;
- rollback or compensation is scoped per row;
- readback can detect target and collateral changes.

## Acceptance

A changeset is apply-ready only when:

- every target identity is frozen;
- field allowlist and protected rules pass;
- required/writable field evidence exists;
- dry-run or preview exists, or the lack is explicitly risk-accepted;
- approval is recorded outside the target app surface;
- readback is defined before apply;
- rollback/recovery readiness matches risk.

## Stop Rules

Stop if:

- the requested write cannot be represented as a bounded changeset;
- target identities are labels only;
- protected fields are not checked;
- recompute/derived state is unknown and relevant;
- rollback is undefined;
- the release claim would round a single-operation proof into bulk readiness.
## OneMaster Draft Addendum

Changesets for domain apps must include semantic blockers, not only field diffs. If a write depends
on provider freshness, scoring method, fiscal period, approval lane, or derived state, those
conditions belong in the changeset contract before apply.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-22, OMD-M-27; tags
APP / BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
