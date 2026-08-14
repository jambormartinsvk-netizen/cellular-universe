# A2-K4 / C7.7c / K7c.3a — predregistrácia presného profilu lineárneho operátora

Dátum: 2026-07-15  
Vstup: skript 180 `TIMEOUT_UNCLOSED` na 200 000 RHS volaniach

## Rozsah

Iba NID/deep pri `x=-25`, bez ODE. Použije sa ten istý HP seed, RHS a envelope škála ako v 180.

## Metóda

Projektovaný systém je lineárny v stave pri fixnom backgrounde. Operátor sa preto zostaví presne stĺpcovo:

```text
A[:,j] = f(x,e_j) - f(x,0)
```

Nejde o konečnú diferenciu: nepoužíva sa malý krok, centrálne odčítanie ani FD condition proxy. Škálovaný operátor je presná similarity transformácia

```text
A_w = diag(1/S) A diag(S).
```

## Povinný výstup

- počiatočný fyzikálny a normalizovaný RHS pre 13 zložiek;
- fyzikálny a škálovaný spektrálny polomer;
- maximum absolútneho prvku oboch operátorov;
- desať najväčších škálovaných couplingov s menami;
- kontrola `rho(A_w)=rho(A)` do `1e-10` relatívne;
- rekonštrukcia počiatočného RHS cez `A*y` do `1e-12` škálovane;
- zdrojový a celkový časový limit.

## Rozhodovanie

- Ak spektrá súhlasia, ale škálované couplingy alebo normalizovaný RHS sú extrémne, timeout sa pripíše error-control súradniciam a ďalšia podkoľaj musí zmeniť iba integračnú metriku/solver podľa zistenia.
- Ak sa spektrá alebo `A*y` nezhodujú, zomiera táto diagnostická implementácia a evolúcia sa nespustí.
- Tento krok nemení skóre ani fyzikálny stav K4.
