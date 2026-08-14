# KMPC-036 — M1 order-7 provenance gate: predregistrácia

**Dátum:** 2026-07-17  
**Identita:** `GLOBAL_C1 / M1_ORDER7_PROVENANCE_GATE`  
**Výslovne nie:** CDI support step 3 ani globálna Fourier C2 brána  
**Stav:** `FROZEN / NOT_RUN`

## 1. Jediná otázka

Možno ten istý hard-anchored standardný CDI M1 seed pri `k=0.05 Mpc^-1`,
nominal a nezmenených rovniciach rozšíriť z order 5 na order 7 bez ranku,
normalizačného driftu alebo full-power driver/`00/0i` rozporu?

KMPC-036 nerieši F0/M3 support `[0,7]`. Ten smie dostať samostatný run až
po immutable výsledku, nezávislých auditoch a autoritatívnom PASS hlavného
agenta.

## 2. Zmrazený kontrakt

| Veličina | Order 5 baseline | Order 7 audit |
|---|---:|---:|
| stavy | 11 | 11 |
| powers | `-1..5` (7) | `-1..7` (9) |
| full vector columns | 77 | 99 |
| po exact hard anchore | 76 | 98 |
| driver coefficients | 77 | 99 |
| frozen initial rows | 22 | 22 |
| augmented matrix | `99×77` | `121×99` |
| reduced solve | `99×76` | `121×98` |
| nezávislé `00/0i` holdouty | 14 | 18 |

Hard anchor ostáva `h[1]=f_c mu`; `00/0i` nesmú vstúpiť do solve. Každý z
11 stavov musí mať explicitne všetky keys `-1..7`. Chýbajúce `j=6,7` sa
nesmú potichu doplniť nulou.

## 3. Povinné brány

1. prerequisite KMPC-035 SHA
   `A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`;
2. exact ordered state/power/count/shape/anchor registry;
3. reduced rank `98/98`, inverse condition `>=1e-10`, finite riešenie;
4. anchor absolute difference `<=1e-14`;
5. nezávisle znovu zostaviť a skontrolovať všetkých 99 driver + 22 initial
   residualov a všetkých 18 holdout residualov na powers `-1..7`;
6. per-row branch: pri term norm `>1e-12` relative `<=1e-10`, inak absolute
   `<=1e-12`;
7. order-5 metadata reprodukujú immutable KMPC-035;
8. common state coefficients `-1..5` a background powers `-4..5` medzi
   order 5/7 spĺňajú `abs(diff)<=max(1e-14,1e-12*scale)`;
9. nové coefficients `6,7` sú explicitné a finite; ich malosť nie je PASS
   podmienkou.

Existujúce helper metadata s `checked_hi=1` sú iba diagnostika a nemôžu
udeliť PASS. Autoritatívne sú nové full-range residual ledgers.

## 4. Negatívne fixtures

Smoke musí odmietnuť: wrong order, reordered state register, missing power 7,
missing anchor, missing holdout a duplicate holdout. Pri žiadnej vetve sa
nesmie importovať ani volať CDI `[0,5]→[0,7]` solve.

## 5. Rozhodovací strom

| Výsledok | Kandidát skriptu | Hlavný význam |
|---|---|---|
| regression drift | `REVIEW_M1_ORDER7_REGRESSION_DRIFT` | support step 3 blokovaný |
| rank/driver/holdout/coverage fail | `REVIEW_M1_ORDER7_CORE_OR_HOLDOUT_UNCLOSED` | formula/precision/provenance audit; nie smrť K4 |
| všetko PASS | `PASS_M1_ORDER7_PROVENANCE_CANDIDATE_ONLY` | iba kandidát na auditovateľný order-7 source |
| exception/timeout/hash/schema | technical failure | fyzika NOT_RUN |

Fyzikálny STOP tejto M1 series formulácie by vyžadoval nezávislé
reprodukovanie invariantného full-power rozporu po vylúčení ranku, precision,
normalizácie a chýbajúceho RHS orderu. KMPC-036 samo nemôže zabiť A2-K4.

## 6. Artefakty a hashe

| Artefakt | SHA-256 |
|---|---|
| `mode_resolved_puiseux.py` | `5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE` |
| `mode_resolved_puiseux_v2_m1_anchored.py` | `5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455` |
| `m1_order7_provenance.py` | `0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7` |
| runner 280 | `EBA6F6D0392F94A511D3D0B9FEFDA07558CB6DE5ED968F0CC02AF6754C2A204B` |

Success output:
`scripts/results/k_mpc_005/RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json`.
Failure output má rovnaký názov s `_TECHNICAL_FAILURE`. Obe cesty sú
immutable a canonical-only. Interný limit je presne `4.8 s`, vonkajší `10 s`.

## 7. Nonclaims

Bez CDI support step 3, BI/NID/NIV, iných `k`/variantov, S-M pôvodu pary,
species `F_l>=3`, full hierarchy, ODE, finite opacity, G8/G9,
BBN/CMB/CLASS/S8/H0 a bez analytického all-order boundu.

`SCORE_EFFECT=NONE`, `PREDICTION_TABLE_EFFECT=NONE`,
`RELEASE_TRIGGER=NONE`, `ZENODO_TRIGGER=NONE`. Skript prideľuje iba kandidáta;
autoritatívny PASS/REVIEW/STOP patrí hlavnému agentovi.
