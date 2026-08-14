# READ FIRST — po numerickom krížovom audite Jacobianu 151/152

**Stav:** A2-K4 živá, `66.5/100`; C7.7c otvorená.

## Uzavretá korekcia

- fyzikálny Jacobian má `max|J|=43.535`, nie `10^10–10^14`;
- veľké hodnoty patrili obálkovým súradniciam;
- lokálne škálovanie bolo ešte horšie;
- spektrálny polomer `3.444151542625` je podobnostne stabilný;
- `scaled_jacobian_resolved_condition_proxy` je stiahnutý;
- FD krok `10^-7` sa nesmie používať ako presný maticový dôkaz, keď priamy lineárny Jacobian existuje.

## Ďalší krok

Prioritou zostáva C7.7c-K7a: odvodenie projektovaných kompenzovaných zdrojov `D,M`. Ďalšia ODE evolúcia sa zatiaľ nespúšťa.

## Autoritatívny audit

`Audit/A2_K4_C7_7C_JACOBIAN_CLAIMS_NUMERICAL_ADDENDUM_2026-07-14.md`.

