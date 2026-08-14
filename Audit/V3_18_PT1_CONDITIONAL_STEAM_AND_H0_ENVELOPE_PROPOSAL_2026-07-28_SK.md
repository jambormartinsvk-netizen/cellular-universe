# Návrh podmieneného PT1 rozsahu pary, `N_eff` a `H0` pre v3.18

**Dátum:** 2026-07-28  
**Stav:** `RELEASE_WORDING_PROPOSAL / NO_PT2 / NO_NEW_PREDICTION`  
**Rozsah:** iba bezpečné ohraničenie historického termálneho scenára  
**Skóre/hĺbka:** bez zmeny

## 1. Rozsudok

Pre `Delta N_eff`, `N_eff`, teplotu reliktu a jeho termálny frekvenčný
vrchol možno uviesť jeden explicitne podmienený sensitivity envelope.
Nesmie sa nazvať odvodeným intervalom teórie, pretože steam source, exit a
reheating ešte nie sú odvodené.

Pre `H0` dnes nemožno poctivo uviesť numerický interval. Existuje iba
historický backgroundový bod s parou `H0 približne 66.37 km/s/Mpc`; nulový
parný endpoint nebol rovnakou zmrazenou pipeline prepočítaný.

## 2. Podmienený parný envelope

Ak sa pre release ako horný sensitivity benchmark zmrazí historický scenár
dvoch termalizovaných bezhmotných gravitačných stupňov odpojených pri
`g_*s=106.75`, možno používať:

```text
0 <= Delta N_eff <= 0.0535
3.046 <= N_eff <= 3.0995
```

Toto nie je fyzikálne odvodená horná hranica všetkých možných steam
mechanizmov. Je to ohraničený interval medzi steam-null a historickým
legacy benchmarkom, určený na citlivostný audit v3.18.

## 3. Termálne pozadie

Pre dva bezhmotné bozónové helicity a termálne Planckovo spektrum platí

```text
Delta N_eff = (8/7) (T_g/T_nu)^4,
T_g(Delta) = 0.905 K * (Delta/0.0535)^(1/4),
nu_peak(Delta) = 53 GHz * (Delta/0.0535)^(1/4).
```

Pre zvolený sensitivity envelope preto:

```text
0 <= T_g <= 0.905 K,
0 < nu_peak <= približne 53 GHz pre nenulový termálny relikt.
```

Pri `Delta N_eff=0` relikt neexistuje, takže frekvenčný vrchol je
`NOT APPLICABLE`, nie fyzický vrchol `0 GHz`.

Teplota a frekvencia nie sú dve nezávislé predikcie. Sú algebraickým
prepisom toho istého zvoleného `Delta N_eff` pri termálnom predpoklade.

## 4. `H0`

Aktuálny korpus podporuje iba tvrdenie:

```text
H0 = 66.37 km/s/Mpc
STATUS = LEGACY_CONDITIONAL_BACKGROUND_POINT
NOT = full CMB/BAO/SN/RSD likelihood prediction
```

Bez výsledku pri `Delta N_eff=0` neexistujú dve hranice intervalu. Rozsah
napríklad `66.x–66.4` by bol dnes iba odhad a nesmie vstúpiť do predikčnej
tabuľky.

Publikačne bezpečné znenie pred PT2 je:

> `H0`: historický podmienený backgroundový bod `66.37 km/s/Mpc`; rozsah po
> odstránení legacy steam normalizácie je v prepočte a zatiaľ nie je
> dostupný.

## 5. Najmenší výpočet potrebný pre `H0` sensitivity interval

Samostatný predregistrovaný backgroundový audit má použiť minimálne tri
zmrazené body:

```text
Delta N_eff = 0
Delta N_eff = 0.02675
Delta N_eff = 0.0535
```

Pri všetkých bodoch sa zachovajú rovnaké `delta`, `lambda`, hustotné
definície, jednotky, backgroundová rovnice a kalibračný protokol. Výstup má
uviesť `H0`, historicky skutočne počítané `r_s(z_star)`, `D_M`,
`theta_*`/použitú kotvu a zmenu voči steam-null. Nesmie refitovať ďalší
parameter s cieľom trafiť konkrétne `H0`.

Výsledok bude iba `THREE_POINT_LEGACY_ANCHOR_SENSITIVITY`, kým neprejdú
A2/P5.4/G8 a plný likelihood. Tri body samy nedokazujú spojitý envelope ani
monotónnosť. Až potom môže vzniknúť PT2 alebo fyzikálny predikčný interval.

### Changelog po lineage audite 2026-07-28

Pôvodné slovo `r_d` bolo neskorším auditom obmedzené: skripty 08/09/17
integrujú po pevné `z_star=1089.9`, a teda počítajú `r_s(z_star)`, nie
drag-epoch `r_d`. Zároveň sa názov `BACKGROUND_SENSITIVITY_ENVELOPE`
obmedzuje na trojbodovú sampled citlivosť. Historická kotva je syntetická
flat-ΛCDM kotva vytvorená z `h=0.673`; nejde o priamo načítané meranie.

## 6. Odporúčané riadky pre v3.18-DOC/ERRATUM

| Veličina | Bezpečný zápis vo v3.18 | Dôkazová trieda |
|---|---|---|
| `Delta N_eff` | `0–0.0535` iba ako steam-null až legacy sensitivity envelope | `E3/CONDITIONAL`, nie predikcia |
| `N_eff` | `3.046–3.0995` v tom istom envelope | algebraický prepis |
| `T_g` | `0–0.905 K` pod termálnym predpokladom | podmienený prepis `Delta N_eff` |
| `nu_peak` | pri relikte `0–53 GHz`; pri nulovom relikte `N/A` | podmienený termálny prepis |
| `H0` | bod `66.37 km/s/Mpc`, interval `NOT YET AVAILABLE` | legacy background result; impact audit open |

## 7. Nonclaims

- Horné `0.0535` nie je odvodené maximum všetkých fyzikálnych steam
  mechanizmov.
- Nulový endpoint nie je tvrdenie, že teória predpovedá nulovú paru.
- Interval nie je posterior, confidence interval ani likelihood constraint.
- Teplota a frekvencia nie sú nezávislé potvrdenia.
- `H0=66.37` nie je plný kozmologický fit.
- Nevznikol PT2 ani release GO.

## 8. Odhad výpočtovej náročnosti

Odhad je predbežný, pretože trojbodový nástupca ešte nemá zmrazený runner
ani nameraný benchmark. Historická pipeline používa iba jednorozmerné
kvadratúry, krátke iterácie backgroundu a približne 3500-bodovú rastovú
mriežku; nejde ešte o plnú Boltzmannovu hierarchiu ani likelihood sampling.

Po autorizácii sa pre minimálny trojbodový sensitivity audit očakáva:

```text
smoke a kontraktové kontroly:             < 10 s na proces
1 backgroundový bod:                      približne 5–30 s
3 frozen body bez refinements:             približne 15–90 s
konvergencia, nulový limit a opakovania:   približne 1–5 min spolu
```

Bezpečný prvý externý limit má byť `60 s` na samostatný segment, s kontrolou
najneskôr každých `10 s`; dlhší výpočet sa rozdelí na checkpointované body,
nie na jeden neobmedzený proces. Príprava predregistrácie, statický audit,
kontrola výstupov a nezávislý posudok pravdepodobne zaberú viac času než
samotná numerika: orientačne `30–90 min` práce hlavného workflowu, pri
náleze technickej chyby alebo fyzikálneho blockeru dlhšie.

Tento odhad sa nevzťahuje na publikovateľnú predikciu. P5.4, plný G8
Boltzmann/recombination convergence balík a G9 likelihood môžu vyžadovať
hodiny až desiatky hodín strojového času podľa počtu módov, `lmax`,
refinementov a samplerov. Pred ich implementáciou nemožno uviesť spoľahlivý
užší runtime interval.

## 9. Procesný výkaz

```text
TASK_ID: V3.18-PT1-CONDITIONAL-ENVELOPE-PROPOSAL-20260728
ROLE: main_orchestrator_read_only_assessment
FILES_CHANGED: Audit/V3_18_PT1_CONDITIONAL_STEAM_AND_H0_ENVELOPE_PROPOSAL_2026-07-28_SK.md
PYTHON_PROCESSES: 0
LIVE_SCIENTIFIC_ARTIFACTS: 0
LIVE_RELEASE_AUDIT_ARTIFACTS: 1
LIVE_CENTRAL_REGISTERS_UPDATED: 0
TOTAL_FILES_CHANGED: 1
AUDIT_PACKAGE_COPIES: 0
NONCLAIMS: no PT2, prediction, score, depth or RUN_AUTHORIZED change
```
