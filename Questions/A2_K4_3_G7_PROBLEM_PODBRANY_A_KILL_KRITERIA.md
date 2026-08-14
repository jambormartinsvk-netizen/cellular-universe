# A2-K4.3 / G7 — problém, podbrány a kill kritériá

**Dátum predregistrácie:** 2026-07-14  
**Vstup:** A2-K4 prešla G6=`60/100`  
**Cieľ:** vlastná úplná Einstein–Boltzmannova realizácia a fyzické transfery  
**Skóre počas práce:** zostáva `60/100`, kým neprejde celá G7

## 1. Prečo K4.3 nie je jeden výpočet

K4.2 používala jednu perfektnú radiačnú tekutinu a `Phi=Psi`. G7 musí
rozlíšiť fotóny, baryóny, štandardné neutrína, paru/extra radiáciu, CDM a
palivo. Musí zaviesť anizotropný stres, Thomsonov rozptyl, rekombináciu,
vyššie multipóly a fyzickú primordiálnu normalizáciu transferov.

Preto sa K4.3 delí na štyri podbrány. Podbrána sama nezvyšuje skóre.

## 2. Podbrány

### K4.3a — druhový a interakčný ledger

Povinné:

1. fixovať jednu Newtonovu gauge a znamienkové konvencie;
2. rozlíšiť `c,f,b,gamma,nu,steam`;
3. zachovať pôvodný K4 transfer iba medzi `c` a `f`;
4. dokázať `sum_A Q_A^mu=0` na pozadí aj v poruchách;
5. doplniť `Phi!=Psi` a anisotropic-stress constraint;
6. dokázať zrušenie Thomsonovej sily v celkovom photon+baryon momentum
   ledgeri;
7. overiť presný návrat ku K4.2 pri nulovom shear a spoločnej radiácii.

### K4.3b — úplné hierarchie a regulárne počiatočné módy

Povinné:

1. photon temperature a polarization hierarchy;
2. massless-neutrino hierarchy;
3. zvolená steam hierarchy;
4. tight-coupling a rekombinačné rozhranie;
5. úplná regulárna adiabatic/isocurvature báza rozšíreného systému;
6. analytický radiation-era rad a constraintový štart.

### K4.3c — implementácia a nulový referenčný test

Povinné:

1. vlastná modifikovateľná implementácia, nie iba binárny CAMB wrapper;
2. `lambda=0` reprodukuje referenčný CAMB 1.6.6 na predregistrovanej mriežke;
3. bodové Einsteinove constrainty;
4. tolerančná, multipólová, tight-coupling a časová konvergencia;
5. druhý gauge alebo nezávislý implementačný cross-check.

### K4.3d — coupled K4 fyzické transfery a G7 rozsudok

Povinné:

1. `lambda=0.15`, `delta=0.02297` bez nového drag fitu;
2. konvergentné `delta_m(k,z)`, metrické a radiačné transfery;
3. žiadny nový ghost, gradient, runaway isocurvature alebo constraint drift;
4. oddelený absolútny K4 transfer, nulový transfer a ich pomer;
5. celý dôkazový balík a rozsudok G7.

Iba prejdenie K4.3a–d dá `70/100` a vstup do A3/G8. `sigma8`, `S8` a
likelihood nie sú súčasťou G7.

## 3. Koľaje pre fyziku pary/Delta Neff

Doterajší CAMB anchor vložil `Delta Neff=0.0535` ako prírastok `nnu`, teda
ako free-streaming massless radiation. Teória však zatiaľ mikroskopicky
neodvodila, či je para free-streaming alebo self-coupled. Preto sa varianty
nesmú zmiešať:

| Podkoľaj | Uzáver pary | Stav | Rozdiel |
|---|---|---|---|
| K4.3-S1 | free-streaming massless hierarchy | `AKTÍVNA PRVÁ` | zhodná s doterajším CAMB `nnu` convention a najľahšie falzifikovateľná |
| K4.3-S2 | self-coupled perfect radiation fluid | `ČAKÁ` | nulový vyšší shear; iný CMB phase shift |
| K4.3-S3 | odvodený sieťový collision kernel | `ČAKÁ NA MIKROFYZIKU` | môže interpolovať medzi S1 a S2, ale nesmie dostať voľný fitovaný opacity parameter |

Smrť S1 nezabíja automaticky S2/S3. S2 alebo S3 však nesmú spätne meniť
`Delta Neff` alebo opacity podľa požadovaného `S8`.

## 4. Kill kritériá

K4.3 vetva zomrie, ak sa po numerickom a znamienkovom audite potvrdí aspoň
jedno:

- nezachovanie `sum Q_A^mu=0` alebo Thomsonovho celkového momenta;
- nemožnosť splniť `00`, `0i` a shear Einstein constraint súčasne;
- neexistencia úplnej regulárnej počiatočnej bázy;
- ghost/gradient/causal alebo high-ell runaway mód;
- coupled transfer stratí linearitu z fyzickej amplitúdy;
- nulový limit nereprodukuje referenciu nad predregistrovanou toleranciou;
- výsledok vyžaduje nový post-data drag, opacity alebo počiatočný mód.

TIMEOUT, chýbajúci zdrojový kód alebo nedokončená podbrána znamenajú
`NEUZAVRETÁ`, nie fyzikálnu smrť.

## 5. Numerické tolerancie sa uzamknú pred K4.3c

K4.3a je algebraická a má limit `10 s` interne/`15 s` externe. Každý
neskorší numerický beh bude mať najviac `50 s` interne/`60 s` externe a
checkpointy. Presné CAMB/transfer tolerancie sa predregistrujú po zvolení
modifikovateľného zdrojového backendu, nie po zobrazení K4 výsledku.

## 6. Primárne referencie

- Ma & Bertschinger: https://arxiv.org/abs/astro-ph/9506072
- CLASS overview: https://arxiv.org/abs/1104.2932
- CAMB line-of-sight implementation: https://arxiv.org/abs/astro-ph/9911177

