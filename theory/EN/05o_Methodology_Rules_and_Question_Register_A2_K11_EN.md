# REGISTER 05 — EN addendum for A2-K11

**Date:** 2026-07-13  
**Status:** binding addendum; existing rules are unchanged

## Duplicate check

P3 already required an adaptive solver, physical bounds, and a convergence
check in general. It did not forbid accepting a result below the solver's
absolute tolerance, forbid a logical convergence bypass, or require an
amplitude-scaling test for a linear system. AR13 is therefore a more precise
new restriction, not a duplicate.

Earlier rules used progress percentages but did not define one common score
for live and dead tracks. AR14 defines audit depth only and changes no older
physical verdict.

## AR13 — A numerical PASS must be resolved, converged, and constraint-safe

A numerical gate must not pass when its tested final amplitude lies below
the solver's absolute tolerance. Convergence conditions must not be replaced
by an expression such as `converged OR result_is_small`. In a homogeneous
linear system, a dimensionless transfer must remain invariant under a common
rescaling of all initial perturbations. A constraint must be assessed
relatively on active points; a small absolute residual with an order-one
relative value is not evidence of conservation.

Each interaction must have its own genuine null limit. A run with another
non-zero coupling must not be called `uncoupled`. If any preregistered gate
fails, a machine `PASS` label is auditorily reclassified as invalid evidence
and the original output is retained.

## AR14 — An N/100 score is audit depth, not probability of truth

A track score reports its furthest documented audit gate. A dead track keeps
its maximum attained score together with its death code and reason; the
number cannot revive it. A live track must state which gates remain. The
common scale is recorded in
`Audit/A2_KATALOG_STAV_SKORE_A_DOVOD_SMRTI_K1_AZ_K11.md`.

## Q42 — Does the corrected script 45 prove superhorizon survival or S8?

**Status:** `NO.`

The audited script-45 revision corrected only the rate factor to `1/E`. Its
submitted minus projector is anti-drag under the stated convention, the
equations are incomplete, the relative `00` residual is `1.0`, and the
result lies below `atol`. Script 53 also rejects amplitude scaling and step
convergence. Script 45 does not compute `S8`.

The physical class of orthogonal momentum transfer therefore continues only
as `A2-K11 SURVIVES THE FORMULATION GATE — 15/100`. Its mandatory next gate
K11.1 is a local operator with a damping sign, a regular `rho_f->0` limit,
and complete constraint-preserving perturbations.

## Restriction of older formulations

- every older script-45 `PASS` formulation now means only that the given
  program revision completed; the physical gate did not pass;
- the sentence in script 51 about an unchanged script 45 applied only to
  the snapshot seen when 51 was created; the current audited revision is
  identified by SHA-256;
- the older Q20 current-state entry point ending at K5 is restricted by the
  newer `Questions/00_READ_FIRST_A2_Q20_AFTER_K11_0.md`.

