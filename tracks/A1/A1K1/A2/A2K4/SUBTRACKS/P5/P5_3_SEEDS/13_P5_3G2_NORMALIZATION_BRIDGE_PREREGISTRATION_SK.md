# P5.3g2 — predregistrácia: algebraický most `qnu ↔ F1`

**Skript:** `scripts/250_script_KMPC_013_P5_3g2_f1_qnu_bridge_ledger.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE a bez skóre.

## Predpoklad, ktorý sa má explicitne overiť

V BR2 platí `q=k/H0` a neutrínová hybnostná premenná je
`U_nu = 3(aE)F1/(4q)`. CAMB audit používa `qnu=4 theta_nu/(3k)` a
`U_nu = 3 Hconf qnu/(4k)`. Ak `Hconf=H0 aE` a `k=H0 q`, oba zápisy sú
rovnaké práve vtedy, keď `F1=qnu`.

## Očakávanie a rozhodnutie

- **FORMULA PASS (úzky rozsah):** textové zdroje obsahujú všetky štyri
  definície a algebraický rozdiel po dosadení `F1=qnu` je presne nula.
  P5.3g3 potom smie z `l=2` BR2 rovnice odvodiť pravidelný koeficient.
- **REVIEW_BLOCKED:** chýba ktorýkoľvek článok. Žiadne prebratie
  normalizácie z názvu premennej ani žiadne ODE.

Rozsah je iba normalizácia neutrínového dipólu v danej bezrozmernej BR2
konvencii; nepreukazuje úplný seed ani G8.
