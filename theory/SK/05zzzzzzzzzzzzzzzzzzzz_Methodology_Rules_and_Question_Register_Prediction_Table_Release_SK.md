# Dodatok k 05 — predikčná tabuľka ako povinný release trigger (SK)

## Kontrola duplicity

AR48 všeobecne vyžaduje materiálny spúšťač Zenodo vydania. AR49 špecifikuje citlivosť verejnej tabuľky predpovedí: určuje hranicu materiálnej zmeny, povoľuje odvolanie bez hotovej náhrady a zavádza operačný protokol proti dlhému ponechaniu chybného čísla. AR49 preto AR48 neduplikuje.

## AR49 — materiálna zmena predikčnej tabuľky povinne spúšťa nové vydanie

Ak uzavretý audit preukáže, že publikovaná predpoveď, interval, status alebo rozsah sú materiálne chybné, starý riadok sa musí verejne označiť `WITHDRAWN` alebo `SCOPE NARROWED`. Na novú hodnotu sa nečaká; náhrada môže byť `NOT YET AVAILABLE`.

Validovaná nová hodnota spúšťa druhé vydanie alebo prediction-table update. Materiálna zmena tabuľky je nová minor verzia `3.x`, nie patch. Pri zmene fundamentu patrí do `4.0`.

Za materiálnu sa považuje zmena statusu, hodnoty nad numerickú toleranciu/zaokrúhlenie, intervalu, neistoty, falsifikačného prahu, znamienka, trendu, mechanizmu, datasetu alebo vedeckej interpretácie.

Ak sa nová hodnota získala po použití cieľových dát, musí byť označená `POST-DATA FIT` alebo `CONDITIONAL ESTIMATE`, nie `PREDICTION`.

Operačný cieľ: pri auditovanom odvolaní pripraviť verejný pracovný záznam do 3 pracovných dní a úzke Zenodo erratum do 14 kalendárnych dní; pri validovanej náhrade vydať aktualizáciu do 30 kalendárnych dní. Omeškanie musí byť verejne označené a zdôvodnené. Lehoty neumožňujú obísť audit, manifest ani Git tag.

## Q75 — ktoré riadky predikčnej tabuľky v3.17 zostávajú aktuálne?

**Stav:** `KRITICKÁ RELEASE ÚLOHA — OTVORENÁ.`

Pred R3.18-DOC musí každý riadok dostať stav `STILL CURRENT`, `SCOPE NARROWED`, `WITHDRAWN`, `REPLACEMENT VALIDATED` alebo `RECALCULATION OPEN`. Odvolaná hodnota sa nesmie automaticky preniesť do v3.18 iba preto, že nový výpočet ešte nie je hotový.

## Obmedzenie staršej formulácie R3.18-PHYS

Požiadavka čakať na A2/A3/A8 platí pre publikovanie **novej hodnoty ako fyzickej predikcie**. Nezakazuje skoršie DOC/ERRATUM vydanie, ktoré odvolá chybnú starú hodnotu alebo ju preklasifikuje na historický/conditional odhad.

