# Addendum to 05 — prohibition of constraint double counting (EN)

**Date:** 2026-07-14  
**Status:** binding addendum; older rules remain unchanged

## Duplication check

AR13 requires a constraint-aware numerical PASS and AR37 separates dependent
evidence. An explicit rule was missing for DAE evolution in which a
constraint directly defines a derivative. AR45 closes this gap.

## AR45 — A constraint used as an evolution definition is not an independent PASS

If an integrator obtains a metric or other derivative directly from a
constraint, a small residual of the same algebraic expression is a
construction identity, not independent evidence of constraint propagation.
Such a constraint:

- may stabilise DAE evolution;
- must be labelled `enforced`;
- may not receive a second point or independent confidence credit;
- must later be tested through a redundant equation, propagated constraint,
  second gauge, or independent implementation.

Trace/traceless equations not used by the integrator are audited separately.

## Q72 — Did K4 pass early evolution after BR3C-b?

**Answer:** `YES, BUT ONLY C7.7b; 66.5/100.` All four trajectories completed
with finite states and right-hand sides. `00/0i` were enforced and have no
independent PASS; deep/shallow agreement, trace/traceless residuals, and
convergence remain open. The large deep-NIV `nfev` is a mandatory numerical
risk for the next audits.

