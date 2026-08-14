# REGISTER 05 — EN addendum for A2-K7.1a-K3

**Date:** 2026-07-13  
**Status:** binding addendum; existing rules are unchanged

## Duplicate check

Earlier rules required local covariance and perturbing a transfer scalar.
They did not explicitly require a background `H` in a dissipative law to be
replaced by a particular local expansion scalar, followed by perturbing its
reference frame. AR16 fills that gap.

## AR16 — Every interaction H needs a local frame and delta Theta

When an effective law contains `H`, the audit must identify whether it means
`Theta_A/3=nabla_mu u_A^mu/3` for a particular component or another local
geometric scalar. A non-local present-day or background-only `H` must not be
used without a covariant definition.

After choosing `Theta_A`, the transfer perturbation must contain its full
`delta Theta_A`, including velocity and metric parts. In Newtonian gauge for
a perfect donor,

```text
a delta Theta_A=theta_A-3Phi'-3Hconf Psi.
```

Passing this formulation check does not establish microphysical origin or
the absence of noise.

## Q45 — Did the expansion-scalar track K7.1a-K3 pass?

**Status:** `THE FORMULATION GATE ONLY; NO SCORE INCREASE.`

Script 57 proves the FRW reduction, the gauge transformation of `delta Q1`,
and exact vector-ledger cancellation. It also finds
`R1~Gamma/epsilon`, so the `epsilon->0` limit remains singular. Neither a
CTP kernel nor a noise correlator has been derived.

K7 remains `SURVIVES 30/100`. K3.1 is next; failure gives K3 the M-014b
verdict.

## Restriction of the older formulation

The K7.0 term `3H epsilon(1-delta)rho_F` must no longer be perturbed as a
fixed background number. In K3 it means
`epsilon(1-delta)Theta_phi rho_F` and carries the mandatory
`delta Theta_phi`.

