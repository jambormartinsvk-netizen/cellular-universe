# REGISTER 05 — EN addendum for the A2-K6/M-013 verdict

**Date:** 2026-07-13  
**Status:** binding addendum; existing rules are unchanged

## Duplicate check

P5 already requires the convention and sensitivity of every number. It does
not specifically require a gravitational-coupling matrix to be converted
when the source-density definition changes. AR11 is therefore not a
duplicate; it codifies the audit failure mode exposed by K6. Q40 is a new
status question.

## AR11 — Map the source density before comparing Gij

Before claiming `G_eff/G`, `mu_ij`, or “weaker/stronger gravity”, the audit
must state which density the coefficient multiplies. If a source uses
`rho_c` but the audited background uses `rho_c_hat=A rho_c`, an explicit
conversion is mandatory, for example

```text
mu_cc=G_cc/(A G),
mu_bc=G_bc/(A G).
```

A density redefinition must not be reported as a physical change of
gravity. Both forms and their null limit must remain in the audit record.

## Q40 — Can A2-K6 produce weak physical ash gravity?

**Status:** `CLOSED — NO; A2-K6 IS DEAD M-013.`

For the action
`f=-f1(phi)rho_c+eta Z^2`, the A1 transfer, canonical `G2=X-V`, and the
healthy interval `eta>=0`, the audit finds

```text
mu_cc(eta=0,z=0)=5.674661891,
lim eta->infinity mu_cc(z=0)=163.646709760.
```

Across the complete interval, `mu_cc` is a monotonically increasing
linear-fractional function. The preregistered grid also increases the growth
diagnostic from `1` to `2.160409`. Both null limits pass at `1.776e-15` and
`2.220e-16`; the death is not caused by a sign or null-limit error.

Decisive record:
`Audit/A2_K6_MRTVA_M013_exact_Gij_a_spojity_eta_no_go.md`.

## Restriction of the older status

The K6.0 entry `SURVIVES 40/100; G_eff open` remains evidence that the
background and kinetic gate passed, but it is no longer a current status.
After M-013, the canonical A2-K6 status is only `DEAD`.

The first null-limit machine label in script 48 is restricted by script 49:
its `5.225e-7` discrepancy came from a boundary numerical derivative. The
analytic form passes, while the physical death verdict remains unchanged.

