# Constraint feasibility gate — non-empty intersection of constraints

**Working identifier:** `FS-GATE-01`  
**Layer:** `tracks/`; `WORKING / NOT_RELEASED`  
**Date:** 2026-07-16  
**Amended:** 2026-07-17 — evidence tiers and decision-basis labels  
**Purpose:** before choosing a concrete function, action, or collision
kernel, determine whether any object can satisfy all mandatory physical
constraints simultaneously.

## 1. Mathematical definition

Let `X_K` be the precisely defined candidate space for track `K`: functions,
kernels, or actions with a fixed domain, codomain, regularity, dimensions,
and parameters. Each constraint defines

```text
C_i = {F in X_K : F satisfies constraint i}.
```

The feasible set is

```text
F_K = intersection_i C_i.
```

All conditions must hold for **the same object, the same parameter point,
and the same boundary conditions**. Passing different constraints with
different functions or parameter values is insufficient.

### 1.1 Behavioral envelope before the function is known

The exact microscopic form is unnecessary for the first exclusion step.
First define the allowed input-output behavior

```text
B_K = intersection_j B_j,
```

where `B_j` encode observed or law-enforced zeros, signs, monotonicity,
finiteness, thresholds, saturation, and energy bounds. Every physical
realization must satisfy

```text
image(F_K) subset B_K.
```

If `B_K` is empty, no exact function can rescue it. This is the fire
analogy: combustion chemistry need not be known to reject, within the stated
scope, “it burns without fuel” or “more water must always make it burn more
strongly” when these contradict observed behavior. A non-empty `B_K` shows
only that the behavioral bounds do not contradict one another; it does not
prove that a physical function exists.

The behavioral passport therefore starts with:

| Input/condition | Required output | Sign or trend | Boundary/null point | Source of knowledge |
|---|---|---|---|---|

## 2. Nested levels

Existence is tested sequentially:

```text
F_K^(3) superset F_K^(5) superset F_K^(6)
        superset F_K^(7) superset F_K^(8-9),
```

where:

- `F_K^(3)` covers track identity and G1–G3: background, conservation,
  locality, covariance, positivity, null limits, and a complete operator;
- `F_K^(5)` additionally covers complete G4 equations and the regular G5
  mode basis;
- `F_K^(6)` adds ghost/gradient/high-`k` and causal stability;
- `F_K^(7)` adds a complete Einstein–Boltzmann realization;
- `F_K^(8-9)` adds CMB-normalized spectra and preregistered observational
  likelihoods.

Emptiness of an earlier set makes all descendants empty. Non-emptiness of
an earlier set does not prove non-emptiness of a later set.

## 3. Mandatory constraint classes

Every passport records:

1. **object identity:** domain, codomain, tensor type, state variables,
   parameters, and difference from existing tracks;
2. **parent ledger:** reproduction of the declared A1 background,
   `sum_A Q_A^mu=0`, positive densities and `H^2`, and no perturbative `k`
   in the background;
3. **locality and causality:** allowed local states, retarded response, no
   future state or hidden cosmological clock;
4. **positivity and thermodynamics:** positive production/noise kernel,
   passivity or non-negative entropy production, and no ghosts;
5. **boundary and null values:** zero coupling, disappearance of every
   medium, equation-of-state singular limits, early/late time, `k->0`,
   `k->infinity`, and any cutoff;
6. **perturbation constraints:** complete `delta Q_A`, gauge/frame map,
   Bianchi identities, regular modes, high-`k` characteristics, noise, and
   anisotropic stress;
7. **predictivity:** provenance of every constant, prohibition of a second
   post-data fit, and the number of remaining free functions;
8. **observations:** only after hard physics, preregistered
   BBN/CMB/BAO/lensing/growth ranges rather than merely hitting a central
   `S8` or `H0` value.

Each row states the equation source, units, exact test, status, and excluded
scope.

## 4. Allowed states

| State | Exact meaning |
|---|---|
| `NOT_MAPPED` | at least one mandatory constraint or its mathematical form is missing |
| `BEHAVIORAL_OPEN` | the known input-output constraints have a non-empty intersection; a physical witness need not yet exist |
| `BEHAVIORAL_EMPTY_SCOPE` | observed or law-enforced behaviors contradict one another in the stated scope; no function exists there |
| `UNDETERMINED_REVIEW` | constraints are only partly mapped, or there is neither a witness nor an emptiness certificate |
| `NONEMPTY_WITNESS` | one explicit object satisfies every constraint at the declared level and the same parameter point |
| `EMPTY_CERTIFIED_SCOPE` | an analytic contradiction, dual certificate, or complete certified bound proves an empty intersection for the stated space |

`NONEMPTY_WITNESS` proves neither uniqueness nor an automatic G5 PASS.
`EMPTY_CERTIFIED_SCOPE` kills only the precisely defined `X_K`.
`BEHAVIORAL_OPEN` adds no score and only permits the search for a
realization. `BEHAVIORAL_EMPTY_SCOPE` is a valid subtrack STOP when its
input-output bounds and scope are fully audited.

## 5. What does not prove emptiness

- a finite grid that finds no solution;
- failure of one ansatz, solver, or initial value;
- separate minima of different residuals at different parameter points;
- a value below tolerance without analytic or interval control;
- the absence of a currently known microscopic model.

Emptiness may be certified by a direct boundary contradiction, sign theorem,
matrix positivity, monotone bound, interval arithmetic, or an optimization
dual certificate. The reason is recorded as **non-existence of a common set
of outputs**, not “we did not find a function.”

## 6. Score, history, and release

- mapping constraints and `NONEMPTY_WITNESS` do not themselves add score;
- points arise only from passing the applicable canonical G1–G10 gate;
- dead subsets, scripts, and calculations are preserved;
- every certificate states its scope and any daughter derived by removing
  the documented failure cause;
- working results remain under `tracks` and enter `theory` only for a
  release candidate under AR70;
- `NONEMPTY_WITNESS` alone triggers no new prediction. An
  `EMPTY_CERTIFIED_SCOPE` triggers release review only if it changes an
  already published mechanism or number.

## 7. Mandatory output

Every track or concrete daughter uses:

| Constraint | Equation/inequality and domain | Required boundary value | Proof/test | Status | Does not cover |
|---|---|---|---|---|---|

It then states `F_K^(n)`, an explicit witness or emptiness certificate, and
the number of remaining free functions, parameters, and initial conditions.

Before that table it states the behavioral-envelope status `B_K`.
Microscopic work does not start while the behavioral constraints contain an
unresolved direct contradiction.

## 8. Evidence tier and decision basis

Each passport constraint receives an evidence tier; tiers are not added into
one number:

| Tier | Source | Decision force | Mandatory content |
|---|---|---|---|
| `E0_EXACT` | mathematical identity, symmetry, or invariant derived in scope | hard constraint | proof and domain of validity |
| `E1_DIRECT_MEASUREMENT` | direct measurement | hard only after mapping the model to the observable | experiment, CL/likelihood, statistical and systematic error, sign/sector, units |
| `E2_REFERENCE_MODEL` | ΛCDM, GR/SM, or another standard effective model | comparator/null limit, not an automatic STOP | common backend or analytic limit and nonclaims |
| `E3_PROVISIONAL` | anomaly, model-dependent inference, fit, or hypothesis | proposal guide; cannot exclude by itself | source, assumptions, open systematics |

For `E1_DIRECT_MEASUREMENT`, a central value alone is not used: the passport
states interval, confidence level, systematics, and exact transformation from
the model variable to the measured quantity. A mismatch with
`E2_REFERENCE_MODEL` only requires a test against data, not a physical
contradiction.

Every no-go or STOP also carries a decision-basis label:

| Label | Meaning | Effect |
|---|---|---|
| `PRECHECK_EXCLUDED_SCOPE` | complete mapping of `E0` or `E1` excludes an exact subclass before constructing a function | `NO_CANDIDATE_RUN`; valid only in scope and adds no canonical depth |
| `COMPUTED_STOP_SCOPE` | a complete preregistered analytic or numerical candidate test fails physically | computational STOP of the precisely tested scope |
| `OBSERVATIONAL_STOP_SCOPE` | complete model -> observable -> likelihood chain lies outside the frozen interval | STOP only after errors, systematics, and parameters |
| `REFERENCE_MISMATCH_ONLY` | mismatch with `E2` without direct data conflict | `REVIEW`, never a STOP by itself |
| `TECHNICAL_STOP` | script, environment, or backend | not a physical STOP |

`BEHAVIORAL_EMPTY_SCOPE` or `EMPTY_CERTIFIED_SCOPE` with a complete
certificate may therefore be `PRECHECK_EXCLUDED_SCOPE`. It is a valuable
result that saves wasteful runs, but may not be summarised as a
`COMPUTED_STOP_SCOPE` or as a passed canonical gate.

## 9. Mandatory function register, ranges, and death topology

Every mandatory unknown function has one live `00_STATUS.md` or work plan at
the lowest route level with at least:

```text
UNRESOLVED_FUNCTION_ID
ROUTE_AND_PARENT
DOMAIN_CODOMAIN_UNITS_TENSOR_TYPE
ADMISSIBLE_FUNCTION_CLASS
E0_EXACT_CONSTRAINTS
E1_MEASUREMENT_REGIONS_AND_PROVENANCE
E2_REFERENCE_LIMITS
E3_PROVISIONAL_GUIDANCE
CURRENT_ALLOWED_INPUT_OUTPUT_RANGES
CURRENT_FEASIBLE_SET_STATUS
EXPLICIT_WITNESS_OR_EXISTENCE_THEOREM
EMPTY_SET_CERTIFICATE
DEPENDENT_GATES
REACTIVATION_INPUT
```

The parent plan carries only the ID, state, and link. Once a range is
accepted, the whole range propagates into descendants; it is not replaced by
one convenient point.

### 9.1 Branch decisions

- An `AND` node represents jointly mandatory mechanisms. Its feasible set is
  the intersection of all child pullbacks, and it dies only after a
  certificate that this common intersection is empty.
- An `OR` node represents alternative tracks. It dies only when the
  alternative partition is proven exhaustive and every alternative is
  `EMPTY_SCOPE_CERTIFIED` in the same scope.
- An untested or merely unfound alternative keeps its parent
  `LIVE / WAITING`; it grants no PASS but prevents a false death verdict.
- The theory may receive `THEORY_PHYSICALLY_DEAD_IN_SCOPE` only when
  `A_theory` is certified empty and every top-level alternative in an
  exhaustive partition has died. Until then the strongest global state is
  `GLOBAL_FEASIBILITY_INCOMPLETE`.

### 9.2 Decision hierarchy

```text
NOT_MAPPED
  -> RANGE_CONDITIONAL_OPEN
  -> RANGE_EXISTENCE_PASS          (at least one common range exists)
  -> NONEMPTY_WITNESS              (an explicit function/object exists)
  -> applicable G-gate tests

or

NOT_MAPPED
  -> EMPTY_SCOPE_CERTIFIED         (exact scope only)
  -> parent AND/OR propagation
  -> TRACK_PHYSICALLY_DEAD_IN_SCOPE
  -> THEORY_PHYSICALLY_DEAD_IN_SCOPE only after a global certificate
```

`RANGE_EXISTENCE_PASS` is a range-existence result, not proof of complete
physics. `EMPTY_SCOPE_CERTIFIED` is a non-existence result for the exact
space, not automatically the death of an entire track or theory.
