# REGISTER 05 — EN addendum after the A2-K1 through A2-K5 retrospective

**Date:** 2026-07-13  
**Status:** binding addendum; older rules remain unchanged

## Duplicate check

AR18 already defines maximum depth as the deepest executed test and forbids
automatic promotion of a parent. AR3 and the erratum rules retain dead tracks
and faulty verdicts. No existing rule explicitly separates absolute transfer
from a ratio to a dynamically decaying null reference. AR25 is therefore not
a duplicate.

## AR25 — Absolute transfer and gain relative to a reference are different gates

A mode test must report separately

```text
T_abs=|y_final/y_initial|,
T_null,
G=T_abs/T_null.
```

If `T_null` strongly decays, a large `G` does not by itself prove large
absolute growth. A final kill verdict must not rely only on `G>e` unless a
pre-derived physical link connects that ratio to a divergence, loss of
linearity, or an observational bound. An instantaneous eigenvalue of a
sub-block must likewise not be identified with the global exponent of the
complete time-dependent system.

## Q51 — Are the A2-K1 through A2-K5 depths and verdicts correct after the retrospective?

**Status:** `PARTLY.`

- K1 `45/100`, K2 `25/100`, K3 `45/100`, and K5 `75/100` are confirmed.
- K4 retains maximum depth `50/100`, but M-011 is suspended.
- K4 is not declared viable; it awaits the complete K4.1 mode basis.

### Limitation of older formulations

The older statement “K4 has 11.5901 e-folds of instability” may now only be
read as `ln(T_K4/T_null)=11.5901`. The absolute result is
`ln(T_K4)=0.4620`. The historical M-011 entry and scripts are retained with
an erratum.

