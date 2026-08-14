# Manifest páru registra 05c v3.18

**Vytvorené a overené:** 2026-07-13  
**Účel:** spätný audit obsahovej synchronizácie SK/EN dodatku

| Jazyk | Súbor | Veľkosť | SHA-256 |
|---|---|---:|---|
| SK — autoritatívny | `theory/SK/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_SK.md` | aktuálna | `842EA0C475E8DDF67311C92E620ABFBAE3AD497401464344BF3D4FED8F8DA994` |
| EN — zrkadlový preklad | `theory/EN/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_EN.md` | aktuálna | `9A8DFDE63D1782E901621807AD04E0DCFE8FC0F941F97FEB349B97BB70654692` |

## Štrukturálna kontrola

- SK pravidlá: AR1–AR8, každý práve raz.
- EN pravidlá: AR1–AR8, každý práve raz.
- SK otázky: Q17–Q34, každá práve raz.
- EN otázky: Q17–Q34, každá práve raz.
- SK obmedzenia: L1–L7, každé práve raz a každé má samostatný blok `Dôvod`.
- EN obmedzenia: L1–L7, každé práve raz a každé má samostatný blok `Reason`.

Kontrola potvrdzuje zhodu identifikátorov a štruktúry. Nejde o tvrdenie, že anglický text má rovnaký binárny obsah; ide o obsahový preklad so zhodnými stavmi a bránami.

Pri akejkoľvek zmene jedného jazykového súboru treba v tom istom kroku:

1. aktualizovať druhý jazyk;
2. zopakovať kontrolu AR/Q/L identifikátorov;
3. vypočítať nové SHA-256;
4. aktualizovať tento manifest a changelog.
