# Source Registry

Every connector project needs a dated registry of sources.

## Fields

- source ID;
- URL or local path;
- vendor/owner;
- area covered;
- access date;
- stability;
- revalidation trigger;
- notes.

## Priority

1. Official vendor docs/specs.
2. Official SDKs/repos.
3. Local installed app files and help output.
4. Live read-only probes.
5. Community posts only as weak hints.

## Rules

- Mark future-dated or unverified claims as `quarantine`.
- Mark marketing claims as `hypothesis` until tested.
- Revalidate fast-moving areas before release: MCP spec, auth, host config, remote connector behavior, Apps SDK, Cowork/Antigravity/Gemini packaging.
## OneMaster Draft Addendum

When source material arrives in layers, keep the chronology. Mark each source as `author_intent`,
`current_guide`, `code_truth`, `bridge_truth`, `user_rule`, or `superseded_but_preserved`. Do not
delete old sources only because code superseded them; they may explain why the connector must ask a
better question.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-01, OMD-M-02,
OMD-M-32; tags APP / BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB; claim limit: method/spec evidence
only.
