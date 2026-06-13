# Gate 0 — Dossier di progetto

Compilare prima di scrivere codice o delegare a un agente.

## A. Identità

| Campo | Valore |
|---|---|
| Nome progetto |  |
| Owner |  |
| Obiettivo operativo |  |
| Data |  |
| Stato | Draft / Review / Ready / Hold / Blocked |

## B. Decisioni bloccanti

| Campo | Valore |
|---|---|
| App target |  |
| Versione / licenza |  |
| OS target |  |
| Host primario | Codex / Claude Code / Cowork / Antigravity / Gemini CLI / ChatGPT Apps / Altro |
| Modalità | Locale / Remota / Ibrida |
| Ambiente reale disponibile | Sì / No |
| Documentazione ufficiale disponibile | Sì / No |
| Superficie ufficiale/autorizzata | API / SDK / Plugin / Add-on / CLI / File workflow / Bridge / Altro |
| Gate 0.0 Domain Model richiesto | Si / No / N/A motivato |
| Domain Model path |  |
| Falsi amici noti |  |

## C. Sicurezza e operazioni

| Campo | Valore |
|---|---|
| Auth |  |
| Dove stanno i segreti | env / keychain / vault / OAuth / ADC / altro |
| Dati sensibili |  |
| Write possibili | Nessuna / Safe / Distruttive |
| Approvazione richiesta |  |
| Audit richiesto |  |
| Rollback possibile |  |

## D. MVP tool list — massimo 5 tool

| Tool | Tipo | Rischio | Output atteso | Evidenza di test |
|---|---|---|---|---|
| health / doctor | Read | Low | Stato sistema |  |
| get_context | Read | Low | Stato app/documento |  |
| search/list/get | Read | Low | Dati strutturati |  |
| export/preview | Safe | Medium | File verificabile |  |
| dry_run/prepare/commit | Write | High | Mutazione controllata |  |

## Regola di arresto

Se manca un dato tra app target, host primario, superficie autorizzata, auth, ambiente reale, MVP tool list o acceptance criteria, il progetto resta in HOLD.
