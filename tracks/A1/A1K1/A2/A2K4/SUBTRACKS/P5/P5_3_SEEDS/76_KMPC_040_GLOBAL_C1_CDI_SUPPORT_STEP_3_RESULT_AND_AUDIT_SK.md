# KMPC-040 — GLOBAL_C1 CDI support step 3: výsledok a audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / CDI_SUPPORT_STEP_3`  
**Autoritatívny rozsudok:**
`PASS_CDI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_WITHIN_CDI_K005_NOMINAL_ONLY`  
**K4:** `LIVE / 60/100`; skóre bez zmeny  
**Dôsledok:** CDI support vetva pre `k=0.05 / nominal` je uzavretá;
ďalší krok je samostatná predregistrácia fail-fast BI coverage, nie `[0,9]`

## Dôkazový artefakt

Canonical JSON:
`scripts/results/k_mpc_005/RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07.json`  
SHA-256:
`69C78F70ECD851D8B8A48E4E09445181C0D4559E9BD2E90A7BA19933351BD219`.

Runner prešiel `compile → help → smoke → jeden audit`. Interný audit trval
`3.234 s` pod limitom `4.8 s`. Success bol zapísaný atomicky a exkluzívne;
failure ani tmp artefakt nevznikol.

## Rozhodujúce brány

| Brána | Výsledok | Najdôležitejší údaj |
|---|---|---|
| support/count guard | PASS | `[0,3]`: `8/52`, `[0,5]`: `12/78`, `[0,7]`: `16/104` pre F0/M3 |
| M1 order-7 rekonštrukcia | PASS | jedna korekcia `2.11114386969413e-15 < 1e-14`, rank `98` |
| immutable KMPC-035 regresia | PASS | všetky 4 bloky; najhorší bound ratio `0.0243729` |
| core `[0,3]/[0,5]/[0,7]` | PASS | rank/driver/holdout/contract/registry restore a finite checks |
| `S-C0` `[0,5]↔[0,7]` | PASS | actual coefficient guard |
| common F0 powers `0…5` | PASS | worst relative `6.58256e-13 < 1e-8`, `delta_f[5]` |
| common M3 powers `0…5` | PASS | worst relative `2.73196e-11 < 1e-8`, `U_b[5]` |
| tail F0 powers `6,7`, `z=.01` | PASS | worst envelope ratio `5.29508e-11 < 1e-6`, `delta_f` |
| tail M3 powers `6,7`, `z=.01` | PASS | worst envelope ratio `8.71681e-9 < 1e-6`, `sigma_fs` |
| tail na `z=1e-4` | PASS | worst relative `2.60412e-24` F0 a `1.14469e-23` M3 |

Autoritatívna tail metrika bola absolútna obálka
`sum(abs(c_j) z^j)` iba pre `j=6,7` voči baseline `j=1…5`. Signed súčet bol
iba diagnostický, takže PASS nevznikol z rušenia kladných a záporných členov.
Prahy, plochy, rovnice aj vstupná identita zostali zmrazené.

## Interpretácia

KMPC-040 ukazuje, že pri tejto jednej predregistrovanej identite je support
`[0,5]` dostatočný voči rozšíreniu `[0,7]`: staré koeficienty `0…5` sú
stabilné a nové členy `6,7` sú na oboch testovaných plochách hlboko pod
zmrazeným tail limitom. Najhoršia tail hodnota je približne `115×` pod
limitom, preto nejde o hraničný PASS.

Tento výsledok neruší historické REVIEW: `[0,1]` a `[0,3]` boli predošlé
nedostatočné candidate supporty. Ukazuje iba to, že ďalšie rozšírenie z
`[0,5]` na `[0,7]` už mení sledovanú CDI aproximáciu zanedbateľne. Preto sa
`[0,9]` nepočíta; neexistuje trigger pre coefficient-growth/radius audit.

## Ďalší predregistrovaný krok

Samostatne predregistrovať prvý fail-fast coverage atóm pre mód `BI` pri
`k=0.05 Mpc^-1 / nominal`: primary `[0,1]`, extended `[0,3]`, leading
`j=1`, s pôvodnými core/common/tail/S-C0 pravidlami. KMPC-040 tento BI krok
nespustil. Po BI sa osobitne rozhodne o NID a až potom NIV; žiadne výsledky
sa medzi módmi neprenášajú.

## Nonclaims a triggery

Bez iných `k`, variantov, BI/NID/NIV výsledku, fyzikálneho pôvodu steam,
S-M, species-resolved vyššej hierarchie, ODE, G8/G9, CLASS/CMB/BBN/S8/H0 a
bez potvrdenia celej teórie. `SCORE_EFFECT=NONE`,
`PREDICTION_TABLE_EFFECT=NONE`, `RELEASE_TRIGGER=NONE`,
`ZENODO_TRIGGER=NONE`.
