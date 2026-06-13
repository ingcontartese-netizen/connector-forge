# UI_FIELD_MAP

Use this template before answering user questions that refer to a visible UI tab, column, button, panel, or section.

Without a verified map, a numerical answer can be wrong because UI labels can differ from backend field names.

Project:
App / UI:
Date:
Owner:

## Field Map

| UI area / tab | Visible label | UI component / file | Real data field | Backend endpoint | Tool / op | Default sort/filter | Evidence |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

## Rules

- Label is not field: verify the component or ask the user before treating the mapping as verified.
- Record units, currencies, normalization, derived totals, and sorting behavior.
- `verified` requires evidence from UI code, backend schema, live probe, or explicit user confirmation.
- Use this with `NATURAL_QUESTIONS.md` for user-facing acceptance tests.
