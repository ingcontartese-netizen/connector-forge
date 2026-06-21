# Write Ladder, RED-Max And Confirmations

Use this reference before exposing any state-changing operation, and especially before any
destructive, massive, or irreversible verb. It sizes the gates, defines the tiers, and fixes how
a human confirmation actually works.

## Core Rule

No write happens by accident; no destructive write happens ambiguously. Every write carries a
tier, a confirmation proportional to real risk, a recap of what will change before it changes, a
readback after, and a receipt. The semaphore guides the operator inside the corridor -- it never
cages them, and it never waves them through blind.

## The Tiers

- **GREEN** -- read-only, no-side-effect, or an operator-commanded low-risk reversible write
  (single non-destructive create, one-field correction, routine refresh): execute without
  pre-confirmation, but always with mandatory readback. Verification replaces confirmation. A verb
  that claims to be pure must *prove* pure (before == after, zero writes, invariants intact). A
  write whose side effects are not proven, or that is derived/cascading, is at least YELLOW.
- **YELLOW** -- reversible or controlled write: one crisp re-confirmation with the impact declared
  ("overwrites X years / Y fields -- confirm?").
- **RED** -- destructive, massive, restore, delete, overwrite, reset, heavy import. Target echo
  ("I resolved [TICKER -- Name, id N]: sure?") plus a free operator answer.

Classify the tier by the **semantics of real effects**, never by HTTP method or UI label: a
"preview" that writes market data, an innocuous simulation POST, a refresh that continues without
backup, a destructive restore dressed as maintenance -- only code/readback certifies the effect.
Each operation carries a verified side-effect class.

## RED-Max -- The Confirmation That Caught The Real Fear

The operator's stated fear is not the action -- data is refetchable, restore exists and is proven.
The fear is **the action you don't know was taken**, or taken on the **wrong target**. So the
discipline is visibility, not ceremony:

- **recap before action**: what will change, on whom, with what effect, what survives, how to
  undo. The operator stays at the wheel and gives the final go on *that* recap;
- for delete-company / restore and other RED-max: the operator confirmation must be **posterior to
  the proposal's creation and cite its id**. A pre-authorization of intent is not an authorization
  of execution. Replaying a prior "yes" given before the proposal existed is the exact procedural
  miss to forbid -- warn when the statement does not cite the proposal id / target;
- the confirmation statement quotes the authority verbatim (the operator's chat go, with date and
  context): a mandatory field becomes a reconstructable provenance chain.

## The Absurdity Test (how to size every gate)

Operator law: if a safeguard would force confirming 500 prices one by one, the design is wrong.
The confirmation either **rises a level** (one confirm for the batch) or **disappears**
(downstream verification). Measure every gate by turns + tokens added against real risk covered.
And the deep corollary: **verification replaces confirmation** -- the readback after the act is
worth more than consent before it, because it catches reality instead of intent. Success measure:
one question = one call in seconds; one command = one turn (two if serious); 500 prices = one
command, zero per-item confirms.

## Hold-First Error Precedence

In a verb categorically on HOLD (e.g. rollback/restore reserved by policy), the policy block must
out-rank shape/completeness errors. If an incomplete payload returns a completeness error instead
of the HOLD signal, the caller deduces "fix the payload and retry" instead of "this is HOLD." Fix
the evaluation order so the contract is honored:

```
categorical-block  ->  shape/schema  ->  resolver/target  ->  creation
```

(the mirror of the shape -> resolver -> creation order already proven on propose.)

## Form Before Substance, And The Human Gate

Run form preflight (comment/payload validation) **before** propose when the content has a
contract -- the preflight finds form errors with clear messages, leaving the human review free for
substance. But never confuse the two planes: a content validator validates *form*, never the
*substance* of a judgment. A perfectly conformant proposal with the wrong decision passes every
validator and must still meet the human gate. The propose-then-approve cycle is not bureaucracy:
on decisional content it is the only substance validator the system has, and it is defended even
when it seems to slow things down. An agent proposing graded content must apply the grid
step-by-step and cite each step in the text, so the operator verifies the reasoning, not only the
result.

## Acceptance

- `propose -> detail -> approve -> readback` for every governed write;
- no RED-max approve uses a confirmation that predates the proposal; warning fires when the
  statement omits the proposal id / target;
- recap-before-action present, quoting authority verbatim;
- a pure/preview verb proves no side effects (no timings = no app calls = blocked before any
  backup/upload/AI -- preflight failing before side effects makes negative-testing free and
  perpetual);
- hold-first precedence proven by a HOLD verb returning the policy signal, not a shape error;
- form preflight available and recommended before propose.

## Stop Rules

Stop when:

- a write's real side-effect class is not verified in code (don't trust the route name);
- a destructive verb has no backup/rehearsal, no target echo, or no readback defined before
  apply;
- the only available confirmation is an intent pre-authorization, not a fresh statement citing the
  proposal;
- a gate's cost in turns/tokens is not justified by the risk it covers (over-gating pushes the
  expert operator to seek the bypass -- a rigid block fails where a semaphore would have held).

## Evidence Provenance

- Source benches: ValuAziende OneMaster Bridge V2 (the tier model, RED-max fresh confirmation,
  recap-before-action, the absurdity test as operator law, form-vs-substance gate, hold-first
  precedence all originate here, several from operator recalibration after a real procedural
  miss); Archicad 29 and Primavera P6 generalize the destructive-write and governance-write-ladder
  patterns to native objects and source-of-truth schedules.
- Field lessons distilled: a delete-company where a pre-authorization was wrongly consumed as
  confirmation -> recap-before-action rule; an "Ottima" vote rejected in three seconds by the human
  gate though it passed every validator; a HOLD verb computing a recovery plan before the HOLD
  signal.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
