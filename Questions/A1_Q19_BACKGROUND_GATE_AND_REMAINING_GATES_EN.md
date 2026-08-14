# A1/Q19 — meaning of “passed only the background gate”

**Updated:** 2026-07-13  
**Track:** A1-K1 — transfer `Q` creates only CDM/ash; baryons are conserved  
**Current verdict:** **SURVIVES 40/100 — cosmological-background candidate only**

## 1. Short answer

“Passed the background gate” means that the equations consistently describe the evolution of **homogeneous mean densities** in an FLRW universe. This test contains no spatial density contrast `delta rho(x,t)`, velocity field, gravitational potentials, CMB, or galaxy growth.

The bookkeeping of mean energy has passed. The physics of an inhomogeneous universe has not.

## 2. What was tested and passed

Working definition:

```text
nabla_mu T_f^(mu nu) = -Q^nu
nabla_mu T_c^(mu nu) = +Q^nu
nabla_mu T_b^(mu nu) = C_b^nu
nabla_mu T_r^(mu nu) = C_r^nu

Q^nu = Gamma rho_f u_c^nu
Gamma = lambda H0
C_b^nu + C_r^nu = 0
```

The homogeneous equations tested were:

```text
rho_f' = -3 delta rho_f - lambda(H0/H) rho_f
rho_c' = -3 rho_c + lambda(H0/H) rho_f
rho_b' = -3 rho_b
rho_r' = -4 rho_r
```

| Background test | What it verified | Status |
|---|---|---|
| A1-K1-T0 | Recipient, flow direction, and signs are unambiguous. | **PASS** |
| A1-K1-T1 | Source `-Q+Q` cancels exactly in the sum of mean equations. | **PASS** |
| A1-K1-T2 | `Q=Gamma rho_f` has dimensions of energy density per time. | **PASS** |
| A1-K1-T3 | At `lambda=0`, the non-interacting limit `rho_b,rho_c proportional a^-3` is recovered. | **PASS** |
| A1-K1-T4 | Splitting total matter into baryons and CDM is algebraically consistent with the background in scripts 08/09. | **PASS** |
| A1-K1-T5 | Densities remain positive; conservation and numerical convergence meet their tolerances. | **PASS** |
| A1-K1-T6 | Late cellular transfer does not change comoving baryon number. | **STRUCTURAL PASS** |

Reproducible evidence:

- `scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py`;
- `scripts/STATUS_A1_K1_SCRIPTS_11_13.md`;
- failed scripts 11 and 12 are preserved with errata.

Reference result at the working point:

- approximately `8.999%` of today's comoving CDM was produced after recombination;
- the baryon fraction in matter fell from about `0.15644` at recombination to `0.14439` today;
- this is a consequence of the working implementation, not a confirmed measurement.

## 3. Why the background is insufficient

In an exactly homogeneous FLRW background, all components share the same cosmological rest frame. Several physically distinct transfers `Q^mu` can therefore lead to the same mean-density equation.

Perturbations reveal:

- how the transfer changes in overdense and underdense regions;
- where momentum goes;
- how baryons and CDM move;
- whether instabilities arise;
- what happens to the CMB, `P(k)`, lensing, and `S8`.

A background PASS therefore does not prove that the full four-vector `Q^mu` has been chosen correctly.

## 4. Remaining gates

### G2 — A2.0: covariant ledger

For each component, specify:

- `rho_A`, `p_A`, and `w_A`;
- four-velocity and rest frame;
- rest-frame sound speed;
- pressure perturbation and anisotropic stress;
- energy part `Q_A` and momentum part `F_A^mu` in

  `Q_A^mu = Q_A u^mu + F_A^mu`, `u_mu F_A^mu=0`;

- the identity `sum_A Q_A^mu=0` away from the homogeneous background.

**Kill condition:** a missing recipient of energy/momentum or a hidden reservoir required without opening a new track.

### G3 — A2.1/A2.2: linear perturbations

Derive:

1. `delta Q` from the local transfer definition, rather than choosing it freely;
2. continuity and Euler equations for fuel, CDM, and baryons;
3. metric constraints;
4. fuel pressure perturbation and sound speed for `w_f=-1+delta`;
5. gauge-invariant observables;
6. adiabatic and any isocurvature initial modes.

Mandatory tests:

| Test | Requirement | Status |
|---|---|---|
| A2-T0 | Unambiguous notation, signs, metric, and Fourier convention. | **WAITING** |
| A2-T1 | `sum_A Q_A^mu=0` at background and perturbation level. | **WAITING** |
| A2-T2 | `lambda->0` recovers standard CDM+baryon perturbations. | **WAITING** |
| A2-T3 | Physical observables are gauge-invariant. | **WAITING** |
| A2-T4 | The superhorizon limit is regular and the evolution of `zeta` is explained. | **WAITING** |
| A2-T5 | The subhorizon limit gives the correct growth equation. | **WAITING** |
| A2-T6 | No ghost, gradient, or uncontrolled early-time instability. | **WAITING** |
| A2-T7 | Densities, sound speeds, and denominators remain physical. | **WAITING** |
| A2-T8 | Initial conditions contain no hidden arbitrary mode. | **WAITING** |

**Main wall:** a confirmed ghost, gradient, or uncontrolled superhorizon instability in the parameter region required by the theory.

### G4 — A2.3: numerical perturbation validation

After deriving the equations, create:

- `scripts/21_script_A2_perturbation_limit_and_stability_tests.py`;
- `scripts/README_AUDIT_SCRIPT_21.md`;
- frozen inputs and outputs.

The script must test the null limit, energy/momentum balance, early times, the range of `k`, singularities, and tolerance convergence.

**Status:** **WAITING; script 21 does not yet exist.**

### G5 — A3: Boltzmann implementation

After a positive A2 result, implement the model in a frozen version of CLASS or CAMB:

1. first reproduce standard LambdaCDM spectra in the same code;
2. enable A1-K1 without an additional drag parameter;
3. compute the background, CMB `C_ell`, matter power `P(k)`, lensing, and growth;
4. test convergence and independent limits.

**Status:** **BLOCKED BY A2.**

### G6 — Q31: ash microphysics

Determine:

- spin and mass;
- stability and quantum numbers;
- distribution function and coldness;
- free streaming and phase-space bounds;
- halo and cluster behavior;
- allowed interactions.

**Status:** **OPEN.** A background equation does not prove that such a particle or excitation can exist.

### G7 — A8: preregistered full data fit

After A2/A3, freeze in advance the datasets, covariance, nuisance parameters, priors, parameter count, statistical threshold, and validation set. The required joint test includes at least CMB, BAO, SN, RSD, weak lensing, `H0`, `Omega_m`, `S8`, and baryon fractions.

The approximately `8.999%` late-created CDM must be tested explicitly.

**Status:** **BLOCKED BY A2+A3.** The local `chi2_3front` is not a substitute for this gate.

## 5. Status map

| Gate | Area | Status |
|---|---|---|
| G1 | Homogeneous background and numerics | **PASSED** |
| G2 | Covariant ledger beyond the background | **WAITING — next step** |
| G3 | Analytical linear perturbations and stability | **WAITING** |
| G4 | Numerical perturbation test | **WAITING** |
| G5 | CLASS/CAMB and spectra | **BLOCKED BY G3/G4** |
| G6 | Ash microphysics | **OPEN parallel branch** |
| G7 | Full data fit | **BLOCKED BY G5** |

## 6. Why the rating is 40/100

The rating expresses **evidence maturity, not a 40% probability of truth**.

- recipient and sign definition: complete;
- conservation, dimensions, null limit, and background positivity: complete;
- reproducible background numerics and convergence: complete;
- perturbations and stability: missing;
- CLASS/CAMB spectra: missing;
- ash microphysics: missing;
- full data fit: missing.

If A2 reaches a wall, A1-K1 is marked `DEAD — ARCHIVED`, and the next track A1-K4, A1-K5, A1-K2, or A1-K3 is opened in the registered order. The background success remains preserved as a negative lesson: consistent mean bookkeeping is insufficient for consistent perturbation physics.

## 7. Authoritative sources

- `Questions/A1_Q19_problem_prijemcu_Q_kolaje_K1-K5.md` — original problem, tracks, and T0–T8 tests;
- `scripts/STATUS_A1_K1_SCRIPTS_11_13.md` — reproducible background numerics;
- `Questions/00_AKCNY_PLAN_v3.18_AKTUALNY_2026-07-13.md` — A2/A3/A8 breakdown;
- `theory/EN/05c_Methodology_Rules_and_Question_Register_v3.18_ADDENDUM_EN.md` — Q19/Q20 state in the main rules and question register.

