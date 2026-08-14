# P5.1 — predregistrácia: statický exact-A1 general-synchronous ledger

**Stav pred behom:** `PRIPRAVENÉ`  
**Skript:** `scripts/236_script_KMPC_003_P5_1_general_synchronous_static_ledger.py`  
**Vnútorný limit:** 5 s. **Vonkajší limit:** 10 s. **Bez ODE.**

## Čo sa overuje ľudskou rečou

Skôr než vznikne nový solver, skript symbolicky overí, že nový stav skutočne
obsahuje dynamické `U_c` a `U_b`, že A1 backgroundové derivácie dávajú
koeficienty `ell`, `gamma`, `beta_c`, `beta_f`, a že prenos palivo ↔ popol
sa v celkovej bilancii presne vyruší. Navyše overí, že Fourierov mód `k`
vstupuje len do `s2=k^2/Hconf^2`, nie do backgroundu.

## Očakávané výsledky

Všetky symbolické rezíduá majú byť presne nula. To nepreukazuje stabilitu,
constrainty ani evolúciu, ale ak čo i len jedna identita nie je nula,
P5 implementácia sa zastaví pred ODE.

## PASS / STOP

- **PASS-P5.1:** všetky identity nula, nový stav obsahuje `U_c` aj `U_b`,
  `M_full` obsahuje CDM hybnosť a `k` nie je v backgroundových koeficientoch.
- **STOP-P5.1:** nenulové rezíduum, chýbajúca hybnosť alebo interný timeout.
- **Po PASS:** pripraviť P5.2 — štyri Einsteinove constrainty. Skóre sa
  nemení a G8 ostáva blokované.
