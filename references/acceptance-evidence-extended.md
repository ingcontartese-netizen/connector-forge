# Acceptance Evidence Extended

Use this reference when a technical result must be promoted into a user-facing or write-capable connector claim.

## Rule

A result is not accepted only because a query returned rows or a write surface reported success. Acceptance evidence must prove the technical result, the domain meaning, the expected negative cases, and the final human-facing answer.

For non-trivial domains, the evidence record must include:

- `domain_classification`;
- `expected_count_or_value`;
- `false_positive_example`;
- `ui_domain_mapping`;
- `expert_validation`;
- `bounded_output_evidence`;
- `final_human_answer`.

For writes, it must also include:

- `readback_tier`;
- `target_readback_query`;
- `collateral_readback_query`;
- `protected_invariants`;
- `expected_before`;
- `expected_after`;
- `actual_after`;
- `diff_result`;
- `recompute_required`;
- `rollback_readiness`;
- `restore_test_result`;
- `claim_scope`.

## Split Verdicts

Do not collapse live operations into a single pass/fail when the evidence is more specific. Useful verdicts include:

- `mechanics_verified / semantics_failed`;
- `live_read_verified / write_not_ready`;
- `applied / recompute_required`;
- `target_changed / collateral_failed`;
- `target_verified / derived_not_final`.

The ledger records the split verdict. The release claim must not round it up.

## Transport Is Not Semantics

An operation can land on the target surface and still mean the wrong thing. Units, dates, percentages, rates, currencies, progress methods, calendars, and derived fields must be checked against the operating manual and readback evidence.

If the semantic value is wrong, the operation is not verified even when the transport succeeded.

## Evidence Tiers

Acceptance can cite these independent tiers:

- `test`: a committed checker or probe was actually run;
- `expert`: a domain owner validated the meaning;
- `cross_read`: another agent or host re-derived the result through an authoritative path.

For write verification, `test` plus `cross_read` is the normal minimum. Add `expert` whenever correctness depends on domain interpretation.

## Stop Rules

Stop promotion if:

- the evidence only proves raw transport success;
- the result could be semantically wrong and no domain validation exists;
- high-risk actuators lack collateral readback;
- rollback readiness is weaker than the actuator risk;
- the final user-facing claim exceeds the recorded evidence tier.
## OneMaster Draft Addendum

For connector generations, acceptance evidence should include old/new parity, semantic readback,
side-effect classification, host-pack state, and two-agent cross-read when available. A second
agent should inspect the artifact and the relay comment, not only the summary.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-21, OMD-M-24,
OMD-M-31, OMD-M-33; tags APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB; claim limit: method/spec
evidence only.
