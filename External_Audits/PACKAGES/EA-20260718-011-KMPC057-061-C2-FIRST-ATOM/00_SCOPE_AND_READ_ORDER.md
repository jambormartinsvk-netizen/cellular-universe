# Scope — KMPC-057 až 061, C2 prvý atóm

- Package ID: `EA-20260718-011-KMPC057-061-C2-FIRST-ATOM`
- Route: `A1-K1 / A2-K4 / P5.3g7 / C2 / AD/k=.005/nominal`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

1. Sú PF-077 až PF-079 správne technické fail-closed smoke udalosti bez
   fyzikálneho atómu a bez JSON výsledku?
2. Oddeľuje KMPC-061 správne V1 false checks `(BI,CDI)` od historického
   S1-extended-vs-closed rozdielu `(AD,CDI,BI)` a obnovuje všetky ownery?
3. Reprodukuje official AD/`k=.005` atóm PASS pre M1/core/common/S-C0 a
   background, ale FAIL frozen tailu `3,4` pri F0 aj M3?
4. Je z toho oprávnený iba scoped REVIEW supportu `[0,2]`, nie STOP A2-K4,
   zmena prahu ani extrapolácia na zvyšných deväť C2 atómov?

## Poradie čítania

1. `EVIDENCE/001–002`: R3 protokol a frozen C1/C2/C3 kontrakt.
2. `003–010`: predregistrácie, technická diagnóza, výsledkový audit a
   error/karanténny register.
3. `011`: immutable referenčný raw výsledok.
4. `012–015`: PF-077 až PF-079 a read-only KMPC-060; 301–303 nespúšťať.
5. `016–021`: official runner, V1–V4 implementácia a stabilný harness.
6. `03_REPRODUCTION_AND_EXPECTATIONS.md`: official T2 vetva iba runner 305.

## Zmrazené kritériá

AD accepted/audit `[0,2]→[0,4]`; M1 depth 5; common `0…2`; tail iba `3,4`;
`z=1e-4,1e-2`; common `1e-8`; tail `1e-6`; absolute fallback `1e-12`;
background relative `1e-12`. Prvý non-PASS zastaví C2 poradie.

## Nonclaims

Nie T3. Bez AD `[0,4]→[0,6]`, AD `k=.15`, ostatných módov, C3 variantov,
S-M, full hierarchy, ODE/P5.4, G8/G9 alebo dát. PF história sa nereprodukuje
spustením karanténnych runnerov. `SCORE_EFFECT=NONE`; všetky release triggery
`NONE`.
