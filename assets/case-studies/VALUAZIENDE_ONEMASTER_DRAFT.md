# Case Study: ValuAziende OneMaster Draft

Status: Draft evidence, sanitized
Purpose: record method/spec lessons from a proprietary FastAPI/React financial-analysis app used
as the OneMaster learning bench.

## Scenario

Target class: database-backed vertical app with domain-specific scoring, user-facing workflows,
AI-assisted proposals, and existing MCP bridges.

Branch under study: hybrid API/MCP/CLI connector evolution.

Decision state:

- evolve the connector method now into OneMaster Draft;
- keep the existing working bridges intact;
- build a new OneMaster generation side-by-side;
- promote OneMaster Ready only after the new bridges produce acceptance evidence.

## What This Case Proves

- A connector must learn the app domain before choosing a control surface.
- Guides, app code, legacy bridge source, and new connector guides are different evidence layers.
- App code can supersede older documentation; docs remain useful as author intent and chronology.
- A working legacy bridge should not be overwritten during evolution.
- Existing bridge names and contracts can drift from implementation and must be audited.
- A route called preview, simulate, read, or proposal is not enough to prove side-effect class.
- Some readbacks must respect the app engine because raw records are not always the semantic truth.
- OneMaster Draft can promote method/spec lessons while keeping runtime capability claims gated.

## Promoted Draft Lessons

- engine-respecting read path;
- generational connector evolution;
- bridge doctor target-pattern;
- old/new parity matrix;
- collaborative handoff with independent brains and mandatory relay comments;
- source chronology and provenance tags for every promoted method lesson;
- clean-nest rule for app-root work;
- Cowork package parity or declared lag before carrier-parity claims.

## What This Case Does Not Prove

- no ValuAziende Bridge V2 implementation is claimed here;
- no CLI/MCP parity is claimed here;
- no governed ValuAziende write smoke is claimed here;
- no Cowork package parity is claimed here;
- no package-ready, public-ready, or production connector claim is made here.

## Connector-Forge Impact

This case strengthens connector-forge as a general method:

- learn in layers before building;
- separate app knowledge, bridge knowledge, guide knowledge, and code evidence;
- keep old and new connector generations side-by-side;
- track every promoted lesson to source tags;
- require owner approval before app changes or package/install changes.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Draft, 2026-06-03.
- Ledger atoms: OMD-M-01, OMD-M-02, OMD-M-03, OMD-M-05, OMD-M-12, OMD-M-13, OMD-M-16, OMD-M-21, OMD-M-31, OMD-M-33.
- Tags: APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB.
- Claim limit: This is method/spec evidence. It does not prove a deployed bridge, package parity,
  production readiness, or public/GitHub readiness.
