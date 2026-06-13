# Risk-Proportional Readback (R3-20)

ID: R3-20
Owner: CODEX lead / CLAUDE co-author evidence
Status: active-v3-candidate / second-read-source-verified
Class: gate + acceptance reference
Evidence rows: L44, L55, L58, L81
Plan-derived correction: rollback-readiness must scale with actuator risk.

## 1. Problem

Readback that checks only the target field is not enough when the actuator can miss the target, alter nearby data, remap identities, or trigger derived state. The readback scope must scale with the risk of the actuator and operation.

## 2. Core Rule

Every apply must define readback before execution. The readback must prove:

- expected target changed;
- expected non-targets did not change;
- identity mapping is still correct;
- derived outputs are either recomputed or explicitly marked not final;
- rollback or recovery is available at a level appropriate to the risk.

The higher the actuator risk, the wider the readback and the stronger the rollback proof.

## 3. Readback Tiers

| Tier | Situation | Minimum readback |
|---|---|---|
| 0 | Read-only or inspect-only | Bounded output, no write claim |
| 1 | API/SDK single object, low risk | Target identity + changed fields + error/audit status |
| 2 | Engine-mediated file/batch write | Target object, source object unchanged if cloned, counts, identity remap, import log |
| 3 | UI/browser/computer-use single operation | Target fields plus anti-collateral diff over the plausible affected surface |
| 4 | Bulk, destructive, regulated, or location-uncertain write | Whole changeset diff, protected-field checks, audit record, restore/rollback rehearsal |

Tier 3 and Tier 4 cannot rely on visual confirmation alone.

## 4. Rollback Readiness

Rollback-readiness is proportional to risk:

- low-risk reversible API write: declared inverse operation or compensation may be enough;
- engine-mediated import: fresh pre-apply snapshot/export plus restore path;
- high-risk UI/computer-use: restore must be pre-tested or recovery must be proven before apply;
- destructive or regulated operation: restore rehearsal, approval record, and audit trail are mandatory.

A backup file existing is not the same as a tested restore. For high-risk actuators, "rollback ready" means the restore path has already been exercised or the operation remains blocked.

## 5. Acceptance Fields

Add these fields to acceptance evidence:

- `readback_tier`;
- `target_readback_query`;
- `collateral_readback_query`;
- `protected_invariants`;
- `expected_before`;
- `expected_after`;
- `actual_after`;
- `diff_result`;
- `rollback_readiness`;
- `restore_test_result`;
- `recompute_required`;
- `claim_scope`.

## 6. Evidence From P6

P6 WP11 used a high-risk live UI actuator. Claude added a project-level diff checker because a target-only check could miss wrong-row or wrong-field collateral. The final evidence was `DIFF_PASS`: CP9010 changed to 80h/80h and the other 14 activities plus control record remained unchanged.

This proves risk-proportional readback for one sandbox single-operation live write. It does not prove bulk edit, production readiness, or generic UI automation.

## 7. Stop Rules

Stop if:

- no readback query exists before apply;
- the readback checks only the happy-path target while the actuator can affect neighbors;
- rollback readiness is weaker than the actuator risk;
- derived outputs are used while `recompute_required=true`;
- readback and user-facing claim disagree.

## 8. Status

`active-v3-candidate / second-read-source-verified`
## OneMaster Draft Addendum

For semantic apps, readback may need more than changed rows. Use explanation, recomputation,
domain status, affected-object summary, and anti-collateral checks when the user-facing meaning can
change without a simple field diff.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-22, OMD-M-24; tags
APP / BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
