# Case Studies Index

Use case studies as sanitized field evidence. They are not app manuals and do not create host-specific core rules.

## Current Evidence

| Case | File | Evidence Class | Promoted Lessons | Claim Limits |
|---|---|---|---|---|
| Archicad hybrid bridge | `assets/case-studies/ARCHICAD_HYBRID_REAL.md` | read/write hybrid local bridge | intent proof, native/proxy distinction, rollback scope, visual placement readback | not an Archicad production connector |
| ValuAziende MCP deployment | `assets/case-studies/VALUAZIENDE_MCP_DEPLOY.md` | MCP/FastAPI app evidence | bounded output, lifecycle, frontend/backend distinction, governed proposal flow | public-ready still needs the new API-native bench |
| ValuAziende OneMaster Draft | `assets/case-studies/VALUAZIENDE_ONEMASTER_DRAFT.md` | layered app/bridge/guide learning bench | engine-respecting read path, generational evolution, bridge doctor target-pattern, collaborative handoff, old/new parity | Draft evidence only; no Bridge V2, package parity, Ready, Deployed, or public-ready claim |
| P6 cold start domain | `assets/case-studies/P6_COLD_START_DOMAIN.md` | domain comprehension evidence | Gate 0.0, domain-semantic validation, false friends, live-vs-persisted | Fascia A only |
| P6 write path Fascia B | `assets/case-studies/P6_CASE_STUDY_COLD_START.md` | governed write-path evidence | engine-respecting write, actuator ladder, risk-proportional readback, unit/operating knowledge gates | sandbox single-operation evidence only |

## Promotion Rule

A lesson can move from case study to core only after it is generalized:

- remove app-specific names from the rule;
- keep the app details in the case study;
- state the evidence and the limit;
- add a stop rule if failure would be unsafe.

## Stop Rules

Stop promotion if:

- the rule only works for one app;
- private/customer data would ship;
- the case study is used as a substitute for Gate 0 on a new app;
- the release claim says production/public when the evidence is only field-tested.
