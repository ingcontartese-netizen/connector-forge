# Purpose Canon And Source Authority

Use this reference at Gate 0/0.0, before writing any connector code, and again whenever you are
unsure which source to trust. It is the first thing you do on a new app and the thing you return
to when sources disagree.

## Core Rule

A connector is built for a person doing a job, not for an API. Before the technical contract,
write one page in the operator's own language that says what the bridge is *for*, and decide --
explicitly -- which source is authoritative for every fact. When the purpose page and a technical
detail disagree, stop and resolve the conflict: the purpose page is authoritative for intent,
operator language, risk appetite, and what the bridge may become; the live/source authority is
authoritative for what the app can actually do and what effect a command really had. When two
sources disagree, the declared authority wins. Guessing is a defect equal to an unverified number.

## Part A -- Purpose Canon (intake before contracts)

Produce a short, operator-language page that fixes scope before any schema. It outranks the
technical Gate 0 dossier: Gate 0 says what the app *is*; this says what the bridge must *be for
the person using it*.

The canon must answer, in plain words:

- the one-sentence purpose ("let the AI work inside X as a collaborator under the operator's
  command: read everything without touching, do what is commanded and verify it, import when
  needed, without ever slowing the operator");
- the operator's three-to-five real jobs (select, monitor, decide; create, schedule, reconcile;
  whatever the domain is);
- the asset risk model: classify every data class by **recoverability** -- irreplaceable
  (method, decision memory, audit trail), repurchasable (provider-refetchable data), workflow
  flux (prices, refreshes). Protection concentrates on the irreplaceable, never spreads evenly;
- what the bridge must **not** be: a cage, a bureaucrat, a recalculator, a bypass;
- the absurdity test for every future gate: measure it in turns + tokens added against real risk
  covered. If a safeguard would force confirming 500 prices one by one, the design is wrong -- the
  confirmation rises to the batch level or moves to downstream verification. Verification replaces
  confirmation; it is the real safety, because it catches reality instead of intent;
- the initiative line: the bridge invents nothing on its own -- every action starts from an
  operator command and returns as a verified answer. The agent is a guardian, not a servant: it
  may warn that an action looks wrong, but the warning is not a veto. Who holds the wheel, and the
  evolution clause ("not autonomous agents *for now*" -- a trust threshold the operator can move).

Acceptance for Part A:

- the operator ratifies the page;
- the first operation list exists with target, risk tier, source, readback, and actor per verb;
- no tool is created before the surface is classified.

## Part B -- Author Method For AI (the richest intake source)

The ideal target is one whose author already wrote the rules for machines. At Gate 0.0 always ask:
*does a proprietary method, AI-facing guide, glossary, DOE/research dossier, or written human
workflow exist?* If yes, it is the direct source of the connector's behavioral brain and outranks
every inference. If no, proposing one is often the connector's first unit of real value (the
purpose canon itself is born this way).

Adopt the target's **taxonomy** -- its words, votes, states, gates, periods, roles, actions,
backup classes (checkpoint vs backup vs export vs restore, with a coverage matrix). Never invent
a parallel vocabulary above the app's; it doubles the false friends. Where the author renamed a
button, a lived false friend was there -- record it.

## Part C -- Source Authority And Drift Model

Declare an authority rank for every artifact, and never resolve a conflict by recency or by the
loudest voice -- always by the written rank:

```
live host/bridge readback  >  source code  >  frozen DB/backup  >  generated report
   >  chat/agent memory  >  screenshot/operator prose
```

Each source carries a label: `evidence`, `diagnostic`, `claim`, `smoke`, `readback`. A backend
endpoint existing is not a capability; a planned check is not an executed check; AI prose is UI,
not state.

Separate the **stable** from the **drifting**:

- philosophy invariants are learned once and rarely move: no-bypass, readback, recovery, target
  echo, instruction-source boundary;
- mechanisms drift every version: model ids, table names, counters, endpoints, P/E variants, UI
  labels. Anchor to philosophy; re-verify mechanisms at each version, and tag every mechanism
  claim with the version it was checked on.

When N author sources exist they drift *between themselves*; cross-compare before the code with a
conflict table, resolve each conflict at code level, and tag the losing source superseded. Even
the most diligent author leaves states only the code describes -- the final Gate 0.0 pass ends on
the code, not from distrust but from the physics of documentation. Ask the author for the
"truth-file list" (the authoritative source files) to aim that pass.

## Part D -- Governance As A Read Operation

Promote the social contract from wiki text to an interrogable surface. Charter, no-bypass policy,
claim taxonomy, encoding policy, selection contract -- expose them as **read-only operations** of
the connector itself, versioned with a marker and a hash, so any agent (including one joining a
running worksite) can query its own perimeter, the allowed claim labels, and the surfaces that do
*not* close a work item. The static brain travels in the connector's server instructions; the
interrogable, versioned part travels as read-ops. A new agent onboards by mounting the lane, not
by reading a wiki.

## Acceptance

- purpose canon ratified by the operator and used as the top source for naming and UX;
- minimal glossary approved; data classes ranked by recoverability;
- source authority rank written; every ready claim cites source and limit;
- every failed test classified (bug / environment / stale lane / unsupported scope / procedure
  error) -- "it's just environment" is a claim that must be argued per item;
- governance queryable as read-op with marker + hash, not only as files.

## Stop Rules

Stop and ask for the missing item instead of inventing it when:

- no operator-language purpose exists and you are about to infer scope from the schema;
- an irreplaceable data class has no protection while flux data is over-gated (the risk model is
  inverted);
- sources disagree and no authority rank is declared;
- a mechanism fact is used without the version it was verified on;
- a claim of target-absence ("the app doesn't have X") has not climbed the imputation ladder
  first: your read/parse -> your surface (stale lane, wrong tool, stale mount) -> transport
  (envelope, dropped params) -> connector -> and only last the target app.

## Evidence Provenance

- Source benches: ValuAziende OneMaster Bridge V2 (FastAPI/React, OneDrive-bound, native
  governance); Archicad 29 (desktop/CAD via add-on); Oracle Primavera P6 (enterprise scheduling,
  standalone SQLite). The lessons here repeated across all three; ValuAziende supplied the
  sharpest cases.
- Field lessons distilled: purpose canon written mid-build and treated as top source; author's
  "method-for-AI" becoming the connector brain; multi-source author drift resolved on code;
  recoverability-based asset classification proven by an accidental mass-reset recovered from
  backup; governance promoted to read-ops queryable by three agent lanes.
- Claim limit: this is method/spec guidance for