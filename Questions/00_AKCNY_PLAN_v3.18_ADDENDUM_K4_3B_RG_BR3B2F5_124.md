# Akčný plán v3.18 — dodatok po BR3B-2f-5 skripte 124

Dátum: 2026-07-14  
A2-K4: **ŽIVÁ, 60/100 = G6**

| Poradie | Úloha | Brána | Stav |
|---:|---|---|---|
| 1 | BR3B-2f-5: úplný NID/NIV mixed matter/fuel reťazec po common fuel | `rank=36/36`, 11 riadkov, nulové limity | **DONE — PASS** |
| 2 | BR3B-2g-a: odvodiť prvý `l=3` feedback | NID `p+4`, NIV `p+3`; species-local velocity a správne znamienka | **NEXT** |
| 3 | BR3B-2g-b: pridať ash transfer do carried `delta_c` | NID `p+4`, NIV `p+3`; nulový limit pri vypnutom transfere | PENDING |
| 4 | BR3B-2g-c: pridať prvý gravitačný ash vstup | NID `p+5`, NIV `p+4`; úplný Einstein ledger | PENDING |
| 5 | BR3B-2g-d: spoločný rank/residual audit | všetky vzniknuté vrstvy, žiadna preskočená mocnina | PENDING |
| 6 | BR3C-a: inicializovať evolúciu z dvoch skorých hĺbok | rovnaké neskoré riešenie v tolerancii | PENDING |
| 7 | BR3C-b: štyri Einsteinove rezíduá | absolútna aj škálovaná brána, žiadne noise/noise ospravedlnenie bez absolútnej brány | PENDING |
| 8 | BR3C-c: zmena kroku, tolerancie a hĺbky hierarchy | konvergenčný PASS | PENDING |
| 9 | BR4: plný fotónový/neutrínový backend | nulový limit a nezávislý cross-check | PENDING |

## Rozhodovacie pravidlá pre ďalší krok

- BR3B-2f-5 PASS nepridáva čiastočné body G7; kanonické skóre ostáva 60/100.
- `l=3` shear feedback musí používať rýchlosť tej istej free-streaming
  zložky. Fotónový zdroj je pre neutrínový shear neprípustný.
- Technická chyba, timeout alebo chybný legacy oracle znamenajú `UNCLOSED`,
  kým sa chyba nelokalizuje; nie automatickú smrť fyzikálnej koľaje.
- Mŕtvy rozsudok vyžaduje fyzikálnu nekonzistenciu úplného, správne
  namapovaného systému. Všetky staré skripty a dôvody obmedzenia ostávajú.
- Každý nový numerický skript musí mať vnútorný aj vonkajší časový limit.

