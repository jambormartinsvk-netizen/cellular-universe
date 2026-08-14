# KMPC-060 — C2 guard false-check diagnostic: predregistrácia

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Rozsah:** iba read-only diagnostika PF-079; žiadny fyzikálny atóm

Skript pred importom overí presné hashe C2 V1/V2/V3, potom jedenkrát zavolá
V3 `contract_guard()` a na stdout vypíše:

- všetky false check názvy a ich hodnoty;
- stale support diff;
- closed, historical a runtime support mapy;
- celkový pass.

Nevykoná M1/F0/M3 solve, nevytvorí JSON, nemení register ani verdikt. Exit 0
znamená iba úspešnú diagnostiku a vyžaduje, aby bol nájdený aspoň jeden false
check; nulový false zoznam je fail-closed chyba diagnostiky.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | rozsah a očakávaný read-only výstup zmrazené | `PREREGISTERED` |
| 2026-07-18 | diagnostic runner SHA `77B487832955893987F797F52CEBE5BA78D065268723D9A95659EA6EC59AC342` | `FROZEN_BEFORE_PYTHON` |
| 2026-07-18 | compile PASS; diagnostic exit `0`; jediný false check `PF077_stale_map_differs_exactly_CDI_BI`; exact historický-vs-closed diff je `(AD,CDI,BI)` | `READ_ONLY_DIAGNOSTIC_COMPLETE_NO_PHYSICS_VERDICT` |

Autoritatívna technická interpretácia: pôvodný V1 guard hlásil iba CDI/BI,
pretože AD osobitne porovnával s native `[0,2]`. V2/V3 stale-map diagnostika
však porovnáva closed support s historickou S1 extended mapou, kde AD
`[0,2] != [0,4]`. Obe množiny sú správne pre svoju otázku a nesmú sa
zamieňať.
