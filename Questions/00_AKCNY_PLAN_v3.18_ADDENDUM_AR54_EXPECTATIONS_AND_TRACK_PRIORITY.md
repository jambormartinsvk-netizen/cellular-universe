# Akčný plán v3.18 — AR54, očakávania a priorita koľají

Dátum: 2026-07-15

## Povinný workflow každého ďalšieho skriptu

1. vytvoriť vyplnený pre-run MD;
2. označiť očakávanie `ANALYTIC`, `REGRESSION` alebo `EXPLORATORY`;
3. zmraziť vstupy, prahy, tolerancie a timeouty;
4. vykonať limitovaný `py_compile`, CLI a JSON smoke-test;
5. spustiť výpočet s interným aj externým limitom;
6. doplniť tabuľku pozorovaných absolútnych a normalizovaných odchýlok;
7. ak treba očakávanie zmeniť, zachovať pôvodné, zapísať dôvod a použiť zmenu až na nový beh/podkoľaj.

## Priorita

- P0: fail-closed K7b regresia podľa `A2_K4_C7_7C_NEXT_RUN_PREREGISTERED_EXPECTATIONS.md`;
- P1: čistý RK4 regresný prepis a potvrdenie, že starý REVIEW sa reprodukuje;
- P2: nový limitovaný `M'` ledger;
- P3: iba podľa P2 založiť fsum alebo algebraickú/high-precision podkoľaj;
- breadth návrat ku K7/K8/K9/K11/K12 iba pri pripravenom novom kerneli alebo po fyzikálnej smrti K4.

Žiadny P0/P1 audit nepridáva body. Aktuálna hĺbka zostáva `66.5/100`.
