# Q22a/Q18 — deriving a function from constraints rather than fitting it

**Purpose:** turn the constraint ledger into a mathematical existence and
uniqueness problem for a steam source or another division product.  
**Status:** `METHODOLOGY PROTOCOL; adds no physical assumption`.

## Core idea

We do not first choose an attractive function `C_s(t)` and then defend it. We
solve the intersection of equations, inequalities, and boundary conditions.
It has only three possible outcomes:

| Intersection result | Meaning |
|---|---|
| one trajectory | the function is derived, provided its input constants are derived too |
| non-empty family of trajectories | the theory permits a class; further laws or independent data must narrow it |
| empty set | the mechanism is physically impossible and the track dies |

If arbitrary width, time, and amplitude remain after all constraints are
applied, it is not a prediction even if one choice agrees with the data.

## Mathematical object to solve

For local product and reservoir states, introduce only abstractly

```text
Y = (rho_s, rho_e, chi, I_1, ...),
dY/dtau = F(Y),
nabla_mu T_s^(mu nu) = +S_s^nu(Y),
nabla_mu T_e^(mu nu) = -S_s^nu(Y).
```

The resulting function is not independently inserted in the homogeneous
limit; it follows as

```text
C_s(tau) = C_s(chi(tau), I_1(tau), ...).
```

If physics contains several genuinely different processes, the result may be
`C_s=sum_j C_s,j`; every term must have its own reservoir and must not debit
the same energy twice. An unknown sum of free bumps is not a derivation.

## How each constraint acts on the final function

| Constraint class | Mathematical effect | What it can determine |
|---|---|---|
| M0 locality | allowed arguments `chi,I_i`, evolution `dchi/dtau` | where the source may turn on/off; forbids free cosmic time |
| M1 ledger | paired sources and `sum Q_A^mu=0` | sign, maximum energy budget, coupling to reservoir |
| M2 positivity | `rho_A>=0`, `H²>0` | forbidden amplitudes and trajectories |
| M3–M5 timing/relic | BBN/CMB boundaries, `rho_s∝a^-4` after source | required early end and allowed integrated source area |
| M6 thermodynamics | second law, temperature, `g_*` | signs and allowed state transitions |
| M7 perturbations | `delta S_s`, frame, noise, correlations | compatibility of background with isocurvature and `P(k)` |
| M8 stability/causality | characteristics, kinetic matrix, rates | excludes runaway, ghosts, and acausal shapes |
| M9 predictiveness | number of derived versus free constants | theory versus fit |
| M10 no `k` in background | homogeneous branch independent of realised mode | separates background function from perturbation transfers |

## Solving order

1. **State existence:** use M0–M1 to specify `Y`, reservoir, and local
   operator. Without this there is no fundamental function, only an effective
   history.
2. **Differential core:** obtain `F(Y)` from conservation, equation of state,
   and microphysics, without a free time profile.
3. **Hard envelope:** turn M2–M6 into inequalities and boundary conditions.
4. **Perturbation filter:** use M7–M8 to discard backgrounds without healthy
   perturbations.
5. **Predictiveness verdict:** M9 counts the remaining free constants.
   Observations may test them; they may not silently replace them.
6. **Only then data:** BBN/CMB/lensing select among pre-allowed solutions or
   exclude the whole non-empty set.

## What is known for steam

Current M1–M5 show that an effective early completed class is non-empty. M0
does not yet specify `chi`, reservoir, or `F(Y)`. We therefore do not yet know
whether constraints lead to one function, a finite family, or none. This is a
precisely localised uncertainty, not a reason to scan free bumps.

## Required output of every future track

Every new mechanism must add:

| Constraint | Equation/inequality recorded | Consequence for function | Status |
|---|---|---|---|

It must conclude with the number of remaining free constants, functions, and
initial conditions. Only this makes it objective whether the constraints have
derived the function.

