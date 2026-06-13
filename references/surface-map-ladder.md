# Surface Map And Ladder

Map every authorized surface before choosing CLI, MCP, Hybrid, or STOP.

## Ladder

Choose the highest surface that is available, authorized, and testable:

1. Official REST/OpenAPI/GraphQL API.
2. Official SDK.
3. Official CLI.
4. Official plugin/add-on.
5. File workflow or import/export.
6. Read-only database/report surface.
7. Authorized local bridge.
8. Browser/computer-use automation as fallback only.
9. STOP when the surface is unauthorized, unstable, or incompatible with terms/security.

## Mapping Questions

- Which surface is primary?
- Which surfaces are secondary or diagnostic only?
- Which surfaces are forbidden?
- Does the host need local reachability, remote reachability, or both?
- Is a local bridge required before an MCP broker?
- What evidence proves this surface exists in the user's environment?

## Rule

Do not move down the ladder for convenience. Use browser/computer-use automation only when no higher authorized surface can satisfy the task safely.
