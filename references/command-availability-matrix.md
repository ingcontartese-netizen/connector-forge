# Command Availability Matrix

Use this reference when a capability depends on a command, SDK function, add-on operation, MCP tool, CLI command, or host-exposed action.

The matrix is not a hard gate by itself. It is a reference used by Surface Map, Capability Ledger, and Gate 13 to prevent "documented" from being mistaken for "available live".

## States

| State | Meaning | Promotion rule |
|---|---|---|
| `documented` | Primary docs, repo, changelog, or guide says the command exists. | Not enough for `verified`. |
| `in_static_schema` | Static schema, changelog, manifest, or generated catalog lists it. | Still not enough for live use. |
| `installed_local` | The local install contains the dependency, package, add-on, plugin, or binary. | Still not enough for host use. |
| `live_available` | The running app/SDK/add-on reports the command as available. | Candidate for dry-run. |
| `host_exposed` | The bridge/MCP/CLI host catalog exposes the command with schema. | Candidate for host smoke. |
| `dry_run_proven` | A no-side-effect or schema-only call succeeds in the target environment. | Candidate for controlled apply. |
| `apply_proven` | A minimal apply succeeds in a sandbox and readback passes. | Can support `verified` for scoped write. |
| `blocked` | Missing, stale, not authorized, wrong version, or unsafe. | Do not expose as stable. |

## Template

| Capability | Command/tool | Documented | Static schema | Installed local | Live available | Host exposed | Dry-run proven | Apply proven | Evidence | Notes |
|---|---|---|---|---|---|---|---|---|---|
|  |  | yes/no/n/a | yes/no/n/a |  | yes/no/n/a | yes/no/n/a | yes/no/n/a | yes/no/n/a |  |  |

## Evidence Rules

- Prefer primary docs, installed files, live version probes, and host catalog snapshots.
- Record version and build stamp when a dependency can drift.
- Record exact schema shape used in the successful dry-run.
- Keep failed probes when they reveal useful schema or version information.
- Do not promote a command to `verified` from examples, screenshots, memory, or another host's report alone.

## Live Version Rule

For SDKs, add-ons, plugins, and CLIs, read the live version before use.

If the live version is older than the guide/schema expects, treat the upgrade as a mini-deploy:

1. backup old package/config;
2. install or switch version;
3. restart host/app if needed;
4. run health/version;
5. run one readback smoke;
6. update the matrix with evidence.

## Output-Shape Diagnostic

If a patch should change output but the output shape remains identical, suspect stale process, bytecode, mount, or host cache. Verify with filesystem-authoritative read, build stamp, and fresh process before editing again.

## Failure Rule

If a command is documented but not live available or host exposed, the connector must either:

- implement the missing bridge/adapter layer;
- use a higher-quality authorized surface;
- keep the capability as `hypothesis`;
- or stop with a diagnostic.
