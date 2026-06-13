# Unit Calibration Gate (R3-22)

ID: R3-22
Owner: CODEX lead / CLAUDE review
Status: active-v3-candidate / second-read-source-verified
Class: gate
Evidence rows: L52, L53, L65, L67, L75, L78

## 1. Problem

Many applications expose the same value in different unit systems depending on surface:

- display unit;
- storage unit;
- API unit;
- import/export unit;
- domain shorthand;
- derived or rollup unit.

If the bridge does not calibrate the unit semantics, an accepted write can be mechanically successful and operationally wrong.

## 2. Evidence And Claim Limit

P6 verified the unit trap: duration values crossed display/import/storage semantics and a wrong-unit write produced a failure case. That is strong evidence that the gate is needed.

However, the P6 bench did not execute a dedicated successful unit-calibration round trip before the operation. Therefore this R3 gate claims:

- problem verified;
- countermeasure motivated;
- calibration workflow specified.

It does not claim that the calibration workflow itself was fully proven on P6.

## 3. Core Rule

Before a write involving numeric units, quantities, dates, durations, currency, percentages, scores, or rates, the bridge must classify unit semantics for the actuator surface.

Minimum fields:

- `field_name`;
- `domain_meaning`;
- `display_unit`;
- `storage_unit`;
- `input_unit`;
- `export_unit`;
- `canonical_unit`;
- `conversion_rule`;
- `rounding_rule`;
- `readback_unit`;
- `calibration_status`.

`calibration_status` can be:

- `verified_round_trip`;
- `problem_verified_countermeasure_motivated`;
- `unknown_block_write`;
- `not_applicable`.

## 4. Calibration Workflow

For a true `verified_round_trip` claim:

1. Read a known value from the target surface.
2. Read the same value through an independent surface if possible.
3. Convert to canonical unit.
4. Apply a safe sandbox change or dry-run payload.
5. Read back through the target and independent surface.
6. Confirm expected conversion and rounding.
7. Revert/restore or document why no persistent write occurred.

If the workflow is not executed, do not claim unit calibration verified.

## 5. Apply Rule

If unit semantics are unknown, the bridge must not perform broad or irreversible writes.

A narrow single-operation write may proceed only when:

- the user/domain expert explicitly confirms the intended unit;
- the operation is sandboxed or recoverable;
- readback checks the stored/canonical result;
- the final claim says the unit gate was risk-managed, not fully calibrated.

## 6. Evidence From P6

The final live duration write was verified by readback and anti-collateral diff. It fixed the specific value. It did not prove a reusable P6 duration calibration routine for every import/UI/API surface.

## 7. Stop Rules

Stop if:

- display and storage units may differ and no mapping exists;
- an import/export surface uses a hidden unit convention;
- a prior wrong-unit failure exists and no mitigation is in the contract;
- readback is not in a canonical or clearly mapped unit;
- the response would claim "calibrated" without a round trip.

## 8. Status

`active-v3-candidate / second-read-source-verified`
## OneMaster Draft Addendum

Financial apps need unit calibration for currency, scale, percentages, ratios, and fiscal-period
semantics. A field named value, score, price, estimate, or forecast is not enough; the connector
must know the unit, source, period, and domain formula before writing or validating it.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-23, OMD-M-27; tags
APP / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
