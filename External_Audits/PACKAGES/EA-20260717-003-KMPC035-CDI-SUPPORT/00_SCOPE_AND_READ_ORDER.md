# Scope — KMPC-035, CDI support 0.3–0.5

- Package ID: `EA-20260717-003-KMPC035-CDI-SUPPORT`
- Route: `A1-K1 / A2-K4 / P5/P5.3g7`
- Audit mode: forenzný algebraický a dependency-closure audit
- Package revision: `R2_PRE_DELIVERY_REFREEZE`; R1 nebola odovzdaná auditorovi
- Target evidence tier: `T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP`
- Autorita: externý auditor odporúča; projektový verdikt nemení

## Presná otázka

Je tvrdenie KMPC-035 o CDI `core/common` podpore v rozsahu `0.3–0.5`
správne, vrátane dependency closure? Je zachované obmedzenie, že remainder
`[0,3]` zostáva `REVIEW` a nebol ticho povýšený na globálny PASS?

Historický token `C2` v názve balíka neznamená globálny Fourierov koeficient
`C2`.

## Poradie čítania

1. `001` až `005`: pravidlá, route a scope.
2. `006` až `008`: preregistrácia, execution a výsledný audit.
3. `009` až `022`: runner, raw JSON, úplný base dependency closure a
   technický ledger.
4. `03_REPRODUCTION_AND_EXPECTATIONS.md`: samostatná reprodukcia v `REPRO/`.

## Zmrazené kritériá

- Core/common výsledok sa nesmie extrapolovať mimo deklarovaného supportu.
- `[0,3]` remainder je `REVIEW`, nie implicitný PASS.
- Všetky zdrojové závislosti v JSON musia byť prítomné a hashovo zhodné.

## Nonclaims

Balík neuzatvára support step 3 `[0,5] -> [0,7]`, nerieši M1 order-7
precision a nerozhoduje o celej A2-K4 koľaji.

## Požadovaný výstup

Urči, či je support dôkaz úplný v deklarovanom lokálnom scope, ktoré
tvrdenie ostáva otvorené a či dependency chain pred ďalším krokom naozaj
zlyháva uzavreto. Každé hlavné tvrdenie označ `OBSERVED_IN_PRIMARY`,
`INDEPENDENTLY_RECOMPUTED`, `INFERRED_FROM_PROJECT_DOCS` alebo
`CONTEXT_ONLY`.
