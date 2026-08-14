# K4 — implicitné mapovanie `D -> H_K4`

**Stav:** `DERIVED_FROM_K7_INTERNAL_DEFINITIONS / NOT_YET_A_UNIVERSAL_BACKGROUND`  
**Nemení skóre ani rozsudok.** Tento zápis iba oddeľuje presnú algebraickú
rekonštrukciu od nezávisle fyzikálne overeného FLRW backgroundu.

## Zdrojové definície K7

V K7 sa používajú súčasne

```text
z = k a /(H0 sqrt(Omega_r0))
s = k / Hconf
s^2 = z^2 / D,
```

kde `Hconf = a H_K4` je konformný Hubbleov parameter a `D` je
`denominator` v skripte 213.

## Presná algebraická rekonštrukcia

Z posledných dvoch vzťahov priamo vyplýva

```text
Hconf_K4^2 = k^2 / s^2 = k^2 D/z^2
            = (H0^2 Omega_r0/a^2) D(a,k),

H_K4^2(a,k) = Hconf_K4^2/a^2
             = H0^2 Omega_r0 D(a,k)/a^4.
```

Teda formálne

```text
H_K4(a,k) = H0 sqrt(Omega_r0) sqrt(D(a,k)) / a^2.
```

Toto je odpoveď na mapovanie `D -> H_K4`: **algebraické mapovanie máme**,
ale bolo doteraz iba rozptýlené v definíciách K7 (`z`, `s`, `s2`), nie
samostatne zaregistrované ako backgroundová rovnica.

## Čo ešte nemáme

1. Nie je to nezávislé odvodenie Friedmannovej rovnice z mikrofyziky siete;
   je to dôsledok interných normalizácií K7.
2. Nie je potvrdené, že symbol `H0` v tomto zápise je súčasne namerané dnešné
   `H_K4(a=1)`. Pre takú interpretáciu musí platiť
   `D(1) = 1/Omega_r0`.
3. Predovšetkým súčasný surový zápis má
   `D(a,k) = 1 + Omega_m a/Omega_r0 + k^p A(a)`, `p=3.93109`.
   Preto dáva `H_K4(a,k)`, nie jedno `H_K4(a)`. To nepovoľuje použiť tento
   zápis ako FLRW background alebo CLASS adapter.

## Rozhodovací dôsledok

Ak sa v K-N1/K-N2 fyzikálne odvodí univerzálny `D_univ(a)`, rovnaké
mapovanie okamžite dá kandidáta

```text
H_K4(a) = H0 sqrt(Omega_r0 D_univ(a))/a^2.
```

Potom musia nasledovať tri samostatné brány: dnešná normalizácia,
kladnosť/konečnosť a energetická bilancia. Bez nich je toto len algebraická
rekonštrukcia, nie vydaná kozmologická predikcia.

## Proveniencia

- `scripts/213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py`,
  definície `z`, `denominator` a `s2`.
- `Questions/A2_K4_BR3C_A_PREREGISTRATION_AND_BREADTH_TRIAGE_DECISION.md`,
  kde je výslovne zapísané `s=k/Hconf`.
- `ARTIFACTS/RUN_FULL_002_BACKGROUND_UNIVERSALITY_AUDIT.md`, ktorý dal
  surovému `D(a,k)` status STOP pre univerzálny background.
