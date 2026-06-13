# Source Registry

Tracciare solo fonti utili alla build. Preferire fonti ufficiali, repository ufficiali, SDK, reference API, changelog e documentazione del vendor.

| Area | Fonte | URL | Tipo | Data accesso | Claim supportato | Affidabilità | Note |
|---|---|---|---|---|---|---|---|
| App target |  |  | Ufficiale / Repo / Community / Blog |  |  | Alta / Media / Bassa |  |
| Host AI |  |  |  |  |  |  |  |
| MCP / CLI |  |  |  |  |  |  |  |
| Sicurezza |  |  |  |  |  |  |  |

## Depth Checklist for Desktop / Standalone Apps

| Surface family | Status (`found|absent|not_installed|forbidden|needs_revalidation`) | Evidence/path/link | Notes |
|---|---|---|---|
| Vendor SDK / API reference |  |  |  |
| Integration / Professional / local-mode API |  |  |  |
| Installed JAR/DLL/shared libraries |  |  |  |
| Demo apps / examples / sample DB |  |  |  |
| CLI tooling / command switches |  |  |  |
| Plugin/add-on API |  |  |  |
| Import/export workflow (XML/XER/Excel/CSV/report) |  |  |  |
| Local config / connection profiles |  |  |  |
| Authorized DB/report read surface |  |  |  |

## Classificazione

- **Verificato**: documentazione ufficiale o test su ambiente reale.
- **Probabile**: deduzione tecnica ragionevole ma non testata.
- **Ipotesi**: da verificare prima di esporre nel catalogo tool.
- **Vietato**: non autorizzato, non conforme o non sicuro.
