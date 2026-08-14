# Constraint ledger for G1–G9 gates and A3/A4 stations

**Status:** `ACTIVE GOVERNING REGISTER`  
**Rule:** AR68; supplements AR30 (sequential depth), and does not retroactively
change an existing PASS, STOP, score, or physical verdict.

**Working non-emptiness execution protocol:**
`tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_EN.md`. This file still
owns the G1–G10 gate content; the `tracks` protocol defines how their common
behavioral and functional intersection is tested before choosing a concrete
function.

## Purpose

A gate is not merely a list of calculations. It is an intersection of
conditions that must all hold at once. Without that intersection, a test can
find a correct number while still violating the energy ledger, null limit, or
the ban on a new fit.

Every future gate must therefore receive a **constraint passport** before
calculation, recording: identity and route prefix; precise scope; physical law
or observational limit; mathematical quantity and units; PASS, physical STOP,
and `REVIEW_BLOCKED`; null limit; forbidden new parameters; and evidence
artifacts with provenance; evidence tier `E0_EXACT/E1_DIRECT_MEASUREMENT/E2_REFERENCE_MODEL/E3_PROVISIONAL`; and decision label
`PRECHECK_EXCLUDED_SCOPE`, `COMPUTED_STOP_SCOPE`,
`OBSERVATIONAL_STOP_SCOPE`, `REFERENCE_MISMATCH_ONLY`, or `TECHNICAL_STOP`.

`PASS` means that **all** constraints in the passport have passed. An
untested, unclear, or technically blocked constraint is `REVIEW_BLOCKED`, not
an implicit PASS or the death of the track.

`E2_REFERENCE_MODEL` (including ΛCDM/GR/SM) is a comparator, not an automatic
kill limit. `E1_DIRECT_MEASUREMENT` must state confidence level, errors,
systematics, and the model-to-observable map. A pre-computation no-go with a
complete certificate is recorded separately from a computed physical STOP and
adds no canonical depth.

Constraints are to be solved as one system: equations and conservation define
the dynamical core, inequalities and null limits form its envelope, and only
then do observations select among the remaining solutions. The precise method
and required counting of remaining free functions are in
`Questions/Q22A_CONSTRAINT_TO_FUNCTION_DERIVATION_PROTOCOL_EN.md`.

## Canonical gates

| Gate | Constraints required in its passport | What the gate must not substitute |
|---|---|---|
| G1 | distinct hypothesis, mechanism, route prefix, dimensions, source of every new parameter, distinction from older track | verbal description or renaming an existing track |
| G2 | complete background ledger, `sum Q_A^mu=0`, positivity of densities/H², null limit, no `k` in background, origin of normalisations | fitting `H0`/`S8` or an undocumented reservoir |
| G3 | locality, covariance/action or equivalent complete closure, transfer frame, energy and momentum, causality, no hidden time | a homogeneous ODE or global `H0` as a microphysical clock |
| G4 | complete linear equations of all species, Einstein constraints, gauge map, signs, `delta Q_A`, null limit and Bianchi identities | an incomplete sector or test field presented as full system |
| G5 | complete regular superhorizon basis, mode count, adiabatic/isocurvature classification, constraints, amplitude linearity | one selected seed or a compensation defined only numerically |
| G6 | complete basis in subhorizon/high-k limit, ghost/gradient/causality, stiffness/convergence, physical denominators | stability of one mode or one tolerance |
| G7 | full Einstein–Boltzmann system, hierarchy/closure, recombination and TCA, conservation/constraint/null tests, independent implementation or gauge cross-check, physical transfers | binary wrapper, decorative identities, or post-data opacity/drag |
| G8 | CMB normalisation and transfers, `A_s,n_s` provenance, linearity, preregistered `k,z` ranges, `sigma8/S8`, null model and convergence | tuning amplitude merely to hit `S8` |
| G9 | frozen datasets/likelihoods/covariances, priors and nuisance parameters, degrees of freedom, systematics, holdout/validation and kill thresholds | selecting only a favourable dataset or hiding a look-elsewhere effect |

G10 remains versioning/reproduction: manifest, hashes, changelog, independent
reproduction, and complete disclosure of open gates.

## A3 station — implementation and spectra

A3 is not a second G7. It is a working station that can progress only through
canonical G7 and G8. Its passport must jointly retain:

| A3 constraint | Minimum content |
|---|---|
| A3-M1 Provenance | frozen CLASS/CAMB version and commit, patch, configuration, units and A2 inputs |
| A3-M2 Reference | with zero cellular transfer, reproduce standard background, `C_ell`, and `P(k)` within preregistered tolerance |
| A3-M3 Physics transfer | implement the full A2 operator, not merely background or growth equation; retain ledger and frame |
| A3-M4 Numerics | independent tolerance/method, grid and multipole convergence, checkpoints and bounded runtime |
| A3-M5 Interpretation | every spectral shift has a mechanism; no post-data drag, opacity, `A_s`, or initial mode |
| A3-M6 Output | physical transfers and CMB-normalised `sigma8/S8`, with G7 distinct from G8 |

## A4 station — steam, exit, and relic sector

A4 is a separate microphysical station. It cannot be closed by inserting
`Delta N_eff` as a finished number.

| A4 constraint | Minimum content |
|---|---|
| A4-M1 Local source | `C_s(chi,I_i)` with local clock/state, not free `ln a`; M0 of Q22a/Q18 |
| A4-M2 Reservoir and ledger | `T_e^(mu nu)`, paired `+S_s^mu/-S_s^mu`, energy and momentum, positive densities |
| A4-M3 Timing | production, equilibrium, decoupling, exit/reheating and vanishing late tail; direct late freely-relativistic channel obeys M-015 |
| A4-M4 Thermodynamics | entropy, temperature, degrees of freedom and BBN limits without double counting |
| A4-M5 Perturbations | from the same operator: `delta S_s`, noise/frame, isocurvature, and steam free-streaming/closure |
| A4-M6 Predictiveness | derive `Delta N_eff` and steam properties; observations test rather than define their shape |

Current A4-M1 is `REVIEW/STOP`: the [M0 provenance audit](Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md)
found no defined `chi` or reservoir in the current theory. This does not kill
the effective FLRW class, but blocks a fundamental A4 PASS.

## Use at the next step

A preregistration must cite its precise Gx or Ax row and state which
constraints the test closes and which remain open. Its resulting audit must
retain the same table with `PASS`, `STOP`, or `REVIEW_BLOCKED`. Only then may
depth change or the next gate begin.
