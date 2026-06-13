# Continuity From 2.2

Use this when promoting Rev3 lessons into an operational version without losing the 2.2 foundation.

## Rule

Rev3/v2.3 lessons extend the 2.2 base; they do not replace it.

Already active in 2.2:

- Gate 10 host-live states;
- Gate 11 bounded output;
- Gate 12 lifecycle observability;
- Gate 13 write-intent and placement-intent proof;
- Gate 14 cold-start acceptance;
- command availability and schema discovery;
- governance write ladder;
- rollback strategies;
- host busy/idle;
- relational create;
- UI field map and natural questions;
- Windows UTF-8 guardrail;
- package integrity and deploy live reload.

Promoted in 2.3 Fascia A:

- Gate 0.0 Domain Comprehension;
- Domain-Semantic Validation;
- resolver freeze and identity keys;
- false friends;
- source-registry depth;
- live-vs-persisted;
- embedded DB/WAL safe read;
- host-access asymmetry;
- acceptance evidence extension;
- packaging/deploy hardening refinement;
- cold-start measurement ledger.

Deferred until v3 evidence:

- changeset;
- engine-respecting write path;
- recompute;
- bulk-edit safe pattern;
- field allowlist;
- writable field introspection.

## Test

When changing the skill, mark each addition as `new`, `extends 2.2`, or `deferred/needs-evidence`. Do not duplicate 2.2 references into new files unless the new file adds a distinct rule.
