# A16-K1. Covariant embedding of V1 for the track “Q creates CDM only”

**Candidate version:** v3.18 draft  
**Track:** A1-K1  
**Track status:** SURVIVES the background tests; perturbations await A2  
**Scope:** covariant effective description of the homogeneous background, not a fundamental network action

## A16-K1.1 Purpose and claim boundary

This section shows that the V1 background equations can be written as a covariant system of interacting effective fluids in general relativity. The total stress-energy tensor is conserved identically.

The section also removes the ambiguity in the original combined “matter” component: only CDM/ash receives the cellular transfer Q. Baryons do not receive this late-time transfer.

This embedding does not prove a microscopic network action, the origin of the parameters δ and λ, or the validity of the original V3 growth equation.

## A16-K1.2 Components

The total stress-energy tensor is

```text
T_tot^{μν} = T_f^{μν} + T_c^{μν} + T_b^{μν} + T_r^{μν}.
```

At the homogeneous-background level, the components obey:

| Component | Meaning | Equation of state |
|---|---|---|
| f | fuel | `p_f = (-1 + δ) ρ_f` |
| c | CDM/ash | `p_c = 0` |
| b | baryons | `p_b ≈ 0` |
| r | relativistic components | `p_r = ρ_r/3` |

For each perfect fluid and metric signature `(-+++)`, we use

```text
T_i^{μν} = (ρ_i + p_i) u_i^μ u_i^ν + p_i g^{μν}.
```

The four-velocities are comoving on an exactly homogeneous FRW background. They generally differ at perturbative order.

## A16-K1.3 Transfer four-vector

Define the constant effective rate

```text
Γ = λ H₀
```

and the local transfer scalar

```text
Q = Γ ρ_f.
```

Track A1-K1 chooses

```text
Q^ν = Q u_c^ν.
```

The covariant equations are

```text
∇_μ T_f^{μν} = -Q^ν
∇_μ T_c^{μν} = +Q^ν
∇_μ T_b^{μν} = C_b^ν
∇_μ T_r^{μν} = C_r^ν

C_b^ν + C_r^ν = 0.
```

The terms `C_b^ν` and `C_r^ν` represent standard collision processes between baryons and radiation only. They are not part of the cellular transfer Q. Their net background energy exchange is neglected in V1; a precise Boltzmann calculation must use the standard CLASS/CAMB collision terms.

Summing the equations gives

```text
∇_μ T_tot^{μν} = -Q^ν + Q^ν + C_b^ν + C_r^ν = 0.
```

Total energy and momentum are therefore conserved by construction. Einstein’s equations with this total source are compatible with the Bianchi identity at the effective-description level.

The constant H₀ in `Γ = λH₀` is used here as a fixed calibration scale with dimensions of inverse time. Covariance of the equations does not explain its microscopic origin.

## A16-K1.4 FRW limit

For a flat FRW background, `x = ln a`, a prime `d/dx`, and `H = ȧ/a`, the equations become

```text
ρ_f′ = -3δ ρ_f - λ(H₀/H)ρ_f
ρ_c′ = -3ρ_c + λ(H₀/H)ρ_f
ρ_b′ = -3ρ_b
ρ_r′ = -4ρ_r.
```

Their sum is

```text
ρ_tot′ = -3δρ_f - 3ρ_c - 3ρ_b - 4ρ_r.
```

With

```text
p_tot = (-1 + δ)ρ_f + ρ_r/3,
```

the right-hand side is exactly

```text
-3(ρ_tot + p_tot).
```

The transfer terms cancel with opposite signs. Energy removed from the fuel is added to CDM.

## A16-K1.5 Dimensionless variables

For numerical work, a density normalized by today’s critical density should be distinguished from the instantaneous density fraction:

```text
X_i(x) = ρ_i(x)/ρ_crit,0
E(x) = H(x)/H₀
Ω_i(x) = X_i(x)/E²(x).
```

For a flat model,

```text
E² = X_f + X_c + X_b + X_r.
```

The evolution equations are

```text
X_f′ = -3δX_f - λX_f/E
X_c′ = -3X_c + λX_f/E
X_b′ = -3X_b
X_r′ = -4X_r.
```

Current scripts sometimes use `Om` for X-type variables. Version 3.18 must state this convention explicitly or rename the variables to prevent confusion with the instantaneous `Ω_i(x)`.

## A16-K1.6 Exact relation to the original V1 system

Define

```text
X_m = X_b + X_c.
```

Then

```text
X_m′ = -3X_m + λX_f/E.
```

This is exactly the original V1 background equation and the equation used in script 09. Splitting the combined matter component therefore leaves the existing background calculation unchanged.

The split is nevertheless physically required for baryon loading of the sound horizon, CMB peak heights, baryon-photon oscillations, the perturbations `δ_b` and `δ_c`, and the present baryon fraction. Script 09 consequently remains a background test only.

## A16-K1.7 Physical interpretation of baryons

The late-time term `Q = λH₀ρ_f` creates CDM/ash, not baryons. After the early baryogenesis epoch has ended, this term does not change the comoving baryon number.

The description of ordinary matter arising from a “rare failure” may remain as a candidate microphysics for an early baryogenesis channel. It must, however:

1. operate before BBN,
2. generate the observed baryon asymmetry,
3. respect electric neutrality and quantum numbers,
4. cease to act as a late source in the baryon continuity equation.

This early mechanism is not derived in A16-K1.

## A16-K1.8 Perturbations: what follows and what does not

The choice

```text
Q^μ = Q u_c^μ
```

sets the projection of the transfer orthogonal to the CDM four-velocity to zero. CDM therefore receives no extra momentum transfer in its own rest frame, and this transfer does not produce a new fifth-force-like term in the CDM Euler equation.

It **does not follow** that the complete linear growth equations retain their standard form. The CDM density-contrast continuity equation generally contains interaction terms. Step A2 must specify:

- the perturbation of the local transfer scalar `δQ`,
- fuel perturbations and its rest-frame effective sound speed,
- any anisotropic stress,
- the gauge and gauge-invariant combinations,
- initial conditions,
- superhorizon, gradient, and ghost stability.

The original statement that “the entire effect enters only through E(x) and Ω_m(x)” is not used in this track. The V3 growth equation remains an unverified approximation until it passes A2.

## A16-K1.9 Test status

Track A1-K1 has passed:

- the analytic conservation sum,
- dimensional and sign checks,
- the `λ → 0` limit,
- algebraic agreement with the backgrounds of scripts 08 and 09,
- positivity of all densities down to `x = -25`, approximately `z = 7.2×10^10`.

At the working point `H₀ = 66.37`, `Ω_m0 = 0.3517`, `λ = 0.15`, `δ = 0.02297`, every density remained positive. The background indicates that about 9% of today’s comoving CDM density is created after recombination. This consequence still requires a full data test.

## A16-K1.10 Audited claim scope

This section **does establish**:

1. the A1-K1 background has a covariant effective formulation within GR,
2. the total stress-energy tensor is conserved identically,
3. the original combined V1 equation follows by summing baryons and CDM,
4. the late cellular transfer creates CDM only.

This section **does not establish**:

1. a fundamental network action,
2. a microscopic derivation of Γ, δ, or λ,
3. baryogenesis,
4. standard perturbation growth,
5. stability of the full perturbation system,
6. agreement with a full CMB+BAO+SN+RSD+lensing likelihood.

## A16-K1.11 Primary methodological references

- [De-Santiago, Wands, and Wang: Inhomogeneous and interacting vacuum energy](https://arxiv.org/abs/1209.0563) — different covariant interaction choices lead to different perturbations and observable spectra.
- [Martinelli et al.: Constraints on the interacting vacuum — geodesic CDM scenario](https://arxiv.org/abs/1902.10694) — an example of a complete linear analysis for a geodesic CDM interaction.
- [Planck 2018: Cosmological parameters](https://arxiv.org/abs/1807.06209) — the CMB distinguishes baryon and CDM densities.

These sources support the mathematical methodology of the effective model. They do not prove the cellular microphysics.
