# Security Mesh

| Rischio | Esempio | Mitigazione CLI | Mitigazione MCP/host | Test |
|---|---|---|---|---|
| Shell injection | input utente concatenato a shell | usa argv, no shell implicita, allowlist | tool schema stretto, approval | payload con `; rm -rf` |
| Path traversal | `../../secret` | canonicalizzazione, root jail | scope filesystem | fixture path malevolo |
| Prompt injection | documento remoto con istruzioni ostili | separa dati/istruzioni | tratta tool output come non fidato | doc contaminato |
| Token leakage | segreti in log | redaction, keychain/vault | no token passthrough | log scan |
| Write distruttiva | delete/deploy/payment | dry-run, prepare/commit, confirm | approval server-side | write test bloccata |
| Over-privilege | scope troppo ampi | profili separati | least privilege | verifica scope |
| Drift | API cambia shape | contract test, drift report | list_changed/refresh | replay smoke |

## Regola

La sicurezza non si delega al prompt. Va implementata in adapter, CLI, server MCP, host pack e processo operativo.
