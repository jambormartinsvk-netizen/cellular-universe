# KMPC-081–083 — BI/k=.15 high-precision boundary: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Interný audítor a tvorca skriptov:** Codex (OpenAI)  
**Stav:** `REVIEW_C2_BI_K0p15_EXACT_ASSEMBLY_REQUIRED`

KMPC-081/PF-086 a KMPC-082/PF-087 skončili pred maticou a bez fyziky.
KMPC-083 dokončil jediný 80-dps solve za `6.266 s`. Raw SHA:
`A8CB50F9593E95013CF96974FA48205152F7D462D30470A83366697D3FD729C9`.

| Metrika | Výsledok |
|---|---|
| driver matica/konštanta SHA | `FE5E5A7C...127240F` |
| 80-dps driver maximum | `9.8186281567e-82 < 1e-10`, PASS |
| holdout matica/konštanta SHA | `1C1896AA...494D2` |
| riadky holdoutu pridané do solve | `0` |
| 80-dps `Einstein_0i[7]` | `3.019756782389909e-9 > 1e-9`, FAIL |
| holdout absolútne rezíduum | `8.728840268468619e-17` |

Výsledok dokazuje, že problém nie je solve-roundoff: zvýšenie presnosti
znížilo driver na ~`1e-81`, no holdout zostal prakticky identický s float64.
Stále to nie je fyzikálny STOP, lebo driver aj holdout matice boli najprv
zostavené vo float64. Ďalší oprávnený krok je exact/high-precision assembly
audit rovnakých rovníc; holdout naďalej nesmie vstúpiť do fitu.

PF-088 sa týka iba agregačného poľa `all_other_frozen_gates_pass`; nemení
priamo vypočítaný holdout FAIL ani výsledný REVIEW. C2 ostáva `5/10`, K4
`60/100`.
