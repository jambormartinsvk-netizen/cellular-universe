# A2-K4 / C7.7c / K7b.3a — smrť vysokopresného soft-constraint solvera

**Dátum:** 2026-07-15  
**Podkoľaj K7b.3a:** **MŔTVA**  
**A2-K4:** živá, `66.5/100`; K7b otvorená

## Základ koľaje

K7b.3a ponechala rovnakú maticu `134×88` a rovnakú pravú stranu ako registrovaný štandardný Puiseuxov solver. Numpy riešenie bolo nahradené 80-ciferným riešením normálnych rovníc, pričom pôvodný double výsledok zostal zachovaný.

## Numerický úspech, ktorý nestačil

- rank: `88/88`;
- podmienenosť: `510.813`;
- max. lineárne rezíduum double: `1.1325e-14`;
- max. lineárne rezíduum 80 dps: `6.8078e-17`;
- max. rezíduum normálnych rovníc: `8.4479e-84`.

## Fyzikálna brána zlyhala

Na NID/deep po dosadení high-precision štandardných koeficientov:

- `D_rhs = 6.6728e-23`;
- `D_series_derivative = 7.8221e-29`;
- activity-relative chyba `D' = 8.53067e5`, pri preregistrovanom limite `<0.1`;
- rekonštrukčná chyba `U_fs = 2.3557e-9`;
- normalizované momentové rezíduum `4.7113e-9`;
- `M_metric = -8.5053e-16`, ale `M_species = -1.9463e-9`;
- najhorší stav prekročil allowance faktorom `2455`;
- najhorší RHS prekročil allowance faktorom `235`.

Zlyhalo päť brán: activity `D'`, `U_fs` rekonštrukcia, momentový constraint, stavová rekonštrukcia a 13-zložkový RHS audit. Podľa preregistrácie sa shallow už nespúšťal.

## Hlavná príčina

Pôvodný overdetermined least-squares systém obsahuje počiatočné a regularitné podmienky ako riadky s rovnakým soft vážením ako dynamické rovnice. Presnejšie minimum preto nemusí presnejšie dodržať fyzikálne kotvy. High-precision riešenie zmenšilo globálne rezíduum tým, že mierne posunulo kotvy; pri NID kompenzácii sa tento posun zosilnil do momentového rozporu.

High-precision registry navyše zachytila koeficienty pred neskoršou exact-zero projekciou skriptu 132. Kombinácia s frakčným a palivovým reťazcom vypočítaným z float konverzie už nebola koeficientovo jednotná.

## Rozsudok

- Menšie least-squares rezíduum nie je fyzikálny PASS.
- 3a sa nesmie opakovať s uvoľneným limitom `D'`.
- Skripty 168 a 169 a ich výpočty sa zachovávajú.
- Ďalšia 3b musí riešiť počiatočné a registrované regularitné podmienky ako tvrdé rovnosti, nie ako mäkké riadky.

## Technická stopa

Prvý pokus skriptu 169 s `--source-runtime-seconds 10` bol odmietnutý parserom, ktorý povoľuje najviac 8 sekúnd. Nevykonal výpočet. Platný beh použil vnútorný limit 14 s, zdrojový limit 8 s a vonkajší limit 17 s.

