# REGISTER 05 — EN addendum for the new A2-K11 revision

**Date:** 2026-07-13  
**Status:** binding restriction of Q42; existing rules are unchanged

## Duplicate check

No new rule is added. AR13 is applied to the new script-45 revision, while
Q43 records which older objections were fixed and which remain.

## Q43 — Did `atol=1e-16`, `rtol=1e-12`, and the new step test change K11's verdict?

**Status:** `NUMERICALLY IN PART; PHYSICALLY NO.`

Hash `973905...` has a final transfer `1.99286e-13` above `atol`, a step
metric `7.59611e-7`, a `k` metric `1.72964e-7`, and an amplitude metric
`1.40315e-7`. Those numerical objections are closed in favour of the new
revision.

The pointwise test nevertheless locates the maximum at `a=9.17247e-4`, not
at the near-zero final state. All constraint terms have the same sign and
the pointwise relative residual is `1.0`. Amplitude scaling increases the
absolute residual from `8.25515e-10` to `825.515`, so this is not
noise divided by noise.

One damped initial vector does not prove stability of every mode, and the
script does not compute `S8`. The canonical status remains
`A2-K11 SURVIVES THE FORMULATION GATE ONLY — 15/100`.

## Restriction of Q42

Q42 remains `NO`, but its “below atol” and “failed step” reasons apply only
to the older hash `61558...`. For the current hash `973905...`, the decisive
issues are the non-closed equations, incorrect sign map, pointwise
constraint failure, and the missing all-mode test.

## Q55 — Does the new script 47 rescue A2-K11?

**Status:** `NO; THE SCRIPT-47 PASS IS INVALID EVIDENCE.`

No new rule is added: AR13, AR14, and AR28 apply. Script 47 is not a new
track because it does not change K11's operator or degrees of freedom.

The audit reproduced its numbers but found:

- a hybrid of the barotropic `c_s^2=w` coefficient and a `c_s^2=1`
  pressure term;
- proper-time rates proportional to `1/(aE)` instead of `1/E`, producing an
  early factor of `1090.9`;
- incomplete continuity equations and an incorrect energy recoil;
- reversed constraint signs;
- a pointwise relative `00` residual effectively equal to `1.0`;
- amplitude scaling that is automatic for a homogeneous linear ODE.

K11 remains at `15/100`; M-015 is not issued. The older description of
script 47 as a “fully consistent Einstein test” is restricted by
`Audit/A2_K11_AUDIT_SCRIPTU_47_GEMINI_NAVRHU.md`.

