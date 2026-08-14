# A2-K3 — MŔTVA: prenos rovnobežný s palivom

**ID:** M-010  
**Dátum:** 2026-07-13  
**Stav:** `MŔTVA — ARCHIVOVANÁ`

## Presná koľaj

```text
Q_f^mu=-Gamma rho_f u_f^mu,
Q_c^mu=+Gamma rho_f u_f^mu,
Gamma=lambda H0>0,
w_f=-1+delta,
c_s,f^2=1.
```

## Dôvod smrti

Presné mapovanie `Gamma_ref=-Gamma` dáva veľkoškálový gauge-invariantný relatívny rýchlostný mód s interakčným exponentom

```text
N_K3=(lambda/delta)H0 Delta t.
```

Pracovný bod od rekombinácie do dneška:

```text
lambda/delta=6.5302568568,
N_K3=6.1065536987,
amplification=448.7893835.
```

Kroková konvergencia `9.1895e-9 < 1e-8`; znamienka a nulový limit `10/10 PASS`.

## Podmienka znovuotvorenia

K3 sa nesmie znovu otvoriť zmenou gauge, kroku alebo počiatočnej amplitúdy. Potrebná je nová fyzika odstraňujúca pól `Gamma/(1+w_f)` alebo dokazujúca, že mód nie je fyzickým stupňom voľnosti.

## Artefakty

- `scripts/25_script_A2_K3_superhorizon_velocity_instability.py`;
- `scripts/26_script_A2_K3_equation_sign_and_null_limit_audit.py`;
- `Audit/A2_2_odvodenie_a_test_A2_K3_A2_K4.md`.

