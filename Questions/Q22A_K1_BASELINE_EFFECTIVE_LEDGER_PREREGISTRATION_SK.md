# Q22a-K1 — preregistrácia auditu efektívneho A1 ledgeru

**Stav pred behom:** `PRIPRAVENÉ; bez fyzikálneho skóre`  
**Koľaj:** Q22a-K1 (`F -> C`, bez priameho produktu `R`)  
**Zdroj formulácie:** `scripts/11_script_A1_K1_cdm_background_audit.py`,
funkcia `rhs`; nezávisle zrkadlené v
`scripts/baseScripts/k_mpc_005/af_from_a1_background.py`, funkcia `rhs`.

## Čo sa počíta ľudskou rečou

Overuje sa najskromnejšie tvrdenie, ktoré už obsahuje zmrazený background A1:
energia prenesená z paliva `F` nezmizne. V efektívnom ledgeri vznikne v
rovnakom kroku iba hmotný relikt `C` (popol); do radiácie/pary `R` nejde
žiadny priamy zdroj.

Toto **nie je** dôkaz, že pri mikroskopickom delení naozaj vzniká najprv alebo
iba popol. Je to len presný baseline, s ktorým budú neskôr porovnané paralelné
a sekvenčné mikrokoľaje.

## Zmrazené rovnice a očakávanie

Pre `x=ln a`, `E>0` a `Gamma=lambda/E` je z A1 čítaný prenos

```text
Q_F = -Gamma rho_F
Q_C = +Gamma rho_F
Q_R = 0.
```

Celé continuity rovnice zahŕňajú aj štandardné riedenie,

```text
rho_F,x = -3 delta rho_F + Q_F
rho_C,x = -3 rho_C       + Q_C
rho_R,x = -4 rho_R       + Q_R.
```

Očakávaný výsledok je presná algebraická nula `Q_F+Q_C+Q_R=0`, nulový
priamy zdroj do `R` a presná zhoda so zdrojovou časťou oboch uvedených A1
implementácií. Pri `lambda=0` musia všetky `Q` zmiznúť.

## PASS / STOP / ďalší postup

* **PASS:** všetky tri zdrojové identity sú nulové a oba zdroje A1 nesú
  rovnakú štruktúru. Verdikt bude iba
  `BASELINE_EFFECTIVE_LEDGER_PASS_NOT_MICRO_SEQUENCE_DECISION`.
* **STOP:** ak sa v zdrojoch líši znamienko, príjemca prenosu alebo ak
  radiácia už obsahuje nepriznaný priamy transfer. Potom sa Q22a-K1 nesmie
  používať ani ako baseline, kým sa neuzavrie proveniencia.
* **Po PASS:** otvorí sa Q22a-K3 iba ako algebraický test minimálneho
  paralelného rozdelenia. Nezavedie sa voľný podiel do fyzikálneho modelu;
  audit má práve ukázať, či ho vie odvodiť existujúca teória.

## Bezpečnostné limity behu

Skript neintegruje ODE ani nečíta externé dáta. Má interný limit 5 s a bude
spustený s vonkajším limitom 10 s. Výstup JSON je príloha; rozhodnutie zostane
zapísané v Markdownu.
