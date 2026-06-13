# Acceptance Tests

Un connettore è pronto solo se supera questi test nel client reale.

| Gate | Prova minima | Evidenza richiesta | Esito |
|---|---|---|---|
| Installazione | package/install senza hack manuali | screenshot/log |  |
| Health | `doctor` o `health` | output JSON/testo |  |
| Handshake | initialize/tools/list o help CLI | transcript |  |
| Fresh process | processo riavviato dopo modifica sorgente | build/version stamp + restart log |  |
| Host loaded | client primario vede server e catalogo corrente | host tools/list snapshot |  |
| Lifecycle log | bridge locale/deployed produce JSONL best-effort | process_start + tool_completed + error/recovery sample |  |
| Discovery | stato reale app/progetto/documento | structured output |  |
| Read | un read tool stabile | output verificato |  |
| Bounded output | read/search/simulate/report con output variabile usa default `page_size=25` o limite equivalente; probe `page_size=3` | result_count + cursor/summary/artifact evidence |  |
| Export | file/preview verificabile | path + checksum/screenshot |  |
| Dry-run | piano mutazione senza side effect | output plan |  |
| Write controllata | una write minima con approval | request_id + audit |  |
| Error path | validation/auth/lock error correggibile | transcript |  |
| Recovery | app chiusa, bridge restart, catalog refresh | runbook provato |  |
| Host smoke | test in Codex/Cowork/Antigravity/etc. | transcript o video |  |
| Windows UTF-8 | payload con accenti/simboli non rompe console/log | env UTF-8 o artifact UTF-8 |  |

## Stop

Se fallisce lifecycle log, bounded output, export, dry-run, error path o host smoke, non dichiarare il connettore pronto.
