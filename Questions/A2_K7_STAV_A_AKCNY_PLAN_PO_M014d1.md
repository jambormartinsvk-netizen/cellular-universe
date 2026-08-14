# A2-K7 — historický stav po M-014d1 s povinným erratom

**Dátum pôvodného stavu:** 2026-07-13  
**Dátum errata:** 2026-07-13  
**Status:** historický smerovník; nie aktuálny akčný plán

Pôvodný dokument je zachovaný ako
`Questions/A2_K7_STAV_A_AKCNY_PLAN_PO_M014d1_PRE_ERRATUM.md`.

## Čo bolo príliš široké

Pôvodný plán predpokladal, že ak neexistuje konzistentný neuniverzálny
spin-2 operátor, zomrie celá K1b pod kódom `M-014d2`. Neskorší audit ukázal,
že použitý soft argument rozhoduje iba vedúcu väzbu `h_mn T^mn`.

## Kanonická oprava

| Podkoľaj | Opravený stav | Max. hĺbka | Dôvod |
|---|---|---:|---|
| K1b1 — vedúca soft spin-2 väzba | `MŔTVA M-014d2a` | `41/100` | vyžaduje `G_eff~1e48 G_N` alebo poruší soft univerzálnosť |
| K1b2 — higher-derivative curvature operátory | `AKTÍVNA` | `5/100` | soft theorem ich sám nevylučuje; čaká operator/cutoff test |
| K1b3 — ďalšie massless spin-2 pole | `ČAKÁ` | `5/100` | samostatná multigraviton brána |

Celá K1b preto nie je mŕtva. Aktuálny plán je
`Questions/A2_K7_STAV_A_AKCNY_PLAN_PO_M014d2a.md` a kanonický smerovník je
`Questions/00_READ_FIRST_A2_Q20_CURRENT_STATE.md`.

Toto erratum nemení rozsudok M-014d1 o gravity-only pare. Obmedzuje iba
neskoršiu, príliš širokú formuláciu plánovaného K1b killu.

