# FULL — brána univerzálnosti K4 backgroundu pred adapterom

**Stav:** `STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED / BLOCKS K4 ADAPTER PATCH`  
**Dôvod:** kozmologický background `H(a)` nesmie závisieť od perturbatívneho
Fourierovho módu `k`.

## Zistenie

K7 skript 213 používa pomocnú premennú

```text
z = k a / (H0 sqrt(Omega_r0))
```

a následne `denominator(z)`, `fuel_piece=z^p`, `g2` a `mu`. Niektoré
kombinácie sa naozaj algebraicky skrátia, napríklad `mu*z` a `g2*z^2`.
Pre CLASS adapter však treba dokázať pre **každý** člen expanzného pozadia,
že po dosadení definícií už neobsahuje `k`. Nestačí, že je K7 ODE stabilná
pre zvolený pivot `K_MPC=0.05`.

Najcitlivejší je palivový/power-law člen `z^p` pri `p=3.93109`: ak jeho
normalizácia neobsahuje príslušnú kompenzačnú mocninu `k`, potom by rovnaký
vesmír mal inú expanziu pre iný perturbatívny mód, čo je neprípustné.

## Povinné PASS kritériá

1. odvodiť k‑nezávislé `H_K4(a)` v CLASS jednotkách `Mpc^-1`;
2. explicitne ukázať zrušenie `k` vo všetkých hustotných členoch, vrátane
   paliva, popola a pary;
3. preukázať, že `d tau/da = 1/(a^2 H_K4)` je konečné a kladné;
4. zmapovať dnešnú normalizáciu na deklarované `H0`, `Omega` a energetickú
   bilanciu bez nového fit parametra;
5. až po PASS vytvoriť malý CLASS patch a jeho nulový limit.

## STOP/REVIEW interpretácia

Nesplnenie alebo neurčitosť tejto brány nie je smrť A2-K4, ale
`REVIEW_BACKGROUND_NOT_READY_FOR_BOLTZMANN`. Zastavuje iba FULL adapter,
pretože by bolo nepoctivé vložiť do CLASS pivotovo závislý background.

## Ďalší krok

Read-only symbolický audit K7 background formúl a pôvodu normalizácie
palivového člena. Až po ňom sa rozhodne, či ide o algebraickú redukciu alebo
o samostatnú fyzikálnu vetvu A1-K1.

## Výsledok RUN-FULL-002

Presný audit potvrdil `D(a,k)=1+Omega_m a/Omega_r+k^p A(a)` pri
`p=3.93109`. Súčasná surová formula preto bránou neprešla. Autoritatívny
rozsudok je `ARTIFACTS/RUN_FULL_002_BACKGROUND_UNIVERSALITY_AUDIT.md`.
