# A2-K4.3b-RG — výstupy skriptov 77 až 86

**Dátum:** 2026-07-14  
**Pravidlo:** neúspešné skripty a výpočty sa nemažú; ich rozsah je označený.

## 1. Príkazy a časové limity

```text
python scripts/77_script_A2_K4_3b_RG_collective_CAMB_regular_seed_audit.py --max-runtime-seconds 45
python scripts/77_script_A2_K4_3b_RG_collective_CAMB_regular_seed_audit.py --max-runtime-seconds 45 --y-min 0.002
python scripts/78_script_A2_K4_3b_RG_collective_CAMB_regular_seed_active_start_fixed.py --max-runtime-seconds 45
python scripts/79_script_A2_K4_3b_RG_collective_CAMB_regular_seed_precompiled_only.py --max-runtime-seconds 45
python scripts/80_script_A2_K4_3b_RG_internal_nu_steam_exact_regular_series.py --max-runtime-seconds 25
python scripts/81_script_A2_K4_3b_RG_CAMB_Newtonian_metric_reconstruction_audit.py --max-runtime-seconds 35
python scripts/82_script_A2_K4_3b_RG_CAMB_Newtonian_metric_reconstruction_fine_grid.py --max-runtime-seconds 35
python scripts/83_script_A2_K4_3b_RG_exact_background_fractional_power_audit.py --max-runtime-seconds 35
python scripts/84_script_A2_K4_3b_RG_CLASS_analytic_collective_seed_CAMB_crosscheck.py --max-runtime-seconds 35
python scripts/85_script_A2_K4_3b_RG_collective_K4_test_field_Puiseux_response.py --max-runtime-seconds 45
python scripts/86_script_A2_K4_3b_RG_general_synchronous_K4_test_field_response.py --max-runtime-seconds 45
```

Externé limity boli 40–60 s. Žiadny beh neprekročil externý limit.

## 2. Supersession ledger

| Skript | Výsledok | Auditný význam |
|---|---|---|
| 77, prvý beh | `REVIEW`, rank 0 | nulové CAMB placeholdery pred interným štartom boli omylom použité ako seed |
| 77, `y_min=0.002` | `PASS`, rank 5 | diagnosticky potvrdil príčinu |
| 78 | `ERROR_UNCLOSED` | symbolický `pi_r` vyžadoval chýbajúci Fortran kompilátor |
| 79 | `PASS` | opravený aktívny štart, iba predkompilované CAMB výstupy |
| 80 | `PASS` | dva exaktné interné `nu-steam` módy |
| 81 | `REVIEW` | riedka derivácia malých CDI/BI potenciálov |
| 82 | `REVIEW` | ani jemnejšia mriežka neodstránila cancellation noise odvodených potenciálov CDI/BI |
| 83 | `PASS` | presný raný mocninový/Puiseuxov register K4 |
| 84 | `PASS` | analytické synchronous seed koeficienty CLASS proti CAMB |
| 85 | `REVIEW` | vedúce NID/NIV série nemali dosť rádov na Newtonovskú transformáciu |
| 86 | `PASS` | general-synchronous K4 test-field odpoveď, `theta_c` sa smie vyvíjať |

Detaily chýb sú v `ERRATUM_77`, `ERRATUM_78`, `ERRATUM_81` a
`ERRATUM_85` v tomto adresári.

## 3. Päť kolektívnych módov — skript 79

```text
common active k*tau = 0.0016
descriptor rank     = 5
singular values     = [1.2265617445, 1.0001750630, 1.0000000389,
                       0.9998244513, 0.7039510772]
verdict              = PASS_NULL_COLLECTIVE_ACTIVE_SEEDS
```

Dominantné invariantné podpisy boli v poradí:

```text
AD  -> Weyl
CDI -> S_c_gamma
BI  -> S_b_gamma
NID -> S_nu_gamma
NIV -> V_nu_gamma
```

## 4. Dva interné módy — skript 80

```text
species-resolved seed rank = 7
max weighted source        = 4.930380657631324e-32
F_steam/F_nu               = -6092/107
```

Vedúce multipólové mocniny:

```text
internal density : [0,1,2,3,4,5]
internal velocity: [1,0,1,2,3,4]
```

Oba koeficientové rezíduá hierarchie boli presne nulové. PASS je podmienený
už registrovanou S1 definíciou: K4 priamo nekopuluje na free-streaming steam
hierarchiu.

## 5. Presný backgroundový mocninový register — skript 83

| Veličina | Očakávaná mocnina `a` | Nameraná mocnina |
|---|---:|---:|
| `lambda/E` | 2 | 1.9999971093 |
| `rho_f/rho_c` | 2.93109 | 2.9310900000 |
| `(lambda/E)(rho_f/rho_c)` | 4.93109 | 4.9310871093 |
| `rho_f/rho_r` | 3.93109 | 3.9310900000 |
| `rho_m/rho_r` | 1 | 1.0000000000 |

Presná konformná mapa splnila `a E (H0 eta)->1` s maximálnou chybou
`1.2961e-5` v auditnom okne.

## 6. Analytické CLASS seed koeficienty — skript 84

| Mód | Fit amplitúdy CAMB/CLASS | Relatívne L2 rezíduum |
|---|---:|---:|
| AD | -0.9999999998 | 3.42045e-10 |
| CDI | 1.0000001964 | 4.14148e-7 |
| BI | 1.0000000288 | 7.42422e-8 |
| NID | 1.0000106714 | 1.51552e-5 |
| NIV | 1.0000106999 | 1.52023e-5 |

Všetkých pätnásť kontrol prešlo. Porovnávali sa iba regulárne
synchronous/CDM-frame veličiny.

## 7. General-synchronous K4 test-field — skript 86

Všetky kontroly prešli. `lambda=0` absolútne rezíduá `delta_c`:

| Mód | `abs(delta_c_num-delta_c_seed)` | štartová zhoda pri `lambda=0` |
|---|---:|---:|
| AD | 7.67064e-12 | 1.31977e-15 |
| CDI | 2.47894e-11 | 2.33425e-15 |
| BI | 4.59752e-12 | 2.22358e-12 |
| NID | 2.68553e-16 | 1.44851e-16 |
| NIV | 6.99397e-14 | 1.13213e-15 |

K4 mínus nulová odpoveď bola v okne `x=-25..-14` podľa očakávania veľmi
malá. Najväčší zobrazený rozdiel bol vo fuel velocity NIV
`-8.82694e-18`; `U_c` vzniklo až pod úrovňou `1e-53`, pretože energy-frame
spätný ťah na popol obsahuje ďalší malý faktor `beta~delta*rho_f/rho_c`.

## 8. Aktuálny fyzikálny rozsudok

```text
A2-K4.3b-RG: ČIASTOČNE PREŠLA, NEUZAVRETÁ, NIE MŔTVA.
A2-K4: ŽIVÁ, 60/100 = G6.
Chýba: back-reacted Puiseux séria a spoločné 00/0i/slip/ij rezíduá.
```

