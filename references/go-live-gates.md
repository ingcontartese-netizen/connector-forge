# Go-Live Gates

Use this reference before calling a connector ready, host-runnable, or go-live.

## Release states

Host-live validation states (DEP-P0-002):

| State | Meaning | Required evidence |
|---|---|---|
| `source_validated` | Source code, contracts, templates, and local checks are valid. This does not prove the host loaded the fresh process. | compile/lint/template check, contract snapshot, local test transcript |
| `fresh_process_validated` | The connector process was restarted or reloaded after the source change; stale bytecode/cache is ruled out or mitigated. | process restart transcript, build/version stamp, cache-bust setting if relevant |
| `host_loaded` | The primary host sees the expected server/connector and current tool catalog. | host settings/config, launch/handshake, tools/list snapshot with expected version |
| `host_live_validated` | The primary host executed at least one real live read and, when relevant, one recovery case. | host transcript with `mode: live`, real app state, recovery/error proof |

Promotion rule: `host_runnable` requires `host_loaded`; `go_live` requires `host_live_validated`.

Release decision states:

| State | Meaning | Required evidence |
|---|---|---|
| `local_validated` | Works from local scripts or direct tools, but host packaging may still be incomplete. | local smoke transcript, read result, dry-run/write evidence if in scope |
| `host_runnable` | The selected primary host can discover and run the connector. | host config, launch/handshake, tool discovery, one read smoke |
| `go_live` | Ready for the intended user workflow in the real host and real app state. | G0-G6 all passed, acceptance evidence, recovery proof, drift/revalidation current |

## G0-G6

| Gate | Name | Pass condition | Block condition | Evidence |
|---|---|---|---|---|
| G0 | Installability | package/adapter/bridge installs without ad hoc hacks | source-only or missing runtime entrypoint | install log, path, version |
| G1 | Handshake | host/client initializes cleanly | startup hangs or handshake fails | transcript/screenshot |
| G2 | Discovery | tools/resources visible with stable schemas | empty/stale/inconsistent catalog | tools list snapshot |
| G3 | State introspection | connector can read app/document/project state | no real state or mock-only without label | health/context output with `mode: live` |
| G4 | Read/export proof | one useful read and one verifiable export/preview; variable-size outputs have bounded-output evidence | ambiguous output, unverifiable artifact, or unbounded large payload | structured output, checksum/path/screenshot, `page_size=3` probe |
| G5 | Safety | dry-run/prepare exists for write path; approval and audit defined | write path lacks dry-run, approval, audit, or recovery | dry-run JSON diff, approval trail |
| G6 | Host smoke + recovery | primary host smoke passes and one recovery case is proven | only local test, no restart/auth/closed-app proof | host transcript, recovery runbook |
| G10 | Host-live states | `source_validated` -> `fresh_process_validated` -> `host_loaded` -> `host_live_validated` evidence is complete for the claimed release state | config exists but live host/process freshness is unproven | build stamp, restart transcript, tools list, live read |
| G11 | Bounded output | variable-size read/search/simulate/report outputs are limited by default and prove `page_size=3` or equivalent | unbounded payloads or no cursor/summary/artifact path | bounded payload transcript |
| G12 | Lifecycle observability | local/deployed bridge emits best-effort UTF-8 JSONL lifecycle events with no secrets | disconnects are opaque, logs go to stdout, or logs include secrets/payloads | lifecycle log sample + redaction check |
| G13 | Write intent proof | write path has intent contract, command availability, sandbox/approval, dry-run, apply, readback, expected-vs-actual intent proof, and rollback scope | technical success without intent proof; proxy passed as native; position/relationship/protected-field mismatch; rollback unknown | `INTENT_CONTRACT.md`, dry-run/apply transcript, readback, intent comparison, rollback scope |
| G14 | Cold-start acceptance | before `deployment-ready`/GitHub-ready claims, the skill guides an app not pre-studied from Gate 0 to first verified read and governed write/dry-run/readback/rollback when in scope | only known-case success; tool chosen from memory instead of method; no case-study evidence | `case-studies/COLD_START_*.md` with source registry, surface map, capability ledger, live proof, recovery |

## Rules

- Config presence is not readiness.
- Source validation is not host-loaded validation.
- Mock success is not live success.
- A patched connector is not fresh until `build_stamp` and lifecycle evidence show the running process is the patched process.
- Default `page_size` is 25 for variable-size read/search/simulate/report outputs; use `page_size=3` as the acceptance probe.
- A tool that cannot limit, project, summarize, cursor, or artifact large output stays `HOLD` for host readiness.
- Local/deployed MCP bridges without lifecycle logging or equivalent diagnostics stay `HOLD` for go-live.
- A write with no intent proof stays `partial` or `HOLD`, even if the API returned success.
- A native-object request must not be satisfied with a visual or metadata proxy unless the user explicitly accepts the downgrade.
- `deployment-ready` and public/GitHub-ready claims require cold-start evidence on an app not already used as the training case. Before that, use `field-tested`.
- On Windows, UTF-8 console/file/log behavior must be verified before rich comments or reports are accepted.
- If the MVP is read-only, write gates are marked `N/A` with reason, not silently skipped.
- If more than one host is in scope, each intended host needs its own G1-G6 evidence.
- `PACKAGE_INTEGRITY_MATRIX.md` is a P0-release gate before publishing packages.
## OneMaster Draft Addendum

Before bridge go-live, run a runtime gate: identity, config, app reachability, schema freshness,
side-effect classification, version trail, and acceptance baseline. A Bridge Doctor can collect
these facts, but it does not replace owner approval or acceptance evidence.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-06, OMD-M-17,
OMD-M-18, OMD-M-22; tags BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
