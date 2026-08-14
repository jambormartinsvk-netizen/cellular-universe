# REGISTER 05 — EN addendum A2-K12

**Date:** 2026-07-14  
**Status:** binding addendum; older rules remain unchanged

## Duplicate check

Existing AR rules already require total energy conservation, separation of an
absolute transfer from a reference ratio, and retention of dead tracks. No
existing rule explicitly requires a multi-species ash model to separate its
total-density mode from its charge/isocurvature mode or to distinguish
particle production from the force between the particles. AR26 is therefore
not a duplicate.

## AR26 — Multi-species ash must pass both total and relative gates

For two or more ash species, the following must be derived and tested
separately:

```text
sum_i Q_i,
delta_total and theta_total,
independent relative/charge modes,
the G_ij or mu_ij matrix,
production sources C_i.
```

Cancellation of forces or sources in the total mode does not prove stability
unless the relative modes also pass. Nonlinear halo fragmentation or
dispersion is not a substitute for a linear `sigma8` calculation. Opposite
charge is not by itself an energy source: if pair production supplies the
energy, its local operator and backreaction must be derived separately.

## Q52 — Can two oppositely scalar-charged ash species preserve the flow and reduce clustering?

**Status:** `PARTLY; A2-K12 SURVIVES 25/100.`

- K12-K1, an exactly symmetric conformal pair without a production operator,
  is `DEAD M-016 — 25/100`: its net scalar flow vanishes and its total linear
  mode is GR-like.
- K12-K2 with a population asymmetry remains open but red: the flow returns
  together with an unscreened force.
- K12-K3, symmetric pair production plus opposite charges, is the active
  hypothesis at `20/100`. It must derive the production operator and charge
  mode.

### Limitation of the older verbal formulation

The statement “opposite charges reverse the fifth force while also providing
the ash energy transfer” is restricted. Opposite charges can change the force
matrix, but exact symmetry cancels the net scalar background flow. A nonzero
flow into a symmetrically produced pair requires a separately derived
production mechanism.

