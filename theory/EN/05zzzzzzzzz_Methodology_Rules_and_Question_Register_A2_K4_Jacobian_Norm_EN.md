# Addendum to 05 — A2-K4, Jacobian norm and FD error (EN)

**Date:** 2026-07-14  
**Status:** binding addendum; earlier rules are unchanged

## Duplication check

AR34–AR37 cover constraint derivatives, compensated sources, conditioning bounds for tolerances, and activity certificates. They do not specify a Jacobian norm or a minimum finite-difference error audit. AR38 fills that separate gap.

## AR38 — A Jacobian verdict must state the coordinate norm and differentiation error

`max|J|`, singular values, an SVD condition number, and top couplings must not be called physical invariants without stating the state scale and norm. Under a diagonal transformation `y=S w`, distinguish `J_y` from `J_w=S^-1 J_y S`.

For a linear RHS, prefer a direct coefficient or basis-built Jacobian. If finite differences are used, perform a step sweep or compare against a direct Jacobian, and derive any SVD cutoff from the measured FD error. Eigenvalues are invariant under an exact similarity transformation, but individual numerical eigenvalues of a non-normal matrix may be sensitive; the spectral radius alone is not a complete stability verdict.

## Q66 — How did the later audit restrict the Jacobian claims from 151/152?

The large `max|J|` and SVD values described envelope-coordinate numerics, not the physical Jacobian. The direct physical test gave `max|J_y|=43.535`, while envelope values reached `4.19×10^14`. The condition proxy using a `10^-14` cutoff was withdrawn because the measured FD error at step `10^-7` was of order `10^-10`.
