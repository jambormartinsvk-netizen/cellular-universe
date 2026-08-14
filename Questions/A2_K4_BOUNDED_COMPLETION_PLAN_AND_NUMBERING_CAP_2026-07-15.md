# A2-K4 — ohraničený plán dokončenia a limit číslovania

Dátum: 2026-07-15

## Finish line

Aktuálna koľaj má presne šesť zostávajúcich balíkov: G5, G4, G6, G7, G8 a
G9. Po G9 nasleduje finálny PASS/STOP audit A2-K4. Nová podkoľaj vznikne iba
pre nový fyzikálny mechanizmus, nie pre parser, timeout alebo serializáciu.

## Aktuálne tri povinné čísla

Pri každej zmene stavu sa aktualizujú spolu:

- jemná hĺbka: aktuálne `66.5/100`;
- strict C7-W1 support: aktuálne `90/100`;
- pracovný WBS-1 progress: aktuálne `90/100`.

Žiadne z nich nie je pravdepodobnosť pravdivosti.

## Maximálny počet iterácií

Každý zostávajúci balík smie mať:

1. jednu prvú implementáciu;
2. najviac dve zdokumentované technické opravy;
3. následne povinný PASS, fyzikálny STOP alebo `REVIEW_BLOCKED`.

Po treťom technickom neúspechu sa nesmie vytvoriť ďalšie písmeno. Potrebné
je architektonické rozhodnutie, nový mechanizmus alebo uzavretie práce.

## Script budget

| Rozsah | Účel |
|---|---|
| 209–212 | P4a runner, source-delta, corpus checker, offline agregát |
| 213–217 | P4b/P4c a spoločné route-local jadro |
| 218–220 | G7 celý interval |
| 221–225 | G8 plná hierarchia |
| 226–230 | G9 likelihood |
| 231–232 | finálny audit a release integrita |
| 233–240 | iba rezerva na najviac dve technické opravy na balík |

Skript 241 je zakázaný bez samostatnej revízie tohto plánu. Po skripte 212
sa nové parameter cases ukladajú ako konfigurácie a JSON, nie nové Python
súbory. Historické skripty sa nemažú.

G8 využije 221–225 presne podľa route predregistrácie: 221 S0+S1, 222 S2,
223 single-case `lmax`, 224 konvergenčný agregát/FULL konfigurácie a 225
finálny gate. Technické opravy nemenia túto logickú postupnosť.

## Q budget

- Q94: vzdialenosť a odhad dokončenia A2-K4;
- Q95: konečný výsledok G5;
- Q96: konečný výsledok G4;
- Q97: konečný výsledok G6;
- Q98: konečný výsledok G7;
- Q99: G8/G9 a finálny rozsudok A2-K4.

Technické chyby patria do `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md`, nie do
nového Q. Bez novej fyzikálnej vetvy je Q99 strop A2-K4.

## Kontrolný bod

Po každom balíku sa znovu odhadnú zostávajúce pracovné dni. Povinný veľký
časový audit je pred G8, pretože plná Boltzmannova hierarchia a likelihood
dominujú kalendárnej náročnosti.

