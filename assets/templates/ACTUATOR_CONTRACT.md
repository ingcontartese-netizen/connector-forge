# Actuator Contract Template

Status: active-v3-candidate / second-read-source-verified
Purpose: reusable template for high-risk or non-API actuators.

```yaml
actuator_contract_id:
target_app:
target_version:
target_host:
target_data_source:
operation_name:
operation_risk: read | safe | write-safe | write | write-destructive
actuator_type: api | cli | file_workflow | browser | desktop_ui | computer_use | human_assisted
actuator_authority: official | vendor_supported | engine_mediated | ui_mediated | unsupported | forbidden
trust_boundary:
  instruction_sources:
  untrusted_data_surfaces:
  approval_source:
target_identity:
  domain_object:
  stable_keys:
  current_selection_required:
selector_or_payload_evidence:
  inspect_artifact:
  selector_strategy:
  ambiguity_check:
expected_before:
expected_after:
stop_rules:
host_state_required:
approval:
  token_required:
  token_hash_or_reference:
rollback_readiness:
  backup_or_inverse:
  restore_test_result:
readback:
  tier:
  target_scope:
  collateral_scope:
  protected_invariants:
recompute:
  recompute_required:
  recompute_action:
claims_allowed:
claims_forbidden:
```

No apply may use this template as evidence unless the fields are filled for the actual host and operation.

