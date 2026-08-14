# THE CELLULAR UNIVERSE — RULES AND QUESTION REGISTER: v3.18 ADDENDUM

**Date:** 13 July 2026  
**Language authority:** the Slovak version  
**Base register:** `theory/EN/05b_Methodology_Rules_and_Question_Register_EN.md`

## 0. Relationship to the base register

This file is the binding v3.18 continuation of file 05. Parts 1–10 of the base register and their rules are **not changed or deleted**. The addendum only adds rules missing from the base register, new questions, and reasoned restrictions on earlier formulations.

If question statuses conflict, the later and narrower verdict in this addendum applies. The historical formulation remains preserved as an audit trail.

## 1. Check that the new rules do not duplicate old ones

| New rule | Nearest older rule | What is added and was not covered |
|---|---|---|
| AR1 | Part 2: PROPOSAL → TRANSLATION → TRIAL → STRIKE-OUT | Formal status of every author input as a hypothesis and a mandatory audit outcome. |
| AR2 | Part 3: TRACK BIRTH | Procedure for multiple possibilities and the exact condition for death of the whole branch. |
| AR3 | Part 2: falsification; Part 6: graveyard | Mandatory evidence bundle, prohibition on deletion, and condition for creating a new track. |
| AR4 | P1–P5 | Mandatory preservation of the script, input, output, environment, version, and corrections. |
| AR5 | No direct equivalent | Immutability of published versions, changelog, manifest, and hashes. |
| AR6 | P5 | Separation of smoke test, toy sensitivity, approximation, prediction, and fit; scope of a verdict. |
| AR7 | No direct equivalent | Mandatory content synchronization of the SK/EN registers. |
| AR8 | AR4 (artifacts) and AR6 (scope) | Mandatory audit of the propagation of the physical formulation into every downstream script; the earlier rules do not test state/coefficient completeness in an implementation. |
| AR9 | AR6 (scope) and AR8 (physics contract) | Prohibition on mistaking an effective/coarse-grained ledger for a derived microscopic causal graph. |

## 2. New audit rules AR1–AR9

### AR1 — Every author input is a hypothesis

Every new physical or numerical claim supplied by the author enters the work as a **HYPOTHESIS**, not a result. The audit assigns it one of these states:

- **SURVIVES N/100** if it has not encountered a confirmed physical contradiction in the tested scope; or
- **DEAD** if the precisely defined formulation fails a physical, mathematical, numerical, or statistical gate.

Reproduction of the author's table confirms reproducibility of the numbers, not automatically their physical mechanism.

### AR2 — Branching into tracks and death of a branch

If a problem has several consistent possibilities, tracks K1 through Kn are created. The track with the highest preliminary chance of success is tested first. Each track has its own hypothesis, tests, outputs, and kill conditions.

A track either passes its gates or reaches a documented wall. A branch dies only when all of its tracks die. This rule supplements TRACK BIRTH; it does not alter its conditions for creating a new track.

### AR3 — Dead tracks are not deleted

A dead track remains marked `DEAD — ARCHIVED`. The following must be preserved:

1. the exact hypothesis and its scope;
2. the test or law it failed;
3. the precise reason for death;
4. inputs, units, data, scripts, and outputs;
5. what the verdict does not kill;
6. the condition permitting a new track.

The same track is not reopened merely by renaming a parameter, extending a grid, or using another optimizer. A new track requires new physics, correction of a demonstrated error, or new independent data, plus a `Difference from the dead track` section.

Detailed protocol: `Audit/00_PRAVIDLO_ARCHIVACIE_MRTVYCH_KOLAJI.md`.

### AR4 — Scripts and calculations are part of the evidence

Every calculation used in an audit has a reproducible script in `scripts`. Scripts and calculations for both living and dead tracks are preserved.

A faulty script is not silently overwritten. The original version is preserved, a corrected version is created, and a Markdown erratum is added. At release, the reproduction command, environment version, input, frozen output, and SHA-256 are stored.

If the reason for death is purely analytical, the record states `calculation script: NOT REQUIRED` and preserves the complete argument. A script is not created merely for appearance.

### AR5 — Published versions are immutable

The numbers and text of an already published Zenodo version are not rewritten retroactively. Every later published version receives:

- a changelog against the preceding version;
- a file manifest;
- SHA-256 hashes;
- links to errata and changed verdicts.

A correction is issued as a new version/record or an explicit erratum, never as a silent alteration of a historical result.

### AR6 — Level of evidence and scope of a verdict

Every numerical result is assigned one of these labels:

- `smoke test`;
- `toy sensitivity`;
- `approximation`;
- `physical prediction`;
- `data fit`.

A local sum of residuals must not be called a global likelihood. A post-data optimum has no predictive weight. A verdict must state whether it applies to the background, perturbations, microphysics, numerics, or a data fit. Passing one gate is not confirmation of the entire theory.

### AR7 — Mandatory SK/EN synchronization

Every important rule, question, status change, reason for death, and reopening condition is entered in the SK and EN registers under the same identifier. The Slovak version is authoritative; the English version is its faithful content mirror.

### AR8 — Formulation-to-implementation propagation audit

Before a lower-level script or pipeline receives physical weight, it must
publish a **physics contract**: parent covariant equation, gauge, state
space, background coefficients, role of the Fourier mode, null limits, and
Einstein constraints. A lineage audit must then verify that every mandatory
contract element is present in the downstream implementation or is explicitly
labelled as a controlled approximation.

A missing dynamical degree of freedom, a changed direction of `Q^mu`, use of
a series background beyond its range, or transfer of `k` into the background
is an **implementation STOP**, not merely a solver issue. Old scripts and
results are preserved, but their physical scope is narrowed. A successor
requires a new state space/derivation and the audit is repeated for all of
its descendants. Passing internal numerical checks of a reduced RHS alone
does not validate the parent mechanism.

### AR9 — An effective ledger does not decide a hidden sequence

Homogeneous source equations `Q_A` can conserve energy and correctly describe
the background, yet do not by themselves decide whether the products of one
event arise in parallel, sequentially, or through an unobserved intermediate
state. Such an order may receive the status of a physical prediction only
after a local operator/action/collision kernel is derived that determines
`Q_A^mu`, branching fractions, any delays, and perturbations `delta Q_A`.

Observations then select or exclude the tracks. A fraction or time set from
those data is a fit, not a derived mechanism. This rule is narrower than AR6
(result scope) and AR8 (propagation into code): it directly protects the
identifiability of a microscopic causal graph.

## 3. Question register Q17–Q34

| Q | Question | Current status and gate |
|---|---|---|
| Q17 | What are the three-point statistics and `f_NL` from V-thermalization? | **OPEN.** The first-order result is only an estimate; derive the shape, sign, second order, gauge-invariant transfer to `zeta`, and the bispectrum. |
| Q18 | When is graviton steam produced relative to approximately 1280 e-folds? | **CRITICAL, OPEN; fundamental A4 is P1 STOP in current v3.18.** Solve `dot(rho_g)+4H rho_g=C_g` through the accelerated phase, exit, and reheating; only then determine `Delta N_eff`. The existence audit confirms that a smooth positive early source with compact support and a paired ledger is a physically possible effective FLRW class. M0/P1.1 and the extended P1.2 audit found no `C_g`, local clock/state, or reservoir `T_e^(mu nu)`; A12 supplies only a conditional thermalisation boundary, not source history. It is therefore not derived covariant microphysics. |
| Q19 | Which matter component is created by the transfer `Q`? | **PASSED THE BACKGROUND GATE.** A1-K1 creates CDM/ash while baryons are conserved. It is not selected for perturbations; T7/A2 and T8/A8 remain. |
| Q20 | What is the complete gauge-invariant perturbation system of the interacting components? | **CRITICAL, OPEN; P5 is `REVIEW_BLOCKED_ARCHITECTURE`.** The reduced K7 basis omitted dynamical `U_c`. P5.3g4/g5/g6 closed their formula scopes, and KMPC-024 hard-anchored the M1 standard seed (`76/76`, standard constraints PASS). A later PF-058 audit restricted its M3 claim: the fractional solver did not establish a complete fuel coefficient/row contract, so 15 fractional constraint failures stop the tested ansatz, not K4 physics; 6 power failures are truncation diagnostics only. A `Phi^0/Phi^1 × z^j` ledger, synchronous species equations, and a total Bianchi map are required before another runner. The full K4-backreacted seed, finite opacity, and a derived S1 steam seed remain missing; P5.4/G8 remain closed. |
| Q21 | What exactly is `T` in `T proportional H`? | **CRITICAL, OPEN.** A thermodynamic or microdynamic definition is required without using the measured `n_s`. |
| Q22 | How does the gauge-invariant curvature perturbation `zeta` arise from `delta E`? | **CRITICAL, OPEN.** Derive `P_zeta`, `A_s`, `n_s`, running, isocurvature, and the bispectrum from one closed system. Sub-gate Q22a: energy-costly divisions must determine a common source `S`, its `P_S(k)`, and any `k_*` without fitting; a realized Fourier `k` must not enter `H(a)`. Q22a-K1 is verified only as the effective A1 `F->C` ledger, not as a microphysical verdict. Q22a-K2 is **DEAD in its supplied persistent direct freely-relativistic form**: the separate `Delta N_eff=0.0535` budget does not allow such a source. Q22a-K3 has an exact conservation ledger, but its direct steam fraction survives only below `f_R~3.2e-5`; no operator yet derives `b`. The only corridor not excluded by this screen is an early completed relic channel Q18/Q23 plus late `F->C`; it is not yet derived or scored. The Q4/Q72 bridge audit closes the common entry gate Q22a-G0: current `delta`, `lambda`, and a scalar production source do not yet determine a complete product operator. Causal graphs and evidence are in `Questions/Q22A_DIVISION_PRODUCT_SEQUENCE_TRACKS_SK.md`. |
| Q23 | What mechanism ends the fuel era and reheats the Universe? | **CRITICAL, OPEN.** Determine the end of acceleration, reheating temperature, entropy production, radiation domination, and BBN initial conditions. |
| Q24 | Is the fundamental network 3D space with a global tick or a 4D causal structure? | **CRITICAL CONCEPTUAL CHOICE.** Derive a 4D Lorentzian limit or admit a preferred frame and test its operators. |
| Q25 | How does one capacity enforce universal coupling of all fields? | **OPEN.** A common effective metric for several spin sectors, the equivalence principle, and birefringence limits are required. |
| Q26 | Is the cross-V weight genuinely entanglement entropy? | **OPEN.** Classical weights are insufficient; define Hilbert spaces, a state `rho`, a quantum channel, and von Neumann entropy. |
| Q27 | What is the local overhead for fluctuating degree `k`? | **OPEN.** Decide by measurement between `1/(<k>+C)` and `<1/(k+C)>` on a growing periodic network. |
| Q28 | What is the dynamical meaning of `C=28` independently of `n_s`? | **OPEN.** Derive `C` from local symmetry/action before CMB data and include the look-elsewhere effect. |
| Q29 | Does cellular dynamics satisfy the second law of thermodynamics? | **OPEN.** Define the entropy of every reservoir and prove non-negative total production during division and transfer `Q`. |
| Q30 | What are the operational kill conditions for each prediction? | **METHODOLOGY PARTLY COMPLETED.** AR1–AR7 and the dead-track archive apply; each prediction still needs a dataset, likelihood, threshold, systematics treatment, and version. |
| Q31 | What is the microphysical model of ash? | **OPEN.** Determine spin, mass, distribution, stability, abundance, free streaming, phase-space, halo, and cluster tests. |
| Q32 | What is the continuum limit of gravity? | **OPEN.** Derive the Poisson/Einstein limit, universal `G`, lensing, PPN, and two gravitational polarizations. |
| Q33 | Does the cellular network derive the sign and size of global curvature without using `H0` data? | **OPEN; K4b SURVIVES 20/100.** Discrete curvature, multiple `N`/seeds, the `N->infinity` limit, and pre-data freezing of `Omega_K` are required. |
| Q34 | Can cell division generate a covariant momentum exchange confined to the dark sector? | **CONDITIONALLY OPEN; S8-K1b SURVIVES 35/100.** Open only after baseline Q20; it requires `F_A^mu`, counter-momentum, stability, and CMB/LSS tests. |

## 4. Reasoned restrictions on earlier formulations

The older formulations are not deleted. The following entries state exactly why a later audit narrowed them.

### L1 — Q11 can no longer be described as globally complete

**Earlier formulation:** Q11 was `COMPLETE`, including the spectrum and amplitude.

**Current scope:** the horizon reading remains a candidate. However, Gaussianity Q11d, the physical meaning of `T proportional H` (Q21), gauge-invariant transfer `delta E -> zeta` (Q22), exit/reheating (Q23), the status of `m=1/2`, and full scalar/tensor normalization remain open.

**Reason:** without these steps, the observable `P_zeta(k)` has not been derived from closed microdynamics. Agreement of one slope with data cannot replace the missing transfer and initial conditions.

### L2 — Q15 and `Delta N_eff=0.0535` are conditional

**Earlier formulation:** the thermal graviton relic and the exact value `Delta N_eff=0.0535` were closed.

**Current scope:** the number is a historical calculation under an assumed thermal scenario.

**Reason:** a relic produced before approximately 1280 e-folds of accelerated expansion dilutes as `a^-4`. Without a source during/after this phase and without a derived exit and reheating history, neither its present temperature nor `Delta N_eff` is a prediction. See Q18 and Q23.

### L3 — Q16 and `C=28` are not an independently derived theorem

**Earlier formulation:** `C=g_B=28` was derived and alternatives were executed by the data.

**Current scope:** `C=28` survives as a mechanistic reading.

**Reason:** the number 28 was present in the theory before the test was formulated and is linked to the `n_s` reading, creating a look-elsewhere effect and a possible circular validation. A local dynamical derivation independent of CMB data is required. See Q28.

### L4 — “The only S8 lever is lambda->0.10” was only a limited screen

**Earlier formulation:** all internal S8 brakes had been excluded and only a change in `lambda` remained.

**Current scope:** the particular tested implementations of warm DM and steam perturbations were excluded, not all physically possible mechanisms.

**Reason:** ad hoc constant drag on all matter, S8-K1a, is dead because it lacks covariant balance and does not distinguish baryons. The new covariant dark-sector track S8-K1b has not yet been tested. Curvature track K4b has not been derived from the network. None is currently a prediction.

### L5 — A generic non-gravitational DM interaction is not automatically fatal

**Earlier formulation:** any confirmed non-gravitational DM interaction kills the model.

**Current scope:** an interaction is fatal if it contradicts the frozen micro-model or observational limits.

**Reason:** ash does not yet have closed microphysics (Q31), so a universal prohibition has not been derived. Q34 may examine local covariant momentum exchange. This is not a return to dead Le Sage track #8 because it must not contain its baryonic drag, heating, and aberration.

### L6 — The v3.17 progress percentages are historical

**Earlier formulation:** `P_global approximately 70%` and compliance approximately `79%`.

**Current scope:** these are values under the question denominator used at that time.

**Reason:** the audit opened new critical gates Q18–Q34 and separated background, perturbations, microphysics, and likelihood. Current status is therefore tracked through gates A0–A8; the old percentages are not used as present progress without an explicit recalculation.

### L7 — K7d `66.5/100` is not physical evidence for energy-frame A2-K4

**Earlier formulation:** K7d G0–G7 PASS and depth `66.5/100` supported the
active K4 physical track through G8.

**Current scope:** `66.5/100` remains the historical technical depth of the
stored reduced 13-state RHS. The currently physically valid K4 depth is
`60/100`; a full general-synchronous P5 basis is mandatory before G8.

**Reason:** a later lineage audit found that the K7 state contains neither
dynamical `U_c` nor CDM momentum in `M`, although the declared energy-frame
transfer `Q^mu=Gamma rho_f u_d^mu` requires them at relative velocity. The
old K7 background also extrapolated a `K_MPC=0.05` series outside its valid
range. See `Independent_Audits/K_MPC_0_05/13_P4C_K7_MISSING_UC_EXACT_BACKGROUND_STOP_SK.md`.

## 5. Current order of work

**AR68 — constraint passports:** every future G1–G9 gate and A3/A4 station
must have, before calculation, its own ledger of physical and observational
constraints; an unclosed constraint yields `REVIEW_BLOCKED`, not a silent
PASS. Canonical register:
`Questions/00_GATE_AND_STATION_CONSTRAINT_LEDGER_EN.md`.

**AR69 — artifact ownership:** every script, base module, result, and audit
has one route-conditioned owner. A manifest records the complete chain
`gate → preregistration → runner → base+SHA → result → audit → verdict`.
Historical files are neither copied nor physically moved without a Git
baseline, a complete path/SHA map, and dependency verification. Full text:
`theory/EN/05_AR69_Canonical_Artifact_Ownership_and_Base_Core_EN.md`.

1. A0 is complete: immutable releases, future changelog, and checksums.
2. Q19/A1-K1 has passed only the background gate.
3. **Q20/A2 is the immediate next step.**
4. A3 implements the model in CLASS/CAMB only after A2 passes.
5. Q18/Q23 and Q21/Q22 close the steam, exit, and primordial sectors.
6. A8 is a preregistered full fit; only then are `S8/H0` predictions updated.
