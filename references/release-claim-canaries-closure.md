# Release Claim, Canary Invariants And Closure Labels

Use this reference before declaring any connector or slice "ready," and throughout a build to make
state machine-readable. Close with a verifiable claim, never with enthusiasm.

## Core Rule

A ready claim separates what is proven live from what is source-only, YELLOW, deferred, and not
covered -- and names the perimeter ("this installation, these paths, this DB, these host lanes").
Closure is a labeled, greppable claim that cites its evidence class; canary invariants prove the
domain didn't silently corrupt under the build. No claim outruns its proof.

## Part A -- Honest Ready Claim

The claim ladder: source_verified -> cli_verified -> host_live_validated, with the gate **class**
declared per item (machine_verified vs operator_attested -- a receipt is attested, a matching
preview hash is verified). The ready statement lists, explicitly:

- **proven live**: what a host lane actually executed with bounded output and readback;
- **YELLOW**: what is source/CLI-green but awaiting a live lane or a restart;
- **deferred / not covered**: declared, with risk and owner -- including future drift and
  unestimated costs;
- the perimeter and the limits: a backend endpoint existing is not a capability; a numeric/parity/
  safety claim cites an artifact path or register row, or it is labeled hypothesis.

The claim is reviewed word-by-word by an independent verifier with power to block phrases too
strong. Numbers in the claim are all re-verified against the register and live batteries. Residual
nominal labels (a status string saying "pending_reload" when parity is true) are declared
non-blocker, not silently trusted.

## Part B -- The Imputation Ladder (before blaming the target)

A claim of target-absence or target-defect climbs the ladder and declares what it excluded: your
read/parse -> your surface (stale lane, stale mount, wrong tool) -> transport (envelope, dropped
params) -> connector -> and only last the target app. The burden of proof grows up the ladder; an
accusation of the app without the climb is an overclaim like a number without an artifact. Each
known failure is argued per item -- "it's just environment" is a claim, and one real sentinel can
die inside a blanket dismissal.

## Part C -- Canary Invariants And Golden Record

Choose 3-5 domain invariants + one golden record at the start of a build, with full expected
values, and verify them in **every** battery -- even when "they don't apply." A method hash (the
engine's identity), a pending count, portfolio/object counts, and a golden record whose
interpretive traps are written *inside* it (e.g. "total_score already includes the tree multiplier:
never re-count it"). Cost: seconds. Value: any silent corruption of engine, method, or queue
surfaces within one cycle. It is the domain-side twin of the doctor parity (which watches the
build); the canary watches the *domain*.

## Part D -- Closure Labels, Machine-Greppable

Every slice closes with a formal, greppable label encoding what is closed and with which evidence
class (`X_CLOSED_TWO_LANE_VERIFIED_LIVE_MCP`), never "done" in prose. The standard
definition-of-done is two-lane closure (creator + verifier, declared surfaces); downgrades have
their own grammar (source_verified / cli_verified / mcp_live / operator-visual-accepted). The
worksite state reconstructs with a grep; no ambiguous closure survives a re-read. Define the label
format at the worksite's day zero; "closed" without a label is not closed.

## Part E -- Promotion Gate (the dual mandate)

A connector build has two declared mandates: ship the connector *and* harvest the lessons for the
skill. Two opposite disciplines: harvesting is continuous and hot (a lesson not written
immediately is lost at the next restart); promotion is **gated** by a quality event (ready) and a
human decision ("collect, don't promote"). The criterion for promoting a lesson into the skill is
the **repetition of evidence across cases**, not the brilliance of one case -- independent
convergence across different targets (Archicad/P6/FastAPI) is the strongest validity signal. No
skill promotion before the connector's functional and integrity tests pass; the updated skill
cites case studies without contaminating the core with proprietary data.

## Acceptance

- ready claim separates proven/YELLOW/deferred/not-covered, names perimeter, declares gate class;
- every number cites an artifact; every residual has owner or a not-do decision;
- imputation ladder applied in every target-defect claim; known failures argued per item;
- canary invariants + golden record verified in every battery, traps embedded;
- closure labels greppable, two-lane definition-of-done; promotion gated by ready + human decision.

## Stop Rules

Stop when:

- a claim says "ready" without separating proven live from YELLOW/deferred/not-covered;
- a number/parity/safety claim has no artifact (it is hypothesis, label it so);
- a target-defect is asserted without climbing the imputation ladder;
- a slice closes in prose without a greppable label and an evidence class;
- the skill is promoted before functional/integrity tests, or with proprietary data in the core.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Bridge V2 (the ready-claim ladder, word-by-word claim review,
  imputation ladder, canary/golden-record discipline, closure labels, dual-mandate promotion gate
  all originate here; the word-by-word ready-claim review was a real Fase C). Generalizes to any
  connector release on Archicad/P6/SaaS/file/browser.
- Field lessons distilled: a ready claim reviewed word-by-word with block power, residual nominal
  label declared; a "it's just environment" dismissal hiding one real marker sentinel; a real-symbol
  golden record with an embedded "never re-count a derived score" trap held across a week of batteries.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
