# P5.3b — výsledok adiabatického vedúceho seedu

**Výstup:** `scripts/results/k_mpc_005/RUN_KMPC_006_P5_3B_ADIABATIC_LEADING_SEED_RERUN1.json`  
**Čas / limit:** 0.266 s / 5 s  
**Verdikt:** `PASS_P5_3B_ADIABATIC_LEADING_SEED`

## Odvodený vedúci seed

Pre `h_x=H a^2+...` a radiačné pozadie:

```text
U_f = -H a^2/(52-24 delta),
delta_f = delta U_f,
U_c = -[delta gamma_2 r_0^2 H]/[(12-6 delta)(52-24 delta)] a^(10-6 delta).
```

Všetkých osem algebraických kontrol prešlo. Palivové členy sú regulárne,
`U_c` je vyšší rád a v `gamma→0` zaniká. Staré presné nuly BR2 pri konečnom
štarte preto nie sú odvodený P5 seed.

## Hranica výsledku

Platí iba pre vedúci adiabatický mód v radiačnej asymptotike. Neurčuje
vyššie rády, isokurvatúrne módy, gauge triedu ani stabilitu. Nasleduje
kontrola konečných štartových plôch, potom samostatné odvodenie ďalších módov.
