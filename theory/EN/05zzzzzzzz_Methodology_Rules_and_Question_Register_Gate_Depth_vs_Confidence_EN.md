# Addendum to 05 — gate depth versus probability of error (EN)

**Date:** 2026-07-14  
**Status:** binding addendum; earlier rules are unchanged

## Duplication check

AR14 separates the score from probability of truth and AR30 defines the
sequential G1–G10 depth. It had not yet been specified how G8–G10 feed back
into confidence in G7 or how dependent tests must be prevented from being
multiplied as independent evidence. AR37 fills this gap.

## AR37 — Later gates are not automatically independent evidence

A score of `100/100` does not mean a 100-percent probability of correctness.
Any residual-risk assessment must record the provenance of each item of
evidence:

- the same equations, code, data, or calibration are common evidence and
  must not be multiplied as independent tests;
- a new dataset tests a prediction but may not reveal a shared implementation
  error;
- an independent derivation, separate code, blind prediction, and external
  reproduction are stronger and can reduce residual risk;
- a numerical probability must not be called scientifically calibrated
  without a prior and defensible empirical or methodological false-pass rates
  for the gates.

Track depth and the confidence ledger must therefore be maintained separately.

## Q64 — If G8, G9, and G10 pass, what is the probability that G7 is wrong?

**Answer:** It cannot be calculated from the score alone.

If all later gates reuse the same implementation, a fatal G7 error can pass
with them and the residual risk remains unquantified.

If G10 includes a genuinely independent derivation, independent code, blind
or held-out predictions, cross-code agreement, and external reproduction, an
operational auditor estimate of a fatal G7 error may be **below 1%**. This is
a decision estimate, not a measured probability of the theory. The chance of
a minor bug, approximation, or documentation defect remains higher and is
never zero.

## Requirement for the future G10

Using the “below 1%” estimate requires G10 to include at least:

1. a derivation checked by a person or team that did not write the main code;
2. a second implementation that does not copy the numerical core;
3. agreement of physical transfers and likelihoods at predeclared tolerances;
4. at least one prediction locked before validation data are opened;
5. a reproducibility package with version, changelog, and checksums;
6. negative and dead tracks preserved for retrospective audit.

