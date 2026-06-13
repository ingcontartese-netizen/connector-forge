# Schema, Allowlist, Row Identity And Rule-To-Capability Binding

Use this reference before exposing any write-capable field or any update/delete granular verb. It
stops "almost-right" payloads the app will misread, and it ties every behavioral rule to a real
capability instead of a hope.

## Core Rule

The bridge's schema must never be more permissive than the app it speaks to, and every rule you
state to a model must be enforced by a capability of the tool. A field domain is enforced like a
spreadsheet cell validation, at every layer; a granular write must name the exact row; and a
written rule with no capability behind it is a false guarantee -- it holds only while the model is
good, which means it does not hold.

## Part A -- Schema No Wider Than The App

The connector's declared payload schema is a *stricter-or-equal* mirror of the app's apply
contract -- never looser. A facade that promises a minimal payload the app then rejects is a
schema that lies: it produces green envelopes on actions the app refuses. Every declared minimal
payload is round-trip tested against the real apply in acceptance; the preflight is at least as
severe as the downstream contract.

`INVALID_PAYLOAD` errors carry `field`, `allowed`, and `example` -- discoverability without three
rounds of typed-error archaeology. A self-documented schema beats blind probing, but the contract
stays the source of truth.

## Part B -- Field Allowlist, Enforced At Every Layer

Per-field value domains are hard, and enforced by the engine as cell-validation at UI + preflight
+ apply-path together; menus are generated from the allowlist, never hardcoded. The allowlist is
**per field**, not per group: one field's exception domain differs from its neighbors' (a price
gate accepts a different softening than a ratio gate). Negative tests for illegal values are
mandatory acceptance.

Stop class: an actuator that can edit the app's own code or validation is out of perimeter. An
agent must never be able to inject an out-of-domain option by editing front-end code -- the engine
holds the domain regardless.

## Part C -- Row Identity For Granular Writes

Update/delete of a single record requires the row's identity in the payload, never a
ticker-only-by-position guess: an explicit id, or the natural key (e.g. period quarter + year,
quarters restricted to the legal set). The contract documents *how* the row is identified for each
verb; the preflight blocks a write that cannot name its row, before any app call. Periods and
dimensions are kept separate and never conflated: annual, quarterly, half-year, TTM, forecast,
earnings are bounded semantics -- a value right in the wrong period is the quietest damage there
is. A preview on periodic data declares the **temporal alignment** (fiscal year vs calendar year,
quarter vs half) before writing: never assume fiscal year = calendar year, a universal domain
false friend.

## Part D -- Rule-To-Capability Binding Matrix

For every behavioral rule in the brain/policy, ask: *which capability enforces it?* If none, build
one or declare it is mere convention. Bind each method rule to a tool, a field, an allowlist, a
test, a readback. Lived instances of the general law: "recovery declared without a recovery verb"
is a paper promise; "row identity required by the app" becomes a preflight block; "never rewrite a
truncated note" becomes an edit-grade read guard; "proposal-specific confirmation" becomes a
manage warning. The audit of a connector includes the rule->capability matrix; a rule with an empty
capability cell is a finding. Direction of hardening: semaphore first, cage never -- but a codified
semaphore beats a written-only rule.

## Part E -- Gates Before Side Effects (free negative testing)

Place all local validation **before** the first side effect (backup, upload, AI, write), verified
by position in code, not by faith. Then a live negative test costs zero: a deliberately broken
payload errors immediately, and the **absence of `meta.timings`** proves locality (zero app
calls). Protections are proven live on every run without sacrificial files, GO ceremonies, or AI
cost. Ordering pipelines as "all local gates before the first side effect" is not only safety -- it
is perpetual testability.

## Acceptance

- ticker-only / row-less granular write -> `INVALID_PAYLOAD` in preflight, no proposal created;
- illegal field value -> blocked with field/allowed/example; replay-the-catalog-example passes;
- declared minimal payloads round-trip tested against the real apply;
- period/temporal semantics declared on periodic previews; fiscal alignment stated;
- rule->capability matrix complete, no empty cells on safety rules;
- a broken payload blocks before side effects with no timings (locality proven).

## Stop Rules

Stop when:

- the bridge schema is looser than the app contract on any verb;
- a write-capable field has no allowlist, protected-field rule, or unit/period profile;
- a granular update/delete cannot name its row;
- a behavioral safety rule has no capability binding (convention masquerading as guarantee);
- an actuator can edit the app's code or validation.

## Evidence Provenance

- Source benches: ValuAziende OneMaster Bridge V2 (per-field allowlist enforce-by-engine, row
  identity for earnings update/delete, schema-no-wider-than-app, temporal/fiscal alignment,
  rule-to-capability binding, gates-before-side-effects all originate here); Archicad 29 (relational
  create / host-bound object identity) and Primavera P6 (required-writable-field introspection on a
  standalone schema) generalize row identity and field introspection.
- Field lessons distilled: a delete-earnings facade declaring ticker-only while the app required
  the natural key (green envelope on a refused action); an out-of-domain gate option injected via
  front-end edit and held by the engine; a fiscal-year-end-month-6 company exposing the
  fiscal!=calendar trap.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
