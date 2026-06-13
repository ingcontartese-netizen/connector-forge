# Field Allowlist And Protected Rules

Status: active-v3-candidate / include-now
Class: template + config rule

Use this before exposing or accepting writable fields in a connector command.

## Problem

Field names from tables, APIs, spreadsheets, UI labels, or exports do not automatically mean "safe to write". Some fields are derived, identity-bearing, protected by lifecycle state, surface-specific, or valid only when another field/mode is active.

## Rule

Every write-capable command has an allowlist. Anything outside the allowlist is forbidden by default.

The allowlist must include:

- domain object class;
- field identifier;
- human label;
- writable surface;
- required state;
- unit profile;
- validation rule;
- protected-field relation;
- dependent fields;
- recompute impact;
- rollback strategy;
- evidence artifact.

## Protected Rules

Protected fields are never written unless an explicit exception path exists. Common protected classes:

- stable IDs and object keys;
- audit fields;
- derived values;
- lifecycle/status fields with workflow implications;
- financial totals or schedule outputs;
- parent/container relations;
- fields owned by another surface or object type.

## Stop Rules

Stop if:

- the user supplies an arbitrary field name and no allowlist row exists;
- the field is writable on another surface but not this one;
- required state or lifecycle conditions are unknown;
- unit profile is missing for numeric/date/duration/progress/rate/currency/quantity fields;
- protected-field exception path is not documented.
