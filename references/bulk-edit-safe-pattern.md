# Bulk Edit Safe Pattern

Status: active-v3-candidate / needs-evidence
Class: pattern + reference

Use this before claiming a multi-record, batch, import, global change, or bulk update is write-ready.

## Problem

A single verified write does not prove a safe bulk edit. Bulk operations add row selection risk, partial failures, ordering effects, rate limits, transaction boundaries, identity remap, and rollback complexity.

## Rule

Bulk edit remains `needs-evidence` until a real sandbox slice proves the pattern end to end.

Minimum pattern:

```text
bounded query -> preview -> row-level selection -> identity freeze -> changeset -> approval -> apply -> readback -> recompute check -> report -> rollback/compensation scope
```

## Required Evidence

- bounded selection query;
- row count and sample preview;
- false-positive row that must not be touched;
- frozen stable IDs for every row;
- per-row before/after plan;
- protected-field checks;
- dry-run or preview;
- partial-failure behavior;
- transaction or compensation behavior;
- readback tier proportional to risk;
- rollback or compensation per row;
- final report with successes, failures, skipped rows, and claim scope.

## Stop Rules

Stop if:

- selection is unbounded;
- preview cannot show the exact rows;
- rows are identified only by display label;
- partial failure behavior is unknown;
- rollback is only "restore everything" when a smaller compensation is required;
- one-row evidence is used to claim bulk readiness.
