# k_mpc_005 — presný A1 background a normalizácia A_f

**Vlastník:** `A1K1/P4`  
**Stav:** `REVIEW — background mapovanie použiteľné, pôvod A_f otvorený`

`af_from_a1_background.py` centralizuje presný A1 background pre runnery
234, 235 a route-conditioned Q22A audit. Číslo `0.05 Mpc^-1` sa nesmie
použiť ako globálny background parameter. Fourierovo `k` patrí poruchám;
homogénny palivový člen musí byť po mapovaní módovo nezávislý.

Modul sám neuzatvára fyzikálny pôvod `A_f` a neprenáša PASS medzi A1-K1 a
Q22A vetvou. Presný hash je v `../00_MODULE_OWNERSHIP_REGISTER.md`.

