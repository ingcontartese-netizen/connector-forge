# Operator Visual Acceptance And Operative UX

Use this reference when the connector touches a UI the operator reads, or when a result's truth
sits between the API and the screen. A connector can be technically correct and still unusable.

## Core Rule

For an app the operator drives, the operator's visual verdict on the screen is part of the proof,
and the operative UX is a requirement, not decoration. Design operator-assisted before adding a
column, popup, filter, or layout; never blank the context the operator is working in; never show a
raw internal enum where a human reads.

## Part A -- Operator-Assisted Probe (truth between UI and API)

When the truth sits across UI and API, the joint experiment beats both a static code-read and a
solitary probe: the operator acts on the UI (moves a selector, clicks an ack), the agent probes
the bridge read-only, the two are compared. Thirty seconds, zero writes, and it *proves* a UI/API
divergence no inspection would show with the same force (it is how the active-model false friend
was caught). Operator visual acceptance is taken **after** refresh -- a governed write can succeed
in the engine while the UI is stale; the connector emits a post-write invalidation, the verifier
trusts the readback, the operator confirms the pixel.

## Part B -- Dense UI: Don't Add What You Don't Need

A grid the operator lives in is dense. Before adding columns or fields, ask if they belong as
attributes / filters / popups / API instead. Operative metadata stays behind the operator's
control, not as fixed columns that clutter the grid and the export. The export is not dirtied by
purely-technical columns. Contextual label discipline: a label that depends on state (in-portfolio
"Sell" vs out "Don't buy") is computed, not hardcoded.

## Part C -- Never A Raw Enum In The Operator's Face

An internal reason code is not UI. "Alert: LEGACY_BASELINE_MISSING", "Alert: CURRENT" -- codes
spilled into a popup are a defect: translate to operator language, and show an alert chip only for
states that are actually alerts (yellow/red), never on a healthy green. A never-baselined legacy
state is a distinct visual state (or no chip), not a false green that reads "verified fresh." When
the operator says "I don't want to see it, the semaphore is enough," remove the chip -- the data
stays in the tooltip and the bridge; the screen obeys.

## Part D -- Visual Behavior And Perceived Performance Are Features

No blank screens, no heavy "loading" when data is already visible:

- a refresh must not empty the page if valid data exists (preserve the table, show a
  non-destructive "updating...", first load alone is full-loading because there is nothing to
  preserve); guard in-flight with a throttle;
- a zero-result keeps headers and spacer mounted (the "no rows found" lives inside the table body),
  so the grid never disappears;
- text fits, no overflow; the perceived latency is managed by the *shape* of the answer (data
  first, prose after) -- a 90-second probe felt slow only because the answer led with prose.

## Acceptance

- operator-assisted probe used where truth is UI/API split; visual acceptance after refresh;
- no redundant columns; export clean of technical-only fields; contextual labels computed;
- no raw enum shown to the operator; alert chip only on alert states; legacy state distinct from
  green;
- refresh preserves context; zero-result keeps headers; no blank loading when data exists.

## Stop Rules

Stop when:

- a UI claim is asserted from memory instead of a screenshot/operator look;
- a column/popup/filter is added without asking if it belongs as attribute/filter/API;
- a raw reason code is shown to the operator, or an "alert" chip appears on a healthy state;
- a refresh blanks the page while valid data exists, or a zero-result hides the grid headers.

## Evidence Provenance

- Source bench: ValuAziende OneMaster Bridge V2 Fase 5 (semaphore column, smart filters,
  operator-assisted 4-hands probe, the raw-enum-in-popup defect, refresh-preserves-context, dense-UI
  discipline all originate here). The operator-visual-acceptance pattern generalizes to any
  connector assisting a human-facing app (Archicad model views, P6 schedule grids).
- Field lessons distilled: the active-model UI/API divergence proven by a 4-hands probe; "Alert:
  CURRENT" shown on a healthy green note (removed on operator order); a refresh that blanked the
  table mid-work; a contextual "Don't buy" label correct for an out-of-portfolio company.
- Claim limit: method/spec guidance only; not a deployed, package, or production claim. Benches
  are sanitized case studies.
