# L1 — výsledok statického auditu prenosu formulácie

**Dátum:** 2026-07-15  
**Autoritatívny rerun:** `scripts/results/k_mpc_005/RUN_LINEAGE_L1_STATIC_CONTRACT_AUDIT_RERUN1.json`  
**Skript:** `scripts/237_script_lineage_L1_static_contract_audit.py`  
**Čas:** `<1 s`; interný limit 5 s, vonkajší 10 s; bez importu modelov a ODE.

## Rozsudok

**PASS-L1: mapa najrizikovejšej línie sa presne zhodla s predregistráciou.**
To je auditný PASS, nie fyzikálne PASS historických redukovaných skriptov.

| Skupina | Stav po L1 | Dôsledok |
|---|---|---|
| K4 test-field 86 | obsahuje `U_c`, `U_d`, `lambda/E`; `k` ostáva perturbatívny | živý iba ako test-field; nemá plné metric constrainty |
| K7 197/209/213 | nemá identifikátor `U_c`; má pevné `K_MPC=0.05` a background z neho | historické numerické artefakty, fyzikálne obmedzené |
| G8 SCREEN 221/shared | má `U_b`, ale jeho `full_momentum` neobsahuje `Omega_c U_c` | screen-only; nesmie slúžiť ako FULL K4 adapter |
| P5.1 236/shared | má `U_c`, `U_b`, `M_full`, `gamma`, `beta_c`; bez pevného K backgroundu | aktuálny statický preflight, ešte bez constraintov/ODE |

## História prvého technického pokusu

Prvý immutable JSON zachytáva PF-038: voľný textový substring `uc` sa
falošne zamieňal za Python identifikátor. Opravený rerun používa hranice
identifikátora; starý JSON sa neprepisuje a nemá fyzikálnu váhu.

## Rozsah a ďalší krok

L1 zatiaľ kontrolovala najrizikovejšiu cestu A1 → K4 → K7/G8 → P5, nie celý
adresár `scripts`. Nasleduje L0b: inventár všetkých závislých skriptov a
ich zaradenie do skupín. Až potom L2 porovná rovnice a rozhodne, ktoré
historické výpočty je nutné opakovať a ktoré len správne obmedziť.
