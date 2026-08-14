# A16. Covariant embedding of the V1 equations (interacting two-fluid system)

**Purpose of this section:** to show that the V1 background system is not
a set of ad-hoc rules standing outside general relativity, but the exact
FRW limit of a standard covariant class of interacting dark-energy
models. The Bianchi identity is satisfied identically, not by
declaration. What remains model-specific is the *microscopic
interpretation* of the two constants (δ, λ), which lives one level
below this description — as kinetic theory lives below Navier–Stokes.

## A16.1 The covariant system

Let the fuel, matter and radiation components carry stress-energy
tensors T_f^{μν}, T_m^{μν}, T_r^{μν} with equations of state
w_f = −1 + δ, w_m = 0, w_r = 1/3, and let energy be exchanged through
a transfer current:

    ∇_μ T_f^{μν} = −Q u^ν
    ∇_μ T_m^{μν} = +Q u^ν
    ∇_μ T_r^{μν} = 0
    Q = λ H₀ ρ_f

where u^ν is the common comoving four-velocity. The sum gives

    ∇_μ (T_f + T_m + T_r)^{μν} = 0

**identically** — total energy-momentum is conserved by construction,
the Bianchi identity holds, and Einstein's equations
G_{μν} = 8πG T^tot_{μν} are consistent. This answers the question
"where does δ appear in Einstein's equations": in T_f^{μν} through
w_f = −1 + δ, and λ in the exchange current Q.

## A16.2 FRW limit reproduces V1 exactly

In a flat FRW background with x = ln a and ρ̇ = H·dρ/dx, the continuity
equations become

    dρ_f/dx = −3(1 + w_f) ρ_f − (Q/H)  = −3δ ρ_f − λ (H₀/H) ρ_f
    dρ_m/dx = −3 ρ_m + λ (H₀/H) ρ_f
    dρ_r/dx = −4 ρ_r

which, divided by the critical density today, are precisely the V1
equations used in the pipeline (script 09). Nothing was added or
removed in the translation.

## A16.3 Position within the literature

The system belongs to the standard, extensively studied class of
interacting dark-energy models with transfer rate Q = Γ ρ_DE and
**constant** Γ = λH₀. The cellular universe selects one member of this
class and, unlike generic phenomenology, ties its two constants to
microphysics: δ = 1/(⟨k⟩ + C) from the division overhead (measured
in-model, Q2/Q9) and λ from scar catalysis (V1 derivation, Q3). At the
level of this section, however, δ and λ function as ordinary constants
of a covariant effective description — no departure from GR is
involved anywhere in the background dynamics.

## A16.4 Perturbations: the transfer choice, stated aloud

Any interacting model must specify how the exchange current enters the
perturbed equations. The pipeline uses the **geodesic (momentum-free)
transfer** choice: Q^ν = Q u^ν with u^ν the matter rest-frame velocity,
i.e. created matter is born comoving with the local flow and the
exchange carries energy but no momentum into the perturbations. Under
this choice the linear growth equations retain their standard form
(section V3), and the entire effect of the cellular sector on structure
growth enters through the background functions E(x) and Ω_m(x) alone.

This is a *choice with a surface trace*: a momentum-carrying transfer
would add a fifth-force-like term to the Euler equation and distort
redshift-space distortions. The present formulation predicts no such
distortion beyond the background effect; a confirmed RSD anomaly
requiring momentum transfer would falsify this reading of the
exchange, not merely re-parametrize it.

## A16.5 What this section does and does not claim

It **does** establish: the V1 system lives inside general relativity
as a covariant interacting two-fluid model; Bianchi is exact; the
background phenomenology (w(z) accounting shadow, H₀, the fuel era)
requires no modification of Einstein's equations.

It does **not** provide: a fundamental Lagrangian for the network
itself, or a derivation of δ and λ from an action. Those remain at
the microdynamic level (VCM measurements and the V1 term-by-term
derivation), registered honestly as such.
