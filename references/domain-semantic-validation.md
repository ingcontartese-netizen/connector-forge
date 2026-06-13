# Domain-Semantic Validation

Use this when a capability counts, lists, filters, summarizes, or answers a natural-language question from technical data.

## Problem

`technical_read_verified` is not enough for a user-facing answer. A table, endpoint, or report row must be classified into the domain concept the user asked about.

## Rule

Promote the answer only through this chain:

```text
technical_read_verified -> domain_semantics_verified -> user_answer_verified
```

The answer must say which domain class it counts or reports. Avoid raw technical labels as final truth unless the user explicitly asked for raw technical data.

## Required Evidence

- source operation and transcript;
- domain class from `DOMAIN_MODEL.md`;
- false-friend row if the technical name is ambiguous;
- identity key or resolver rule for the object class;
- expected count/result when known;
- validation tier: `test`, `cross-read`, `expert`, or `source-doc`.

## Naming

If a tool exposes raw structure, name it honestly:

- `list_project_structure`, not `list_projects`, if it returns EPS, templates, baselines, and projects;
- `read_raw_records`, not `answer_business_count`, if no semantic classification is done.

## Stop Rule

If the domain class is unknown, answer with the technical read and explicitly mark the user-facing interpretation as `hypothesis`.
## OneMaster Draft Addendum

For financial, scoring, or explainability workflows, validate the semantic answer, not only the row
or endpoint. A valid readback may be an explanation, a recomputed score, a user-facing status, or a
bounded comparison when that is how the app expresses the domain result.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-03, OMD-M-09,
OMD-M-24; tags APP / BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
