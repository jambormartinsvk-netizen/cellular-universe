# Q20/A2 — čítaj ako prvé po BR3B-2f skripte 116

Dátum: 2026-07-14

| Koľaj | Stav | Skóre | Aktuálna brána |
|---|---|---:|---|
| A2-K4 | **ŽIVÁ** | **60/100 = G6** | G7/BR3B-2f-5 zmiešaný matter/fuel reťazec |

## Čo je uzavreté

- štandardné NID/NIV Frobeniove vstupy sú v potrebnej hĺbke jedinečné;
- nulový smer odrezaného radu nezasahuje cieľové koeficienty;
- ash stress gravituje až po common fuel sektore;
- čisté radiačné sektory zo skriptov 104 a 108 zostávajú platné.

## Čo bolo opravené v stave

BR3B-2e sa už nesmie označovať ako úplné poradie. Pri nenulovej ranej hmote
chýbajú:

- NID `p+1 = 4.93109`;
- NIV `p = 3.93109`.

Staré súbory sa nemažú. Ich PASS platí iba pre sektory, ktoré skutočne
riešili. K4 nezomrela; G7 ostáva otvorená.

## Nasleduje

BR3B-2f-5: vyriešiť celý zmiešaný reťazec NID
`p+1 -> p+2 -> p+3` a NIV `p -> p+1 -> p+2`, pri každej vrstve so všetkými
deviatimi riadkami a carried baryónovými/CDM premennými.

Autoritatívny audit:
`Audit/A2_K4_3B_RG_BR3B2F_STANDARD_INPUTS_AND_MIXED_POWER_AUDIT.md`.

