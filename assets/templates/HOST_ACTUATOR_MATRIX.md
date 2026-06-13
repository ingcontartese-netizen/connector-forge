# Host Actuator Matrix Template

Status: active-v3-candidate / second-read-source-verified
Purpose: compare host actuator surfaces before choosing a branch.

| Surface | Available | Authority | Supports read | Supports dry-run | Supports write | Supports target data source | Risk | Evidence | Decision |
|---|---|---|---|---|---|---|---|---|---|
| Official API/SDK | unknown | official | unknown | unknown | unknown | unknown | unknown | | |
| CLI/batch | unknown | official/vendor | unknown | unknown | unknown | unknown | unknown | | |
| File import/export | unknown | engine-mediated | unknown | unknown | unknown | unknown | unknown | | |
| Browser UI | unknown | ui-mediated | unknown | unknown | unknown | unknown | high | | |
| Desktop UI/computer-use | unknown | ui-mediated | unknown | unknown | unknown | unknown | high | | |
| Human-assisted | unknown | human-mediated | unknown | n/a | user-performed | unknown | variable | | |
| Direct datastore | unknown | forbidden unless vendor-authorized | read-only maybe | n/a | forbidden | unknown | critical | | |

Decision must explain why higher-authority surfaces were unavailable or insufficient before promoting a lower-authority actuator.

