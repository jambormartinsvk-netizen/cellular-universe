# A2-K4.3b-RG BR3C-b — výstup skriptov 136 až 138

**Dátum:** 2026-07-14  
**Rozsudok C7.7b:** `PASS`  
**K4:** `ŽIVÁ; 66.5/100; G6 PASS; G7 OTVORENÁ`

## Rovnicový audit 137

```text
execution_verdict = PASS_BR3C_B_EQUATION_SIGN_AUDIT
13/13 ODE/constraint rearrangement identít
8/8 jednoznačných source-token kontrol znamienok
runtime = 0.047 s
```

Audit zahŕňal `00`, `0i`, photon/baryon, free-streaming hierarchy po `L4`,
CDM transfer aj oba fuel riadky. Neauditoval ešte trace/traceless rezíduá
počas evolúcie.

## Segmentovaná evolúcia 136

```text
execution_verdict = PASS_BR3C_B_SEGMENTED_EARLY_EVOLUTION
checks             = 27/27
runtime            = 6.390 s
rhs_calls          = 364000
fine_depth         = 66.5/100
```

| Mód/povrch | `x_start -> x_final` | Segmenty | `nfev` | Najväčšia zložka počas behu |
|---|---|---:|---:|---:|
| NID/deep | `-25 -> -18` | `7/7` | `4298` | `max|delta_fs|=1.0000000` |
| NID/shallow | `-23 -> -18` | `5/5` | `3070` | `max|delta_fs|=0.999999999999` |
| NIV/deep | `-25 -> -18` | `7/7` | `312842` | `max|U_fs|=2.3385705e6` |
| NIV/shallow | `-23 -> -18` | `5/5` | `43762` | `max|U_fs|=3.1649115e5` |

Všetky checkpointy mali konečný 13-zložkový stav aj RHS a zostali pod
`1e12`. Každý segment mal najviac jeden e-fold; `max_step=0.02`,
`rtol=1e-10`, `atol=1e-14`.

## Povinné riziko pre ďalší audit

Hlboký NIV beh je numericky drahý: spotreboval približne `3.13e5` RHS
vyhodnotení. C7.7b z toho nerobí fyzikálnu nestabilitu, pretože stav ostal
konečný a dominantná veľká rescalovaná rýchlosť bola prítomná už v
počiatočnej konvencii. Zároveň to nie je dôkaz konvergencie. C7.8 musí
porovnať krok, toleranciu a vhodnosť solvera; prípadný falošný stiffness sa
nesmie skryť.

## Rozsah PASS

BR3C-b dokazuje iba, že štyri predregistrované trajektórie s rovnakou ODE
sústavou dobehli do `x=-18` bez nefinitej hodnoty, tichého vynechania alebo
safety-cap runaway.

Neznamená:

- zhodu deep/shallow endpointov;
- PASS evolučného species/mode auditu C7.7c;
- nezávislý PASS `00/0i`, pretože určovali `h_x/eta_x`;
- PASS trace/traceless rovnice;
- krokovú, tolerančnú alebo `lmax` konvergenciu;
- plný Boltzmannov backend, G7 alebo `S8`.

## SHA-256

| Súbor | SHA-256 |
|---|---|
| `136_script_A2_K4_3b_RG_BR3C_b_segmented_early_evolution.py` | `85c5190c7d7fa48c36d10742ab42c9a860ffd03c31f7dc08e93a41ca45442cba` |
| `137_script_A2_K4_3b_RG_BR3C_b_equation_sign_audit.py` | `6d3fc139255b65287cbcdcb842151282d3e2a4babe805397465468a4ba79cfa1` |

Skript 138 vytvoril manifest s verdiktom
`PASS_BR3C_B_MANIFEST_CREATED`.

