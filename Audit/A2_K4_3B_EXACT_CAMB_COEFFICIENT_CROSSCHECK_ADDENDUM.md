# A2-K4.3b — dodatok exact CAMB coefficient cross-check

**Dátum:** 2026-07-14  
**Vzťah k hlavnému auditu:** spevňuje B1, nemení celkový rozsudok K4.3b

Skript 75 pôvodne hlásil dve rezíduá pri `ell=3`. Ich tvar bol presne
rozdiel medzi všeobecným názvom multipólu a CAMB aliasom:

```text
J_2 - pi_g, G_2 - pi_r.
```

Pôvodný skript a výstup zostávajú zachované. Skript 76 opravil iba auditné
mapovanie aliasov a zopakoval rovnakú bránu.

| Kontrola | Počet | Výsledok |
|---|---:|---|
| photon `J_l`, `l=2..8` | 7 | všetky rezíduá `0` |
| massless-neutrino `G_l`, `l=2..8` | 7 | všetky rezíduá `0` |
| polarization `E_l`, `l=2..8` | 7 | všetky rezíduá `0` |
| `polter` zdroj | 1 | rezíduum `0` |

**Rozsudok B1:** exact CAMB symbolic coefficient cross-check prešiel.

**Rozsudok celej K4.3b:** bez zmeny — `NEUZAVRETÁ`, pretože chýba sedem
finite-start radov v regulárnej gauge. A2-K4 zostáva živá na `60/100` a
nový dôvod smrti sa nevydáva.

