# REGISTER 05 — EN addendum for A2-K7.0

**Date:** 2026-07-13  
**Status:** binding addendum; existing rules are unchanged

## Duplicate check

Earlier rules required an explicit mediator and a closed ledger. They did
not state that a positive mediator density must be included in the already
registered background and its enthalpy budget. AR12 is therefore not a
duplicate. Q41 updates the previously waiting K7 status.

## AR12 — A dynamical mediator must not be hidden from the background

Every explicit mediator with its own `T_M^{mu nu}` must report `rho_M`,
`p_M`, its enthalpy, and its place in the Friedmann equation. If the original
total sector `rho_F,p_F` is to remain unchanged, then

```text
rho_F=sum_i rho_i,
p_F=sum_i p_i,
rho_F+p_F=sum_i(rho_i+p_i).
```

A positive `rho_M` must not be added on top of the original `H(z)` or
discarded as “virtual” when it carries linear energy or momentum. If an
effective transfer follows from coarse-graining a local action, the audit
must retain the memory/noise term or justify a Markovian limit.

## Q41 — Did A2-K7 pass its first action and ledger gate?

**Status:** `YES — SURVIVES K7.0, 30/100.`

For a dust-like massive mediator and the exact A1 background, the audit
derives

```text
0<epsilon<delta=0.02297,
Q2=Gamma rho_F,
Q1=(1-epsilon)Gamma rho_F+3H epsilon(1-delta)rho_F.
```

The maximum ledger residual is `2.220e-16`. The donor-aligned collision
matrix has only `-R1,-R2<0` eigenvalues; no local anti-damping is found.
However, the ash collision-only mode is damped only by a factor `0.9100`
from recombination, and the microphysical origin of `Q1,Q2` remains open.

Decisive record:
`Audit/A2_K7_0_akcna_ledgerova_a_collision_brana.md`.

## Restriction of the older status

The catalog entry `WAITING` is the historical state before this gate. The
canonical status is now `SURVIVES K7.0 — 30/100`; it must not be shortened
to “stable” or “solves S8”.

