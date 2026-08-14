# Addendum to 05 — A2-K4/C7.7c, conditioned activity evidence (EN)

**Date:** 2026-07-14  
**Status:** binding addendum; earlier rules are unchanged

## Duplication check

AR34 addresses conditioning of a constraint derivative, AR35 the natural scale of compensated sources, and AR36 a pre-derived condition bound for tolerances. They do not specify what constitutes valid evidence of dynamical activity when a component source lies below the arithmetic floor of the working precision. AR37 fills only that gap.

## AR37 — Activity below the conditioning floor requires a separate certificate

A component must not be declared active or inactive solely from a double-precision evolution when its precomputed source-to-roundoff-bound ratio is not greater than `1`. Tightening `atol`, extending runtime, or retaining a nonzero JSON key is not evidence. At least one of the following certificates is required:

1. a convergent higher-precision calculation whose initial coefficients use the same precision;
2. an algebraically projected compensated basis with verified zero limit and constraints;
3. an analytic/Puiseux coefficient proof with a nonzero leading term and a closed recurrence.

This does not lower the physical activity thresholds. Numerical non-resolution remains `REVIEW_UNCLOSED`, not a physical death verdict.

## Q64 — How did the later condition audit restrict the old C7.7c wording?

The older wording required all 13 components to pass the activity condition in every one of the four double-precision trajectories. The audit by scripts 155/156 found that the NID total-density source and `h_x` have source-to-roundoff-bound ratios below `0.2` on both deep and shallow surfaces. A single double-precision run therefore cannot be a universal certificate for all 13 components.

The requirement that every component have activity evidence remains unchanged. Only the old implementation requirement — that the same double-precision evolution must certify every component — is restricted. Resolvable components remain numerical; conditioning-limited components must pass AR37.

## Q65 — What is the next A2-K4/C7.7c step?

`C7.7c-K7a`: derive the projected compensated source `D=sum Omega_A delta_A` and momentum `M` directly from the registered equations and higher-precision Puiseux coefficients. No further evolution or score increase above `66.5/100` is allowed before K7a/K7b pass.

## Q99 — What must A2-K4 still pass after K7d?

The later K7d audit closed G0–G7 and raised strict support/WBS to `90/100`;
it therefore restricts the old Q65 answer, which was correct only before
K7a/K7b. Exactly two mandatory gates remain:

1. `C7-G8` — a full photon, polarization, and neutrino Boltzmann hierarchy
   with a separate baryon velocity, Thomson scattering, recombination on the
   exact K4 background, multipole convergence, and Einstein constraints;
2. `C7-G9` — the CMB/S8 likelihood on physics frozen after G8.

A cheap coefficient or early-hierarchy G8 screen awards no points. Only a
full G8 PASS raises support to `95/100` and opens G9. A timeout or backend
error is REVIEW; a physical STOP requires valid numerics and independent
confirmation. The authoritative criteria are in the route document
`G8_FULL_BOLTZMANN/00_PREREGISTRATION.md`.

