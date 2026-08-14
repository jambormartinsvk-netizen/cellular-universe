# A2-K4 / K7d — V1 preregistrácia opravy species/projected diagnostiky

**Dátum:** 2026-07-15  
**Stav:** `PREREGISTERED / NOT RUN`  
**Rozpočet AR66:** prvá z najviac dvoch technických opráv  
**Fyzika a prahy:** bez zmeny

## Spúšťač

Prvý raw prípad NID-deep dokončil celý interval, všetkých 29 checkpointov a
13/13 activity kontrol. Dostal však technický REVIEW pre parity
`3.6841e-2 > 1e-10`. Trace audit na prvom checkpointe navyše hlásil
rezíduum `1.2393`, čo je nekonzistentné s kompenzovaným NID seedom.

## Dve potvrdené chyby diagnostiky 213

1. `species_rhs_and_projected_derivative` vracia najprv **deriváciu species**,
   ale checkpoint audit ju čítal ako species stav. Do tlaku preto vstúpilo
   `delta_fs'` namiesto `delta_fs` a do šmyku derivácia namiesto stavu.
2. Nezávislá species cesta znovu skladala kompenzované `D,M` vo float64 a
   použila ich pre `h_x,eta_x`. Tým obnovila známu cancellation chybu, ktorú
   projektovaná K7 odstránila. Pre metrické zdroje musí species kontrola
   použiť autoritatívne projektované `D,M`; iba `D_x,M_x` sa ďalej počítajú
   nezávislým product rule.

Tieto chyby nemenia integráciu: `solve_ivp` volal iba auditovanú
`physical_rhs`. Raw trajektória sa preto zachová a diagnostika sa prepočíta
offline.

## Zmrazená V1 oprava

- načítať immutable raw JSON a overiť jeho hash, štruktúru a runner hash;
- rekonštruovať skutočný species stav z checkpointového `D,M`;
- v species RHS použiť `h_x=3D+2s²eta` a `eta_x=M` z projektovaného stavu;
- `D_x,M_x` vypočítať nezávisle product rule z backgroundových derivácií a
  species spojitostí/Eulerových rovníc;
- trace/traceless tlak a šmyk počítať zo species **stavu**;
- zachovať všetky pôvodné prahy `1e-10`, `1e-12+1e-8*norm` a activity;
- zapísať nový immutable corrected JSON; raw JSON sa nemení.

## Očakávanie a rozhodovanie

Parita po odstránení dvoch formálnych chýb má byť `<=1e-10`. Ak nie je,
V1 ostáva technicky neuzavretá a ďalšie fyzikálne prípady sa nespustia.
Trace/traceless výsledok je exploratívny: PASS pokračuje ďalšími tromi
základnými prípadmi; FAIL je iba kandidát na nezávislé potvrdenie podľa
AR67, nie okamžitá smrť K7.

