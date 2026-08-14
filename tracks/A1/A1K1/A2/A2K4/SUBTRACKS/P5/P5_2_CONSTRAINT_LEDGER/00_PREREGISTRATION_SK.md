# P5.2 — predregistrácia algebraického constraint ledgeru

**Koľaj:** `A1-K1 → A2-K4 → P5 → P5.2`  
**Stav pred behom:** `PRIPRAVENÉ; bez ODE a bez skóre`  
**Skript:** `scripts/241_script_KMPC_004_P5_2_full_constraint_ledger.py`  
**Vnútorný / vonkajší limit:** 5 s / 10 s

## Cieľ

Overiť, že nový plný species-first ledger zapisuje `00`, `0i`, trace a
traceless Einsteinove constrainty bez vypadnutia `U_c`, `U_b` alebo
palivovej hybnosti. Porovnáva sa algebraický tvar BR2 90 s exact-A1/P5
premennými, nie stará projektovaná K7 báza.

## Povinné kontroly

1. plná hybnosť obsahuje samostatne CDM `X_c U_c`, palivo `delta X_f U_f`,
   baryóny `X_b U_b`, fotóny a voľne prúdiace zložky;
2. `00` a `0i` constraint majú po dosadení svojich explicitných
   rekonštrukcií presnú algebraickú nulu;
3. trace a traceless tvar majú samostatné rezíduá a ich rekonštrukcie sú
   presné nuly; nesmú sa zlúčiť do jedného testu;
4. energy- a momentum-product ledger má správne znamienka podľa BR2 90;
5. `gamma→0` odstráni transfer z backgroundu aj z `U_c`/`U_f` Eulerových
   couplingov; `U_b` a `U_gamma` ostanú oddelené cez symbolický slip.

## Očakávaný výsledok

Očakávajú sa presné sympy nuly a prítomnosť všetkých povinných symbolov.
PASS znamená iba **algebraické uzavretie zápisu** a zachovanie stavového
priestoru. Neznamená nezávislé dynamické zachovanie constraintov, regulárne
seedy, stabilnú ODE, úplnú Thomsonovu fyziku, plnú hierarchiu ani dáta.

## STOP a ďalší krok

Chýbajúca hybnosť, opačné znamienko alebo nenulový algebraický zvyšok je
STOP P5 implementácie pred ODE. Pri PASS sa otvorí P5.3 seed ledger; P5.4
evolúcia zostáva zakázaná, kým P5.3 neprejde.

## Korekcia po prvom behu

Prvý immutable beh `RUN_KMPC_004_P5_2_FULL_CONSTRAINT_LEDGER.json` zastal
za 0.328 s iba na kontrole slipu. PF-041: test porovnal nezávislý symbol
`Slip` s rovnosťou `Slip=U_gamma-U_b` bez dosadenia definície, preto dostal
očakávaný výraz `Slip+U_b-U_gamma` namiesto nuly. Všetky ostatné kontroly
prešli. Oprava nahrádza iba tento test explicitným dosadením definície a
samostatne kontroluje, že `U_gamma` a `U_b` ostávajú rôzne symboly. Fyzika,
brány, rozsah ani prahy sa nemenia; nový výstup bude `..._RERUN1.json`.
