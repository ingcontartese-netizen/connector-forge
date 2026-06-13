# Governance Write Ladder

Load this reference when a write touches regulated, critical, financial, CRM, ERP, database, or other source-of-truth data.

## Required Ladder

```text
read -> simulate -> propose -> approve -> apply -> audit
```

- `read`: read real state before proposing a change.
- `simulate`: when a what-if surface exists, run it with bounded output.
- `propose`: stage a change as a proposal instead of mutating the domain directly.
- `approve`: a human approves; the agent does not approve on their behalf.
- `apply`: apply only after explicit approval.
- `audit`: record request_id, operator_id, proposal_id or object_ids, outcome, and time.

## Domain Integrity

- Do not touch the calculation or decision engine unless the user explicitly asks for engineering work on that engine.
- Do not invent numbers. If data is missing, say it is missing.
- Direct write is forbidden for governed data even if technically possible.
- Prefer app-native proposal surfaces such as `propose`, `manage_proposals`, review queues, or approval workflows.

## Required Evidence

- Capability Ledger risk class is `write-governed`.
- `declared_limits` states what the connector cannot apply directly.
- Tool metadata and README do not promise direct mutation beyond the governed surface.
- Audit trail is present before the write is called ready.

## Failure Rule

If approval, audit, or source-of-truth integrity is missing, the connector can at most prepare a proposal. It cannot claim write success.
## OneMaster Draft Addendum

When a target app already has proposal queues, approvals, or guarded actions, map connector writes
onto that governance instead of bypassing it. If a native endpoint is missing, an interim path must
be pinned, named, and explicitly marked evidence-gated until replaced.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-10, OMD-M-11,
OMD-M-20; tags APP / BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
