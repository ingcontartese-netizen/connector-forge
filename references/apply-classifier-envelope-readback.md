# Apply Outcome Classifier, Envelope Honesty And Readback Tiers

Use this reference when wiring any apply path and when defining what "done" means. It keeps an
application error from ever travelling as a success, and it sizes the proof of an action to its
risk.

## Core Rule

The envelope tells the truth or it is worthless. An apply must parse the target's real outcome
and classify it; a failure must surface as a failure, never hidden inside `ok:true`. And "the
command returned" is not proof -- the readback proves the effect, on as many dimensions as the
risk demands. What you control is what counts, not what the command declares.

## Part A -- Apply Outcome Classifier

After every apply, classify the target's response, never assume success from a 200:

```
success | blocked | partial | app_error | timeout | stale
```

Rules:

- if the app returns an error in the body/text/result string, the envelope is **failure** --
  `ok:false` with a dedicated error code (e.g. `APPLY_FAILED`), details carrying the app result
  and any pending flag;
- `ok=true` only when the intended side effect *and* a minimal readback are coherent;
- a separate audit event for application failures;
- timings present even on failures (an observability tool built for SLAs doubles as the locality
  proof of gates -- it earns its keep twice).

The poison this kills: a RED proposal approved with `ok:true, status:"executed"` while the
`result` is the app's error string and the action is still pending. The average agent reads the
status, not the prose -- so the status must not lie. Verifier corollary: after every RED approve,
check `pending_after_contains_action` and the result string, not only ok/status -- that is where
the false positive betrays itself.

## Part B -- Host Echo Of Effective Parameters

The transport layer can silently drop unknown parameters and answer plausibly to the question you
never asked (wrong-name argument -> call "succeeds" with defaults -> global list instead of the
filtered scope). The connector defends both ways:

- the envelope echoes the **effective** parameters/filters actually applied (`data.filters` /
  `meta.filters`), not the ones requested;
- agent rule: before using a response, verify the echo matches the request (expected filters ==
  declared filters);
- after any lane restart, re-fetch the tool schemas -- the memory of a signature is a hypothesis;
- never assume the transport enforces the schema, even when it declares `additionalProperties:
  false`.

A filter declared but not applied is worse than no filter -- it manufactures false evidence (an
agent believes it did a targeted readback and holds the global top). Same class at the tool-call
layer, outside the bridge's control: catch it with the echo.

## Part C -- Readback Tiers And Derived-State Parity

Size the readback to the risk:

- **raw** -> business dimensions -> audit -> derived/score -> UI/API parity -> exact-absence;
- for a destructive op, readback must cover **every** cleanup dimension (business + audit + log +
  backup + pending + per-table counts) and distinguish business-residue from audit-residue.
  Exact-absence proof: deleting means proving absence on all dimensions, not merely not seeing it
  in the UI;
- a readback used as proof must also exist as an **autonomous read-only operation** on the same
  surface agents use -- otherwise independent verification requires running the very risky
  operation you want to gate;
- truth is the engine readback; a governed write can succeed in the engine and leave the UI stale.
  Operator visual acceptance is taken *after* refresh; the connector should emit a post-write
  invalidation signal; the verifier trusts the readback, not the screen. AI prose is UI, not
  state -- reconcile every state assertion in a report against an engine readback; if they diverge,
  the engine wins and the divergence *is* the finding.

## Part D -- One Lock, Every Door (derived state is contract)

Cache invalidation and derived state are part of the contract, not an afterthought:

- every write door that mutates the same datum must share the same side effects (baseline refresh,
  cache invalidation, recompute). A side effect mounted on the UI route only is a bug invisible
  from the UI and found only by testing the second door;
- the invalidation helper is total-try/except + lazy import: a cache exception must never break an
  apply, and it sits after commit and before return on *every* call site;
- after wipe/update/import, raw and derived (summary, list, UI) must realign or declare recompute;
- acceptance discipline: grep "who else writes this field?" (UI, bridge, AI tools, import) -- all
  doors, one lock; the logic is imported, not copied. Distinguish symptom-mitigation from
  class-cure and declare which one a fix is.

## Part E -- Expected Warnings Are Evidence

Declare expected warnings *before* the action: an expected alarm that appears is evidence the
guard is alive; an unexpected one is a finding to stop on; an expected one that does **not** appear
is also a finding (the guard may be dead). Legacy-format and environmental warnings (OneDrive,
pycache, host-catalog) are declared baseline, not noise -- un-declared, they breed alarm fatigue,
the antechamber of disaster.

## Acceptance

- a test replays a historical app error -> envelope is failure, audit event present, no
  `proposal_approved`;
- no "success with hidden error" anywhere; timings on failures too;
- envelope echoes effective parameters; agent verifies echo before using a response;
- destructive readback covers all cleanup dimensions; exact-absence proven;
- every shared-field write door proven to share side effects; raw/derived realign after mutation;
- each action plan/handoff lists its expected warnings with reasons.

## Stop Rules

Stop when:

- an apply path can return `ok:true` while the app result is an error;
- a readback used as proof has no standalone read-only surface;
- a write door mutates a shared field without the shared side effects;
- the envelope echoes only requested (not effective) parameters;
- a warning appears that no plan predicted, or a predicted guard warning is silently absent.

## Evidence Provenance

- Source benches: ValuAziende OneMaster Bridge V2 (apply classifier / `APPLY_FAILED`, host-echo,
  readback tiers, derived-state cache invalidation, expected-warnings discipline all originate
  here); Archicad 29 and Primavera P6 generalize engine-respecting readback and recompute to CAD
  geometry and schedule rollups.
- Field lessons distilled: a RED approve returning ok:true with the app error in the result
  string; two same-session episodes of a transport dropping a mis-named parameter and answering
  with the global scope; a baseline-refresh side effect mounted only on the UI route (invisible
  bug); a read-after-write cache race under concurrency.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
