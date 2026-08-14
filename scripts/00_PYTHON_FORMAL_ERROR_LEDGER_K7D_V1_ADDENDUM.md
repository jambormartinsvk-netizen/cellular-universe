# Python formal error ledger — K7d V1 dodatok

**Dátum:** 2026-07-15  
**Dotknutý skript:** 213  
**Fyzikálny dopad:** žiadny na uloženú ODE trajektóriu; pôvodné diagnostické
verdikty parity a trace/traceless sú neautoritatívne

## FE-K7D-01 — RHS pole zamenené za stav

Funkcia vracala `(species_rhs, projected_derivative)`, ale volajúci prvý
prvok pomenoval `species` a použil ho ako stav v tlaku a šmyku. Prevencia:
návratové objekty musia mať typovo jednoznačné názvy; test musí obsahovať
kompenzovaný seed s analyticky malým tlakovým zdrojom.

## FE-K7D-02 — nezávislá parita obnovila odstránenú cancellation chybu

Species kontrola znovu skladala `D,M` z veľkých takmer sa rušiacich členov
vo float64 a tieto neautoritatívne hodnoty použila pre metrické zdroje.
Prevencia: pri audite projektovanej formulácie sa constraintové `D,M`
injektujú ako autoritatívne metrické zdroje; nezávislosť sa testuje cez
product-rule `D_x,M_x`, nie opakovaním numericky degenerovaného súčtu.

## Stav

Obe chyby opravuje offline nástupca 215 podľa datovanej V1 preregistrácie.
Raw výsledok 213 sa nemaže. Kým 215 neprejde, trace/traceless FAIL z raw 213
sa nesmie citovať ako fyzikálny rozpor.

