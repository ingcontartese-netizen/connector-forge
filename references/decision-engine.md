# Decision Engine

Use this after Gate 0, Source Registry, Surface Map, and Capability Ledger.

## Inputs

- Host primary: Codex, Claude Code, Cowork, ChatGPT Apps, Antigravity, Gemini, custom app.
- Target app: name, version, environment, owner, allowed surfaces.
- Surfaces found: API/OpenAPI, GraphQL, CLI, SDK, plugin/add-on, file import/export, database, MCP, browser/UI, none.
- Auth: user, service account, OAuth, API key, local session, secrets handling.
- Operations: 3-5 MVP capabilities with read/write risk.
- Acceptance: concrete proof of success and rollback.

## Choose CLI

Choose CLI when:

- the work is local, repo-based, batchable, or terminal-friendly;
- FastAPI/OpenAPI/GraphQL can be wrapped into a stable control plane;
- a desktop app needs a local bridge before remote exposure;
- deterministic smoke tests matter more than cross-host discovery;
- the user needs scripts, `COMMANDS.md`, or a local operational adapter.

## Choose MCP

Choose MCP when:

- multiple AI hosts must discover and call tools;
- the primary host is ChatGPT Apps, Claude/Cowork remote connector, Antigravity, Gemini, or another MCP client;
- tool catalog, schema discovery, auth, audit, and host packaging are first-class;
- the app already has an MCP server or broker surface.

## Choose Hybrid

Choose Hybrid when:

- a local app must be reached from a remote host;
- CLI is the safest local control plane, but MCP is needed for discovery;
- desktop/plugin/API surfaces need a site bridge plus remote broker;
- local credentials must stay local while a broker exposes constrained tools.

## Choose STOP

Choose STOP when:

- no authorized surface exists;
- the only path is fragile UI automation for a non-stable workflow;
- auth or environment is missing;
- a write path lacks dry-run, approval, rollback, and audit;
- the user asks for bypassing controls, licenses, or security boundaries.
