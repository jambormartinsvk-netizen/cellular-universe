# KMPC-035 — CDI support step 2 `[0,3]→[0,5]` predregistrácia

**Dátum:** 2026-07-16  
**Stav:** `PREREGISTERED / NO PYTHON PROCESS RUN`  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / CDI_SUPPORT_STEP_2`  
**Názvový guard:** `NOT_GLOBAL_C2_FOURIER_GATE`  
**K4/P5:** `LIVE / 60/100`; `3.5/6`; bez automatickej zmeny

## 1. Jediná otázka balíka

KMPC-034 ukázal, že support `[0,1]` nestačí iba pre zmrazený
`CDI / k=0.05 / nominal` tail test na dvoch zaregistrovaných plochách.
Nedokázal, či už `[0,3]` stačí. KMPC-035 preto testuje iba:

```text
regression support       [0,1]
accepted-candidate base  [0,3]
audit support            [0,5]
```

Fyzika, `k=0.05 Mpc^-1`, CDI mód, `nominal` vstupy, normalizácia,
constrainty, surfaces a prahy sa nemenia.

## 2. Povinná proveniencia a regression gate

Pred interpretáciou sa načíta immutable KMPC-034:

```text
RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json
SHA-256 37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20
```

Novo vypočítané koeficienty supportov `[0,1]` a `[0,3]` sa porovnajú s
KMPC-034 pre F0 aj všetkých 13 M3 stavov. PASS vyžaduje pre každý
koeficient:

```text
abs(new-old) <= max(1e-14, 1e-12*max(abs(new),abs(old))).
```

Nezhoda znamená `REVIEW_CDI_SUPPORT_STEP_2_REGRESSION_OR_FORMULA_DRIFT`; chvost sa
nesmie fyzikálne interpretovať.

## 3. Support/count a scope guard

Počty sa odvodia z počtu mocnín, nie iba prepíšu:

| support | powers | F0 `2*N` | M3 `13*N` |
|---|---:|---:|---:|
| `[0,1]` | 2 | 4 | 26 |
| `[0,3]` | 4 | 8 | 52 |
| `[0,5]` | 6 | 12 | 78 |

Audit support sa odvodí ako `candidate.hi+2=5`. Negatívny fixture s
`hi+3` sa musí odmietnuť. Dočasná zmena shape guardu pre `[0,5]` sa musí
po solve obnoviť aj pri výnimke.

## 4. Core brány každého supportu

Pre `[0,1]`, `[0,3]` aj `[0,5]` musia prejsť:

1. F0 rank, driver a leading postcheck;
2. M3 plná hodnosť a driver;
3. nezávislé `Einstein_00/0i` holdouty;
4. forbidden earlier layers a forbidden stress;
5. production contract;
6. `U_c` lower-order regularita `<=1e-12`;
7. konečnosť všetkých koeficientov;
8. rovnaký frozen B1/contract/TCA0 zdroj;
9. podmienený S-C0 lower-moment mapping guard.

Holdout používa spoločný equation engine; je nezávislý od fitu, nie od
možnej spoločnej formulačnej chyby.

## 5. Dve rozdielne konvergenčné brány

### 5.1 Common coefficients

Medzi `[0,3]` a `[0,5]` sa porovnajú všetky spoločné powers `0..3`
osobitne pre F0 a M3. Ostávajú staré prahy:

```text
relative <= 1e-8
absolute fallback <= 1e-12.
```

### 5.2 Čistý vynechaný remainder

Z koeficientov supportu `[0,5]`:

```text
base            = sum(j=1..3) c5[j] z^j
signed_tail     = c5[4] z^4 + c5[5] z^5            # diagnostika
tail_envelope   = |c5[4]| z^4 + |c5[5]| z^5       # autoritatívna brána
full            = base + signed_tail.
```

Na `z=1e-4` a `z=1e-2` platí rovnaký branch ako v KMPC-034:

- ak `max(|base|,|full|)>1e-12`, potom `tail_envelope/scale <=1e-6`;
- inak `tail_envelope<=1e-12`;
- všetko musí byť konečné.

Rovnaká definícia sa vyhodnotí oddelene pre dvojstavovú F0 vežu aj pre
13-stavový M3 systém. Autoritatívny tail gate prejde iba vtedy, keď
prejdú oba; výstup musí ukázať ich výsledky osobitne.

Signed tail a pomer zrušenia signed/envelope sa exportujú iba diagnosticky,
aby sa veľké členy `j=4,5` nemohli skryť vzájomnou kanceláciou. Pomer
zmenšenia tailu `2,3 -> 4,5` sa tiež exportuje iba diagnosticky. Nesmie
nahradiť absolútnu bránu ani zmeniť prah.

## 6. Rozhodovací strom

| Výsledok | Kandidát, nie automatický verdikt | Ďalší postup |
|---|---|---|
| regression/core/common/tail PASS | `PASS_CDI_SUPPORT_STEP_2_SUPPORT_03_ADEQUATE_CANDIDATE` | tri read-only audity; main môže scoped prijať `[0,3]` |
| regression FAIL | `REVIEW_CDI_SUPPORT_STEP_2_REGRESSION_OR_FORMULA_DRIFT` | audit zdrojov/normalizácie; tail neinterpretovať |
| core FAIL | `REVIEW_CDI_SUPPORT_STEP_2_CORE_GATE_UNCLOSED` | formula/sign/conditioning audit |
| common FAIL | `REVIEW_CDI_SUPPORT_STEP_2_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED` | conditioning/refinement bez zmeny prahov |
| iba tail FAIL | `REVIEW_CDI_SUPPORT_STEP_2_SUPPORT_03_REMAINDER_UNCLOSED` | zastaviť balík; `[0,5]→[0,7]` iba po novom audite a predregistrácii |

Žiadna vetva sama neudeľuje fyzikálny STOP K4.

## 7. Limity a nonclaims

Jeden proces má interný limit `4.8 s` a vonkajší `10 s`. Smoke, compile a
help nie sú vecné výsledky. Vecný interpretovateľný výsledok resetuje
aktívne technické počítadlo, aj keď je REVIEW.

Balík netestuje BI/NID/NIV, iné `k`/varianty, S-M, fyzický pôvod pary,
species-resolved `F_l>=3`, finite opacity, ODE, G8/G9, CLASS, CMB, BBN,
`S8/H0`, skóre ani release.

```text
SCORE_EFFECT=NONE
RELEASE_TRIGGER=NONE
ZENODO_TRIGGER=NONE
PREDICTION_TABLE_EFFECT=NONE
```

## 8. Zdroje na zmrazenie pred prvým Python procesom

- nový base: `scripts/baseScripts/p5_general_synchronous/cdi_support_ladder.py`;
- nový runner: `scripts/279_script_KMPC_035_P5_3g7_CDI_C2_support_03_05_ladder.py`;
- immutable výsledok:
  `scripts/results/k_mpc_005/RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json`.

## 9. Zmrazené hashe pred prvým Python procesom

| Zdroj | SHA-256 |
|---|---|
| `cdi_support_ladder.py` | `A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068` |
| runner 279 | `09F86A2A6E8BA81F4F41C73722BC40264888D1EF45BB4016F223A5E2C76649E3` |

Runner navyše fail-closed porovná presnú množinu jedenástich base hashov.
Prvý Python proces je zakázaný, kým tri read-only preflight audity
nepotvrdia rozsah, implementáciu a registračné záznamy.

## 10. Zapracované read-only preflight opravy pred Python procesom

- autoritatívny tail používa cancellation-safe absolute-term envelope;
- identita je `GLOBAL_C1 / CDI_SUPPORT_STEP_2`, nie Fourier C2;
- runner hashuje všetkých 11 zdrojov samostatne ešte pred importom;
- povolená je iba kanonická výstupná cesta a presný limit `4.8 s`;
- smoke vyvolá deterministickú výnimku po zmene shape registry a overí
  úplnú obnovu cez `finally`;
- nonfinite diagnostika sa potlačí na `None` s explicitným statusom;
- hlavný aj failure JSON sa zapisujú cez fsync + atómový hard-link publish,
  takže čiastočný temp súbor nemôže predstierať immutable výsledok.
