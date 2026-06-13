# Rollback Strategies

Use this reference before any write that may need to be reversed.

Rollback is designed before apply. A manual visual correction is a recovery note, not automatic rollback evidence.

## Levels

- L1 dry-run: safest rollback is not writing. Default to dry-run until approval.
- L2 compensating action for create: capture created IDs, then delete/archive only those IDs if rollback is needed.
- L2 compensating action for modify: capture before snapshot, then apply an inverse modify if rollback is needed.
- L3 native transaction or undo: use a real transaction/undo API when the platform exposes one.

## Required Fields

- rollback level available;
- created IDs or modified IDs;
- before snapshot for modify operations;
- inverse operation;
- authorization required for rollback;
- manual recovery if no automated rollback exists.

## Rules

- No broad delete as rollback.
- No apply in persistent apps without sandbox identity or explicit approval.
- Rollback scope must be limited to objects touched by the current operation.
- For governed writes, rollback may be proposal rejection or withdrawal.

## Failure Rule

If a write cannot be rolled back or safely recovered, mark it `HOLD` unless the user explicitly accepts the risk and the operation is not destructive.
## OneMaster Draft Addendum

Soft backups, local copies, and app restore folders are not rollback proof by themselves. The
connector must state which restore path is authoritative for the operation and which recovery path
is only a convenience copy.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atom OMD-M-22; tags APP / BRIDGE /
G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
