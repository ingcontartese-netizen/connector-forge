# connector-verifier

Use this checklist before declaring connector-forge package/source changes ready.

## v2.3 Fascia A Checks

- `SKILL.md` version says `2.3.0 field-tested`.
- Operating funnel includes Gate 0.0 before Gate 0 when the app domain is non-trivial.
- `DOMAIN_MODEL.md` template exists.
- References exist for domain comprehension, domain-semantic validation, resolver freeze, false friends, source depth, live-vs-persisted, embedded DB/WAL, host-access asymmetry, acceptance evidence extended, packaging/deploy hardening, cold-start ledger, and case-studies index.
- Continuity reference exists and states what is new, what extends 2.2, and what remains deferred.
- `ACCEPTANCE_EVIDENCE_EXTENDED.md` exists or equivalent fields were merged into the host package.
- P6 case-study is marked evidence, not a host-specific rule.
- Fascia B write-path items remain deferred/needs-evidence until bridge proof.
- No angle-bracket placeholders remain in user-facing package metadata.
- Changelog includes 2.3.0 and explicit deferred write-path note.

## Release Reminder

This verifier confirms source/package consistency. It does not prove `deployment-ready`; host live load still needs build/version/read evidence.
