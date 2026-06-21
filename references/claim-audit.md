# Claim Audit

Use this reference before writing connector claims, tool descriptions, app metadata, host-pack text, release notes, or user-facing summaries.

## Forbidden Claims

Do not claim:

- "works with any app";
- "fully automatic";
- "MCP/CLI solves everything";
- "computer use is enough";
- "guaranteed token/cost/speed reduction";
- "safe writes" without dry-run, approval, rollback, and audit;
- "supports operation X" when the Capability Ledger says `hypothesis`;
- "production-ready" without Source Registry, Security Mesh, acceptance tests, and Revalidation Matrix.

## Allowed Claims

Prefer:

- "works for authorized and accessible surfaces";
- "chooses CLI, MCP, Hybrid, API, plugin, file workflow, or STOP after Gate 0";
- "uses evidence-backed capabilities";
- "supports read-only readiness before writes";
- "requires revalidation for fast-moving hosts/protocols";
- "MCP branch is self-contained for ordinary MCP design through internal Forge references";
- "Hybrid branch handles local bridge plus remote broker when justified".

## OneMaster V1 MCP Claim Boundary

Allowed claim:

- "Connector Forge OneMaster V1 working source includes an internal MCP procedure for ordinary connector design, packaging governance, and revalidation."
- "Connector Forge OneMaster V1 is published as a public GitHub working source after no-secret audit, sanitized case studies, Apache-2.0 license/NOTICE, README/changelog reconciliation, install/test evidence, and Giuseppe sign-off."

Required qualifiers:

- self-contained means method/procedure/reference self-containment, not a live server, host package, deployed endpoint, or production connector;
- carrier parity requires package rebuild/import/install/reload proof and host smoke for each claimed carrier;
- future MCP protocol material stays in watchlist/quarantine until final specification, SDK support, and host behavior are revalidated;
- the former MCP specialist material is historical source material only, not an operational dependency.

Not claimed:

- production-ready;
- package-ready;
- host-live parity;
- deployed MCP endpoint;
- all-host support;
- MCP 2026-07-28 compliance.

## Audit Questions

- What source proves this claim?
- Is it about the method or about a specific app?
- Does the Capability Ledger mark it `verified`?
- Does the Revalidation Matrix have an open high-fragility assumption?
- Is the claim scoped to a host, version, auth mode, and environment?
- Would the claim still be true if the app has no API, no auth, or no test environment?

## Rule

If a claim cannot be traced to evidence, downgrade it to hypothesis or remove it.

## OneMaster Draft Rule

When a real bench produces candidate method lessons, use `recommend-for-draft` or `promoted into draft guidance` only after the lesson is traced to its source artifact. Do not use `approved`, `released`, `ready`, `deployed`, `package-ready`, or `public-ready` unless the matching release gate has evidence.

For OneMaster-style evolution:

- source tags stay visible: app study, bridge study, guide study, user rule, colleague second-read;
- method/spec lessons may move into the skill as Draft;
- app-specific or bridge-specific behavior stays in the case study or connector project;
- runtime capability claims stay `evidence-gated` until implemented and read back;
- generated packages and installed host copies require their own parity evidence.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Draft, 2026-06-03.
- Ledger atoms: OMD-M-01, OMD-M-02, OMD-M-13, OMD-M-21, OMD-M-31, OMD-M-33.
- Tags: APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB.
- Claim limit: This is method/spec evidence. It does not prove a deployed bridge, package parity, production readiness, or public/GitHub readiness.
