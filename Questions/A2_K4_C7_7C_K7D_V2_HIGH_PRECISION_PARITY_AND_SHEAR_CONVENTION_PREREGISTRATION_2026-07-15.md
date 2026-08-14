# A2-K4 / K7d — V2 preregistrácia HP parity a konvencie šmyku

**Dátum:** 2026-07-15  
**Stav:** `PREREGISTERED / NOT RUN`  
**Rozpočet AR66:** druhá a posledná technická oprava  
**ODE, fyzická RHS a prahy:** bez zmeny

## Spúšťač V2

V1 znížila parity chybu z `3.6841e-2` na `2.2169e-7` a uzavrela trace.
Zvyšok je výlučne v kompenzovanom `D` pri absolútnom rozdiele približne
`3.9e-21`. Float64 species product rule tak znovu naráža na cancellation.

Traceless rezíduum na `x=-18` bolo `9.2048707e-9`. Audit konvencie ukázal,
že starší zdroj používal multipól `F2=2 sigma`, kým K7 stav ukladá priamo
`sigma_fs`. Pre K7 preto platí anizotropný zdroj
`S=(rho+p)sigma/rho_crit=(4/3) Omega_fs sigma_fs`, nie `(2/3)`.
Chýbajúci faktor dva presne zodpovedá rezíduu.

## Zmrazená oprava

1. `D_x,M_x` species product rule a projektovaná RHS sa vyhodnotia pri
   80 desatinných miestach z presných desatinných reprezentácií checkpointu.
2. Background sa v HP prepočíta z pôvodných zmrazených parametrov, nie z
   zaokrúhleného evolved endpointu.
3. V traceless ledgeri sa použije `S=(4/3) Omega_fs sigma_fs`.
4. Ostatných 11 parity zložiek sa ďalej overí nezávislou float64 species
   implementáciou V1.
5. Raw 213 aj V1 215 zostávajú zachované; V2 vytvorí nový immutable JSON.

## Očakávanie a STOP

- HP species/projected parita: `<=1e-10` v pôvodnej obálkovej norme;
- trace aj traceless: pôvodná mixed hranica `1e-12+1e-8*norm`;
- activity a solverové výsledky sa nesmú zmeniť.

Ak V2 prejde, technická prerequisite je uzavretá a pokračujú zostávajúce
tri základné prípady. Ak neprejde, opravný rozpočet je vyčerpaný a výsledok
je `REVIEW_BLOCKED`; prah sa neuvoľní a nevznikne V3.

