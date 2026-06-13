# Collaborative Handoff

Use this reference when two or more agents work on a connector with independent passes and shared
governance.

## Core Rule

Each handoff must leave evidence for the next worker. A silent handoff is not valid collaboration.

## Four-Hands Loop

1. Agent A performs its assigned work.
2. Agent A verifies its own work.
3. Agent A writes a relay comment with scope, files touched, evidence, issues, and next request.
4. Agent B reads both the artifact and the relay comment.
5. Agent B second-reads or continues the work, then verifies its own part.
6. Agent B writes a relay comment with findings, suggestions, problems, and next request.

Repeat until the gate is closed.

## Separation Rules

- Keep independent brains separate unless the owner asks for merge or second-read.
- Do not edit the colleague's brain or private notes.
- Shared ledgers, relays, maps, and registers are the collaboration surface.
- When a colleague report and the file disagree, verify the file.
- When host access differs, assign work by capability: who has the actuator applies, who has
  independent readback verifies.

## Required Relay Fields

- status;
- artifact path;
- what changed;
- what did not change;
- evidence or command summary;
- claim limits;
- problems or suggestions for the colleague;
- next owner.

## Stop Rules

Stop the loop when:

- an apply would occur without owner approval;
- the second reader cannot inspect the real artifact;
- the relay omits touched files or claim limits;
- a step depends on private host state that only one agent can see and no independent readback is planned.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Draft, 2026-06-03.
- Ledger atoms: OMD-M-31, OMD-M-33.
- Tags: GIUSEPPE / LAB / BRIDGE.
- Claim limit: This is method/spec evidence. It does not prove a deployed bridge, package parity,
  production readiness, or public/GitHub readiness.
