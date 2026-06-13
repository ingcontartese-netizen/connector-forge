# Eval And Drift

Do not call a connector ready until it passes acceptance and drift checks.

## Acceptance Tests

Minimum:

- `doctor` or health check;
- install/handshake in the primary host when possible;
- lifecycle log evidence for local/deployed bridges;
- one discovery/read operation;
- schema validation for output;
- bounded-output proof for variable-size read/search/simulate/report operations;
- export/preview artifact with checksum when relevant;
- auth failure test;
- forbidden capability test;
- timeout/error test;
- dry-run test for first write;
- intent proof for first write: expected vs actual, native/proxy class, placement/relationship or protected-field comparison when relevant;
- rollback or recovery note for write path.
- UTF-8 output guardrail when running on Windows or emitting rich text.

Use non-promotional benchmarks only: same account, same task, same network conditions where possible, cold/warm runs, p50/p95 latency, retry count, failure taxonomy, and token/tool-call cost if available.

## Drift Report

Record:

- source docs checked and dates;
- local app/API version;
- contract hash or snapshot;
- changed fields/tools/scopes;
- tests run;
- failures and follow-up.

Use `scripts/drift_report.py` for simple expected/current comparisons and extend when the target project needs richer checks.

## Go-Live Gates

Use these gates when the user asks for release, readiness, version bump, publishing, or real host use.

Release states:

- `source_validated`: source code, contracts, templates, and local checks are valid, but host freshness is not proven.
- `fresh_process_validated`: the connector process was restarted or reloaded after source changes, with stale cache/bytecode ruled out or mitigated.
- `host_loaded`: the primary host sees the expected server and current tool catalog.
- `host_live_validated`: the primary host executes a real live read and, when relevant, a recovery case.
- `local_validated`: works from local scripts or direct tools, but host packaging may still be incomplete.
- `host_runnable`: the selected primary host can discover and run the connector.
- `go_live`: the intended workflow has live evidence, recovery proof, current security checks, and current drift/revalidation.

Promotion rule: `host_runnable` requires at least `host_loaded`; `go_live` requires `host_live_validated`.

Minimum G0-G6 evidence:

- G0 installability: package/adapter/bridge installs without hidden manual steps.
- G1 handshake: host/client initializes cleanly.
- G2 discovery: tools/resources are visible with stable schemas.
- G3 state introspection: connector reads real app state in `mode: live`, or marks mock/stub as hypothesis.
- G4 read/export proof: one useful read and one verifiable export/preview; variable-size outputs prove default `page_size=25` or equivalent limit, plus an acceptance probe with `page_size=3`.
- G5 safety proof: dry-run/prepare, approval, audit, and recovery for write paths; explicit `N/A` when the MVP is read-only.
- G6 host smoke + recovery: primary host smoke passes and one recovery case is proven.
- G10 host-live states: `source_validated` -> `fresh_process_validated` -> `host_loaded` -> `host_live_validated` are evidenced.
- G11 bounded output: variable-size operations prove default `page_size=25` or equivalent, plus `page_size=3` acceptance probe.
- G12 lifecycle observability: deployed/local bridges have best-effort UTF-8 JSONL logging with start/transport/tool/error/end events and no secrets.
- G13 write intent proof: state-changing operations prove command availability, intent contract, dry-run, approval, apply, readback, expected-vs-actual comparison, and rollback scope.
- G14 cold-start acceptance: `deployment-ready`/GitHub-ready claims wait for a case-study on an app not pre-studied by the current project.

Use `references/go-live-gates.md` plus `assets/templates/SPRINT1_READINESS.md`,
`assets/templates/ACCEPTANCE_EVIDENCE.md`, `assets/templates/WORKING_PAYLOADS.md`, and
`assets/templates/LIFECYCLE_LOGGING.md`, `assets/templates/WINDOWS_UTF8_GUARDRAIL.md`, and
`assets/templates/PACKAGE_INTEGRITY_MATRIX.md`, plus `assets/templates/INTENT_CONTRACT.md` when writes are in scope.

## Readiness Gate

Ready means:

- Source Registry current;
- Revalidation Matrix current for high-fragility assumptions;
- Capability Ledger has no unreviewed hypothesis in MVP path;
- Security Mesh complete;
- branch-specific smoke passed;
- host pack verified in the target client when possible;
- Go-Live Gates G0-G6 evidenced before claiming `host_runnable` or `go_live`.
- host-live states evidenced before claiming `host_runnable` or `go_live`;
- bounded-output evidence recorded before promoting any variable-size read/search/simulate/report operation.
- lifecycle observability evidenced for local/deployed bridges, or an equivalent diagnostic channel documented;
- Windows UTF-8 guardrail verified when applicable.
- write intent proof evidenced before calling a write successful;
- cold-start case-study complete before calling the skill `deployment-ready` or public-release ready.
