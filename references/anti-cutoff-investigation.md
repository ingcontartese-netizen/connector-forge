# Anti-Cutoff Investigation

Use this when docs are missing, stale, contradictory, newly released, or beyond model memory.

## Evidence Order

1. Vendor docs and changelog.
2. Official SDK/repository examples and tests.
3. Local installation files, manifests, help output, plugin registry, logs.
4. Authorized backend surfaces such as `/openapi.json`, route inventory, schemas.
5. Read-only live probing in a test environment.
6. Community sources as weak hints only.

## Five Phases

1. Source scouting: collect primary docs and current versions.
2. Local inspection: verify what is installed and enabled on this machine.
3. Live probing: run harmless reads and capture exact output/error shape.
4. Wrapper validation: normalize schemas, aliases, errors, and recovery.
5. Technical/legal stop: stop when authorization, surface, or terms are unclear.

## Controlled Documentation Creation

When docs are absent, create:

- route inventory;
- command registry;
- error catalog;
- OpenAPI diff;
- `COMMANDS.md`;
- `PROJECT-KNOWLEDGE.md`;
- fixture transcripts.

Do not invent missing fields, endpoints, scopes, IDs, or workflows.
