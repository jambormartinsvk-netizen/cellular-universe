# P5.3g7-M3-FULL/R-A — technický pokus 4/10, predregistrácia

**Dátum:** 2026-07-16  
**Stav pred behom:** `PREREGISTERED / NOT_RUN`  
**Rozsah:** B1 symbolický preflight bez matice, solve alebo ODE  
**Technický counter pred behom:** `3/10`  
**Fyzikálne pokusy:** `0`  
**Skóre/hĺbka:** bez zmeny, K4 `60/100 = G6`

## Ľudský význam

Tento krok ešte nehľadá numerický seed. Overí iba to, či nový R-A základ
obsahuje presne tie stavy a rovnice, ktoré sme pred kódom odvodili, či
používa správny tlak paliva a či sa energia, hybnosť a Einsteinove
constrainty algebraicky zachovávajú. Zámerne doň vložíme aj chybné príklady:
vynechané palivo, extra stav a starý trojnásobný tlak. Preflight ich musí
odmietnuť.

Ak všetko prejde, výsledok iba uzavrie B1 implementačný kontrakt a povolí
neskorší seedový solve v tom istom fyzikálnom suffixe. Ak niečo neprejde,
zapíše sa technická alebo formulačná príčina; K4 tým automaticky neumiera.

## Artefakty

```text
scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py
scripts/264_script_KMPC_025_P5_3g7_m3_full_ra_b1_preflight.py
scripts/results/k_mpc_005/RUN_KMPC_025_P5_3G7_M3_FULL_RA_B1_PREFLIGHT.json
```

## Zmrazené zdroje

| Zdroj | SHA-256 | Použitý rozsah |
|---|---|---|
| script 88 conservation ledger | `0F13DA6CE761CFEF99909B492E30CF5ED751F56A555594334729330ED4888364` | synchronné fuel/ash rows, tlak, total energy/momentum |
| M1 hard-anchor V2 | `5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455` | iba exact column elimination helper; legacy M3 pressure sa neimportuje |
| M1 source map doc 26 | `7C927999F0D5BAECD0E45E52DFF760FA17DC0A48A3799242D147AEDE4228999B` | nezávislá štandardná amplitúda/gauge mapa |

S-C zostáva iba podmieneným matematickým splitom podľa dokumentu 27:
neutríno a para majú rovnakú collisionless bázu a ich vážený súčet sa musí
rovnať agregovanému sektoru. Tento preflight neodvodzuje pôvod pary.

## Povinná dátová schéma

Výstup musí obsahovať:

```text
test, run_id, scope, runtime_seconds, internal_limit_seconds,
physics_evolution_executed=false, matrix_solve_executed=false,
score_effect=0, source_hashes, conventions,
state_manifest, driver_manifest, holdout_manifest,
coefficient_support, exact_residuals, negative_fixtures, checks,
execution_verdict.
```

Ordered state má presne 13 položiek a driver presne 13 riadkov podľa
dokumentu 32. Holdout je presne `(Einstein_00, Einstein_0i)` a nesmie byť
podmnožinou drivera.

## Očakávané presné výsledky

| Kontrola | Očakávanie/PASS | Ak neprejde |
|---|---|---|
| k-cancel | presná symbolická nula | `STOP_FORMULA_BACKGROUND_K_DEPENDENCE` |
| state/driver parita | exact ordered `13/13` | `SCRIPT_IMPLEMENTATION_FAILURE`; solve zakázaný |
| pressure formula | presne `delta_f+(2-delta)(3delta+gamma)U_f` | `STOP_FORMULA_PRESSURE` |
| legacy pressure fixture | musí byť nenulový a presne o faktorovú chybu odlišný | fail-closed technická chyba testu |
| total energy product rule | presná nula | `STOP_FORMULA_CONSERVATION` |
| total momentum product rule | presná nula | `STOP_FORMULA_CONSERVATION` |
| Bianchi `C00` propagation | presná nula | `STOP_FORMULA_BIANCHI` |
| Bianchi `C0i` propagation | presná nula | `STOP_FORMULA_BIANCHI` |
| coefficient okná | presné AD/CDI/BI/NID/NIV a `m_max` z dokumentu 32 | technický STOP manifestu |
| negatívne state fixtures | každý chybný tuple odmietnutý | technický STOP parity guardu |
| zakázaný `fuel[1]` v `Phi^1` source | odmietnutý | `STOP_FORMULA_ORDER_MIXING` |
| S-C vážený split | presná nula, označený conditional | STOP implementácie splitu; nie fyzikálny verdict pary |

Všetky algebraické rezíduá musia byť presne nula po `sympy.simplify`, nie
iba menšie než numerická tolerancia.

## Negatívne fixtures

Povinne sa odmietnu:

1. stav bez `delta_f`;
2. stav bez `U_f`;
3. stav s extra `fake_state`;
4. rovnaká množina v inom poradí;
5. driver bez fuel continuity alebo Euler;
6. driver obsahujúci `Einstein_00` alebo `Einstein_0i`;
7. starý pressure výraz z PF-063;
8. lokálny count bez exact-set porovnania;
9. `Omega_f[1]*fuel[1]` vložený do `Phi^1` stressu;
10. chýbajúci explicitný lower regular fuel coefficient.

## Prevádzkové kroky a limity

Každý Python proces sa spustí samostatne priamym
`C:\Python311\python.exe`, s vonkajším timeoutom najviac 10 s:

1. `py_compile` base;
2. `py_compile` runner;
3. `--help`;
4. `--smoke --max-runtime-seconds 2`;
5. plný preflight `--max-runtime-seconds 5 --output ...`.

Každý krok patrí do jedného technického balíka `4/10`. Prvé zlyhanie
zastaví ďalšie fázy a zapíše presný dôvod. Úspech je iba

```text
PASS_R_A_B1_PREFLIGHT_ONLY
```

Nie je to seed PASS, P5.3 PASS, G7/G8 PASS ani fyzikálny pokus.
