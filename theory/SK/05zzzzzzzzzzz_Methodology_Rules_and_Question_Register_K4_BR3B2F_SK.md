# 05 — Dodatok metodiky a registra: K4/BR3B-2f (SK)

Dátum: 2026-07-14

Tento dodatok nemení existujúce pravidlá.

## AR40 — Zoznam Puiseuxových sektorov musí byť uzavretý pod backgroundovými mocninami

Pred vyhlásením vzostupného Puiseuxovho reťazca za úplný sa musí zoznam
mocnín uzavrieť pod súčtami so všetkými nenulovými backgroundovými rádmi,
ktoré môžu vstúpiť do rovníc do cieľovej hĺbky. Najmä nenulová matter korekcia
`epsilon_m ~ a` z každého sektora `p+j` generuje kandidáta `p+j+1`; gradient
`k^2/Hconf^2 ~ a^2` generuje `p+j+2`.

Čistý radiačný PASS sa nesmie dediť na `epsilon_m != 0`, kým sa neoveria
zmiešané matter/fuel sektory, carried baryónové/CDM premenné a celý
species/Einstein zdrojový vektor. Starší PASS sa nemaže; jeho rozsah sa
explicitne obmedzí.

## Q67 — Je NID/NIV reťazec do common fuel úplný?

**Stav: NIE; K4 ŽIVÁ, G7 OTVORENÁ.**

Skript 115 uzavrel štandardné NID/NIV Frobeniove vstupy. Skript 116 však
dokázal nenulový matter-dressed Eulerov zdroj a povinné medzisektory NID
`p+1=4.93109` a NIV `p=3.93109`. Skripty 104 a 108 zostávajú platné pre svoje
čisté radiačné sektory, ale netvoria úplný reťazec pri nenulovej hmote.
Nasleduje BR3B-2f-5 so všetkými zmiešanými vrstvami a deviatimi riadkami.

