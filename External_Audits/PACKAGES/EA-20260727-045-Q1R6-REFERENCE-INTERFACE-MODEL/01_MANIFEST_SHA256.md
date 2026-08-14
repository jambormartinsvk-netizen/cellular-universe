# SHA-256 manifest EA-045

Strojovým zdrojom pravdy je `01_MANIFEST_SHA256.tsv`. Balík obsahuje `13`
jedinečných single-copy evidence položiek, `7` control súborov a explicitne
hash-bound scope control položku `00_SCOPE_AND_READ_ORDER.md`.

| Rozsah | Súbory | Úloha |
|---|---:|---|
| Q1R6 immutable evidence | 4 | preregistrácia, jediný source archive, receipt a result |
| route/provenance context | 4 | current/K4/P5 plans a append-only ledger |
| isolated auditor bootstrap | 5 | rules, protocol, profile a manifest binding |

Primárny SHA-256 archívu `2204.13120`:
`5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416`.

`REPRO=0`; runtime mapa je header-only. Balík nemá executable vetvu,
generated JSON ani Python proces.

Control hash pre mandatory protocol classification and sealed lifecycle:
`C9D7D19B487C6794CE1B560E1BB217EFF11D477B18EB034DF2BD79357865C3CD`.
