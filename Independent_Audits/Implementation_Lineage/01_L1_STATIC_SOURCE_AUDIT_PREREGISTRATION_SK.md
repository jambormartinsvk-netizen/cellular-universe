# L1 — predregistrácia statického auditu zdrojového prenosu

**Stav pred behom:** `PRIPRAVENÉ`  
**Skript:** `scripts/237_script_lineage_L1_static_contract_audit.py`  
**Vnútorný limit:** 5 s. **Vonkajší limit:** 10 s. **Bez ODE a bez importu modelov.**

## Čo sa overuje

Skript iba číta presne určené zdrojové súbory a kontroluje kontrakt C1–C5:
energy-frame `U_d`, dynamické `U_c`, samostatné `U_b`, presný A1 background
versus `K_MPC` background a deklarovaný rozsah. Nevykoná žiadnu fyzikálnu
evolúciu ani nemení starý súbor.

## Predregistrované očakávanie

| Skupina | Očakávaný stav |
|---|---|
| skript 86 K4 test-field | obsahuje `U_c`, `U_d`, `lambda/E` a používa `k` iba pre poruchu; zostáva test-field bez plných constraintov |
| K7 197/209/213 | nemajú `U_c`, majú pevné `K_MPC=0.05` v backgrounde; historicky fyzikálne obmedzené |
| G8 221/shared structural | samostatné `U_b`, ale `M` bez CDM hybnosti; screen-only obmedzenie |
| P5 236/shared | obsahuje `U_c`, `U_b`, exact-A1 koeficienty; iba statický preflight |

## PASS / STOP

- **PASS-L1:** zdrojový audit potvrdí presne vyššie očakávané rozlíšenie a
  vytvorí nemenný JSON. To potvrdzuje auditnú mapu, nie fyzikálnu správnosť
  obmedzených skriptov.
- **STOP-L1:** chýba cieľový súbor, skript sa zmenil proti očakávanej mape,
  alebo timeout. Potom sa fyzikálny rozsah nesmie odhadovať.
- **Ďalej:** L2 porovná rovnice len tam, kde L1 neurčila vedomé obmedzenie;
  historické K7/G8 dostanú permanentný scope label, nie tiché prepočítanie.

## Poznámka k prvému technickému pokusu (2026-07-15)

Prvý L1 pokus nepremenil auditnú mapu na výsledok: hľadal podreťazec `uc` a
falošne ho našiel v slovách `success`/`structural` (PF-038). Nevykonal ODE
ani nevykonal fyzikálny výpočet. Vytvoril však immutable technický STOP JSON,
ktorý sa správne neprepisuje. Kontrola sa opravila na hranice Python
identifikátora a tá istá predregistrovaná mapa sa opakuje pod novým názvom
výstupu.
