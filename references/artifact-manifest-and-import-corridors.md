# Artifact Manifest And Import Corridors

Use this reference whenever the connector exports, imports, reports, or ingests a real file, or
when a provider feed writes financial/business data. Files and feeds are governed chains, not
fire-and-forget.

## Core Rule

Every real artifact carries a manifest; every import is parse -> validate -> governed apply ->
readback, with the AI at the edges and never in the middle of a structured-data path. A preview
is not an apply. The deterministic corridor is the default; the AI corridor is for unstructured
files only, with a cost guard and the operator's chosen model.

## Part A -- Artifact Manifest

For every export/import/report/backup, record: path, sha256, origin, actor, timestamp,
operation/source, target, and the linked readback or proof. The manifest is the diary that keeps
real files and real proofs from getting lost. Verify the sha at the points that matter (local,
preview manifest, apply manifest) -- a hash mismatch across a transport boundary is a real failure
mode (numbers that cross Python<->JS can change type and break a staged-data round-trip hash;
type the staged payload).

## Part B -- Preview Is Not Apply

`provider.preview` / `import_preview` are read-only and must prove it (no side effects, no
timings). Preview declares: the diff vs current state, the field/period mapping, the conflicts
(identical / real conflict / new), and -- on periodic data -- the temporal/fiscal alignment. Target
echo and mismatch block on the binding (e.g. the file's declared target must match the resolved
company, or block). The semantic mapping is validated against allowlists **derived from the
runtime catalogs**, never a parallel list; blocked semantics (half-year, TTM into an annual slot)
fail in preflight before any upload/backup/AI, with per-entry errors.

## Part C -- Deterministic-First, AI At The Edges

When a file is machine-readable, parse it deterministically (openpyxl over the column names the
sheet already uses) and write through the existing governed verbs -- do not build a second AI
parser. Never use an LLM as the *transport* of a structured tool call: it adds latency (timeouts),
premium token cost, and non-determinism, and decides nothing the payload doesn't already carry.
The integrated app AI, if any, is the *interpreter* of unstructured artifacts; the bridge is
governance/validator/receipt/readback; the operator decides if a not-observed mapping gap is
acceptable. Before building a new dedicated corridor, **inventory the granular verbs you already
have and try composition** -- the dedicated facade is convenience built afterward, not a
prerequisite. The strongest validation of a new corridor is a two-lane parity test (same file,
corridor A vs B, field-by-field diff): every difference is either a bug or a semantics not yet
understood; a difference that is provenance (residuals under a template) is declared as such.

## Part D -- Provider Apply Tiers And Trace Rows

Provider apply separates `only_empty` (YELLOW: fill gaps) from `overwrite_all` (RED: target echo +
automatic backup before apply). The provider audit rows it writes (one RawProposal per staged
block, dedup by sha256) are **trace/provenance, not the canonical queue and not drift** -- declare
them in the schema/atlas so a +N delta after an import is never mistaken for drift. Company
metadata is not written by a financial-staged apply unless the contract says so.

## Acceptance

- import preview shows diff + mapping validation + fiscal alignment; preview proves no side
  effects;
- apply carries backup (RED) + receipt + readback; target echo + mismatch block present;
- a broken/mismatched mapping fails in preflight (per-entry errors, zero app calls);
- deterministic vs AI two-lane parity tested where both exist (field-by-field, zero unexplained
  diff);
- manifest complete with sha verified across boundaries; staged payload typed;
- provider trace rows classified as trace in atlas/schema.

## Stop Rules

Stop when:

- a "preview" can write, or an apply lacks backup/receipt/readback at its tier;
- an LLM is the transport of a structured tool call (parse deterministically instead);
- the import schema validates against a parallel list instead of the runtime catalogs;
- a sha is not verified across a transport boundary, or staged numbers are untyped;
- a provider/app trace delta is read as drift without being declared.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Bridge V2 (artifact manifest, preview!=apply, semantic
  mapping governance, deterministic-vs-AI two-lane parity, provider tiers and trace-row
  classification all originate here). Archicad 29 (file/object import into a host model) and
  Primavera P6 (external schedule ingestion) generalize the import-corridor and changeset
  patterns.
- Field lessons distilled: an AI-transport import dying of timeout while the deterministic
  corridor (parse + existing governed verbs) imported the same file with 936 values and zero
  diff; numeric typing across Python<->JS breaking a preview hash; a +10 raw_proposals delta after
  an import that was provenance, not drift.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
