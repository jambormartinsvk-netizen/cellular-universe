# REGISTER 05 — EN addendum for A2-K7.1a-K3.1

**Date:** 2026-07-13  
**Status:** binding addendum; existing rules are unchanged

## Duplicate check

AR15 distinguishes reconstruction from microphysics and AR16 requires a
local `Theta`. They did not require positivity of the full Onsager/noise
matrix or distinguish a subtrack's maximum depth from its parent's accepted
depth. AR17 and AR18 are therefore not duplicates.

## AR17 — Cross dissipation requires a positive full matrix and noise

A scalar cross coefficient between expansion and reaction must not be
audited in isolation. In a near-equilibrium open EFT it must belong to a
full Onsager matrix with a non-negative entropy quadratic form. A non-zero
off-diagonal term requires sufficient diagonal coefficients and, in a local
KMS limit, a positive noise covariance. Reciprocal stress, bulk pressure,
and noise must not be discarded when positivity requires them.

## AR18 — A subtrack's maximum depth does not automatically promote its parent

Every subtrack must carry a `Maximum depth` column. It reports the deepest
performed test, not an automatically accepted parent gate. A parent score
increases only after every acceptance criterion at that level passes. A
dead subtrack retains its maximum depth together with its death reason.

## Q46 — Did K7.1a-K3.1 pass the Onsager/noise gate?

**Status:** `BARE K3 DID NOT; THE COMPLETED SUBTRACK PASSED FORMULATION ONLY.`

K3.1-K1 died as M-014b because `[[0,alpha],[alpha,0]]` has eigenvalues
`±alpha`. K3.1-K2 admits a positive completion with
`ell*zeta>alpha^2` and positive normalised noise over the full grid, but
`ell,zeta,T`, bulk pressure, and the bath have not been derived
microphysically.

Both subtracks have a maximum depth of `38/100`; K7's accepted score remains
`30/100`. The next step is the dimensionful bath/background closure
K3.1-K2.1.

