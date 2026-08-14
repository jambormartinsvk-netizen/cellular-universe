# A2-K4 BR3C-b — predregistrácia skorej evolúcie

**Dátum:** 2026-07-14  
**Vstup:** `C7.7a PASS; K4=66.2/100`  
**Možný prírastok:** `+0.3` po úplnom PASS C7.7b

## Rozsah

BR3C-b integruje štyri trajektórie: NID a NIV z povrchov `x=-25` a `x=-23`
na spoločný skorý koniec `x=-18`. Koniec zodpovedá približne
`z=k a/(H0 sqrt(Omega_r))=3.52e-4`, teda zostáva pod predregistrovanou
hranicou skorého sektora `z<1e-3`.

BR3C-b testuje iba to, či úplná registrovaná skorá ODE sústava dobehne s
konečným stavom. Zhoda oboch štartov patrí do C7.7d a Einsteinove trace/
traceless rezíduá do C7.8; ich výsledok sa nesmie vopred započítať.

## Stavový vektor

```text
y = (h, eta, delta_gamma, delta_fs, delta_b, delta_c,
     U_gamma, U_fs, sigma_fs, L3_fs, L4_fs, delta_f, U_f)
```

`U_b=U_gamma` v tight-coupled spodnom momente. `U_c=0` je explicitný
synchronous first-order limit; skript 128 ukázal, že interakčný zdroj `U_c`
je v tomto balíku `O(Phi^2)`. Nie je to tichý placeholder.

## Zmrazený background

Použijú sa rovnaké hodnoty ako v 127/132:

```text
delta=0.02297, lambda=0.15, h=0.6637, Omega_m0=0.3517,
ombh2=0.02237, Delta_Neff=0.0535, k=0.05 Mpc^-1,
Phi_coefficient=1 v per-unit Puiseux normalizácii.
```

Nech `p=4-3delta`, `mu=H0 Omega_m0/sqrt(Omega_r)`,
`g2=lambda (H0/k)^2 sqrt(Omega_r)`, `z=k a/(H0 sqrt(Omega_r))` a

```text
D = 1 + mu z + Phi z^p [1 + g2(1/(p+1)-1/2)z^2].
```

Z neho sa priamo vyhodnotia `q=-1+D_x/(2D)`, `s^2=z^2/D`, päť `Omega_A`,
baryónové zaťaženie a transferové sadzby. Background sa počas integrácie
nefituje ani neinterpoluje.

## ODE uzáver z riadkov 119/126/127

Derivácia je podľa `x=ln(a)`. `h_x` a `eta_x` sa určia z constraintov:

```text
h_x   = 3 sum_A(Omega_A delta_A) + 2 s^2 eta
eta_x = 2 Omega_gamma U_gamma + 2 Omega_fs U_fs
        + 1.5 Omega_b U_gamma + 1.5 delta Omega_f U_f.
```

Evolučné riadky sú presné rearrangementy auditovaného ledgeru:

```text
delta_gamma,x = -(4/3)s^2 U_gamma -(2/3)h_x
U_gamma,x     = q U_gamma - R/(1+R) U_gamma
                + delta_gamma/[4(1+R)]
delta_fs,x    = -(4/3)s^2 U_fs -(2/3)h_x
U_fs,x        = q U_fs + delta_fs/4 - sigma_fs
sigma_fs,x    = (2/15)h_x +(4/5)eta_x +(4/15)s^2 U_fs -(3/10)L3
L3,x          = -q L3 +(6/7)s^2 sigma_fs -(4/7)L4
L4,x          = -2q L4 +(4/9)s^2 L3
delta_b,x     = -s^2 U_gamma -h_x/2
delta_c,x     = -h_x/2 + gr(delta_f-delta_c)
delta_f,x     = -3(2-delta)delta_f -delta s^2 U_f -delta h_x/2
                -9delta(2-delta)U_f -3(2-delta)g U_f
U_f,x         = (q+2)U_f +delta_f/delta +(2/delta)g U_f.
```

Uzáver `L5=0` je iba registrovaný bounded BR3C uzáver skriptu 127. Plná
hierarchia a `lmax` konvergencia zostávajú povinné v C7.8/C7.9.

## Numerika a limity

| Položka | Zmrazená hodnota |
|---|---:|
| solver | `DOP853` |
| `rtol` | `1e-10` |
| `atol` | `1e-14` pre každý stavový komponent |
| `max_step` | `0.02` e-fold |
| segment | najviac `1.0` e-fold |
| interný limit celého skriptu | `50 s` |
| vonkajší limit | `60 s` |
| safety cap | `max(abs(y_i)) < 1e12` |

Každý segment uloží checkpoint. Predĺženie za `x=-18` nie je povolené v
tomto kroku.

## Acceptance kritériá C7.7b

PASS vyžaduje súčasne:

1. autoritatívny vstup 132 skončí machine PASS;
2. všetky štyri trajektórie použijú rovnakú ODE sústavu a dosiahnu `x=-18`;
3. solver hlási úspech v každom segmente a nevznikne timeout;
4. všetkých 13 stavových komponentov a ich RHS je konečných v každom
   checkpointe;
5. žiadny komponent neprekročí safety cap `1e12`;
6. ledger neobsahuje vynechaný alebo ticho nulovaný komponent;
7. výstup obsahuje segmenty, `nfev`, konečný stav a maximum každej zložky.

C7.7b PASS dá `66.5/100`. Nezhoda deep/shallow sama v tomto kroku ešte nie
je FAIL; bude rozhodovať C7.7d. Timeout, solver error alebo prekročenie capu
je `UNCLOSED/REVIEW`, nie automatická fyzikálna smrť.

