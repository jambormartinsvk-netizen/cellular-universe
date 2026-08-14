# Register mŕtvych koľají — dodatok retrospektívy M-011

**Dátum:** 2026-07-13  
**Pravidlo:** historický riadok M-011 sa nemaže

## M-011 — zmena statusu bez straty stopy

| Pole | Hodnota |
|---|---|
| Historický stav | `MŔTVA — ARCHIVOVANÁ` |
| Stav po retrospektíve | `ROZSUDOK POZASTAVENÝ; KOĽAJ ZNOVU OTVORENÁ NA K4.1` |
| Max. hĺbka | `50/100` |
| Platný dôkaz | rovnice, determinant interakčného podbloku, konvergencia a constrainty skriptu 30 |
| Neplatný krok | `ln(T/T0)>1` bol interpretovaný ako `ln(T)>1` |
| Nové skripty | 63 a 64 |
| Podmienka uzavretia | úplná constrained báza módov a absolútny transfer hlboko v radiačnej ére |

Tento dodatok nevyhlasuje K4 za preživšiu. Znamená iba, že doterajší dôkaz
nepostačuje na konečnú smrť. Ak K4.1 zlyhá, M-011 sa potvrdí novým dodatkom;
pôvodný chybný rozhodovací krok zostane zdokumentovaný.

## Dodatok 2026-07-14 — K4.1 prešla

| Pole | Hodnota |
|---|---|
| Historický riadok M-011 | **zachovaný; nemaže sa** |
| Výsledok úplnej regulárnej bázy | `PASS_K4_1_REGULAR_SUPERHORIZON_BASIS` |
| Nezávislý fixed-RK4 test | `PASS_INDEPENDENT_CROSSCHECK` |
| Aktuálny stav K4 | `PREŽÍVA K4.1 — 55/100` |
| Dôvod obmedzenia M-011 | pomer k zanikajúcej referencii bol zamenený za absolútny rast; historický velocity seed navyše neleží v regulárnom primordiálnom priestore |
| Najbližšia stena | K4.2 high-k/subhorizontový hlavný symbol a fyzický rast |

K4.1 nedokazuje observačnú správnosť K4. Historická smrť sa však nesmie
citovať ako aktívny rozsudok. Ak K4 neskôr zomrie, pridá sa nový riadok s
novým dôvodom, výpočtom a skriptom; M-011 zostane iba auditnou históriou.

