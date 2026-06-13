# False-Friends Register

Use this to avoid treating technical names as domain truth.

## Problem

Technical names can mislead: a table, field, endpoint, or UI label may suggest a meaning that is wrong in the domain.

## Rule

Maintain a per-app false-friends register:

| Technical name | Wrong interpretation | Correct handling | Evidence |
|---|---|---|---|
|  |  |  |  |

Every natural-language answer that depends on an ambiguous technical name must cite the register or mark the interpretation as `hypothesis`.

## Examples

- P6 `PROJECT`: not every row is a user-facing project; classify EPS, projects, templates, baselines.
- CRM `accounts`: not always customers; can include partners, prospects, internal accounts.
- PM tool `task`: may include summary, milestone, container, or leaf activity.

## Test

For every "how many/list X" capability, verify at least one false-positive example that must not be counted as X.
## OneMaster Draft Addendum

Add a false friend whenever a route, button, sheet, endpoint, or command name implies a side-effect
class that the implementation does not prove. Names such as preview, simulate, read, proposal, or
refresh are hypotheses until code, docs, or live probes prove the real effect.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-02, OMD-M-07,
OMD-M-19; tags APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB; claim limit: method/spec evidence
only.
