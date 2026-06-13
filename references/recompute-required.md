# Recompute Required

Status: active-v3-candidate / include-now
Class: state + gate

Use this when a write may affect derived outputs, schedules, totals, balances, cached views, geometry, reports, critical paths, KPIs, or audit-derived fields.

## Problem

After a write, persisted source fields may be updated while derived outputs are stale, incomplete, cached, or not recalculated. Without an explicit state, the agent can report success while the host still needs schedule, rebuild, refresh, publish, recalculation, or audit.

## State Values

- `false`: no recompute is needed for the claimed result.
- `true`: recompute is required before derived outputs are final.
- `unknown_blocking`: the bridge cannot determine whether recompute is required; derived-output claims are blocked.
- `not_applicable`: the command has no derived outputs.

`recompute_required=true` does not mean a visible value must move. It means derived outputs are not final until the recompute action is addressed.

## Required Evidence

Record:

- source field changed;
- derived outputs affected;
- recompute action;
- whether the action was run;
- before/after derived readback;
- final claim limit.

## Stop Rules

Stop if:

- derived outputs are used while recompute state is unknown;
- the bridge reports final totals/dates/geometry/criticality before recompute is handled;
- recompute is required but no action or user handoff is available;
- a visual "nothing moved" observation is treated as proof that recompute was unnecessary.
