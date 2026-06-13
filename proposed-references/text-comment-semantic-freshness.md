# Decisional Text, Semantic Freshness And Content Parsers

Use this reference whenever the connector reads or writes long human text (comments, notes,
decisions, descriptions), or classifies text into actions/votes/states, or signals that a
judgment may be stale. Decisional text is a critical asset, not a string.

## Core Rule

Decision memory is the one datum you cannot refetch -- treat it like an irreplaceable asset. Never
mutate long text from a truncated or whitespace-compacted view; prove an edit with a byte-level
diff; classify decisional text with parsers tested against the negated case of every positive
token; and signal, never silently, when data has moved under a written judgment.

## Part A -- Edit-Grade Read vs Display Read

Distinguish two read classes and never confuse them:

- **display read**: truncatable, whitespace-compactable, for showing an excerpt;
- **edit-grade read**: byte-faithful, newlines and emoji and accents preserved, bounded to an
  explicit small scope.

Never do read-modify-write from a view with `truncated=true` or with whitespace normalization -- it
silently destroys the tail and the formatting of the operator's text. The expansion flag that
returns full content is born in the same slice as its scope guard (explicit targets, <= N,
preflight fires before any app call); the display cap may be raised but is documented in code as
*not* a rewrite base. The app-side `old_value` requirement is a second independent net -- keep it
even when it seems redundant.

## Part B -- Byte-Level Diff Is The Acceptance Of An Edit

For edits to someone else's text, acceptance is the diff, not the outcome ("executed" doesn't say
what changed). The readback's changed-fields must equal exactly the intended insertion + tag
change, the rest byte-identical. Legacy-format warnings are expected semaphores: the operator's
historical content is not reformatted as a side effect of an edit. Strict on generated content,
tolerant on read for legacy -- and a targeted edit of a legacy note inherits the tolerance, never
the strictness.

## Part C -- Minimal Contracts, Not Cages (skeleton fixed, judgment free)

For structured text, enforce a minimal contract (e.g. exactly one action marker, at least one
recognized source anchor) but leave prose free where human judgment lives. The constitution:
standardize the skeleton and the discipline of evidence (fixed sections, source tags with dates,
penalty always traced, divergence always declared, append-only evolution log); leave free the
direction/measure of judgment. The validator enforces *form*; the human gate owns *substance*; a
declared divergence is the contract working, not a violation.

## Part D -- Never Substring On Negated Semantics

A classifier of decisional text (actions, intents, votes) is tested with the **negated case of
every positive token first**. "Non comprare" contains "compra" -- evaluate negations before the
positive branch, and anchor to canonical tokens by equality, not substring on free text. Substring
matching on natural language is a bug class, not a technique; declared residual edges (a token
inside a compound word) go in the parser contract. And when two surfaces parse the same decisional
content, both emit one canonical vocabulary; display translation lives only in the UI -- the
cross-surface vocabulary drift is invisible until someone compares the answers side by side.

## Part E -- Semantic Freshness (decisions age)

If data, gates, score, or interpretive parameters change after a comment was written, the comment
may be stale: signal it.

- VERDE: judgment written after the current data/gates; GIALLO: quarterly/gates/PE-type/forecast
  changed since; ROSSO: new annuals, mass annual import, or a strong contradiction (score 0 with a
  very positive comment). ROSSO means stronger attention, not forced rewrite;
- two-way clearing: confirm-without-change (attested) or rewrite (update / "evolution" line); both
  leave a trace (actor, date, reason, the event that lit the semaphore);
- the baseline is a signature of the data/gates/score at write time -- metadata beside the note,
  invisible; clearing it touches only the baseline, never a byte of the note;
- the freshness chip exposes a state, not a raw enum -- a green "CURRENT" is not an "Alert", and a
  never-baselined legacy note is a distinct state, not a false green.

## Part F -- Smart Filters Are Operative

A filter over decisional content searches text, vote, action, state/semaphore, and dates when
available; predicates are AND across sections, OR within; vote matching is startsWith
case-insensitive (decorated votes), action by equality on canonical tokens. A filter that looks
structured but cannot find vote/action/state is a serious bug; a zero-result must keep headers and
context mounted, never blank the grid.

## Acceptance

- long-text mutation only from an edit-grade byte-faithful read; expansion flag scope-guarded;
- every edit proven by a byte-level diff = insertion + tag change, rest identical;
- every content parser has negated-token tests; one canonical vocabulary across surfaces;
- freshness VERDE/GIALLO/ROSSO proven with data/gate/comment changes; clearing leaves a trace and
  does not touch the note;
- filter finds the expected cases and preserves context on zero result.

## Stop Rules

Stop when:

- a long note would be rewritten from a truncated/compacted view, or with `truncated=true`;
- a content classifier has no negated-token test (the "non comprare -> compra" inversion lurks);
- two surfaces emit different vocabularies for the same decision;
- a freshness clear would alter the note text, or a raw enum is shown to the operator as an
  "Alert" on a healthy state;
- a zero-result filter blanks the grid or hides headers.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Bridge V2 (edit-grade read / VF-2, byte-level diff
  acceptance, minimal-contract-not-cage, negated-token / BUG-F5-1, canonical-vocabulary /
  DRIFT-F5-2, semantic freshness semaphore, smart filters all originate here). The decisional-text
  pattern generalizes to any connector carrying human judgments (review notes, change rationales,
  inspection findings on Archicad/P6).
- Field lessons distilled: a 2000-char + whitespace-compacted note read that would have destroyed
  operator comment tails (caught before damage); a "non comprare" classified "Acquista" by
  substring; a healthy green note showing "Alert: CURRENT" to the operator.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
