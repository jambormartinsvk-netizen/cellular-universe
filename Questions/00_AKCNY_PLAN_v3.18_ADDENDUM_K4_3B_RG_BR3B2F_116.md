# Akčný plán v3.18 — dodatok po BR3B-2f skripte 116

Dátum: 2026-07-14  
K4: **ŽIVÁ, 60/100 = G6**

| Poradie | Úloha | Brána | Stav |
|---:|---|---|---|
| 1 | BR3B-2f-5a: zostaviť generátor mocnín uzavretý pod `+1` matter dressingom a `+2` gradientom | žiadna povinná mocnina do common fuel nesmie chýbať | **NEXT** |
| 2 | BR3B-2f-5b: vyriešiť NID `p+1`, potom znovu `p+2`, potom `p+3` | pri každej vrstve `rank(A)=rank(A|b)`, konečné koeficienty, 9 riadkov | PENDING |
| 3 | BR3B-2f-5c: vyriešiť NIV `p`, potom znovu `p+1`, potom `p+2` | rovnaká deväťriadková brána | PENDING |
| 4 | Nulový matter limit | musí reprodukovať skripty 104 a 108 | PENDING |
| 5 | Common fuel injekcia | posledná vrstva použije fuel stress 95/100 a vstupy 115 bez nového fitu | PENDING |
| 6 | Prvý neskorší `l=3` feedback a ash-gravity ledger | musí nasledovať po common fuel podľa auditovaných mocnín | PENDING |
| 7 | BR3C: dve hĺbky a zmena kroku/presnosti | štyri Einsteinove rezíduá a konvergencia | PENDING |
| 8 | BR4: plný fotónový/neutrínový backend | nulový limit a nezávislý referenčný cross-check | PENDING |

## Rozhodovacie pravidlá

- technický timeout alebo zle podmienená extrakcia je `UNCLOSED`, nie smrť;
- mŕtvy rozsudok je dovolený až po úplnom zmiešanom zdrojovom vektore;
- čistý radiačný PASS sa automaticky neprenáša na `epsilon_m != 0`;
- žiadny starý skript ani dôvod obmedzenia sa nemaže;
- kanonické skóre ostáva 60/100, kým neprejde celé G7.

