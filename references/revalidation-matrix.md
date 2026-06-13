# Revalidation Matrix

Use this before release, before using a fast-moving host/protocol, or when a connector depends on current auth, transport, SDK, plugin, or host behavior.

## Purpose

Prevent stale assumptions from entering connector design.

## Minimum Columns

| Area | Assumption | Fragility | Revalidate when | Evidence/Test | Owner |
|---|---|---|---|---|---|
| MCP spec | | high/medium/low | | | |
| MCP auth/transport | | | | | |
| Host config | | | | | |
| App API/SDK | | | | | |
| CLI contract | | | | | |
| Security controls | | | | | |
| Acceptance tests | | | | | |

## Fragility Rules

- `high`: auth, transports, SDK versions, remote hosts, Apps/Cowork/Antigravity behavior, security guidance.
- `medium`: CLI grammar, adapter contract, OpenAPI shape, plugin packaging.
- `low`: stable local templates and project conventions.

## Release Rule

Do not release or rely on a connector if a high-fragility assumption is unverified and affects the MVP path.

Future-dated or non-final sources stay in quarantine until rechecked.

Revalidation status is separate from capability status: `verified` here means the assumption was refreshed, not that an operation is safe or implemented.

Revalidation status is separate from capability status: `verified` here means the assumption was refreshed, not that an operation is safe or implemented.
