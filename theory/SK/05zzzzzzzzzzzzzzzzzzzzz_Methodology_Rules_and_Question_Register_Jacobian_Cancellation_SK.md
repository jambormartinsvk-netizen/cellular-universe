# Dodatok k 05 — odčítanie v deriváciách Jacobiánu (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR38 vyžaduje pomenovať súradnicovú normu a zmerať FD chybu. Neurčuje však postup, keď algebraicky totožný zápis derivácie stráca cifry katastrofickým odčítaním, ani povinnosť zachovať neúspešné nastavenia. AR39 vypĺňa túto medzeru a AR38 nemení.

## AR39 — Oprava odčítania musí zachovať neúspešnú stopu a pôvodné prahy

Ak sa malá derivácia počíta cez odčítanie veľkých takmer rovnakých čísel, musí sa pred ďalšou evolúciou porovnať s algebraicky totožným priamym tvarom alebo s autoritatívnou vyššou presnosťou. Neúspešný FD krok, vzorec, parser a jeho výstup sa zachovajú ako mŕtva numerická podkoľaj s dôvodom. Prah sa po výsledku nesmie uvoľniť; alternatíva sa preregistruje a spustí v rovnakom rozsahu povrchov.

Zložený verdikt musí oddeliť historickú neautoritatívnu diagnostiku od jej náhradného dôkazu a musí zlyhať uzavreto pri chýbajúcej alebo nesprávne vnorenej dátovej ceste.

## Q67 — Ktoré staršie formulácie K7a boli neskorším auditom obmedzené?

Double centrálna diferencia \(T'\) v skripte 159 a zápis `ell=2*(q+1)` nie sú autoritatívne na hlbokých radiačných plochách. Prvý dal najlepšiu relatívnu chybu približne `6.28e-6`; druhý sa od 80-cifernej referencie líšil o `1.51e-9`. Priamy tvar `ell=B'/B` dosiahol približne `2e-16` bez zmeny rovníc. Skript 163 bol navyše obmedzený na neplatný agregátor, pretože preskočil jednu úroveň JSON; jeho fyzikálne podvýsledky tým neboli vyvrátené.

