# P6 Cold Start And Write Path Case Study

Status: sanitized field evidence
Scope: Primavera P6 Professional 25, standalone SQLite sandbox
Claim limit: method evidence only; not a P6 production connector

## Why This Case Matters

P6 proved that connector-forge must understand both transport and operating semantics. A connector can read tables, import files, or operate UI controls and still be wrong if it misunderstands the domain object, unit, progress method, or derived state.

## Fascia A: Domain Comprehension

The first read-only probes found technically correct records, but the domain answer required expert interpretation. Raw project rows included EPS, projects, templates, and baselines. The user-facing question "how many projects" could not be answered by counting raw database rows.

Promoted generic lessons:

- Gate 0.0 Domain Comprehension for non-trivial domains.
- Domain-Semantic Validation before user-facing counts/lists/details.
- False-friends register for labels, tables, and UI terms.
- Live-vs-persisted distinction for open/active/running state.
- Embedded DB/WAL safe read rules.

## Fascia B: Governed Create

The first governed create used an engine-mediated file/import path in sandbox. The bridge created a new project clone through P6's import surface, then read back:

- new object identity was created;
- source project remained unchanged;
- expected counts matched;
- rollback/restore route existed.

Promoted generic lessons:

- prefer engine-respecting write paths over private datastore writes;
- prove identity remap instead of assuming it;
- read back both target creation and source non-mutation.

## Fascia B: Governed Live Update

The live update changed one activity duration through real desktop controls. UIA could not reach the target field, but win32 exposed the `TCDBEdit` controls. The operation proceeded only with:

- frozen target identity;
- trusted user token;
- selector/control evidence;
- post-edit gate;
- schedule/recompute handling;
- target readback;
- anti-collateral diff over the plausible affected surface.

The first attempted value was wrong and the post-edit gate prevented success from being claimed. The corrected value was then verified by independent readback.

Promoted generic lessons:

- actuator backend fallback is part of the method;
- high-risk UI/computer-use writes require risk-proportional readback;
- target-only checks are not enough when the hand can miss;
- no success before readback.

## Unit And Operating Knowledge Trap

P6 exposed a unit trap: an input that landed mechanically could mean the wrong duration because display/input units and canonical storage differed. The fix was not "try harder with the UI"; it was to require an operating manual with unit profiles and field semantics.

Giuseppe also added a domain note on progress methods: Physical percent complete does not re-estimate Remaining Duration, while Duration-based progress can. Unit progress may diverge from activity progress. This stays P6/planning-specific, but the generic rule is clear: a connector must know which operating method is active before writing progress or duration.

Promoted generic lessons:

- transport success is not semantic success;
- numeric/date/progress writes require unit calibration status;
- operating knowledge is a gate, not documentation garnish;
- derived state can require recompute even when visible dates do not move.

## What This Does Not Prove

This case does not prove:

- a P6 production connector;
- a general P6 Java API path for standalone SQLite;
- direct SQLite writes;
- true bulk edit;
- reusable UI automation for every P6 field;
- public/GitHub-ready connector-forge.

Every new app and every new command still starts at Gate 0 and earns its own evidence.
