# Surface Census, Doctor, Tool Atlas And Natural Questions

Use this reference after the purpose canon and before promoting any operation: it maps every
surface that can diverge, builds the doctor that proves which build is live, and generates the
command map agents use to act instead of guessing.

## Core Rule

A serious connector knows all the places its target's state can live, proves at runtime which
copy of itself is actually answering, and exposes a contract-generated map of what to do -- so an
agent chooses a command from evidence, never from memory. A surface you did not census is a
surface that will lie to you; a catalog you maintain by hand is a second source of truth that
will drift.

## Part A -- Surface And State Census

Before writing operations, enumerate every surface that can hold or mutate state, because they
diverge:

- UI, API, MCP, CLI, the database, files, caches, the AI assistant, the browser, host processes;
- behavioral state that lives **outside** the datastore (a settings/state file beside the DB:
  rules, profiles, thresholds -- a DB restore does not roll it back). Restore semantics are part of
  the truth contract: declare, per surface, what a restore winds back and what it does not;
- capability that depends on **active configuration**, not only version: feature flags with
  fallbacks make the same build behave two ways -- the doctor must report which mode is live;
- multiple governance pipelines: when the target has more than one (e.g. a provider audit lane
  and an agent proposal lane), every write verb declares which pipeline it lands in, and expected
  deltas on *every* pipeline (even the unused one) go in the readback or environment notes -- the
  bare word "pending" is ambiguous when there are several queues.

## Part B -- The Doctor (prove the live build, don't decorate)

A bridge doctor is a target-pattern for evidence, not a health claim. It must let a second reader
verify lifecycle, route, schema, runtime, identity, and host-pack state. Required dimensions:
identity (name, generation, version, build stamp); **source/runtime parity** (the marker read
from disk vs the marker of the module actually imported by the answering process -- they must
match, or traffic RED with a dedicated warning); contract version and op count; lifecycle and
reload behavior; capability state; side-effect class; output discipline; security/trust boundary;
old-new and package-vs-source parity; environmental warnings declared but never confused with
blockers.

Hard-won doctor rules:

- **deployment state travels in the marker.** Embed who-verified and what-is-pending into the
  version/status string; reading it via schema-describe is the only reliable proof of host-loaded.
  Bump the marker in the same commit as the code; bonify stale status labels as debt, never let
  them decay (a label saying `pending_reload` after the reload is active disinformation);
- **disk-reading surfaces lie about stale lanes.** Census which operations read from
  disk/external resources at call time vs from the imported module. Disk-readers (an atlas
  generated from a contract file each call; a doctor reading the marker from disk) can answer with
  the *new* contract on a lane running *old* code -- they are never build discriminators, and must
  self-declare parity (carry the runtime-imported marker) before any host-loaded claim;
- **a restart may not recycle the right process.** Orphan/duplicate processes survive; the doctor
  parity check after a restart is mandatory before any battery, not optional;
- **identity pin: pin only the stable.** Pin project root, DB path, instance fingerprint; exclude
  volatiles (pid, start time, runtime fingerprint) and document the exclusion *inside* the pin;
  emergency env override with declared precedence. A pin that includes volatiles cries wolf every
  boot and gets disabled -- an identity alarm with routine false positives is worse than none.

The doctor produces a bounded report naming what passed, failed, is missing, is stale, which
claims are blocked. It never auto-promotes a connector.

## Part C -- Tool Atlas, Command Map, Natural Questions

The number-one time sink on a new bridge is figuring out *which* tool and *how*. Kill it with a
machine-readable, **contract-generated** atlas -- never hand-maintained:

- per operation: purpose, when-to-use / when-not, tier, read/write class, target echo, valid
  examples, expected errors, recommended readback, recovery class, forbidden fallbacks;
- an intent router that maps the operator's natural request to a command or to STOP;
- a UI field map generated from the runtime catalogs when the bridge assists a grid/app;
- a materialized false-friends register inside the atlas (same word, two states; a P/E variant;
  a vote vs an engine verdict) -- queryable, not buried in minutes.

Two acceptance disciplines:

- **replay the example.** Every machine-readable example in the catalog must reproduce the
  documented outcome when executed verbatim; a self-doc catalog whose examples don't run is worse
  than none. Run them as a replay suite.
- **replay natural questions.** Real operator prompts and UI phrasings become router replay tests.
  Destructive requests must route to STOP / RED_HOLD, never to a convenient shortcut. The router
  decides whether an agent proceeds or stops -- it is a safety layer, and needs its own guardrail
  tests, including the precedence of ambiguous domain phrasing (e.g. "results" -> earnings vs
  "data" -> quarterly).

Operating rule promoted from the field: **atlas first.** To *operate*, agents start from the
atlas / intent-router / schema-describe -- verb, schema, template, semaphore in one call -- never
from grepping the source. The source is read to *verify* (the verifier role), not to discover how
to operate; and before a batch of a risky verb, probe one row first.

## Acceptance

- doctor read-only, source/runtime parity verifiable, environmental warnings declared not
  confused with blockers; identity `pinned_match` where the risk justifies a pin;
- every state surface enumerated; restore semantics declared per surface; active config reported;
- atlas generated from contracts, generic and specialist views coherent, hash deterministic;
- replay-the-example passes; natural-questions replay passes; destructive intents route to STOP;
- false-friends register materialized and queryable.

## Stop Rules

Stop when:

- you cannot inspect the actual host-loaded copy, or the advertised catalog disagrees with the
  implementation;
- a disk-reading operation is being used as proof of build (it never is);
- a restart was declared but doctor parity still shows the old marker (orphan process -- recycle
  before any test);
- the atlas is hand-maintained, or an example does not reproduce its documented outcome;
- a destructive natural-language request resolves to anything but STOP.

## Evidence Provenance

- Source benches: ValuAziende OneMaster Bridge V2 (the doctor, marker parity, identity pin, tool
  atlas, natural-questions replay, false-friends register all originate here); Archicad 29 and
  Oracle Primavera P6 as the desktop and standalone-DB generalizations (host-loaded proof,
  embedded-DB/WAL surfaces, host-access asymmetry).
- Field lessons distilled: source-vs-import parity catching a real stale lane in production; three
  separate disk-reader false-witness episodes; restart-not-recycling-the-process; first
  `pinned_match` after a full PC reboot; atlas-first cutting a 7-minute reconnaissance to one call.
- Claim limit: method/spec guidance only; not a deployed-bridge, package, or production claim.
  Benches are sanitized case studies.
