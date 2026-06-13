# COMMANDS — comandi verificati

Compila solo comandi provati su ambiente reale.

| Comando | Stato | Payload minimo | Output atteso | Errori tipici | Note refresh/restart |
|---|---|---|---|---|---|
|  | Verified / Draft / Broken |  |  |  |  |

## Discovery / error mining

| Probe | Esito | Comando/op reale scoperta | Stato | Note |
|---|---|---|---|---|
| unsupported op / help / schema / docs |  |  | verified / hypothesis / forbidden |  |

## Command Availability Matrix

| Capability | Command/tool | Documented | Static schema | Installed local | Live available | Host exposed | Dry-run proven | Apply proven | Evidence | Notes |
|---|---|---|---|---|---|---|---|---|---|
|  |  | yes/no/n/a | yes/no/n/a |  | yes/no/n/a | yes/no/n/a | yes/no/n/a | yes/no/n/a |  |  |

States:

- `documented`: source says it exists.
- `in_static_schema`: static schema, changelog, manifest, or generated catalog lists it.
- `installed_local`: dependency/add-on/plugin/binary is present locally.
- `live_available`: running app/add-on/SDK reports it available.
- `host_exposed`: bridge/MCP/CLI host exposes it with schema.
- `dry_run_proven`: no-side-effect/schema-only call works.
- `apply_proven`: minimal apply in sandbox works and readback passes.
- `blocked`: missing, stale, unauthorized, wrong version, or unsafe.

## Output grandi

- Default read/search/simulate/report: `page_size=25` o `limit` equivalente, `cursor` quando disponibile, `--fields`/summary artifact per payload grandi.
- Acceptance probe: eseguire almeno una chiamata con `page_size=3` o limite piccolo equivalente.
- Non riversare payload grandi in chat o log: estrai, sintetizza o usa `--fields`.
- Registra limite testato e comportamento `has_more` / `next_cursor`.

## Regole

- Non inserire comandi non verificati.
- Registra alias tra versioni.
- Registra shape reale di argomenti e risposta.
- Registra workaround e bug SDK.
- Se il comando produce write governata, registrare proposal/approval/audit e non direct write.
- Su Windows, impostare `PYTHONIOENCODING=utf-8`/`PYTHONUTF8=1` o scrivere output ricco su file UTF-8; non far dipendere commenti lunghi dalla console cp1252.
- Per bridge locali, registrare `health/version` con `build_stamp` e lifecycle log path prima di dichiarare il processo fresco.
