# Dodatok k Zenodo release checklistu v3.18 — aktuálnosť predikčnej tabuľky

**Status dodatku:** `POVINNÝ PRE KAŽDÉ VYDANIE OBSAHUJÚCE ALEBO ODKAZUJÚCE NA PREDPOVEDE`

## I. Prediction-table currency gate

| ID | Kritérium | Aktuálny stav v3.18 |
|---|---|---|
| ZR-I1 | Každý riadok publikovanej v3.17 tabuľky má stav `STILL CURRENT/SCOPE NARROWED/WITHDRAWN/REPLACEMENT VALIDATED/RECALCULATION OPEN`. | `OPEN` |
| ZR-I2 | Žiadna hodnota so zlyhaným mechanizmom alebo chybným skriptom nezostala označená `PREDICTION`. | `OPEN` |
| ZR-I3 | Pri odvolanej hodnote sa nečaká na náhradu; tabuľka povoľuje `NOT YET AVAILABLE`. | `OPEN` |
| ZR-I4 | Každá materiálna zmena má starú hodnotu, novú hodnotu/status, dôvod, audit a superseding verziu. | `OPEN` |
| ZR-I5 | Predikcie, conditional estimates a post-data fits sú oddelené. | `OPEN` |
| ZR-I6 | Každý nový číselný riadok má skript/výpočet, vstupy, toleranciu, manifest a nezávislý audit. | `OPEN` |
| ZR-I7 | Je zaznamenané, ktoré cieľové dáta boli známe pred zmrazením hodnoty. | `OPEN` |
| ZR-I8 | Materiálna zmena tabuľky je klasifikovaná ako nová `3.x` alebo `4.0`, nie patch. | `OPEN` |
| ZR-I9 | PT1/PT2 dátum a 14/30-dňový operačný cieľ sú zaznamenané; omeškanie má dôvod. | `OPEN` |
| ZR-I10 | Zenodo changelog a README ukazujú na aktuálnu tabuľku a zachovávajú DOI historickej tabuľky. | `OPEN` |

## GO pravidlo

Vydanie, ktoré obsahuje predikčnú tabuľku alebo na ňu odkazuje ako na aktuálnu, je `NO-GO`, kým ZR-I1 až ZR-I10 nie sú `PASS` alebo oprávnene `N/A`.

Pre úzke PT1 erratum môže byť nová hodnota `NOT YET AVAILABLE`; ZR-I6 je vtedy `N/A FOR REPLACEMENT`, ale dôkaz neplatnosti starej hodnoty musí byť auditovaný.

