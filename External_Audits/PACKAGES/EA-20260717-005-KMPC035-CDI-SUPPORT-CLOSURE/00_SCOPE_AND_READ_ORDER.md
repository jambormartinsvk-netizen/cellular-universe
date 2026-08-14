# Scope — KMPC-035 external reproduction closure

- Package ID: `EA-20260717-005-KMPC035-CDI-SUPPORT-CLOSURE`
- Predecessor: `EA-20260717-003-KMPC035-CDI-SUPPORT`
- Route: `A1-K1 / A2-K4 / P5/P5.3g7`
- Audit mode: dependency-closure, official reproduction and technical-hygiene follow-up
- Package state: `SEALED_READY_FOR_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

1. Odstraňuje priloženie immutable KMPC-034 JSON technický blocker F1 a
   prejdú teraz predpísané smoke aj official audit vetvy bez obídenia
   guardov?
2. Reprodukuje external platforma scoped KMPC-035 pattern: core/common
   stabilita `[0,3]↔[0,5]` a remainder `REVIEW`, vrátane presných dvoch
   tail failov pri `z=1e-2`?
3. Zostáva same-machine prah `1e-12` nezmenený a je nová tolerancia `1e-9`
   použitá iba ako cross-platform diagnostika s `verdict_effect=NONE`?
4. Zanechá nový publish wrapper po simulovanej kolízii nezmenený cieľ a
   nulový počet vlastných temp súborov?

## Poradie čítania

1. `001–004`: pravidlo hypotéz, protokol R3, externý nález a hlavný posudok.
2. `005–009`: pôvodná preregistrácia, execution, výsledok, runner a direct base.
3. `010–011`: chýbajúci runtime prerequisite a reference raw výsledok.
4. `012–014`: error ledger, preventívne vzory a nový package-local runner.
5. `015–024`: úplný import closure base modulov.
6. `04_RUNTIME_DEPENDENCY_MAP.tsv`: presná runtime cesta každého vstupu.
7. `03_REPRODUCTION_AND_EXPECTATIONS.md`: oficiálne príkazy a očakávania.

## Zmrazené autoritatívne prahy

Pôvodné prahy sa nemenia:

```text
regression relative/absolute = 1e-12 / 1e-14
common relative/absolute     = 1e-8  / 1e-12
tail relative                = 1e-6
tail absolute norm/tolerance = 1e-12 / 1e-12
```

Nový cross-platform pár `1e-9 / 1e-13` je predregistrovaný iba ako
`DIAGNOSTIC_ONLY_AFTER_EXTERNAL_FINDING_F2`. Nemôže meniť pôvodný candidate
interpretation ani projektový verdikt.

## Opravy oproti balíku 003

- KMPC-034 JSON je v `EVIDENCE/010` aj presnej runtime ceste `REPRO/`.
- Runtime vstupy majú samostatnú strojovú mapu a hash guard.
- Runner exportuje Python, knižnice, platformu a NumPy/BLAS config.
- Immutable publish používa cleanup vo `finally` a race/collision fixture.
- Absolute-branch stavy dostanú would-be relative diagnostiku.
- Šesťbodový z-scan je iba diagnostika lokálneho dvojčlenného remainderu.
- Official audit a cross-platform comparison sú oddelené polia.

## Nonclaims

Balík nie je T3: používa rovnaký equation engine a nevytvára druhú
nezávislú fyzikálnu implementáciu. Neuzatvára nekonečný Puiseuxov rad,
support step 3, KMPC-036 precision floor, BI/NID/NIV, iné `k`/varianty,
S-M, full hierarchy, ODE, G8/G9, CLASS, CMB, BBN ani `S8/H0`.

Predikcia externého auditora, že support `[0,5]` pravdepodobne prejde, je
testovateľná hypotéza bez verdict effect. Support step 3 zostáva blokovaný
až do autoritatívneho closure KMPC-036.

```text
SCORE_EFFECT=NONE
PREDICTION_TABLE_EFFECT=NONE
RELEASE_TRIGGER=NONE
ZENODO_TRIGGER=NONE
```

## Požadovaný výstup

Auditor musí oddeliť official smoke, official audit a každú odchýlku;
uviesť príkazy, exit codes, wall times, generated JSON SHA-256, prostredie,
najvyšší tier a neautoritatívne odporúčanie. Každé hlavné tvrdenie označí
predpísaným tagom dôkazu.
