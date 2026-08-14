# K-N2/P4 — exact-background rederivation: plán a audit zdroja K7

**Stav:** `P4a–P4b2b PASS; P4c STOP pre K7 13-zložkovú bázu; G8 na nej zakázané.`  
**Nepridáva mechanizmus ani parameter:** zachováva A2-K4
`Q^mu = Gamma rho_f u_d^mu`, kde `Gamma=lambda H0`.

## Čo presný A1 background určuje sám

Definujme `a=e^x`, `E^2=X_f+X_m+X_r` a

```text
D_A1(a) = a^4 E(a)^2 / Omega_r0.
```

Potom platia presné identity, nezávislé od Fourierovho módu `k`:

```text
H(a)       = H0 E(a) = H0 sqrt(Omega_r0) sqrt(D_A1)/a^2,
Hconf(a)   = a H(a) = H0 sqrt(Omega_r0) sqrt(D_A1)/a,
d tau/da   = 1/[H0 sqrt(Omega_r0) sqrt(D_A1)].
```

Zo súčtu A1 continuity rovníc sa prenos medzi palivom a hmotou vyruší:

```text
(E^2)_x = -3 delta X_f - 3 X_m - 4 X_r,
(D_A1)_x = a^4/Omega_r0 * [(4-3delta) X_f + X_m].
```

To je **P4a PASS**: `H`, konformný čas, podiely
`Omega_i(a)=X_i/E^2` a `ell=(D_A1)_x/D_A1` sú k‑nezávislé a určené už
existujúcim A1 backgroundom. Numerická kladnosť na `x=[-18,0]` je v P3;
nie je to globálny dôkaz pre každé možné `a`.

## Konzistencia s existujúcim A2-K4 operátorom

V A1 sa zdroj v rovnici podľa `x=ln a` zapisuje `lambda X_f/E`. Po prechode
na fyzikálny čas je

```text
H * lambda X_f/E = lambda H0 X_f = Gamma X_f,
Gamma = lambda H0.
```

Preto existujúci A2-K4 zápis `Q^mu=Gamma rho_f u_d^mu` presne reprodukuje
zmrazený homogeneous A1 zdroj. **P4 nemení smer prenosu, piatu silu ani
fyzikálnu koľaj.** Mení iba neplatnú neskorú aproximáciu backgroundových
koeficientov za ich presné A1 hodnoty.

## Audit zdroja 213

`213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py`, riadky 63–123,
zostavuje K7 pozadie z

```text
z=K_MPC a/(H0 sqrt(Omega_r0)),
denominator=1+MU z+z^p(1+TRANSFER_SHAPE z^2),
g=G2 z^2.
```

P3 ukázala, že tento `denominator` nie je prípustný až po `a=1`.
Navyše `g=G2 z^2=lambda a^2/sqrt(Omega_r0)` je iba radiačný limit

```text
Gamma/H = lambda/E(a) -> lambda a^2/sqrt(Omega_r0)
```

keď `E=sqrt(Omega_r0)/a^2`. Preto je zakázané nahradiť iba `denominator`
za `D_A1`: `ell`, podiely druhov, `g`, `gr`, `beta_c` a `beta_f` musia byť
odvodené nanovo z A1 a rovnakého `Q^mu`.

## P4 brány

| Brána | Otázka | Stav | Rozsudok pri neúspechu |
|---|---|---|---|
| P4a | Je presné `H`, `Hconf`, `d tau/da`, `ell` bez `k`? | **PASS** | — |
| P4b1 | Majú backgroundové interaction/species koeficienty jednoznačné A1 definície? | **PASS** | — |
| P4b2a | Majú Newtonove species source termy kovariantný pôvod, znamienko a `Gamma->0` limit? | **PASS** | — |
| P4b2b | Je `y -> z` transformácia, jej exact-A1 `T_x` a connection člen úplný? | **PASS** | — |
| P4c | Má K7 báza synchronné species RHS, explicitný projected RHS a constrainty s rovnakým exact-A1 obsahom? | **STOP** | chýba dynamické `U_c`; K7 adapter a G8 na nej končia, A2-K4 automaticky nie |
| P4c | Prejde nový RHS Einsteinovými constraintmi, conservation a limitom `Gamma->0`? | otvorená | STOP adapteru |
| P4d | Majú regular-mode seedy, deep/shallow a G8 hierarchia konzistentný nový background? | otvorená | G8 zostáva blokované |

## Nulové limity — presné rozlíšenie

`lambda->0` pri zachovanom `delta` dá neinteragujúce palivo
`X_f propto a^(-3delta)`, štandardnú hmotu `X_m propto a^-3` a radiáciu
`X_r propto a^-4`. Je to správny **interaction-null limit**, nie automaticky
čistý radiačno-hmotný vesmír. Ten by navyše vyžadoval zmenu/odstránenie
palivovej dnešnej hustoty a tým aj zmenu flat closure. Budúce testy nesmú
tieto dva limity zamieňať.

## Najbližší praktický krok

P4b1 a P4b2a prešli: `10_P4B1_EXACT_A1_COEFFICIENT_LEDGER_SK.md` a
`11_P4B2A_COVARIANT_K4_SPECIES_LEDGER_SK.md` a
`12_P4B2B_PROJECTED_TRANSFORMATION_LEDGER_SK.md`. P4c zastavila K7
13-zložkovú bázu pre chýbajúce `U_c`; dôkaz je v
`13_P4C_K7_MISSING_UC_EXACT_BACKGROUND_STOP_SK.md`. Nástupca potrebuje nový
stavový priestor, nie patch 213; staré výsledky sa neprepisujú.
