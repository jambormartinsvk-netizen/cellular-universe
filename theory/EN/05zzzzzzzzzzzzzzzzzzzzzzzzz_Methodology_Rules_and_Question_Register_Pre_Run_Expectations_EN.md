# Addendum to 05 — expectations and deviations before a numerical run (EN)

Date: 2026-07-15  
Status: binding addendum; earlier rules remain unchanged

## Duplication check

AR13 requires a resolved, convergent, constraint-aware numerical PASS. AR36 allows a tolerance expansion only from a condition bound derived in advance. AR39 prohibits relaxing a threshold after a cancellation result, and AR53 requires technical smoke tests. A general rule was missing that requires a numerical or qualitative expectation, an allowed deviation, and a post-run distance-from-expectation table before every scientific run. AR54 fills that gap without changing any older threshold.

## AR54 — The expected result and allowed deviation are recorded before the run

Before the first physical or numerical execution of a new script, a dated MD record following `Questions/00_SCRIPT_PRE_RUN_EXPECTATION_TEMPLATE.md` must exist. For every decision-bearing quantity it must state:

- whether the expectation is analytic, regression-based, or exploratory;
- the expected value, interval, sign, order of magnitude, or trend;
- the source of the expectation and independent invariants;
- the numerical and physical allowed deviations when derivable;
- exact PASS, acceptable, REVIEW, and physical kill criteria;
- both internal and external time limits under AR29.

When no numerical expectation can honestly be derived, record `UNKNOWN/EXPLORATORY`; a central value must not be invented. Physical ranges, invariants, safety caps, and the decision procedure must still be preregistered.

After the run, report the observed value, absolute and relative or normalized deviation, and whether it lies inside the preregistered interval. A result inside tolerance may be `ACCEPTABLE_WITHIN_TOLERANCE` only when independent physical gates also pass.

The original expectation and tolerance are never overwritten after seeing the result. A change requires a dated amendment, independent justification, and a new run or subtrack. The original run retains the verdict under its original gate. An unsupported post-hoc change is prohibited.

## Q79 — What expectations apply before the next K4/K7c continuation?

The next fail-closed successor of 175/176 is a regression audit: the physical payload may not change; only missing-rank-key behaviour may change. NID/NIV deep/shallow must reproduce the K7b table, while a synthetically missing key must fail closed.

A clean standalone RK4 rewrite must first reproduce the 184/185 REVIEW, including the ratio near `0.367`; a refactor alone may not manufacture convergence. Only a later term ledger may test the hypothesis that `math.fsum` reduces the `M'` error by at least a factor of ten at every active checkpoint.
