# Addendum to 05 — A2-K4.3b-BR, residual conditioning and mode-dependent Puiseux orders (EN)

**Date:** 2026-07-14  
**Status:** binding addendum; earlier rules are unchanged

## Duplication check

AR32 addresses a backend zero prefix and AR33 the sufficient order of a gauge
map. They do not define conditioning of Einstein derivatives, the scale for
compensated species sources, or when a tolerance may be relaxed. AR34–AR36
fill these three distinct gaps without duplication.

## AR34 — A constraint verdict must respect derivative conditioning

A deep-radiation test must not issue a physical `FAIL` solely from a raw
finite second metric derivative multiplied by a large `Hconf^2`. It must use
at least one stable alternative: a constraint DAE formulation, an analytic
Bianchi derivative of the product ledger, or demonstrated convergent higher
precision. The unsuitable derivative remains archived as a numerical REVIEW.

## AR35 — Compensated sources are formed on their natural scale

For NID, NIV, and internal species modes, total `delta rho`, momentum, and
shear must not be formed by subtracting raw `X_A ~ a^-4` values when this
destroys valid digits. Use `Omega_A=X_A/E^2`, higher precision, or an
algebraically projected compensated basis. A physical verdict must not rest
on catastrophic cancellation.

## AR36 — A tolerance may be widened only by a pre-derived condition bound

A fixed tolerance for a named compensated ledger may be replaced only by a
bound derived from `sum(abs(species components))`, machine epsilon, and a
declared operation-count allowance. The bound must be computed before the
residual is interpreted, apply only to the named equations, and must not
weaken the other gates globally.

## Q61a — Current K4.3b status after BR3A

**Status:** `BR1 PASS; BR2 PASS; BR3A PASS; K4.3b UNRESOLVED.`

Seven early modes passed two depths, four Einstein equations, and two
conservation ledgers. Five collective modes passed their mode-dependent
Puiseux sources. The induced fractional metric/species coefficient and the
full photon/polarization/recombination implementation are still missing.

## Q62 — How did the later audit restrict the old exponents 3.93109 and 4.93109?

They remain correct for the background prefactors `Omega_f` and
`(Gamma/H)(rho_f/rho_c)`. They are not universal final perturbation
exponents. A complete source also carries the leading power of its seed. The
verified pressure orders for AD/CDI/BI/NID/NIV are `5.93109`, `4.93109`,
`4.93109`, `6.93109`, `5.93109`; the ash-transfer orders are `6.93109`,
`4.93109`, `5.93109`, `7.93109`, `6.93109`.

## Q63 — What is the next decision step?

`BR3B`: solve the induced fractional coefficients of the metric and every
gravitating species, then coefficient-test all four Einstein equations.
Without BR3B and the full photon backend gate, neither G7 nor a score above
`60/100` may be awarded.

