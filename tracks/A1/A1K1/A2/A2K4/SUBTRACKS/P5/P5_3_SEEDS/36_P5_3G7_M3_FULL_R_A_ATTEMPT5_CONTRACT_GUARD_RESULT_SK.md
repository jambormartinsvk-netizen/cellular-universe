# P5.3g7-M3-FULL/R-A — pokus 5/10, contract-guard výsledok

**Dátum:** 2026-07-16  
**Runner:** `265_script_KMPC_026_P5_3g7_m3_full_ra_b1_contract_guard_rerun1.py`  
**Výsledok:** `RUN_KMPC_026_P5_3G7_M3_FULL_RA_B1_CONTRACT_GUARD.json`  
**SHA-256:** `69E78B433540055712F9C0DD2A35E8AC8F1A81BBBF9BE8FF21318E93917EDE68`  
**Autoritatívny verdict:** `PASS_R_A_B1_CONTRACT_GUARD_ONLY`  
**Counter:** `5/10`  
**Fyzikálne pokusy:** `0`  
**Hĺbka:** bez zmeny, K4 `60/100 = G6`

## Výsledok

| Brána | Výsledok |
|---|---|
| tri `py_compile` | PASS |
| CLI | PASS |
| smoke | `9/9`, deväť negatívnych fixtures odmietnutých, `0.156 s` |
| full | `9/9`, deväť negatívnych fixtures odmietnutých, `0.157 s` |
| frozen algebra hash | presná zhoda |
| produkčný exact ordered contract | PASS |
| všetky presné algebraické rezíduá | reťazec `0` |
| solve/ODE | nevykonané |

Nový autoritatívny contract má hash
`F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464`.
V2 preflight a runner majú hashe
`27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C` a
`5CC93695C41024410D227B6D56938F077D8EBB34F118A0AE312851955EA1DFB4`.

## Čo je tým uzavreté

- PF-064 je opravená bez prepisu pokusu 4;
- presný state/driver/holdout tuple je oddelený od implementácie;
- rovnaký validator odmieta missing, extra, fake, reordered a overlap
  fixtures;
- tlak PF-063, total conservation, Bianchi, `k`-cancel a S-C split zostali
  presnými algebraickými nulami;
- B1 je uzavretá na úrovni `PASS_CONTRACT_PREFLIGHT_ONLY`.

## Čo tým uzavreté nie je

- nebola riešená coefficient matica ani K4 seed;
- `00` a `0i` neboli numericky vyhodnotené ako holdouty;
- nebežali dva štarty, ODE, finite opacity ani plná hierarchia;
- S-C je iba podmienené matematické rozdelenie pary;
- skóre a fyzikálna hĺbka sa nemenia.

## Ďalší povolený krok

Pokus 6/10 môže byť jeden úplný M3-TCA0 seedový solve na zmrazenom
contracte. Pred kódom musí dostať samostatnú Markdown predregistráciu s
presnými unknown/row počtami pre každý mód, expected rankom, nezávislými
`00/0i` holdoutmi, tromi `k`, `z<<1` plochami, hash guardom a výsledkovými
vetvami PASS/REVIEW/STOP. Pokus 6 nesmie meniť tlak, contract ani B1 prahy.
