# CAPABILITY_LEDGER

Verifiable capability ledger for the connector.

## Capability Table

| Capability | Surface | State | Evidence | Risk | Native/proxy class | Domain class | declared_limits | Notes |
|---|---|---|---|---|---|---|---|---|
| health / doctor |  | verified / hypothesis / forbidden |  | read | N/A | N/A |  |  |
| get active context |  |  |  | read | N/A |  |  |  |
| list/search/get |  |  |  | read | N/A |  |  |  |
| export / preview |  |  |  | safe | visual_proxy/artifact |  |  |  |
| simulate |  |  |  | safe | N/A |  |  |  |
| propose governed change |  |  |  | write-governed | native_hypothesis |  | direct apply forbidden until approved |  |
| create/update/delete |  |  |  | write-safe/write/write-destructive | native_verified/hypothesis |  |  |  |
| batch/sync |  |  |  | safe/write |  |  |  |  |
| auth/login/logout |  |  |  | read/write-governed | N/A |  |  |  |

## Canonical Values

State:

- `verified`
- `hypothesis`
- `forbidden`

Risk:

- `read`
- `safe`
- `write-safe`
- `write-governed`
- `write`
- `write-destructive`
- `open-world`

Native/proxy class:

- `native_verified`
- `native_hypothesis`
- `visual_proxy`
- `metadata_only`
- `unsafe_generic`
- `forbidden_proxy_for_native_request`

## Rules

Expected behavior is not evidence.

A capability enters the stable catalog only after repeatable evidence on a real environment.

Read/search/simulate/report capabilities with variable-size output require bounded-output proof: default `page_size=25` or equivalent limit, probe `page_size=3`, and metadata/cursor/summary/artifact when applicable.

`declared_limits` is mandatory when a capability can be misunderstood. State what the connector cannot yet do instead of promising beyond proof.

For user-facing counts/lists/details, `verified` also requires Domain-Semantic Validation: fill `Domain class`, link `DOMAIN_MODEL.md`, and cite false-friend handling when relevant.
