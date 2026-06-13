# Transport, Windows, Encoding And Cloud Sync

Use this reference when the connector runs on Windows, emits rich text, carries JSON payloads over
a shell, or lives on a cloud-synced store (OneDrive, Drive, FUSE mount). The environment is a
surface to tame, not a given.

## Core Rule

A connector that works in a clean lab and breaks on a real machine is not built. PowerShell
quoting, UTF-8 corruption, numeric type drift across transport, and cloud-sync read lag are
connector tests, not afterthoughts. Declare the authoritative surface for every artifact class and
the environmental warnings the doctor will always carry.

## Part A -- Windows Carrier And JSON Transport

The CLI/PowerShell carrier is a real acceptance surface: native argv and PowerShell strip JSON
quotes and split values with spaces. Do not pass complex payloads as fragile shell strings -- use a
payload-file mode or a CLI safe mode (stdin/file), and document the quoting. Bad payloads return
envelopes, not tracebacks: a JSON parse failure at the CLI boundary is connector behavior with a
clean error, never a stack trace. Include carrier examples in the host pack.

## Part B -- Numeric Typing Across The Transport Boundary

Round numbers that cross a transport boundary (Python <-> JS, JSON round-trips) can change type and
break the round-trip hash of a preview/staging. The number is not transport-safe by default: type
the staged payload (e.g. an explicit `staged_data_json` with declared float typing), and verify
the hash on both sides of the boundary. This is a named false friend -- register it.

## Part C -- UTF-8 And Mojibake, Precisely

Cover reports, PowerShell, relay files, long comments, accents, symbols, emoji. The useful symbols
(a calendar glyph next to a date, status emoji) must stay possible -- the problem to close is
encoding corruption, not the presence of symbols.

> Meta-note (lived): this reference cannot safely contain literal mojibake -- a host that sanitizes
> encoding will rewrite the very examples that teach the rule. So examples below are given by
> **codepoint and byte structure** (U+00C3, lead-byte 0xC3 + continuation), not by pasting the
> corrupt glyphs. The lesson is recursive: any artifact that teaches encoding rules must encode its
> examples as escapes/codepoints, or it corrupts its own evidence.

Detect mojibake by the **byte structure of the corruption**, not by suspicious single characters.
Blocking a bare lead byte U+00C3 (capital A-tilde) or U+00C2 (capital A-circumflex) produces false
positives on legitimate foreign uppercase -- "S<U+00C3>O PAULO", "<U+00C2>GE", "C<U+00C2>MARA" are
valid Portuguese/French and must pass. Real mojibake has a signature: a mis-decoded UTF-8 lead byte
+ continuation byte (`0xC3 [0x80-0xBF]`, `0xC2 [0xA0-0xBF]`) plus the cp1252 literal sequences
(`0xC3 0x83`, the `a-euro` group U+00E2 U+20AC, the emoji-prefix U+00F0 U+009F). Always verify
precision *and* recall with adversarial cases from both sides: "C<U+00C2>MARA" passes; the
corruption of "e-grave" (U+00C3 U+00A8) and the corruption of "Perche" (ending U+00C3 U+00A9) block.
The guard has independent veto: text that is contract-conformant but mojibake is
`generation_allowed=false`. Textual guardrails are designed from the mechanics of the corruption,
not the appearance of the symptom.

## Part D -- Cloud Sync Is An Eventually-Consistent Cache

OneDrive/FUSE/Drive mounts are eventually-consistent: a freshly-written file can appear truncated,
stale, or (for a DB the backend is writing) malformed when copied mid-sync. The discipline:

- declare, per artifact class, the **authoritative surface**: DB -> the bridge's read, never a file
  copy during active sync; source files -> the owner-side read tool, never the mount right after a
  write; shared logs -> the authoritative file tool, not the mount seconds after an append;
- any verification of a file written seconds ago via the mount is suspect by default; the repair
  pattern (splice authoritative tails into a /tmp test copy) is documented routine, not rediscovery;
- never read a live DB by copying it while the backend writes, unless declared safe; the finished
  backup file is the static, copyable surface for read-only inspection.

## Part E -- Pycache, Process Hygiene, Restart Reality

Bytecode and process state are environment too: stale pyc with mixed Python tags, orphan/duplicate
bridge processes that survive a restart, a reload that did not recycle the answering process. These
are diagnostics the doctor reports (pyc tags, process freshness) -- facts, never auto-delete/rebuild
decisions, which stay manual. A cold restart is a full-reload opportunity *and* a hygiene event;
the doctor parity check after restart is mandatory before any battery.

## Acceptance

- tests with accents, emoji, newline, long text; PowerShell/Windows carrier test;
- payload-file or safe mode for complex payloads; CLI parse failure returns an envelope;
- numeric typing across boundary tested (preview hash matches both sides); the false friend
  registered;
- mojibake precision+recall proven with adversarial cases both ways;
- authoritative surface declared per artifact class; environmental warnings explicit in the doctor;
- restart followed by doctor parity before any test.

## Stop Rules

Stop when:

- a complex payload is passed as a fragile shell string;
- mojibake detection blocks legitimate foreign letters or is tuned by symptom not byte-structure;
- a live DB is copied mid-sync and trusted (it will be malformed -- use the bridge or a frozen
  backup);
- a file written seconds ago via a synced mount is trusted without the authoritative-surface
  check;
- a battery runs after a restart without a doctor parity check (orphan-process risk).

## Evidence Provenance

- Source bench: ValuAziende OneMaster Bridge V2 on Windows + OneDrive (PowerShell carrier,
  mojibake precision M-22/M-22b, numeric-typing false friend, OneDrive/FUSE authoritative-surface
  discipline, pycache/process hygiene all originate here). Archicad 29 (Windows desktop) and
  Primavera P6 (Windows + standalone DB) confirm the environment-as-surface generalization.
- Field lessons distilled: a live-mount DB copy failing malformed repeatedly; a "S<U+00C3>O PAULO"
  false positive fixed by byte-structure detection; a numeric round-trip breaking a staged hash;
  three FUSE-truncation episodes on freshly-edited source repaired from the authoritative read; and
  this very file's literal special characters rewritten by the host encoding on save -- the rule
  proving itself.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
