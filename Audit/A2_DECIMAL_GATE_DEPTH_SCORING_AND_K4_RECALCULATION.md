# A2 — audit jemnej desatinnej hĺbky a rekalibrácia K4

**Dátum:** 2026-07-14  
**Rozsudok:** `K4 = 66.0/100; G6 PASS; G7 OTVORENÁ`  
**Fyzikálny rozsudok:** bez zmeny; koľaj je živá, G7 ešte neprešla

## 1. Čo sa opravuje

Hodnota `60/100` správne hovorila, že posledná úplne prejdená kanonická
brána K4 je G6. Súčasne však skrývala šesť uzavretých auditných balíkov
vnútri G7. Odteraz sa vedú dva údaje:

| Údaj | K4 |
|---|---|
| Posledná úplná brána | `G6 PASS` |
| Jemná auditná hĺbka | `66.0/100` |
| Aktívna brána | `G7 OTVORENÁ` |
| Fyzikálny stav | `ŽIVÁ` |

Číslo `66.0` nie je pravdepodobnosť správnosti, confidence ani tvrdenie, že
je hotových 66 % práce. Je to poloha v zmrazenom sekvenčnom ledgeri.

## 2. Zmrazený G7 ledger K4

Každý hlavný checkpoint má váhu `1.0`. Prvých šesť je jednorazová
rekonštrukcia z chronologicky archivovaných auditov. Posledné štyri sa
zmrazujú **pred** ďalším BR3C výpočtom.

| ID | Auditované tvrdenie | Dôkaz | Stav | Bod | Kumulatívne |
|---|---|---|---|---:|---:|
| C7.1 | K4.3a species/interakčný ledger, anisotropný stres, konzervácia a nulový návrat | `Audit/A2_K4_3A_SPECIES_LEDGER_ANISOTROPIC_STRESS_AND_NULL_AUDIT.md`; skript 72 | PASS | `1.0` | `61.0` |
| C7.2 | regulárne seedy, Puiseux register a synchronous test-field odpoveď | `Audit/A2_K4_3B_RG_REGULAR_SEEDS_PUISEUX_AND_SYNCHRONOUS_TEST_FIELD_AUDIT.md`; skripty 77–86 | PASS v registrovanom rozsahu | `1.0` | `62.0` |
| C7.3 | backreaction BR1, constraintový BR2 a prvé zdroje BR3A | `Audit/A2_K4_3B_RG_BR1_BR2_BR3A_AUDIT.md`; skripty 88–95 | PASS v registrovanom rozsahu | `1.0` | `63.0` |
| C7.4 | background dressing a spoločné AD/CDI/BI sektory | `Audit/A2_K4_3B_RG_BR3B_BACKGROUND_DRESSING_AUDIT.md`; skripty 97–102 | PASS v registrovanom rozsahu | `1.0` | `64.0` |
| C7.5 | NID/NIV hierarchia, štandardné vstupy a úplný mixed reťazec po common fuel | audity BR3B-2e, 2f a 2f-5; skripty 104–124 | PASS | `1.0` | `65.0` |
| C7.6 | gradientovo regulárny `l=3`, transfer-corrected fuel a prvý ash gravity ledger | `Audit/A2_K4_3B_RG_BR3B2G_L3_ASH_FULL_LEDGER_AUDIT.md`; skripty 126–128 | PASS; skript 126 ostáva REVIEW | `1.0` | **`66.0`** |
| C7.7 | BR3C dvojhĺbkový počiatočný stav a konečná skorá evolúcia | budúci BR3C audit | PENDING | `1.0` | `67.0` |
| C7.8 | štyri Einsteinove rezíduá a kroková, tolerančná a `lmax` konvergencia | budúci BR3C audit | PENDING | `1.0` | `68.0` |
| C7.9 | plný photon/polarization/neutrino/steam/recombination backend a nulový referenčný cross-check | budúci BR4 audit | PENDING | `1.0` | `69.0` |
| C7.10 | coupled fyzické transfery, všetky kill kritériá, reprodukčný balík a integrovaný rozsudok G7 | budúci G7 verdict | PENDING | `1.0` | `70.0` |

Checkpointy C7.1–C7.6 neznamenajú, že celá pôvodná K4.3b prešla. Sú to
uzavreté dôkazové kroky vo vnútri otvorenej G7. Pôvodné acceptance kritériá
K4.3a–d a kill kritériá sa nemenia.

## 3. Jemné body budúcich krokov

### C7.7 — spolu 1.0

| Podcheckpoint | Podmienka PASS | Bod |
|---|---|---:|
| C7.7a | rovnaký fyzikálny počiatočný stav zostavený v dvoch skorých hĺbkach | `0.2` |
| C7.7b | obe úplné skoré evolúcie dobehnú v limite s konečnými premennými | `0.3` |
| C7.7c | všetky registrované species a módy sú v evolučnom stave, bez tichého nulového placeholdera | `0.2` |
| C7.7d | po prenose na spoločný neskorší bod sa dve štartové hĺbky zhodnú v predregistrovanej tolerancii | `0.3` |

### C7.8 — spolu 1.0

| Podcheckpoint | Podmienka PASS | Bod |
|---|---|---:|
| C7.8a | `00` Einsteinovo rezíduum prejde absolútnou aj škálovanou bránou | `0.1` |
| C7.8b | `0i` rezíduum prejde | `0.1` |
| C7.8c | trace `ij` rezíduum prejde | `0.1` |
| C7.8d | traceless `ij` rezíduum prejde | `0.1` |
| C7.8e | polovičný krok zachová transfery a rezíduá | `0.2` |
| C7.8f | prísnejšia tolerancia zachová transfery a rezíduá | `0.2` |
| C7.8g | zmena počiatočnej hĺbky a `lmax` zachová spoločné riešenie | `0.2` |

### C7.9 — spolu 1.0

| Podcheckpoint | Podmienka PASS | Bod |
|---|---|---:|
| C7.9a | úplná photon temperature hierarchy | `0.2` |
| C7.9b | polarizácia, Thomsonov člen a tight-coupling rozhranie | `0.2` |
| C7.9c | neutrino a steam hierarchie vrátane shear/high-ell regularity | `0.2` |
| C7.9d | rekombinácia/opacity a referenčný nulový transfer | `0.2` |
| C7.9e | druhý gauge alebo nezávislý implementačný cross-check | `0.2` |

### C7.10 — spolu 1.0

| Podcheckpoint | Podmienka PASS | Bod |
|---|---|---:|
| C7.10a | coupled beh používa zmrazené `lambda=0.15`, `delta=0.02297` bez nového fitu | `0.2` |
| C7.10b | úplná báza nemá ghost, gradient, runaway isocurvature ani constraint drift | `0.2` |
| C7.10c | absolútny K4 transfer, nulový transfer a ich pomer sú oddelené a konvergentné | `0.2` |
| C7.10d | dôkazový balík, výstupy, verzie a kontrolné súčty sú úplné | `0.2` |
| C7.10e | integrovaný rozsudok všetkých K4.3a–d je PASS | `0.2` |

Body sa získavajú iba v uvedenom poradí. Ak napríklad C7.8a neprejde,
neskorší vykonaný C7.8e nezvýši jemnú hĺbku; ostane zapísaný ako hlbšie
vykonaný test.

## 4. Dopad na ostatné koľaje

Fyzikálne rozsudky ani dôvody smrti K1–K12 sa nemenia. Starším koľajam bez
zmrazeného vnútrobránového ledgeru sa neprideľujú spätné desatiny podľa toho,
ako blízko vyzeral ich výsledok. Ich celé skóre sa iba zapisuje s desatinnou
nulou a najhlbší vykonaný test zostáva samostatný údaj.

Aktuálny katalógový dodatok je v
`Audit/A2_KATALOG_DECIMAL_DEPTH_ADDENDUM_2026-07-14.md`.

## 5. Auditný záver

Nové zobrazenie opravuje informačnú stratu bez oslabenia brán:

```text
A2-K4: ŽIVÁ | jemná hĺbka 66.0/100 | posledná celá brána G6 PASS |
aktívna brána G7 OTVORENÁ | najbližšie C7.7a / BR3C-a.
```

