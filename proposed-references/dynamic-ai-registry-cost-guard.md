# Dynamic AI Registry And Cost Guard

Use this reference whenever the connector calls an AI model, exposes model settings, or routes a
governed operation through an AI provider. Models and their costs change under you; never hardcode
them.

## Core Rule

Model ids are volatile; families and aliases are stable. The bridge discovers the active model and
settings dynamically from the app/config/runtime, never hardcodes a name, and before any expensive
AI call declares the provider, model, settings, cost tier, and a GO requirement when the call is
non-default or costly. Secrets never leave as anything but a boolean.

## Part A -- Dynamic Registry

Read the registry from the app/runtime on every call. The effective default follows the operator's
app selector; never fabricate a fallback -- a missing default is an explicit
`missing_default_model` state with a warning and a request for an explicit model, not an invented
id. New models are added in the app/registry, not in bridge-hardcoded lists. Stable aliases
(`ai_assistant_default`, `deep_research_default`) name *roles*, with `used_by_bridge_ops` explicit;
the volatile id resolves under them.

The registry hash is canonical (sort_keys, fixed separators) over default+models+providers+aliases
-- deterministic cross-lane. The criterion is **dynamic, not frozen**: not "same hash as
yesterday" but "deterministic hash on the current state." A hash that changes when the operator
moves the selector is the feature, not a bug -- the registry made a divergence visible. (Lived: the
UI "active model" chip and the API default_model can diverge -- a false friend; document it or
expose the UI-selected model, but the bridge reports the endpoint truthfully.)

## Part B -- Cost Guard Before Expensive AI

API models bill per call, and settings (reasoning Low/High, search context) change cost radically.
Rule: the connector always uses the operator-configured settings; an upward override only with an
explicit GO; a preflight before any heavy AI op declares model + settings + profile_hash + cost
tier. Three warning classes, escalating:

```
INFO_OPERATOR_DEFAULT  ->  REVIEW_BEFORE_AI_CALL  ->  CONFIRM_BEFORE_AI_CALL (operator_go_required)
```

Surprise is declared **both ways**: a setting saved-but-not-applicable to the current model
(reasoning ignored by an "Auto" model) is a cost surprise in reverse, and must be declared, not
silently dropped. Per-setting applicability status is explicit: `applied` /
`saved_but_not_applicable_to_current_model` / `inactive_other_provider` /
`provider_setting_not_supported_by_current_model`; the else-branch for future models *declares*
non-support instead of faking application.

## Part C -- Applicability Is Provider Knowledge That Ages

Declaring which settings apply to the current model encodes the app's provider-factory behavior --
an unavoidable coupling, as volatile as the models. Pattern: explicit status for every outcome;
the future-model else-branch declares non-support; claim wording anchored to the present ("the
CURRENT app provider..."); a drift sentinel in the tests for when the catalog evolves. The
applicability map and the provider factory move in lockstep -- a test fails if the app exposes an
uncovered model.

## Part D -- Secrets

Provider keys leave only as the boolean `configured` (derived from `{field}_set`);
`secret_value_returned` and `masked_suffix_returned` wired to false -- strip even the masked
suffixes the app already masks. Zero secrets in any manifest or receipt.

## Acceptance

- moving the UI selector changes the registry hash (dynamic determinism);
- missing default -> explicit `missing_default_model` + warning, no fabricated id;
- cost guard blocks/warns before AI; preflight declares model+settings+profile_hash+cost tier;
- per-setting applicability status correct, including saved-but-not-applicable;
- zero secrets in payloads/manifests; only `configured` booleans.

## Stop Rules

Stop when:

- a model id is hardcoded in the bridge, or a fallback id is fabricated for a missing default;
- a heavy AI call runs without a declared cost-guard preflight;
- a saved-but-inapplicable setting is silently dropped (declare the surprise both ways);
- any secret value or masked suffix appears in a payload, manifest, or receipt;
- the applicability map has no drift sentinel against catalog evolution.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Bridge V2 (dynamic registry M-28, selector/default
  governance M-28b, cost/profile guard M-28c, the UI-active-vs-API-default false friend FF-7,
  secrets-as-booleans all originate here). The model-volatility and cost-guard patterns generalize
  to any connector that calls an AI provider on the operator's behalf.
- Field lessons distilled: lived model churn (Fable 5 in chat, Opus/Sonnet/GPT in app, legacy
  migration map already needed); the UI selector not writing the API default; a creator's own
  functional test catching a missing-return dead block before the claim.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
