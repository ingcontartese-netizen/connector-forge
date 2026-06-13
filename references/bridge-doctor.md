# Bridge Doctor

Use this reference before diagnosing, promoting, or repairing a local bridge, MCP server, CLI
adapter, host plug, or hybrid connector.

## Core Rule

A bridge doctor is a target-pattern for evidence collection. It is not a claim that the bridge is
healthy. The doctor must expose facts that let a second reader verify lifecycle, route, schema,
runtime, and host-pack state.

## Diagnostic Dimensions

- identity: bridge name, generation, version, host plug, source root, build stamp;
- lifecycle: installed, configured, process started, loaded by host, reload behavior;
- route map: read, simulate, propose, manage, apply, logs, health;
- schema state: advertised contract vs implemented code vs tested behavior;
- capability state: verified, hypothesis, planned_contract_only, adapter_stub, forbidden;
- side-effect class: read-only, simulate, proposal, governed apply, maintenance write;
- output discipline: limits, fields, pagination, artifact output;
- security: secrets location, auth mode, data class, trust boundary;
- parity: old/new, host-vs-host, package-vs-source;
- acceptance: smoke, golden operations, readback, negative tests.

## Required Output

The doctor should produce a bounded report that names:

- what passed;
- what failed;
- what is missing;
- what is stale;
- which claims are blocked.

## Stop Rules

Do not use a bridge doctor to auto-promote a connector. Stop when:

- the doctor cannot inspect the actual host-loaded copy;
- the advertised tool catalog and implementation disagree;
- an operation called preview/simulate can write;
- source and package hashes diverge without a declared drift row;
- no golden baseline exists for a connector generation that will be refactored.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Draft, 2026-06-03.
- Ledger atoms: OMD-M-06, OMD-M-07, OMD-M-14, OMD-M-18, OMD-M-21, OMD-M-29.
- Tags: APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB.
- Claim limit: This is method/spec evidence. It does not prove a deployed bridge, package parity,
  production readiness, or public/GitHub readiness.
