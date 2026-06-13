# Domain Comprehension

Use this before Gate 0 when the app has a non-trivial domain: CAD/BIM, scheduling, project controls, ERP, CRM, finance, database-backed vertical apps, proprietary workflows, or any system where technical objects are not the same as user-facing concepts.

## Problem

A connector can read the correct table, endpoint, UI field, or file and still answer the wrong human question. That is not a bridge bug; it is a missing domain model.

## Rule

Before promoting user-facing capabilities, produce a lightweight `DOMAIN_MODEL.md`:

- core hierarchy;
- object classes;
- false friends;
- identity keys;
- validated counts or known classifications;
- source-of-truth boundaries;
- live vs persisted state;
- open questions.

Usage guides are not enough. Prefer a structure guide, data model guide, SDK concepts guide, glossary, or expert validation. If none exists, do targeted research on how the software structures work.

## Evidence

P6 showed the failure mode: a technical `PROJECT` record count was not the same as the human count of projects. Domain comprehension had to distinguish EPS nodes, projects, templates, and baselines.

## Test

Gate 0.0 is ready only when every user-facing capability can point to a domain object class and any false friends are named.

If the app is truly simple, mark Gate 0.0 as `n/a` with a reason.
## OneMaster Draft Addendum

For layered proprietary apps, domain comprehension starts before bridge design. Read author method
docs, app guides, current code, and existing bridge source as separate evidence layers. Later code
can supersede older docs, but older docs still preserve author intent and chronology.

OneMaster Draft promotes this as a method rule only. It does not promote any ValuAziende runtime
capability.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-01, OMD-M-02,
OMD-M-03, OMD-M-32; tags APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB; claim limit: method/spec
evidence only.
