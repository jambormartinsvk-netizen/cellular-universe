# AR66.2 — vykonávací checklist formula provenance

Tento checklist sa priloží ku každej bráne, ktorá mení rovnice, gauge,
stavový priestor alebo approximation. Je určený na zachytenie situácie,
keď nižší skript používa podobný, ale nepresný vzorec.

| Kontrola | Povinný dôkaz | Zakázaný náhradný dôkaz |
|---|---|---|
| Rodič | presná kanonická/kovariantná rovnica, konvencie a zdroj | slovný opis mechanizmu |
| Projekcia | každý člen, znamienko a koeficient do nižšieho tvaru | iba výskyt názvov premenných |
| Aproximácia | čo sa zahadzuje, poradie a interval platnosti | tiché nastavenie na nulu |
| Implementácia | term map rodič → riadok/funkcia/stav | úspešný runtime alebo malý solver residual |
| Nezávislá kontrola | invariant, iný constraint alebo product-rule residual | rezíduum definované tou istou rekonštrukciou |
| Limity | `Gamma→0`, relevantný `k→0`/superhorizon limit a rozmery | iba jeden fiducial beh |
| Verdikt | `PASS_MAPY`, `PASS_SCOPE`, `STRUCTURAL PASS` alebo `FORMULA PASS` | neurčité slovo „PASS“ |

## Uplatnenie na P5

| P5 artefakt | Správny status podľa AR66.2 | Čo ešte chýba |
|---|---|---|
| L2-B1/B2 source audity | `PASS_MAPY` | nie formula PASS |
| P5.1/P5.2 | `STRUCTURAL PASS` | dynamické nezávislé constraint zachovanie |
| P5.3b–e | `FORMULA PASS — leading radiation scope` | gauge, vyššie rády, plný hierarchy seed, dva štarty |
| budúce P5.4 | žiadny status vopred | musí mať term map a nezávislé dynamické residualy |

Ak audit neskôr odhalí chybu v nižšom vzorci, tento dokument sa neprepisuje:
pridá sa errata, pôvodný hash a downstream brána sa označí `REVIEW_BLOCKED`.
