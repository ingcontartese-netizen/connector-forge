# Operating Manual Template (R3-21)

Owner: JOINT
Status: active-v3-candidate / WP12.5 source verified
Purpose: per-connector operating knowledge artifact required before non-trivial writes or live operations.

This template records how to operate through the target app correctly. It is not a product manual. It captures the subset of domain rules, command grammar, units, side effects, host state, and readback checks needed for a connector to act without guessing.

## 1. Scope And Claim Limits

| Field | Value |
|---|---|
| target_app | |
| target_version | |
| target_host | |
| target_data_source | |
| connector_branch | cli / mcp / hybrid / api / file_workflow / ui_actuator |
| domain_owner_or_expert | |
| manual_status | draft / expert_reviewed / verified_for_scope |
| claim_scope | |
| not_claimed | |

Rule: a command may only claim the scope covered by this manual. Missing operating knowledge blocks writes.

## 2. Domain Objects

| Human object | Technical object | Stable identity keys | Human labels | False friends | Lifecycle states |
|---|---|---|---|---|---|
| | | | | | |

Each write-capable command must map to a domain object class, not only to a table, endpoint, sheet, or UI label.

## 3. Command Schema

| Column | Meaning |
|---|---|
| `command_id` | Stable command identifier, e.g. `activity.update_duration` |
| `human_intent` | Natural-language operation this command serves |
| `domain_operation` | Domain action, not transport action |
| `target_object_class` | Domain class affected |
| `operation_risk` | read / safe / write-safe / write / write-destructive |
| `actuator_rank` | API, CLI, file, browser, desktop UI, computer-use, human-assisted |
| `actuator_authority` | official, vendor-supported, engine-mediated, ui-mediated, human-mediated, forbidden |
| `required_host_state` | Host/session state required before command |
| `identity_keys_required` | Frozen keys required before apply |
| `required_fields` | Inputs required before dry-run/apply |
| `writable_fields` | Fields the command may write |
| `protected_fields` | Fields the command must not write |
| `unit_profile` | Unit/calibration entry used by this command |
| `preflight_checks` | Checks before dry-run/apply |
| `approval_requirement` | none / user approval / token / proposal approval |
| `readback_tier` | R3-20 tier |
| `rollback_class` | inverse / restore / compensation / manual recovery |
| `recompute_state` | not_required / required / unknown_blocking |
| `evidence_tiers` | test / expert / cross-read |
| `command_status` | hypothesis / verified_for_read / verified_for_single_write / needs-evidence / forbidden |

Command atlas:

| command_id | human_intent | domain_operation | target_object_class | operation_risk | actuator_rank | required_host_state | approval_requirement | readback_tier | command_status |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## 4. Surface Grammar

| surface_id | surface_type | authority | object_scope | required_fields | writable_fields | fields_defined_elsewhere | selector_or_header_evidence | dry_run_available | status |
|---|---|---|---|---|---|---|---|---|---|
| | API / CLI / file sheet / UI tab / control | | | | | | | | |

Rules:

- A field valid on one surface may be invalid on another.
- Sheet names, tab names, control classes, endpoint paths, and command flags are part of the command grammar.
- The manual must state where resources, relationships, attributes, and units are defined if they are not writable on the current surface.

## 5. Field And Unit Semantics

| field_id | domain_meaning | display_unit | input_unit | storage_or_canonical_unit | export_unit | conversion_rule | rounding_rule | calibration_status | evidence |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Allowed `calibration_status` values:

- `verified_round_trip`;
- `problem_verified_countermeasure_motivated`;
- `unknown_block_write`;
- `not_applicable`.

Unit rule: a write involving numbers, dates, durations, currency, percentages, rates, quantities, or scores must cite a unit profile. If the unit profile is unknown, the command is not write-ready.

## 6. Minimal Write / Dependent Read

| command_id | minimal_authoritative_write | dependent_fields_to_read | fields_not_to_force | reason |
|---|---|---|---|---|
| | | | | |

Rule: write the smallest field the host engine expects, then read dependent or derived fields. Do not force dependent fields unless the manual says they are independently writable and required.

## 7. Side Effects And Recompute

| command_id | possible_side_effect | recompute_required | recompute_action | derived_outputs_blocked | evidence |
|---|---|---|---|---|---|
| | | true / false / unknown | | | |

Allowed `recompute_required` values:

- `false`;
- `true`;
- `unknown_blocking`;
- `not_applicable`.

Rule: `recompute_required=true` does not imply visible derived-output movement. It only means derived outputs are not final until the recompute action is addressed.

## 8. Protected Rules

| object_or_field | protection_rule | reason | exception_path | evidence |
|---|---|---|---|---|
| | never-write / proposal-only / expert-only / read-only | | | |

Direct private datastore writes must remain `forbidden` unless vendor-authorized for the actual data source.

## 9. Host And Actuator Assignment

| command_id | reading_agent_or_host | actuating_agent_or_host | actuator_backend | verifying_agent_or_host | blocker_if_unavailable |
|---|---|---|---|---|---|
| | | | | | method_blocked / actuator_blocked / host_blocked |

Rule: the agent/host with the actuator may differ from the agent/host doing readback. Separation is acceptable and often stronger, as long as the contract and evidence chain are explicit.

## 10. Required Checks

Pre-apply checks:

- domain object class resolved;
- identity keys frozen;
- command schema row complete;
- surface grammar row complete;
- unit profile known or write blocked;
- protected fields checked;
- host state valid;
- actuator available and inspected;
- approval/token/proposal ready;
- rollback/recovery readiness matches risk.

Post-apply checks:

- target readback matches expected value;
- collateral scope checked according to readback tier;
- protected invariants unchanged;
- recompute state recorded;
- claim scope matches evidence;
- rollback remains available until acceptance is complete.

## 11. Example Check Definitions

```yaml
preflight_check:
  command_id:
  target_identity_frozen: true
  required_fields_present: true
  unit_profile_status: verified_round_trip | problem_verified_countermeasure_motivated | not_applicable
  protected_fields_checked: true
  actuator_status: available | actuator_blocked | host_blocked
  approval_status: not_required | pending | approved
  rollback_readiness: inverse_ready | snapshot_ready | restore_tested | recovery_documented

post_apply_check:
  command_id:
  target_readback: pass | fail
  collateral_readback: pass | fail | not_applicable
  recompute_required: true | false | unknown_blocking | not_applicable
  derived_outputs_final: true | false | not_applicable
  evidence_tiers:
    test:
    expert:
    cross_read:
  final_verdict: verified | pass_with_notes | needs_fix | rollback_required | blocked
```

## 12. Expert Notes

| Date | Expert/source | Note | Binding level | Affected command/field | Evidence |
|---|---|---|---|---|---|
| | | | binding_rule / case_specific / hypothesis | | |

Expert input is evidence. It does not bypass dry-run, approval, readback, rollback, or claim audit.

## 13. Appendix A - Worked Example (P6, non-normative)

This is an illustrative instance, NOT part of the reusable template. It shows the template populated by one real operation that was actually verified, with honest scope. Anything not proven stays out.

A.1 Scope and claim limits:

| Field | Value |
|---|---|
| target_app | Primavera P6 Professional 25 |
| target_data_source | SQLite standalone (PPMDBSQLite) |
| connector_branch | hybrid / ui_actuator |
| manual_status | verified_for_scope |
| claim_scope | one governed single-operation duration update, sandbox, app open |
| not_claimed | bulk edit; production; general P6 Java API; direct SQLite write; any other command |

A.2 Command atlas (one row, filled):

| command_id | human_intent | domain_operation | target_object_class | operation_risk | actuator_rank | required_host_state | approval | readback_tier | command_status |
|---|---|---|---|---|---|---|---|---|---|
| `activity.update_duration` | set an activity original duration | change planned duration of an Activity | Activity | write | desktop UI (win32) | P6 open, CFSBX01 loaded, CP9010 selected, Status tab visible | token | tier 3 (UI single-op + whole-surface diff) | verified_for_single_write |

A.3 Unit profile (duration):

| field_id | display_unit | input_unit | storage/canonical | conversion | calibration_status |
|---|---|---|---|---|---|
| original_duration | days | days (Original Duration column) | hours | days * 8h = hours | problem_verified_countermeasure_motivated |

Note (non-overclaim): the wrong-unit failure (80 read as 80 days) proved the trap; a successful calibration round-trip was not executed, so the status is `problem_verified_countermeasure_motivated`, not `verified_round_trip`.

A.4 Minimal write / dependent read:

| minimal_authoritative_write | dependent_fields_to_read | fields_not_to_force | reason |
|---|---|---|---|
| Original Duration | Remaining, At Complete | Remaining, At Complete | for a not-started activity P6 propagates dependents; forcing them risks desync |

A.5 Side effects and recompute:

| possible_side_effect | recompute_required | recompute_action | derived_outputs_blocked |
|---|---|---|---|
| schedule dates shift | true | F9 / Schedule | finish/derived dates not final until recompute (may already match: true != visible movement) |

A.6 Host and actuator assignment (the WP11 split):

| reading_agent_or_host | actuating_agent_or_host | actuator_backend | verifying_agent_or_host | blocker_if_unavailable |
|---|---|---|---|---|
| Codex (win32) + Claude (sandbox, immutable read) | Codex | win32 TCDBEdit (after uia fallback) | Claude (`project_diff_check.py`, DIFF_PASS) | uia=actuator_blocked; computer-use pipe=host_blocked |

A.7 Protected (what stayed untouched): the source project, the other 14 activities, control CORP00591/CP1040; direct SQLite write remained forbidden. Evidence: DIFF_PASS, collateral empty.

A.8 What this example does NOT establish: that any other P6 command is write-ready, that this routine generalizes to every import/UI/API surface, or that calibration is proven. Each new command starts at `hypothesis` and earns its own row.

A.9 Operating-knowledge depth note (P6-specific, non-core, from Giuseppe). The chosen progress / percent-complete method changes which fields re-estimate. Example: a Physical %-complete method does not change Remaining Duration (and unit progress can diverge from activity progress), whereas a Duration-based method re-estimates Remaining. A bridge that wrote duration or progress without knowing the active method could silently corrupt the schedule. This is exactly the per-connector operating knowledge the manual must capture (a `progress_method` field in the command/operating rows for P6) - and it stays P6/planning-specific, never a generic core rule. It is the concrete proof of R3-21: knowing the tool, not only reaching it.

## 14. Template Status

`active-v3-candidate / WP12.5 source verified`
