# A2-K1 — finálny záznam mŕtvej koľaje

**Stav:** `MŔTVA — ARCHIVOVANÁ`  
**Dátum:** 2026-07-13

## Presná hypotéza

```text
Q_f^mu = -Gamma rho_f u_c^mu,
Q_c^mu = +Gamma rho_f u_c^mu,
Gamma=lambda H0,
lambda=0.15,
w_f=-1+delta,
delta=0.02297,
c_s,f^2=1,
pi_f=0.
```

## Test, ktorý neprešla

A2-T4: regulárny superhorizontový limit bez nekontrolovaného rastúceho módu.

## Dôvod smrti

Veľkoškálový gauge-invariantný relatívny rýchlostný mód obsahuje interakčný rast

```text
d ln R/dt = 2 Gamma/delta.
```

Pre pracovné parametre je `Gamma/(H0 delta)=6.5303`. Na validovanom backgrounde od rekombinácie do dneška vznikne exponent `12.2131` a zosilnenie približne `2.014e5`.

## Analytický dôkaz

`Audit/A2_1_linearne_perturbacie_Einsteinove_constrainty_a_superhorizontovy_test.md`

## Skripty

- `scripts/22_script_A2_K1_superhorizon_velocity_instability.py`;
- `scripts/23_script_A2_K1_superhorizon_velocity_instability_converged.py`;
- `scripts/24_script_A2_K1_equation_sign_and_null_limit_audit.py`.

## Čo verdikt nezabíja

Background A1-K1 ani alternatívne perturbačné koľaje A2-K3 až A2-K5.

## Podmienka novej koľaje

Musí sa zmeniť smer/štruktúra štvorvektora, časová závislosť odvodená z mikrofyziky alebo kinetická štruktúra paliva. Iná gauge, menší krok alebo ručné nulovanie módu nestačí.

