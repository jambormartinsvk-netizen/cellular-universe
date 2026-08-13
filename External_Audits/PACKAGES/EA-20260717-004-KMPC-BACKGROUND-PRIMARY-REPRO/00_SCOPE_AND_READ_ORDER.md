# Scope — primary-source follow-up auditu K_MPC backgroundu

- Package ID: `EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO`
- Predecessor: `EA-20260717-001-KMPC-BACKGROUND-LINEAGE`
- Route: `A1-K1 / A2-K4 / P4→P5`
- Audit mode: primárny formula-lineage + reprodukcia troch malých behov
- Target tier: `T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

Potvrdia primárny historický runner, nezávislý symbolický audit a dva
numerické backgroundové behy záver prvého externého auditu, že:

1. fixed `K_MPC=0.05` preniklo do starého K7 denominatoru cez `z^p`;
2. tento denominator preto nie je univerzálny FLRW background;
3. `A_f` je odvodené z konkrétneho zmrazeného A1 closure pri `lambda=0.15`,
   nie nový nezávislý fit;
4. normalizovaný skrátený K7 rad je skorá aproximácia a pri
   `a≈0.70896` stráca fyzikálnu prípustnosť ako plný background?

## Poradie čítania

1. `001–002`: pôvodný externý audit a jeho vyhodnotenie.
2. `003–006`: primárny historický runner, predchodca a symbolický audit.
3. `007–010`: expectation, raw výsledok, audit a formula provenance.
4. `011–014`: A1→`A_f` runner, base, raw výsledok a audit.
5. `015–017`: exact-A1 verzus truncated-K7 runner, raw výsledok a audit.
6. `03_REPRODUCTION_AND_EXPECTATIONS.md`: tri nezávislé reprodukcie.

## Zmrazené hranice

- Žiadna zmena rovníc, parametrov alebo tolerancií.
- Symbolický STOP runnera 224 má očakávaný procesový `exit 1`; nejde o
  technický pád.
- `A_f` je parameter-bookkeeping výsledok podmienený A1 vstupmi, nie
  mikrofyzikálne odvodená konštanta.
- STOP skráteného radu nezabíja exact-A1 background ani celú A2-K4.

## Nonclaims

Balík neauditue CLASS/CAMB, CMB/S8, úplné perturbácie, zámer autora pri
voľbe čísla `0.05` ani celý registrovaný balík v3.17.

## Požadovaný výstup

Vytvor formula ledger s presnými riadkami a označ každé hlavné tvrdenie
`OBSERVED_IN_PRIMARY`, `INDEPENDENTLY_RECOMPUTED`,
`INFERRED_FROM_PROJECT_DOCS` alebo `CONTEXT_ONLY`. Uveď, či sa dôkazová
úroveň pôvodného auditu zvýšila z `PASS_MAPY` na reprodukovateľný formula/
calculation audit a ktoré otázky zostávajú otvorené.
