# KMPC-043 — BI M1 order-7 provenance: výsledok a audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / BI_M1_ORDER7`  
**Autoritatívny rozsudok:**
`PASS_BI_M1_ORDER7_REGRESSION_SHAPE_RANK_ANCHOR_CONDITION_STATE_ONLY /
REVIEW_BI_M1_ORDER7_DRIVER_AND_HOLDOUT_PRECISION_BOUNDARY_UNCLOSED`  
**K4:** `LIVE / 60/100`; skóre bez zmeny  
**Dôsledok:** BI support step 3 `[0,5]→[0,7]` zostáva `BLOCKED`

## Dôkazový balík

| Artefakt | SHA-256 |
|---|---|
| base `bi_m1_order7_provenance.py` | `69C65F408635E71B455FBF2135FB5057E0DA01B8E4895B5B5D96733AC4AF03C2` |
| runner 287 | `DB765083E645886F332EBD542F3126EA91D6CF901C2C621AE9092D0EA4C1D358` |
| immutable výsledok | `B02D1D16CFAE4331378B68F12258142F84A424419BB9D3A52AAEE87D0CC61EB0` |

Kanonický JSON:
`scripts/results/k_mpc_005/RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE.json`.
Audit trval `0.297 s`; failure ani temp artefakt nevznikol. Identita je
presne `BI / k=0.05 Mpc^-1 / nominal / order=7` a immutable prerequisite
je KMPC-042 SHA
`E5F18DA4DE5A718C4448D095804F6D41FE88445A95FB99645EFBCCB48D48CA61`.

## Čo prešlo

- immutable BI order-5 metadata;
- BI order-5 → order-7 common state na powers `-1…5` a celý background;
- full shape `121×99`, reduced shape `121×98` a nezávislý rank `98/98`;
- hard anchor `h[1]`, explicitný 11-stavový register a powers `-1…7`;
- condition `634.79684624517`, inverse condition `1.5753e-3 > 1e-10`;
- finite guard a správna BI identita bez použitia CDI stavu alebo korekcie.

Najväčší lower-state rozdiel je `1.7586e-15 < 1e-14` na `dfs[2]`;
background regresia je presná v rámci zapísaného výsledku. Nevznikol
rankový, anchorový, stavový ani lower-order rozpor.

## Čo zostalo otvorené

Pri zmrazenom relative prahu `1e-10` zlyhalo 5 zo 121 driver/initial riadkov
a 1 z 18 nezávislých holdoutov:

| Riadok | relative metrika | absolute residual | term norm |
|---|---:|---:|---:|
| `gamma_Euler[7]` | `1.31519e-9` | `-6.08052e-16` | `4.62328e-7` |
| `fs_Euler[6]` | `1.08206e-10` | `-7.58142e-16` | `7.00645e-6` |
| `fs_Euler[7]` | `1.15065e-9` | `-8.43230e-16` | `7.32828e-7` |
| `cdm_continuity[7]` | `2.53656e-10` | `9.96254e-17` | `3.92757e-7` |
| `tight_coupling[7]` | `8.20456e-10` | `-4.08289e-17` | `4.97637e-8` |
| holdout `Einstein_0i[7]` | `2.19459e-10` | `1.32990e-16` | `6.05991e-7` |

Absolútne residualy sú iba `4.1e-17…8.4e-16`. Formálny FAIL je napriek
tomu platný: pri nenulovej norme riadka sa používa scale-aware relatívna
vetva, takže malé absolútne číslo samo osebe prah neobchádza. Koncentrácia
na powers 6–7, bez lower/rank/anchor driftu, robí z float64 flooru silného
kandidáta príčiny. Na rozdiel od CDI KMPC-036 však zlyhal aj jeden nezávislý
holdout; numerická príčina preto ešte nie je autoritatívne potvrdená.

## Autoritatívna interpretácia

Výsledok nepotvrdzuje chybu BI fyzikálnych rovníc, ale ani plný order-7
provenance PASS. Dokazuje iba, že BI-specific RHS a anchor majú stabilnú
nižšiu časť, správne rozmery a plný rank, zatiaľ čo jednoprechodový float64
solve neuzavrel zmrazenú presnostnú hranicu na šiestich riadkoch.

KMPC-043 netestoval tail metriku supportu a nemôže povedať, či je BI
`[0,5]` dostatočný. Preto sa nesmie preskočiť priamo na `[0,7]` ani zvyšovať
support na `[0,9]`.

## Ďalší predregistrovaný krok

Samostatne predregistrovať `BI_M1_ORDER7_NUMERICAL_BOUNDARY_CLOSURE` na
presne tej istej BI float64 matici, RHS, anchore a prahoch. Musí:

1. immutable reprodukovať KMPC-043 vrátane presných 5+1 otvorených riadkov;
2. vykonať najviac jednu deterministickú residual correction na reduced
   `121×98` systéme a vyžadovať `max|delta_x| < 1e-14`;
3. nezávisle overiť tú istú už zostavenú maticu pri 80 dps;
4. znovu skontrolovať 121 driver/initial, 18 holdoutov, lower powers `-1…5`
   a exact anchor;
5. nepoužiť CDI stav ani CDI korekčný vektor.

Ak obe numerické vetvy uzavrú všetkých 139 riadkov bez regresie, BI support
step 3 sa iba odblokuje pre samostatnú predregistráciu. Ak invariantný
residual pretrvá, ďalší krok bude exact recurrence/last-layer formula audit,
nie zmena prahu.

## Nonclaims a triggery

Bez BI support step 3, NID/NIV, iných `k`/variantov, S-M, full hierarchy,
ODE, P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.
`SCORE_EFFECT=NONE`, `PREDICTION_TABLE_EFFECT=NONE`,
`RELEASE_TRIGGER=NONE`, `ZENODO_TRIGGER=NONE`.
