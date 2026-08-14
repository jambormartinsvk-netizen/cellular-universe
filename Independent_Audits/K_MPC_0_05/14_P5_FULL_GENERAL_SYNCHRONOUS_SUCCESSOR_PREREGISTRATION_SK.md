# P5 — úplná general-synchronous báza: jediný nástupca K7

**Stav:** `P5.1 PASS; P5.2–P5.4 OTVORENÉ; žiadny ODE runner ešte nevznikol.`  
**Fyzikálna koľaj:** stále A2-K4. **Nie je to A2-K4-K8 ani nový mechanizmus.**

## Prečo P5 vzniká

P4c dokázala, že K7 13-zložková báza implicitne vypustila dynamické `U_c`.
To nie je opraviteľné toleranciou, solverom, closure ani premenovaním
premennej. P5 je jeden matematicky odlišný stavový priestor, ktorý zachová
už definovaný energy-frame prenos

```text
Q^mu=Gamma rho_f u_d^mu,  Gamma=lambda H0,
u_d=(1-beta_d)u_c+beta_d u_f.
```

## Minimálny fyzikálny obsah

Pred akoukoľvek projekciou musí species báza obsahovať samostatne:

```text
metric:       h, eta,
photons:      delta_gamma, U_gamma, photon multipoles,
neutrinos:    delta_nu, U_nu, sigma_nu, L3_nu, ...,
baryons:      delta_b, U_b,
ash/CDM:      delta_c, U_c,
fuel:         delta_f, U_f.
```

`U_b` a `U_gamma` nesmú byť pred G8 zlúčené, pretože plná Thomsonova
evolúcia musí vedieť o photon-baryon slippage. `U_c` nesmie byť gauge
podmienkou; je dynamické v dôsledku energy-frame momentum transferu.

Optionalná transformácia na `D,M` je povolená až neskôr, iba ak `M` obsahuje
všetky relevantné hybnosti vrátane `3 Omega_c U_c/2` a ak je `T_x T^-1`
úplne auditované. Prvý P5 runner bude species-first.

## Povinné brány v poradí

| Brána | Presná otázka | PASS | STOP |
|---|---|---|---|
| P5.1 | Je exact-A1 background + species RHS algebraicky zhodný s P4a/P4b2a? | všetky identity nula, `Gamma->0` limit | chýbajúci/rozporný člen → STOP P5 implementácie |
| P5.2 | Sú `00`, `0i`, slip a trace Einsteinove constrainty úplné s `U_c` a `U_b`? | nezávislé rezíduá v limite | neuzavretý constraint → STOP |
| P5.3 | Existujú regulárne general-synchronous seedy pre exact-A1 a plný stav? | štartová konvergencia, bez gauge fixu `U_c=0` | singularita/neprípustný seed → REVIEW/STOP |
| P5.4 | Je species-first krátka evolúcia stabilná a lineárna na dvoch štartoch? | constrainty + kroková konvergencia | fyzikálny rast/porušenie → STOP A2-K4 alebo review podľa invariantu |
| G8 | Plná photon/neutrino hierarchia, recombination a `lmax` sweep | pôvodná G8 definícia | až po P5.1–P5.4 |

## Čo sa nesmie robiť

- patchovať 213 alebo meniť jeho immutable hash;
- pridávať nový parameter s cieľom potlačiť `U_c`;
- nazvať `U_c=0` gauge voľbou pri nenulovom `Q^mu` momentum transfere;
- získavať G8 body pred P5.1–P5.4;
- zlúčiť baryón a fotón mimo explicitne testovaného tight-coupling limitu.

## Rozpočet práce a ukazovateľ vzdialenosti

P5 má štyri povinné fyzikálne brány pred G8, nie otvorený počet podkoľají.
Každá má binárny PASS/STOP/REVIEW a samostatný dôkaz. Ak P5.1 alebo P5.2
zlyhá algebraicky, nemá zmysel písať solver. Ak P5.3 alebo P5.4 zlyhá
reprodukovateľne, A2-K4 môže dostať nový fyzikálny STOP. To je hranica, pri
ktorej sa má rozumne prejsť na A2-K8/K9/K12, nie pokračovať v K7 suffixoch.

## Prvý najmenší krok

P5.1: statický coefficient a constraint ledger bez ODE. Pred jeho Python
behom bude samostatná Markdown predregistrácia s očakávanými algebraickými
nulami, interným limitom a vonkajším timeoutom. Výsledok nebude meniť skóre.

## Výsledok P5.1

P5.1 prešla ako `RUN_KMPC_003_P5_1_GENERAL_SYNCHRONOUS_STATIC_LEDGER.json`:
všetkých deväť kontrol prešlo a symbolické rezíduá boli presne nula. Úplný
zápis: `16_P5_1_STATIC_LEDGER_RESULT_SK.md`. Nasleduje P5.2; G8 ostáva
blokované.
