# Addendum to 05 — A2-K4.3b-RG, backend zeros and gauge-map order (EN)

**Date:** 2026-07-14  
**Status:** binding addendum; earlier rules are unchanged

## Duplication check

AR31 requires gauge-invariant regularity. It does not specify how to treat
zero rows returned before a numerical backend's internal start, nor how many
source-series orders are required when the target gauge contains
cancellations or Laurent behaviour. AR32 and AR33 fill these two distinct
gaps and do not duplicate earlier rules.

## AR32 — A backend zero prefix is not a physical seed

Before using a solver's time output, its first active perturbation row must be
identified. An exact zero prefix returned before internal initialization is a
placeholder and must not enter a rank, normalization, residual, or physical
verdict.

If the active start cannot be identified unambiguously, the test remains
unclosed.

## AR33 — A gauge transformation requires sufficient series order

A regular source series may be mapped to another gauge only if it contains
every coefficient that survives cancellation in the target quantity. A
finite nonzero time alone does not prove that the source order is sufficient.

If a truncated synchronous NID/NIV series produces a large value or breaks
the null limit after a Newtonian transformation, a higher order must first be
tested or the evolution must remain in a regular gauge. Such an interface
failure is not a physical death.

## Q59a — Did all seven series pass?

**Status:** `PARTIALLY.`

- five collective regular synchronous seeds passed;
- two internal `nu-steam` series passed exactly;
- the general-synchronous K4 test-field response passed;
- the fully back-reacted Puiseux series and common `00/0i/slip/ij` residuals
  are missing.

K4 therefore remains live at `60/100`, but K4.3b is not closed.

## Q60 — Is the internal `nu-steam` PASS unconditional?

**Answer:** No. It applies to S1, where already decoupled steam has the same
collisionless operator as neutrinos and K4 does not couple to it directly. A
direct transfer into the steam hierarchy requires a new kinetic track and a
new audit of rank, compensation, and constraints.

## Q61 — What remains before K4.3b can close?

A back-reacted general-synchronous Puiseux solver must include fuel
stress-energy at `a^(4-3delta)=a^3.93109`, the resulting ash correction at
`a^(5-3delta)=a^4.93109`, and make all seven modes pass `00`, `0i`, slip,
`ij`, the null limit, and two start depths.

