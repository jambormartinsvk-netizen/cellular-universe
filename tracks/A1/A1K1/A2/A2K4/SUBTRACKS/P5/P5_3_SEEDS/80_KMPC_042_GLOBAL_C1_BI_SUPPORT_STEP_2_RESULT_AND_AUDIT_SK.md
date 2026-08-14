# KMPC-042 — GLOBAL_C1 BI support step 2: výsledok a audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / BI_SUPPORT_STEP_2`  
**Autoritatívny rozsudok:**
`PASS_BI_SUPPORT_STEP_2_CORE_AND_COMMON_03_05_STABILITY_ONLY / REVIEW_BI_SUPPORT_03_REMAINDER_UNCLOSED`  
**K4:** `LIVE / 60/100`; skóre bez zmeny  
**Dôsledok:** BI candidate `[0,3]` je nedostatočný; `[0,7]` zostáva
zablokovaný samostatnou BI M1 order-7 provenance bránou

## Dôkazový artefakt

Canonical JSON:
`scripts/results/k_mpc_005/RUN_KMPC_042_P5_3G7_BI_SUPPORT_STEP_2_03_05.json`  
SHA-256:
`E5F18DA4DE5A718C4448D095804F6D41FE88445A95FB99645EFBCCB48D48CA61`.

Base `bi_support_step2.py` má SHA
`08A8071D5D3DC8A1A0D58CB76CAF08548ADC6D85F067D51151CE78129CC1F19F`;
runner 286 má SHA
`F1C068BC358B98F1D8FA056D4A008BC7FB5A943324FB247192BB4E2D6ECFEDD1`.
Proces prešiel `compile → help → smoke → jeden audit`; audit trval `1.735 s`
pod limitom `4.8 s`. Failure ani tmp artefakt nevznikol.

## Prejdené brány

| Brána | Výsledok | Dôkaz |
|---|---|---|
| support/count | PASS | `[0,1]/[0,3]/[0,5]`; F0 `4/8/12`, M3 `26/52/78` |
| immutable KMPC-041 regresia | PASS | všetkých `4+26+8+52` koeficientov presne reprodukovaných |
| M1 order-5 | PASS | rank `76/76`, anchor zachovaný |
| core všetkých supportov | PASS | rank/driver/holdout/forbidden/production/regularity/finite |
| actual S-C0 `[0,3]↔[0,5]` | PASS | lower-moment coefficient guard |
| F0 common powers `0…3` | PASS | worst relative `7.47199e-15 < 1e-8`, `delta_f[3]` |
| M3 common powers `0…3` | PASS | worst relative `1.44663e-12 < 1e-8`, `U_f[3]` |

Common drift je viac než štyri rády pod limitom. Tail FAIL preto nie je
zmena starých koeficientov ani strata hodnosti.

## Neuzavretý remainder

Autoritatívny tail bola obálka powers `4,5` voči baseline `1…3`.

| Rodina/plochа | Najhoršia metrika | Stav | Výsledok |
|---|---:|---|---|
| F0, `z=1e-4` | `1.52688e-14` | `U_f` | PASS |
| F0, `z=.01` | `2.52402e-5` | `delta_f` | FAIL |
| M3, `z=1e-4` | `6.93329e-14` | `delta_gamma` | PASS |
| M3, `z=.01` | `3.21671e-3` | `sigma_fs` | FAIL |

Pri plytšej ploche zlyhali presne dva stavy: F0 `delta_f` a M3 `sigma_fs`.
FAIL nie je spôsobený rušením znamienok: signed/envelope pomer je `0.99927`
pre `delta_f` a `0.99911` pre `sigma_fs`. Prah zostal `1e-6`.

## Mode-routing a interpretácia

Read-only porovnanie s CDI KMPC-035 ukázalo odlišné BI M3 koeficienty,
napríklad `h[1]` približne o `0.02` a viaceré hustoty o `0.01`. Zhodné
najhoršie tail metriky teda nevznikli nesprávnym CDI routovaním; ide o
spoločnú subleading štruktúru frozen rovníc v tomto rozsahu.

KMPC-042 dokazuje iba, že BI `[0,3]` nestačí. Nevykonal `[0,5]→[0,7]` a
nedáva fyzikálny STOP BI. Candidate `[0,5]` ešte nebol overený voči vyššiemu
supportu.

## Ďalší predregistrovaný krok

Samostatne predregistrovať `BI_M1_ORDER7_PROVENANCE_GATE`:

- BI identita, nie prenos CDI order-7 stavu;
- order 5 immutable regresia a order 7 hard-anchor solve;
- presné shape/rank/state/powers kontroly;
- full-power driver/initial a nezávislé `00/0i` holdouty;
- lower `-1…5` regresia, condition a finite guard;
- žiadny support `[0,7]` v tom istom behu.

Iba ak BI order-7 hranica prejde, smie vzniknúť BI support step 3
`[0,5]→[0,7]`. Ak sa objaví iba solver-floor rezíduum, musí dostať vlastnú
numerickú boundary predregistráciu; CDI korekcia sa nesmie skopírovať.

## Nonclaims a triggery

Bez BI `[0,5]` adequacy, NID/NIV, iných `k`/variantov, S-M, full hierarchy,
ODE, P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez potvrdenia celej teórie.
`SCORE_EFFECT=NONE`, `PREDICTION_TABLE_EFFECT=NONE`,
`RELEASE_TRIGGER=NONE`, `ZENODO_TRIGGER=NONE`.
