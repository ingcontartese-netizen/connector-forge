# Release Claim Audit + Zero Drift (R3-24 / R3-S10)

ID: R3-24 (release gate) + R3-S10 (support checklist)
Owner: CLAUDE lead / CODEX checks
Status: active-v3-candidate / second-read-pass-with-notes
Class: release gate + process reference
Evidence rows: L08, L11, L22, L26, L31, L46, L50

## 1. Problem

A connector can look finished and still be unsafe to claim. Throughout the P6 bench the same trap recurred: a thing was documented but not installed, installed but not live, live but not writable, writable but not semantically correct, reported as PASS but never actually run. Release is the moment those gaps become public, so release needs its own gate.

## 2. The Claim Ladder

Each rung is a separate, non-inheriting claim. Promoting one does not promote the next.

- `documented`: the vendor/source says the capability exists.
- `installed`: the capability is present on this host (bytes on disk, runtime starts).
- `live`: the capability runs against the real running target.
- `readable`: live read verified through an authoritative path.
- `writable`: a governed write was applied and read back.
- `semantically_correct`: the write meant what was intended (units, domain, derived state).
- `repeatable`: proven beyond a single sandbox operation.
- `production`: drift-tested, secured, supported.
- `public_release`: packaged, secret-audited, licensed, sanitized.

A release claim must name the highest rung that has evidence, and explicitly mark everything above it as not-claimed.

## 3. Authoritative Verification Rule (MR4 as release law)

A claim is not evidence until it is checked through the most authoritative path available, not through a colleague's or tool's report.

- compile/run the committed checker; do not trust a printed PASS (P6: a truncated checker "passed" without compiling - L50).
- when file views disagree, prefer the authoritative read (file-tool over a possibly stale or truncated mount; DL-009).
- every status claim cites the artifact that proves it: file path plus hash or verdict.
- a second reader re-derives the result independently; "I ran it and it passed" is a starting point, not a conclusion (L11, L46).

## 4. No-Overclaim Register (binding for R3 final)

Never claim, unless and until evidence exists:

- "universal connector complete";
- "deployment-ready" / "production connector";
- "general <app> API proven" when only one surface/operation was proven;
- bulk/multi-record edit, when only single-operation was proven;
- automatic writable-field introspection beyond the proven field;
- live write, when only live read was proven;
- "calibrated", when no unit round-trip was executed (see R3-22);
- success from a high-risk UI/computer-use actuator, without anti-collateral readback.

Failure and superseded evidence (e.g. the wrong-unit P6 rows) is kept as proof that a gate is needed, never repurposed as proof that the wrong value was correct.

## 5. Zero-Drift Gate (R3-S09 hook)

Before any `v3 field-tested` or `public/GitHub-ready` claim, the same R3 content must match across all carriers included in that claim:

- core skill;
- Codex host pack;
- Cowork host pack;
- generated package;
- installed copy.

The `ZERO_DRIFT_MATRIX.md` must show parity for the claimed carriers (same file set, same versions, except declared host-specific packaging differences). Any undeclared divergence blocks the claim. Lesson counts must be machine-counted from the source ledger at release time, never hand-carried (the 83-vs-82 episode).

## 6. Release Gate Checklist (R3-S10)

A release claim passes only when all are true and cited:

1. claim ladder rung named, with the artifact proving it;
2. everything above that rung explicitly marked not-claimed;
3. every promoted capability has a committed, runnable check that was actually run;
4. no entry in the No-Overclaim Register is violated;
5. no-secret audit: no tokens, passwords, or auth blobs in shipped files (approval tokens stored as hash/reference only, per L38);
6. zero-drift matrix passes;
7. package integrity + install/reload smoke on the real host;
8. case-study content is sanitized (no customer/private data);
9. for `public/GitHub-ready` only: a second real-case bench beyond P6 (ValuAziende, API-native) has exercised the actuator ladder, so the method is not overfit to one UI case;
10. Giuseppe domain sign-off recorded.

## 7. Claim Scope Language

Every release note states three things in plain words: what is earned (with evidence), what is scoped/limited, and what remains needs-evidence. Example, from this bench:

- earned: governed single-operation write - file/import create and one live UI-actuator update - in sandbox, with readback and anti-collateral diff.
- limited: P6 standalone SQLite only; UI/win32 is a high-risk actuator under mandatory gates.
- needs-evidence: P6 Java API on SQLite (forbidden for that target), bulk edit, production, public release.

## 8. Stop Rules

Stop the release if:

- any promoted claim rests on a report that was not independently re-run;
- a checker referenced as evidence does not compile/run;
- drift exists between core, host packs, package, or installed copy;
- a secret would ship;
- the claim language blurs earned vs needs-evidence;
- Giuseppe has not signed off the domain scope.

## 9. Status

`active-v3-candidate / second-read-pass-with-notes`

## 10. Codex Second-Read (WP12.4)

Verdict: `PASS_WITH_NOTES`.

What was verified:

- Claim ladder separates `documented`, `installed`, `live`, `writable`, `semantically_correct`, `repeatable`, `production`, and `public_release`.
- No-overclaim register blocks the known risky claims: universal connector, production, app-general API, bulk edit, automatic writable introspection, live write without live-write evidence, calibrated without unit round trip, and high-risk actuator without anti-collateral readback.
- Release checklist includes no-secret audit, zero-drift, package integrity/install smoke, case-study sanitization, ValuAziende/API-native second bench for public readiness, and Giuseppe domain sign-off.
- P6 claim language is scoped to sandbox/single-operation and leaves production/public/bulk as needs-evidence.

Conservative correction applied by Codex:

- Zero-drift requirement now applies to the carriers included in the claim. Public/GitHub-ready still requires all shipped carriers. This avoids over-blocking a narrower host-specific `field-tested` claim while preserving the no-drift rule.

What is not claimed:

- no active skill migration;
- no host-pack/package parity yet;
- no public/GitHub-ready;
- no ValuAziende/API-native bench completed in this cycle.

## 11. OneMaster Draft Claim Boundary

OneMaster Draft is a method/spec claim, not a deployment claim.

Allowed claim:

- `connector-forge OneMaster Draft active in the Codex lane`.

Not claimed until separate evidence exists:

- OneMaster Ready;
- OneMaster Deployed;
- package-ready;
- public/GitHub-ready;
- Cowork package parity;
- package install/reload smoke;
- no-secret audit;
- ValuAziende Bridge V2 implementation;
- CLI/MCP parity;
- governed ValuAziende write smoke.

Carrier rule:

- if only the Codex active lane is patched, the release note must say so;
- if Cowork packaging is deferred, record `DECLARED_COWORK_LAG`;
- carrier parity requires `COWORK_PACK_PARITY`: rebuilt package, checksum, install/reload or host-visible proof, smoke, and declared host-specific differences.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Draft, 2026-06-03.
- Ledger atoms: OMD-M-12, OMD-M-13, OMD-M-18, OMD-M-21, OMD-M-29, OMD-M-30, OMD-M-33.
- Tags: APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / R3 / LAB.
- Claim limit: This is method/spec evidence. It does not prove a deployed bridge, package parity, production readiness, or public/GitHub readiness.
