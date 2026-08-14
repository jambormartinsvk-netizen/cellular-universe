# KMPC-036 — M1 order-7 provenance gate: výsledok a audit

**Dátum:** 2026-07-17  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / M1_ORDER7_PROVENANCE_GATE`  
**Autoritatívny rozsudok:**
`PASS_M1_ORDER7_REGRESSION_SHAPE_RANK_ANCHOR_CONDITION_STATE_AND_HOLDOUT_ONLY /
REVIEW_M1_ORDER7_POWER7_DRIVER_PRECISION_FLOOR_UNCLOSED`  
**K4:** `LIVE / 60/100`; support step 3 zostáva blokovaný

## Dôkazový balík

| Artefakt | SHA-256 |
|---|---|
| base `m1_order7_provenance.py` | `0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7` |
| runner 280 | `EBA6F6D0392F94A511D3D0B9FEFDA07558CB6DE5ED968F0CC02AF6754C2A204B` |
| immutable výsledok | `39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497` |

Kanonický JSON:
`scripts/results/k_mpc_005/RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json`.
Audit skončil technicky úspešne; failure ani temp artefakt nezostal.

## Čo prešlo

- immutable order-5 metadata, common state `-1..5` a background `-4..5`;
- shapes `121×99`, reduced `121×98`, nezávislý rank `98/98`;
- exact hard anchor `h[1]`, condition `634.8`, explicitné powers `-1..7`;
- finite state a všetkých 18 nezávislých `Einstein_00/0i` holdoutov;
- všetky driver/initial riadky do `j=6`.

Nevznikol constraint, normalizačný, rankový ani provenance rozpor.

## Čo neprešlo

Iba tri terminal power-7 driver riadky prekročili zmrazený relative prah
`1e-10`:

| Riadok | relative residual | absolute residual | term norm |
|---|---:|---:|---:|
| `gamma_Euler[7]` | `2.8658e-10` | `7.8509e-16` | `2.7395e-6` |
| `cdm_continuity[7]` | `4.6572e-10` | `1.0839e-15` | `2.3273e-6` |
| `tight_coupling[7]` | `1.1663e-9` | `3.4390e-16` | `2.9487e-7` |

Fail je formálne platný a prah sa spätne nemení. Absolútne residualy sú však
iba približne `1.55–4.88` násobku IEEE-754 epsilonu, všetky sú na poslednej
vrstve a holdouty prešli. Preto súčasný dôkaz podporuje numerický precision
floor oveľa viac než chybnú fyziku, ale plný M1 order-7 PASS ešte neudeľuje.

## Ďalšia koľaj odvodená z príčiny

Nasledujúci run dostane identitu
`M1_ORDER7_NUMERICAL_REFINEMENT_AND_BOUNDARY_CLOSURE_AUDIT`. Použije presne
tú istú zmrazenú `121×98` sústavu a nezmenené prahy. Musí oddeliť:

1. float64 solver floor (`A^T r`, backward error, bounded refinement);
2. rounding už zostavenej float64 matice (high-precision solve tej istej matice);
3. coefficient-generation floor (native high-precision rebuild);
4. skutočný terminal-layer formula/truncation rozpor.

Najviac jeden refinement a jeden nezávislý high-precision solve. Lower
coefficients a holdouty sa musia regresne zachovať. Support step 3, `[0,9]`
ani iná fyzika nesmú byť súčasťou toho istého runu.

Ak vyššia presnosť tri riadky uzavrie, vznikne nový order-7 provenance
kandidát. Ak invariantný residual pretrvá aj po native high-precision rebuild,
nasleduje formulačný audit exact recurrence/last-layer closure. Ani to samo
automaticky nezabíja A2-K4; zabilo by to nanajvýš túto konkrétnu Puiseux
order-7 implementačnú koľaj po nezávislej reprodukcii.

## Nonclaims a triggery

Bez CDI support step 3, BI/NID/NIV, iných `k`/variantov, S-M, full hierarchy,
ODE, G8/G9, BBN/CMB/CLASS/S8/H0 a bez zmeny teórie.
`SCORE_EFFECT=NONE`, `PREDICTION_TABLE_EFFECT=NONE`,
`RELEASE_TRIGGER=NONE`, `ZENODO_TRIGGER=NONE`; bilingválny 05 sa nemení.
