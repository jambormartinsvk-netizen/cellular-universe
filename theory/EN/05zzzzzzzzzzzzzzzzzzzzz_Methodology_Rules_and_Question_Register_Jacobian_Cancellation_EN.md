# Addendum to 05 — cancellation in Jacobian derivatives (EN)

**Date:** 2026-07-14  
**Status:** binding addendum; earlier rules are unchanged

## Duplication check

AR38 requires the coordinate norm to be named and the FD error to be measured. It does not prescribe the procedure when an algebraically equivalent derivative expression loses digits by catastrophic cancellation, nor does it require failed settings to remain in the audit trail. AR39 fills that gap without changing AR38.

## AR39 — A cancellation repair must preserve the failed trail and the original thresholds

If a small derivative is evaluated by subtracting large nearly equal quantities, it must be compared with an algebraically identical direct form or authoritative higher precision before any further evolution. The failed FD step, formula, parser, and output must be retained as a dead numerical subtrack with a reason. A threshold must not be relaxed after seeing the result; the alternative must be preregistered and run over the same set of surfaces.

A composite verdict must distinguish a historical non-authoritative diagnostic from its replacement evidence and must fail closed when a data path is missing or incorrectly nested.

## Q67 — Which earlier K7a formulations were restricted by the later audit?

The float64 central difference for \(T'\) in script 159 and the expression `ell=2*(q+1)` are not authoritative on deep radiation-era surfaces. The former reached only about `6.28e-6` relative error; the latter differed from the 80-digit reference by `1.51e-9`. The direct form `ell=B'/B` reached about `2e-16` without changing the equations. Script 163 was additionally restricted to an invalid aggregator because it skipped one JSON level; this did not invalidate its physical child results.

