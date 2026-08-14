# KMPC-079/080 — interný audit BI/k=.15 holdout hranice

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Interný audítor a tvorca skriptov:** Codex (OpenAI)  
**Stav:** `INTERNAL_AUDIT_COMPLETE / HIGH_PRECISION_BOUNDARY_JUSTIFIED`

## Zistenia

1. `full_ra_m3_seed._solve_m3` zostaví driver maticu a rieši ju skôr, než
   zostaví `Einstein_00/0i` holdout maticu. Holdout nie je fitovaná rovnica.
2. KMPC-080 patchuje iba `_solve_equilibrated` pre exact rank 104. Nepridáva
   holdout riadky, nemení support, `rcond`, prahy ani rovnice.
3. Po troch same-matrix corrections main driver prešiel na
   `1.3521906982651137e-16`; jediná false audit check je
   `M3_independent_00_0i_holdout`.
4. Holdout maximum `3.019756779905407e-9` má absolútne rezíduum iba
   `8.728840268468619e-17`. Je preto numericky nerozhodnuté, nie fyzikálne
   vyvrátené.

## Povolený nástupca

Jeden 80-dps solve presne tej istej float64-zostavenej 104×104 matice.
Vstupné floaty sa prenesú exact `as_integer_ratio`; nezávislá holdout matica
sa vyhodnotí v 80 dps na high-precision riešení, bez pridania jej riadkov do
solve. Scope rozlišuje solve-roundoff od prípadnej assembly-roundoff chyby.

PASS je dovolený iba ak high-precision driver aj holdout prejdú pôvodné
prahy a všetky ostatné frozen KMPC-080 brány sú PASS. Ak holdout neprejde,
ďalší krok smie byť exact-assembly audit, nie fyzikálny STOP.
