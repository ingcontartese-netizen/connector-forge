# Packaging And Deploy Hardening

Use this reference before packaging, installing, reloading, or claiming a connector/skill/host pack is live.

## Rule

A package is not ready when files merely exist. It is ready only when the package was built from authoritative content, validates against the host layout, matches the declared source scope, contains no secrets, and is proven loaded by the target host when a live claim is made.

## Build Discipline

- Build in a scratch/output directory, not in a mounted or locked host directory.
- Keep host layout valid. Do not add top-level folders the host does not accept.
- Write critical manifests from an authoritative string or validated source, not from a stale mount view.
- Validate JSON/YAML manifests after build.
- Record file hashes for the carrier included in the claim.

## Progressive Disclosure

The front-door `SKILL.md` stays small. It lists the funnel, gate names, stop rules, and reference map. Full gates and templates live in `references/` and `assets/templates/` and are loaded on demand.

No gate may exist only in the front door. The front door is an index, not the manual.

## Zero Drift

Before any host-ready or field-tested claim, prove parity across the carriers included in that claim:

- source/draft core;
- active Codex skill;
- Codex host pack;
- Cowork host pack;
- generated package;
- installed copy.

Only carriers included in the claim need parity, but omitted carriers must be declared not claimed. Host-specific differences are allowed only when declared and must not change gates, stop rules, claim limits, or evidence requirements.

## Public-Ready Blockers

Public/GitHub-ready additionally requires:

- no-secret audit;
- sanitized case studies;
- license/readme/release notes;
- package/install/reload evidence;
- parity across every shipped carrier;
- a second API-native/live-app bench beyond the P6 desktop/UI evidence.

## Stop Rules

Stop the package/release claim if:

- source and package differ without a declared host-specific reason;
- the host-loaded version cannot be proven;
- a manifest is invalid or host layout is untested;
- a private path, token, password, database, or customer artifact would ship;
- the release label exceeds the evidence.
## OneMaster Draft Addendum

When the app root is also a working product, keep the connector nest clean and put learning,
support files, simulations, and planning artifacts in the lab. Only the approved connector nest
belongs beside the app, and app-code edits require a separate owner-approved gate.

Packaging claim rule: if Codex source is patched but Cowork packaging is not rebuilt and
installed, say `Codex active lane only` and record package lag.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-12, OMD-M-28,
OMD-M-30; tags BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB; claim limit: method/spec evidence only.
