# Scope — KMPC-036, order-7 driver precision

- Package ID: `EA-20260717-002-KMPC036-ORDER7-PRECISION`
- Route: `A1-K1 / A2-K4 / P5/P5.3g7`
- Audit mode: forenzný numerický a formula-provenance audit
- Package revision: `R3_REFREEZE_AFTER_EXTERNAL_TECHNICAL_STOP`
- Predchádzajúci stav: R2 bol externe auditovaný; oficiálna `--audit` cesta
  skončila technickým STOP-om pre chýbajúci KMPC-035 prerequisite.
- Target evidence tier: `T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP`
- Autorita: externý auditor odporúča; projektový verdikt nemení

## Presná otázka

Sú tri neprejdené order-7 driver riadky v KMPC-036 dôkazom chyby vzorca,
chyby implementácie alebo iba float64 precision floor? Bol aktuálny
`REVIEW` aplikovaný podľa zmrazeného prahu bez post-hoc zmeny?

## Poradie čítania

1. `001` až `005`: pravidlá, aktuálna route a zmrazený scope.
2. `006` až `008`: preregistrácia, execution ledger a výsledný audit.
3. `009` až `014`: runner, raw JSON, base dependency closure a technický
   ledger.
4. `015`: presný raw prerequisite KMPC-035, ktorý runner hash-gatuje.
5. `03_REPRODUCTION_AND_EXPECTATIONS.md`: samostatná reprodukcia v `REPRO/`.
6. `05_R3_REFREEZE_AFTER_EXTERNAL_AUDIT.md`: rozsah mechanickej opravy R3.
7. `06_AUDITOR_RESPONSE_TEMPLATE.md`: povinná štruktúra nového Markdown
   výstupu auditora.

## Zmrazené kritériá

- Nezmeniť rovnice, parametre ani prah po behu.
- Overiť raw JSON, zdrojové hashe a tri driver `[7]` kontroly.
- Rozlíšiť absolútne rezíduum blízke machine precision od relatívneho
  prahu, ktorý formálne neprešiel.

## Nonclaims

Balík nerozhoduje o celej fyzikálnej životaschopnosti K4, neotvára support
step 3 a nespúšťa high-precision refinement. Môže ho iba presne navrhnúť.

## Požadovaný výstup

Uveď, či výsledok naozaj podporuje `REVIEW`, či existuje formula/lineage
chyba, a aký najmenší nezmenený high-precision test by vec uzavrel.
Každé hlavné tvrdenie označ `OBSERVED_IN_PRIMARY`,
`INDEPENDENTLY_RECOMPUTED`, `INFERRED_FROM_PROJECT_DOCS` alebo
`CONTEXT_ONLY`.

## Zákaz tichej zmeny medzi R2 a R3

R3 smie meniť iba úplnosť reprodukčného balenia a jeho opis. Runner 280,
base moduly, rovnice, prahy, KMPC-036 raw výsledok a projektový verdikt sú
identické s R2. Opakovaný audit má najprv overiť, že oficiálna `--audit`
cesta už nepadá na `FileNotFoundError`; až potom smie hodnotiť výpočet.
