# KMPC-041 — GLOBAL_C1 BI primary/extended: výsledok a audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / BI`  
**Autoritatívny rozsudok:**
`PASS_BI_C1_CORE_AND_COMMON_COEFFICIENT_STABILITY_ONLY / REVIEW_BI_C1_PRIMARY_01_INSUFFICIENT_EXTENDED_03_REMAINDER_NOT_YET_TESTED`  
**K4:** `LIVE / 60/100`; skóre bez zmeny  
**Dôsledok:** BI primary `[0,1]` je nedostatočný; ďalší krok je samostatná
predregistrácia BI support step 2 `[0,3]→[0,5]`

## Dôkazový artefakt

Canonical JSON:
`scripts/results/k_mpc_005/RUN_KMPC_041_P5_3G7_BI_C1_PRIMARY_EXTENDED_COVERAGE.json`  
SHA-256:
`8BB006EF6606476D85168FBDCD913249E9EDE024C1017473376A33CF4C7AE183`.

Base `bi_c1_coverage.py` má SHA
`303515C80945905BFC537B8FFDB94F1F126B73EB939679D46A95DD4BDE384BF6`;
runner 285 má SHA
`078C67C0B815E3D03292F5499A10D4633E7D976159FC9074BF333ABA3E9A059C`.
Proces prešiel `compile → help → smoke → jeden audit`, audit trval `1.172 s`
pod limitom `4.8 s`; failure ani tmp artefakt nevznikol.

## Čo prešlo

| Brána | Výsledok | Dôkaz |
|---|---|---|
| support/count | PASS | `[0,1]→[0,3]`, F0 `4/8`, M3 `26/52`, leading `j=1` |
| M1 order-5 | PASS | rank `76/76`, hard anchor zachovaný |
| F0/M3 core | PASS | rank/driver/leading/forbidden/production/regularity/finite |
| nezávislé `00/0i` holdouty | PASS | max relative `3.36e-14` primary, `2.75e-13` extended |
| actual S-C0 | PASS | BI primary aj extended lower-moment coefficients |
| F0 common powers `0,1` | PASS | worst relative `6.71272e-16 < 1e-8`, `U_f[1]` |
| M3 common powers `0,1` | PASS | worst relative `6.05936e-14 < 1e-8`, `U_f[1]` |

Common koeficienty sa pri rozšírení prakticky neprepísali. Tail FAIL teda
nevznikol kolapsom ranku, zmenou normalizácie ani common driftom.

## Čo neprešlo

Autoritatívna metrika bola cancellation-safe obálka
`sum(abs(c_j)z^j)` iba pre powers `2,3` voči baseline power `1`.

| Rodina/plochа | Najhoršia metrika | Stav | Prah |
|---|---:|---|---:|
| F0, `z=1e-4` | `1.13130e-5` | `U_f` | `1e-6` |
| F0, `z=.01` | `1.0000000000001` | `delta_f` | `1e-6` |
| M3, `z=1e-4` | `3.13648e-5` | `delta_f` | `1e-6` |
| M3, `z=.01` | `0.999999999727` | `sigma_fs` | `1e-6` |

Pri `z=.01` zlyhali oba F0 stavy a 12 z 13 M3 stavov. Nejde o efekt
rušenia znamienok: pri rozhodujúcich hustotách a `sigma_fs` je pomer signed
súčtu k obálke prakticky `1`. Aj po ignorovaní stavov s takmer nulovým
nižším baseline ostávajú bežné hustoty, rýchlosti a metrika s hodnotami
približne `1.8e-3…3.1e-3`, teda jasný FAIL primary `[0,1]`.

## Mode-routing audit

BI výsledok nie je omylom opakovaný CDI payload. Read-only porovnanie s
KMPC-034 ukázalo mode-specific M3 rozdiely, napríklad `h[1]` o približne
`0.02` a `delta_gamma[1]`, `delta_fs[1]` o približne `0.01`. Zhodné F0
fuel-zero koeficienty v tomto úzkom rozsahu preto neznamenajú zhodnú BI/CDI
stavovú vetvu; M3 routing je odlišný a core brány ho spracovali ako BI.

## Interpretácia a ďalší krok

Výsledok dokazuje iba, že BI baseline `[0,1]` nestačí pri zmrazených
plochách a prahoch. Nehovorí, že `[0,3]` nestačí, pretože remainder nad
`[0,3]` nebol vypočítaný. Nie je to fyzikálny STOP BI ani K4.

Ďalší povolený atóm je samostatne predregistrovaný BI support step 2:

```text
immutable regression [0,1] a [0,3] proti KMPC-041,
candidate [0,3], audit [0,5],
common powers 0…3,
tail envelope iba powers 4,5 voči baseline 1…3.
```

F0 počty budú `4/8/12`, M3 `26/52/78`. Ak tail `4,5` zlyhá, ďalšie
rozšírenie nevznikne automaticky; najprv sa rozhodne o BI order-7 provenance
a numerickej hranici.

## Nonclaims a triggery

Bez NID/NIV, iných `k`/variantov, S-M, full hierarchy, finite opacity, ODE,
P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez potvrdenia celej teórie.
`SCORE_EFFECT=NONE`, `PREDICTION_TABLE_EFFECT=NONE`,
`RELEASE_TRIGGER=NONE`, `ZENODO_TRIGGER=NONE`.
