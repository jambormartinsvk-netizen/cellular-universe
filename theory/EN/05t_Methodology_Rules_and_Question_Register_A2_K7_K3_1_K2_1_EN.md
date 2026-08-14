# REGISTER 05 — EN addendum for A2-K7.1a-K3.1-K2.1

**Date:** 2026-07-13  
**Status:** binding addendum; existing rules are unchanged

## Duplicate check

AR15 distinguishes reconstruction from microphysics, AR16 requires a local
`Theta`, AR17 requires a complete positive Onsager/noise matrix, and AR18
distinguishes maximum from accepted depth. They do not define the status of
a free dimensionful transport grid or require physically distinct bath
states to branch. AR19 and AR20 are therefore not duplicates.

## AR19 — Dimensional existence on a free transport grid is not microphysics

A positive existence point obtained by choosing dimensionful transport
coefficients proves only that a non-empty consistent region exists. The
coefficient must not be reported as a prediction or fitted to `S_8` until
it is derived from a collision integral or a retarded spectral kernel. If
the coefficient depends on `H`, `rho`, or another state variable, its
perturbation must also be specified before the linear gate.

## AR20 — Thermal, vacuum, and non-thermal baths are separate subtracks

A local thermal/KMS white-noise limit, a vacuum quantum coloured kernel,
and a non-thermal coloured bath must not be silently interchanged. Each
requires its own retarded/noise kernel, memory range, and stress-energy
ledger. Bath energy and pressure must enter the A1 ledger unless an
explicit derivation shows where they have already been counted or
renormalised.

## Q47 — Did K3.1-K2.1 pass the dimensional background gate?

**Status:** `YES, AS AN EXISTENCE TEST ONLY — 39/100.`

Eighteen of 24 grid points passed. Every point with
`ell_hat=1,10,100` had a positive determinant, positive scalar enthalpy,
`|A|<1`, and a bulk correction below 10%. Points with `ell_hat=0.1` failed
only `|A|<1`. However, `ell_hat`, the bath, absolute noise, and the
microphysical kernel were not derived. K7's accepted score remains
`30/100`; K3.1-K2.2-K1 is next.

