# A2-K4 / C7.7c / K7c.3c — predregistrácia druhého RK4 zjemnenia

Dátum: 2026-07-15  
Vstup: K7c.3b endpoint rozdiel `1.44327e-6` pri prahu `1e-6`

Jediná fyzikálne neutrálna zmena je ďalšie zjemnenie oboch uniformných mriežok:

- hrubá: `h=0.00125`, 200 krokov;
- jemná: `h=0.000625`, 400 krokov;
- rovnaký interval, midpoint, HP seed, RHS, closure, envelope škála a všetky fyzikálne prahy;
- RHS cap `4000`, čo pokrýva presne 2 400 RK4 volaní plus audit;
- vnútorný/vonkajší časový limit sa nemení.

Acceptance endpoint rozdiel ostáva `<1e-6`; nesmie sa upraviť podľa výsledku. Reportuje sa aj pomer `previous_difference/current_difference`; hodnota blízka 16 je očakávaná pre asymptotický štvrtý rád, ale nie je samostatnou PASS podmienkou.

Ak druhé zjemnenie prejde, K7c má prvú krátku konvergovanú NID/deep evolúciu. Ak neprejde alebo neklesá, K7c.3c ostáva REVIEW/FAIL podľa príčiny a ďalší krok sa určí až po audite.
