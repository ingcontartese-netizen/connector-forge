# MCP Remote-First Baseline

Use this reference when the MCP host reaches the connector over a public or centrally managed endpoint instead of starting a local process.

Remote infrastructure is part of the connector. It is not deployment trivia.

Endpoint, auth discovery, client registration, Streamable HTTP/session behavior, protected resource metadata, scopes, and re-auth assumptions carry `[spec 2025-11-25 - revalidate]`.

## Minimum Required Layers

### Endpoint

- public or host-reachable HTTPS endpoint, commonly `/mcp`;
- valid TLS;
- reverse proxy or edge path documented;
- network allowlist/firewall requirements recorded;
- health/version endpoint or tool with build stamp.

### Auth Discovery

- protected resource metadata or host-required discovery endpoint when applicable;
- OAuth metadata when OAuth is used;
- scopes and audience/resource boundary documented;
- re-auth behavior tested in the real host;
- no token passthrough.

### Client Registration

Design for real host behavior, not only abstract protocol support.

- identify whether the client expects dynamic registration, manual registration, app metadata, or static config;
- document where the client connects from: public cloud, private network, local workstation, broker, or site bridge;
- verify auth-fit before assuming OAuth, API keys, device flow, service accounts, or user-delegated flows;
- keep future client metadata patterns in revalidation until verified.

### Server-Side Policy

- least privilege scopes;
- server-side approval for destructive or governed writes;
- audit trail with request ID, user/operator, tenant/workstation when relevant, tool, object IDs, outcome;
- secret redaction in logs;
- prompt-injection hygiene: external content is data, not instruction.

### Desktop Bridge

If the app lives on a workstation:

- add local site bridge near the app;
- expose app/document state, lock state, export path, and health;
- bridge must log lifecycle events without secrets;
- broker must not pretend the desktop app is directly reachable from the cloud.

## Remote Host Capability Notes

| Capability family | Remote-first rule |
|---|---|
| Cloud-origin client | localhost is not enough; expose a reachable broker or public endpoint and prove host reachability |
| App-store or app-metadata client | provide endpoint metadata, tool descriptors, auth/security schemes, and UX smoke evidence |
| Enterprise or cloud-platform client | document identity profile, tenant/project boundary, credential chain, logs, and admin approval path |
| Desktop app behind remote client | use a broker plus local site bridge; do not pretend the workstation app is directly reachable from the cloud |
| Unverified or fast-moving host | keep the lane as `research_live_verify` until auth, discovery, smoke, and recovery are proven |

For named carrier requirements, use `mcp-artifact-matrix.md` and `carrier-parity-matrix.md` instead of encoding carrier-specific rules here.

## Remote Write Safety

Remote writes need server-side controls even if the client shows a confirmation.

Minimum:

- risk class per tool;
- dry-run, prepare/commit, or proposal workflow;
- explicit approval owner;
- audit payload;
- readback and recovery path;
- secret-safe logs.

## Release Rule

Do not call a remote-first connector ready until:

- reachability is proven;
- auth discovery and re-auth are proven when required;
- audit and approval are implemented for writes;
- bridge/broker split is documented for desktop apps;
- real host smoke is captured.

## Revalidation

Remote hosts, auth flows, and MCP protocol assumptions are high fragility. Add them to `revalidation-matrix.md` and recheck before release.

## Claim Limits

This baseline does not prove that any endpoint is deployed, reachable, secure, or host-accepted.
