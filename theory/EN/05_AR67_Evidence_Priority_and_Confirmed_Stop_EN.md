# Addendum to 05 — evidence priority and confirmed STOP (EN)

**Date:** 2026-07-15  
**Status:** binding addendum; earlier rules remain unchanged  
**New rule:** AR67

## Duplication check

AR30 and C7-W1 separate sequential depth from evidence weight. AR54 requires
a pre-run expectation. AR66 limits a numerical search to the initial
implementation and at most two technical corrections. AR67 changes none of
those rules. It adds only a work-order rule based on physical weight and the
condition under which a numerical discrepancy may become a physical STOP.

## AR67 — Test the high-weight gate first; a physical STOP needs confirmation

When several tests remain open, priority belongs to independent conservation,
Einstein-constraint, stability, causality, degree-of-freedom completeness,
and robust-convergence gates. Auxiliary, tautological, or low-weight metrics
are run only when they can change the decision or diagnose the exact failure
cause. Many green low-weight checks may not hide one red high-weight gate.

A track may not be declared physically dead from a timeout, parser,
checkpoint, single solver, or single tolerance setting alone. A physical STOP
requires:

1. a preregistered physical kill criterion;
2. valid provenance, a finite state, and a numerically resolved signal;
3. reproduction by an independent method, tolerance, or analytic invariant,
   as appropriate to the test;
4. exclusion of known formal failures in the Python error ledger;
5. an audit record of equations, inputs, outputs, hashes, and the exact STOP
   reason.

Confirmation does not authorize unlimited retries. The AR66 budget remains
binding. If the discrepancy can neither be confirmed nor removed inside that
budget, the result is `REVIEW_BLOCKED` followed by an architectural decision,
not another suffix.

## Application to A2-K4 / K7d

The integrated C7-G4+G6+G7 package has priority over the full G8 hierarchy
and G9 likelihood. Its baseline is four NID/NIV × deep/shallow cases. The
whole package may use at most two targeted confirmation or technical
iterations. A reproducible trace/traceless conflict or instability can stop
K7; a timeout alone remains technical REVIEW.

