# KMPC-043 — BI M1 order-7 provenance: predregistrácia a execution ledger

**Dátum predregistrácie:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / BI_M1_ORDER7`  
**Stav:** `EXECUTED_IMMUTABLE / AUTHORITATIVE_REVIEW`  
**Identita:** `BI / k=0.05 Mpc^-1 / nominal / order=7`  
**Skóre a triggery:** `NONE`

## 1. Účel a immutable vstup

KMPC-042 ukázal, že BI support `[0,3]` nestačí, ale nevykonal `[0,7]`.
Pred ďalším support krokom musí BI samostatne preukázať, že jeho štandardný
M1 seed možno rozšíriť z order 5 na order 7 bez regresie a invariantného
rozporu.

Immutable prerequisite:
`RUN_KMPC_042_P5_3G7_BI_SUPPORT_STEP_2_03_05.json`, SHA-256
`E5F18DA4DE5A718C4448D095804F6D41FE88445A95FB99645EFBCCB48D48CA61`.

CDI KMPC-036/039 sa používa iba ako metodický vzor. CDI stav, pravá strana,
rezíduá ani korekcia nie sú BI vstupom.

## 2. Presný matematický kontrakt

BI order-7 systém sa zostaví priamo z frozen BI počiatočných constraints:

- stavy presne `11` v poradí frozen `VARS`;
- powers presne `-1…7`, spolu `9` na stav;
- full unknowns `99`, hard anchor `h[1]`, solved unknowns `98`;
- driver rows `99` plus `22` initial rows, spolu `121`;
- reduced matica `121×98`, požadovaný rank `98`;
- holdouty `Einstein_00/0i` pre všetkých 9 powers, spolu `18`.

Prahy sa nemenia:

- residual relative `1e-10`, absolute `1e-12`;
- order-5/lower regresia relative `1e-12`, absolute `1e-14`;
- anchor absolute `1e-14`;
- inverse resolved condition najmenej `1e-10`.

Order 5 sa znovu vyrieši a jeho metadata musia reprodukovať immutable
KMPC-042. Order 5 a order 7 sa porovnajú na stavových powers `-1…5` a na
background sériách. Order-7 driver/initial a oba Einsteinove holdouty sa
vyhodnotia po všetkých powers; nič sa nesmie vynechať podľa očakávania.

## 3. Rozhodovací strom

1. Technická chyba → `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`.
2. Order-5 immutable metadata, lower state alebo background regresia FAIL →
   `REVIEW_BI_M1_ORDER7_REGRESSION_DRIFT`.
3. Shape/rank/anchor/condition/state/finite, driver/initial alebo holdout FAIL
   → `REVIEW_BI_M1_ORDER7_CORE_OR_HOLDOUT_UNCLOSED`.
4. Všetko PASS → `PASS_BI_M1_ORDER7_PROVENANCE_CANDIDATE_ONLY`.

Skript neurčuje autoritatívny verdikt. Ak zlyhajú iba floor-level order-7
rezíduá, nasleduje samostatná same-matrix numerical-boundary predregistrácia
pre BI. Nesmie sa skopírovať CDI korekčný vektor. Ak prejde všetko, BI
support step 3 `[0,5]→[0,7]` sa iba odblokuje; ešte nie je vykonaný.

## 4. Prevádzkový kontrakt a nonclaims

Poradie `compile → --help → --smoke → jeden --audit`, interný limit presne
`4.8 s`, externý najviac `10 s`, atomic/exclusive immutable output.
Zakázané: refinement, high precision, zmena matice/anchoru/prahov, support
solve, `[0,7]`, NID/NIV, iné `k`/varianty, S-M, ODE, P5.4, G8/G9 a release.

## 5. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-18 | používateľ prikázal pokračovať | `AUTHORIZED` |
| 2026-07-18 | BI identita, rozmery, residual/regression prahy a strom zmrazené | `PREREGISTERED` |
| 2026-07-18 | `py_compile` nového base a runnera | `PASS` |
| 2026-07-18 | runner `--help` | `PASS` |
| 2026-07-18 | smoke vrátane wrong-mode CDI fixture a publish guardov | `PASS` |
| 2026-07-18 | jediný autorizovaný `--audit`; kanonický JSON vznikol atomicky | `TECHNICAL_PASS` |
| 2026-07-18 | nezávislá kontrola identity, hashov, ranku, regresií, 121+18 riadkov a publish guardov | `PASS_AUDIT / PHYSICS_REVIEW` |

Autoritatívny výsledok a presný zoznam otvorených riadkov je v dokumente 82.
Ďalší uzol je samostatná BI same-matrix numerical-boundary closure; tento
run sa nesmie opakovať ani použiť ako povolenie pre support `[0,7]`.
