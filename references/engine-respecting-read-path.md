# Engine-Respecting Read Path

Use this reference when a connector reads derived, calculated, semantic, explainable, user-facing,
or workflow state from a source-of-truth app.

## Core Rule

A read is engine-respecting when it uses the target app's authoritative semantic surface for the
state being claimed.

Examples of authoritative read surfaces:

- documented API endpoint that returns the same concept the user sees;
- exported report produced by the app engine;
- UI state when the question is explicitly about what is open/selected/visible;
- domain service or calculation engine used by the app;
- read-only database access only when the table/field is proven to be the authoritative surface
  for that exact concept.

## False Friends

Do not promote a read as semantically correct just because a technical record exists.

Common traps:

- raw table row when the UI applies scoring, filters, derived labels, or post-processing;
- cached value when the app has recompute or refresh semantics;
- draft/local/browser state when the user asks for persisted state;
- endpoint name that says `preview`, `simulate`, `read`, or `summary` but can still write or
  trigger a maintenance update;
- explanation text that is generated from a different rule set than the persisted result.

## Gate

Before promoting a read capability to `verified`, record:

- user-facing concept being read;
- candidate read surface;
- why this surface is authoritative for that concept;
- stale/cache/recompute risk;
- sample probe with bounded output;
- independent readback or cross-check for non-trivial domains.

## Stop Rules

Stop or downgrade to `hypothesis` when:

- the read surface returns a technical proxy for a domain concept;
- the app has a known calculation engine but the read bypasses it;
- the endpoint has side effects or unclear maintenance behavior;
- UI/report/API/DB disagree and no authoritative source is declared;
- the result will be used as readback for a write but cannot prove the intended semantic change.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Draft, 2026-06-03.
- Ledger atoms: OMD-M-03, OMD-M-05, OMD-M-09, OMD-M-24.
- Tags: APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB.
- Claim limit: This is method/spec evidence. It does not prove a deployed bridge, package parity,
  production readiness, or public/GitHub readiness.
