# Host Access Asymmetry

Use this reference in multi-agent or multi-host connector work where agents do not see or control the same environment.

## Rule

Declare which host or agent can read, inspect, actuate, and verify each capability. Do not treat one agent's sandbox limitation as proof that the application has no usable surface.

## Read Asymmetry

One host may see live processes, windows, registry keys, local ports, WAL files, and installed SDKs. Another may only see mounted files or immutable snapshots. Assign probes to the host with the real access, then use the other host as an independent reader, policy reviewer, or claim auditor.

Cross-read parity is strong evidence only when both reads are independent and the access limits are declared.

## Actuator Asymmetry

For writes, also declare who has the hand:

- `reading_agent_or_host`;
- `actuating_agent_or_host`;
- `actuator_backend`;
- `verifying_agent_or_host`;
- `blocker_if_unavailable`.

The agent with the actuator may differ from the agent doing readback. This is acceptable and often stronger when the contract, token, and readback chain are explicit.

## Blocker Classes

- `method_blocked`: the bridge does not know what the operation should mean.
- `actuator_blocked`: the method is known but no backend reaches the target field on this host.
- `host_blocked`: the environment does not offer the actuator at all.

Route the fix according to the blocker. Do not weaken governance just because the first actuator failed.

## Human As Last-Resort Actuator

If no agent can act natively, the workflow may escalate to a human as the actuator of last resort, under the same contract, approval, readback, and rollback rules.

Claim the result honestly:

- `agent-actuated`: the agent performed the operation.
- `agent-governed, human-actuated`: the agent prepared/governed the operation, but the human performed it.

## Stop Rules

Stop if:

- the executor and verifier are not declared;
- a host limitation is presented as a universal app limitation;
- a human action is claimed as agent-actuated;
- a high-risk actuator lacks independent readback.
