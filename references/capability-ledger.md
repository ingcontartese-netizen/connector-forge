# Capability Ledger

Use the ledger to prevent wishful connector design. Every capability must be evidence-backed.

## States

- `verified`: proven by official docs, code, live read-only probe, local install, or passing test.
- `hypothesis`: plausible but not proven.
- `forbidden`: disallowed by policy, license, auth, surface limits, or user scope.

## Risk Classes

- `read`: reads state only.
- `safe`: creates a local preview/export artifact.
- `write-safe`: write with reversible change and dry-run.
- `write-governed`: regulated/source-of-truth write that must go through proposal, human approval, and audit.
- `write`: changes remote/app state.
- `write-destructive`: delete/reset/deploy/irreversible operation.
- `open-world`: broad action needing strict schema and approval.

## Native / Proxy Classes

- `native_verified`
- `native_hypothesis`
- `visual_proxy`
- `metadata_only`
- `unsafe_generic`
- `forbidden_proxy_for_native_request`

## Minimum Columns

| Capability | Surface | State | Evidence | Risk | Native/proxy class | Domain class | Declared limits | Test |
|---|---|---|---|---|---|---|---|---|
| doctor/health | | verified/hypothesis/forbidden | | read | N/A | N/A | | |
| list/search/get | | | | read | N/A | | | |
| export/preview | | | | safe | visual_proxy or artifact | | | |
| propose governed change | | | | write-governed | native_hypothesis | | direct apply forbidden until approved | |
| create/update | | | | write-safe/write | native_verified/hypothesis | | | |
| delete/reset/deploy | | | | write-destructive | native_verified/hypothesis | | | |

## Rule

Expected behavior is not evidence. A capability enters MVP only after it is `verified`, or it is explicitly carried as a `hypothesis` with a test plan and no production exposure.

If a capability cannot do something the user might assume, write it in `declared_limits` instead of hiding it in notes.

For user-facing counts, lists, details, or natural-language answers, `verified` also requires Domain-Semantic Validation: the capability must cite a domain class from `DOMAIN_MODEL.md`, false-friend handling when relevant, and evidence that the technical read maps to the human answer.
## OneMaster Draft Addendum

Capability state must describe the implemented effect, not the advertised category. Add states such
as `schema_stale`, `adapter_stub`, `planned_contract_only`, `active_needs_test_evidence`, and
`evidence_gated` when code, schema, and tests diverge.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-06, OMD-M-07,
OMD-M-14; tags BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
