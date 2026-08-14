# A2-K4 / C7.7c / K7 / P4a — execution freeze a rozpočet technických opráv

**Dátum:** 2026-07-15  
**Stabilné ID:** `SCI-A2K4-C7G5-K7C-P4A-METHOD-TOLERANCE`  
**Stav:** záväzný dodatok pred implementáciou skriptov 209–212  
**Fyzika vykonaná týmto dokumentom:** nie

## Ľudskou rečou

Po odstránení dvoch algebraicky nulových float64 artefaktov prešla RK4
kroková konvergencia. Teraz overíme, či rovnaký normalizovaný endpoint na
rovnakom NID/deep intervale dostanú aj adaptívny DOP853 a implicitný Radau.
Nemeníme fyziku, seed, background, stavovú bázu, closure ani interval.

P4a je najbližšia vysoko vážená stena K7. Jej cieľom je rozhodnúť, nie
vytvoriť ďalšie voľné vetvenie.

## Zmrazené očakávanie

Štyri rozdiely musia byť `<=1e-8`:

1. DOP853-tight verzus P3b RK4-grid400;
2. DOP853-medium verzus DOP853-tight;
3. Radau-tight verzus P3b RK4-grid400;
4. Radau-tight verzus DOP853-tight.

Každý prípad musí skončiť úspešne presne v `x=-24.75`, zachovať 13 mien v
správnom poradí, mať konečný stav a RHS, zostať pod normalized safety cap
`1e8` a pod RHS cap `100000`.

## Rozhodovanie

- všetky štrukturálne kontroly a štyri rozdiely PASS → celý C7-G5 PASS;
- DOP853-tight a Radau sa zhodnú, ale nie s RK4 → otvorí sa referencia P3b,
  nie fyzika K4;
- platné alternatívne metódy sa nezhodnú → STOP formulácie K7 na G5 a
  architektonický audit pred úvahou o K8;
- timeout, parser, provenance, CLI alebo export chyba → technický REVIEW,
  nie fyzikálny verdikt.

## Povolené technické opravy

Povolené sú najviac tri implementačné stavy:

| Stav | Povolenie |
|---|---|
| V0 | prvá implementácia 209–212 |
| V1 | jedna atomická oprava presne diagnostikovanej technickej chyby |
| V2 | druhá atomická oprava zostávajúcej technickej chyby |

Po V2 nasleduje PASS, STOP alebo `REVIEW_BLOCKED`. V3 je zakázaná bez
samostatného architektonického rozhodnutia.

Povolené atomické triedy opravy:

1. CLI, marker, import alebo solver-API plumbing;
2. odovzdanie už zmrazeného case mappingu, runtime limitu alebo RHS capu;
3. fail-closed provenance, hash alebo cesta k immutable artefaktu;
4. natívna JSON serializácia, povinný kľúč alebo offline agregácia.

Oprava smie iba uviesť implementáciu do zhody s už zmrazeným kontraktom.
Nesmie meniť RHS, znamienka, seed, scale, interval, stavovú bázu, tolerancie,
PASS hranicu, normu ani fyzikálny parameter.

Ak by jedna oprava menila viac nezávislých príčin súčasne, nie je atomická a
nesmie sa použiť ako V1/V2.

## Maximálny počet behov

Jeden implementačný stav obsahuje tri vedecké prípady: DOP853-medium,
DOP853-tight a Radau-tight. V0+V1+V2 preto povoľujú najviac **9 hlavných
solverových behov**. Každý prípad má interný limit 20 sekúnd, vonkajší 25
sekúnd a žiadny timeout sa automaticky nepredlžuje.

Offline agregát fyziku nespúšťa. Source-delta, compile, help a corpus
preflight nie sú solverové behy, ale každý má vlastný krátky externý limit.

## Vzdialenosť k smrti koľaje

Neúspešná technická V0/V1/V2 môže zastaviť implementáciu alebo K7, nie
automaticky A2-K4. A2-K4 dostane STOP na tejto stene iba po dôkaze spoločného
no-go alebo po architektonickom audite, ktorý nenájde fyzikálne a matematicky
odlišnú auditovateľnú reprezentáciu.

## Väzba na staršiu preregistráciu

Tento dodatok nemení fyzikálny ani numerický kontrakt v
`Questions/A2_K4_C7_7C_K7C_P4A_G5_METHOD_TOLERANCE_PREREGISTRATION_2026-07-15.md`.
Spresňuje iba opravný rozpočet, význam steny a zákaz kombinatorického
hľadania.

