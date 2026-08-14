# 05 — Methodology and Question Register Addendum: K4/BR3B-2e (EN)

Date: 2026-07-14

This addendum does not alter existing rules.

## AR39 — A PASS cannot be inherited by an unaudited variable

An implementation cross-check applies only to variables explicitly included in the compared vector. If a later calculation requires an omitted stress, shear, or multipole, its coefficient must receive its own Euler/Boltzmann/Einstein audit. A PASS for densities, velocities, and the metric does not automatically transfer to omitted shear.

If primary backends provide different coefficients, prefer the coefficient that simultaneously passes the dynamical equation, the Einstein constraint, and an independent numerical backend. The older formulation is not deleted; its scope is explicitly restricted.

## Q66 — Are the earlier NID/NIV shear sectors regular?

**Status: YES FOR THE FIRST TWO SECTORS; FULL G7 REMAINS OPEN.**

The earliest relative-velocity sectors are exactly compensated metric-null modes. The first shear sectors, NID 5.93109 and NIV 4.93109, have rank 7, exact Bianchi residuals `0,0`, finite solutions, and scaled residuals below `6e-15`. For NIV, the `1/(4Rnu+5)` factor was confirmed by CAMB 1.6.6 and the Euler equation. K4 remains alive at 60/100; the common fuel sector and later `l>=3` recursion remain open.

