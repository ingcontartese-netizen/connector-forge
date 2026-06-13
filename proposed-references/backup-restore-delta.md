# Backup, Restore, Rehearsal And Delta Replay

Use this reference before any destructive verb, any reset, and before declaring a connector
recovery-capable. Recovery is a capability you prove, not a promise you write.

## Core Rule

A recovery class is invalid until a verb executes it and a readback proves it. Destructive and
mass operations carry a fresh backup or a restore rehearsal sized to risk; on an irreplaceable
asset, a failed backup aborts the action; the audit that records governance lives outside the
blast radius of the thing it audits.

## Part A -- Backup Before Destruction, Abort On Irreplaceable

Every destructive verb and every mass reset takes a backup *before* the loop that destroys, and
before commit -- a backup taken after the wipe is waste paper. The backup uses the same connection
type as the app (SQLite backup API over the live connection, file-copy only as a declared
fallback) so it captures all data, including uncommitted/WAL state.

Then the decision the recoverability model dictates (see purpose-canon, asset risk model):

- on **flux/refetchable** data, backup-fail may warn-and-continue (prices refetch);
- on an **irreplaceable** asset (decision memory, method, audit), backup-fail **aborts** the
  action -- `HTTPException`, operation cancelled, nothing destroyed. The mass-rule-reset that
  zeroes hand-written notes is the canonical case: it must abort if its backup fails, not proceed.

The confirmation carries the impact count ("this will erase N notes and M manual gates"); the
response carries the created backup filename. Visibility, not ceremony.

## Part B -- Restore Rehearsal As Acceptance

The reversible rehearsal is *the* way to close a write acceptance: a governed forward+inverse
round-trip (propose -> detail -> approve -> semantic readback -> inverse_modify -> propose inverse ->
approve -> before==after from the engine) proves, in one experiment, the semantic readback, the
authorization chain, the positive target-lock, and the L2 recovery -- five evidences from one act.

Honesty of the rehearsal: **"reversible" is not "zero residue."** Business state returns identical
(the note hash as witness), but derived-history tables grow (score_history) and the audit lane
grows (+2 approved). The honest claim is "business state restored, declared history residue,"
never "no trace." The per-table cleanup readback is the tool that declares the delta.

Gate class discipline (the claim that must not blur): every safety gate is declared
`machine_verified` (a preview hash that must match) or `operator_attested` (a receipt string the
preflight cannot distinguish from a real rehearsal). "HOLD with attestation required" is not
"restore proven." The ledger exposes the class of each gate per write verb; the ready claim states
which gates are which.

## Part C -- Real Restore And The Post-Backup Delta

Rehearsal first; a real restore on live data only with a fresh backup, a disposable/golden target,
or an explicit operator GO, and a before/after parity hash. Backup taxonomy is the target's, not
invented (checkpoint != backup != export != restore, with an "includes state-file?" matrix), and
restore semantics are declared per surface -- a DB restore winds back the DB but not a sibling
state file.

The trap to plan for: a restore winds back the app's internal audit row of the very delete that
triggered it -- the history is erased by its own remedy -- while the bridge's audit lane, **outside
the DB**, keeps the whole sequence. And after a real restore from an older backup, build the
**post-backup delta list**: the writes that happened in the window between the backup and now,
to replay byte-faithfully. (Lived: a restore from a 22:32 backup, then the four trade-comment
writes of 22:43-22:52 replayed with identical final hashes.)

## Part D -- The Frozen-Backup Surface (when the live mount lies)

On synced/cloud-backed stores the live DB cannot be copied while the backend writes (it comes out
malformed -- the FUSE/OneDrive trap). The authoritative read for live data is the bridge, not a
file copy. But a **finished backup file** is static and copyable: open it read-only to verify
contents (integrity, counts, the irreplaceable asset present) -- this is how a verifier certifies
a backup *contains* what it claims before trusting it.

## Acceptance

- restore rehearsal documented; real restore tested at least on disposable/golden before ready;
- backup-before-destroy proven by position in code; backup-fail aborts on irreplaceable asset;
- backup is complete (not a convenient table, but every asset needed for operational survival);
- before/after parity hash on real restore; per-table cleanup delta declared;
- gate class (machine-verified vs operator-attested) declared per write verb;
- post-backup delta list produced after any older-backup restore.

## Stop Rules

Stop when:

- a destructive verb has no backup or rehearsal sized to its risk;
- a backup-fail proceeds on an irreplaceable asset;
- "reversible" is claimed as "zero trace" without the residue declared;
- a restore is claimed without a before/after readback, or its per-surface semantics are
  undeclared;
- a backup is trusted without verifying it *contains* the asset (open the frozen file read-only).

## Evidence Provenance

- Source bench: ValuAziende OneMaster Bridge V2 (the rehearsal-as-acceptance pattern, gate-class
  declaration, audit-outside-blast-radius, abort-on-irreplaceable, frozen-backup verification, the
  post-backup delta replay all originate here, several proven in a real accidental mass-reset
  recovered in 25 minutes). Archicad 29 and Primavera P6 generalize backup/rollback to native
  project files and standalone schedules.
- Field lessons distilled: a real restore on a live company with perfect before==after parity
  hash; an accidental "recalculate rules" zeroing 79 notes + 44 gates, recovered from a verified
  22:32 backup; the live-mount copy failing malformed while the frozen backup opened clean.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
