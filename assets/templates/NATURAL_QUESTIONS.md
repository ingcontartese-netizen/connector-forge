# NATURAL_QUESTIONS

Natural user questions are high-level acceptance tests. They validate UI-to-data mapping, read-only behavior, bounded output, filtering, long text, encoding, and human-readable synthesis.

Project / Bridge:
Primary host:
Date:
Owner:

## Question Bank

| # | Type | Natural question | Expected tool/op | Expected result | Actual result | Evidence |
|---|---|---|---|---|---|---|
| 1 | read count | How many records have FIELD = VALUE? | read/list with filter | correct count, bounded output |  |  |
| 2 | filtered read | Show only records in CATEGORY. | read/list + filter | only expected rows |  |  |
| 3 | detail retrieval | Give me the details for OBJECT. | get/read one | one record with key fields |  |  |
| 4 | no-write dry-run | Simulate CHANGE without applying it. | simulate/dry-run | preview/diff, no write |  |  |
| 5 | first matching + human summary | Among records matching CONDITION, how many have FIELD? Give me the first one. | read/list + projection | count plus one readable item |  |  |

## Rules

- For UI terms such as tab/column/button/score, consult `UI_FIELD_MAP.md` before querying.
- Use bounded output: `page_size`, `fields`, summary, or artifact output.
- Natural questions must not trigger writes without propose/approve/audit.
- Rich text and non-ASCII content must pass the Windows UTF-8 guardrail when applicable.
- Record evidence in `ACCEPTANCE_EVIDENCE.md`.
