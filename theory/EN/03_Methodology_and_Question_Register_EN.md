# 03 — Quantum Cellular Theory of Space v3.18: methodology and question register

**Author:** Martin Jámbor<br>
**Semantic authority:** Slovak version<br>
**Release class:** `R3.18-CONSOLIDATED / COMPLETE_SELF_CONTAINED_SNAPSHOT`<br>
**Content cutoff:** 9 August 2026<br>
**Planned publication window:** 11–13 August 2026<br>
**Theory status:** working physical hypothesis with audited partial results;
not yet experimentally confirmed

## 0. Purpose, authority, and self-containment

This is the sole complete release methodology and question register for
v3.18. It contains every rule required to read the current release and
states the present, narrower status of each question. No earlier methodology
document is required. Historical statements are not erased; if a later
audit restricted one, this register gives the reason and current reach.
Working chronology and detailed calculation branches remain in `tracks/`,
not in the release document.

The coherent physical account is in
`01_The_Cellular_Universe_EN.md`, while the stable machine-readable
P01–P11 prediction register is in
`02_Prediction_Status_Table_EN.csv`. The complete index of exact laws,
open constraints, calibrations, prediction links, and death reach is in
`04_Theory_Existence_Conditions_Register_EN.csv`. This file explains
the rules by which their status is audited and identifies the questions that
remain open.

For interpretation of v3.18, this frozen Slovak release payload controls
according to the division of roles in guide `00`: document `02` is the
authority for P01–P11 rows, document `01` for the coherent physical account
and track state, this document `03` for methodology and questions, and
document `04` for the existence-condition index. An older published record
remains immutable provenance, but it must not overwrite a later narrower
state accepted in this release. A new author decision changes the meaning of
the release only through a hash-bound erratum or a new version. A route-local
contract controls only its working scope and must not broaden or overwrite an
approved release claim. V3.18 changes no foundation and adds no new fit.

Status meanings are exact:

- `PASS` — closes only the stated scope;
- `STRUCTURAL_PASS` — an algebraic or structural gate, not full physics;
- `LIVE / CONDITIONED` — no proved contradiction, but dependent on open gates;
- `LIVE / WAITING` — not dead; a precise input or derivation is missing;
- `REVIEW` — evidence or claim reach is not closed;
- `STOP_SCOPE` — only the precisely tested scope is dead;
- `WITHDRAWN` — an old statement may no longer be presented as current;
- `HISTORICAL` — preserved record without current predictive weight;
- `SURVIVAL_TARGET` — a preregistered value or range required for the exact
  declared scope to survive; it is not automatically a posterior or proved
  theorem;
- `EXACT_SCOPED_SURVIVAL_CONDITION` — an exact condition derived only within
  the stated operator or mechanism scope;
- `HISTORICAL_TARGET_PROVENANCE` — archival information about the origin of
  an older calculation; it is not a separate current decision class. If the
  value remains an active v3.18 survival condition, it must receive its own
  current class and exact death reach;
- `OPEN_NO_KILL_WINDOW` — the obligation is known qualitatively or
  functionally but no numerical range and observable map have been derived;
  a result cannot yet create a physical death verdict;
- `CALIBRATION_BENCHMARK` — a frozen input or derived bookkeeping value of
  an exact calculation; not automatically a prediction or kill boundary;
- `NOT_A_SCIENTIFIC_SURVIVAL_CONDITION` — a process or numerical value with
  no physical death reach.

These labels do not form one linear list. The first eight describe the
verification state of a claim or track; the remaining labels describe the
scientific role of a value or condition. A typical workflow for one exactly
frozen scope is:

```text
LIVE / WAITING
  -- supply the missing input or derivation --> REVIEW
REVIEW
  -- pass only an algebraic/structural gate --> STRUCTURAL_PASS
STRUCTURAL_PASS
  -- further mandatory gates remain --> LIVE / CONDITIONED
REVIEW or LIVE / CONDITIONED
  -- all mandatory gates of the scope pass --> PASS
REVIEW or LIVE / CONDITIONED
  -- a contradiction is proved in the scope --> STOP_SCOPE
```

`STRUCTURAL_PASS` is therefore not a weaker name for a complete `PASS`; it is
an accepted intermediate result after which the parent track usually remains
`LIVE / CONDITIONED`. `WITHDRAWN` and `HISTORICAL` are publication/provenance
states outside this branch: a withdrawn claim must not be used as current,
but its origin and the reason for restriction remain in history. Labels from
`SURVIVAL_TARGET` through `NOT_A_SCIENTIFIC_SURVIVAL_CONDITION` do not define
workflow order; they state the decision weight carried by a particular value
or condition.

Register `04` uses exactly six shared values in its `canonical_class`
column: `OBSERVATIONAL_SURVIVAL_TARGET`, `EXACT_PHYSICAL_LAW`,
`CONDITIONAL_MODEL_OUTPUT`, `CALIBRATION_BENCHMARK`, `MECHANISM_READING`, and
`OPEN_NO_KILL_WINDOW`. A finer historical label is retained separately in
`subtype_v3_18`; it must not create a seventh decision class.

`CONDITIONAL_MODEL_OUTPUT` is a value calculated only under the declared
inputs and closure; it becomes a survival condition only if an exact target
and death reach are separately registered. `MECHANISM_READING` is a
physically motivated interpretation without independent exclusion weight.

## 1. Anchor and working protocol

**ANCHOR:** Is observed physics a surface trace of the metabolism of a
cellular network of space?

The working sequence remains:

`PROPOSAL -> TRANSLATION INTO EQUATIONS AND TRACES -> JUDGMENT -> PASS/REVIEW/STOP_SCOPE`.

Every author input enters as a hypothesis. Reproducing a table confirms its
numbers, not its mechanism. Falsification of an exact scope is information
gain. A decided scope can be reopened only by new physics, a demonstrated
error, or new independent data.

### 1.1 Survival conditions, death reach, and prohibition of data double use

A prediction can be scientifically binding before full microphysical proof
when it is recorded as a survival condition. Measurement inside the target
window means only that the exact scope remains alive; it does not confirm a
cellular mechanism. Measurement outside the window yields `STOP_SCOPE` only
after a complete model-to-observable map, experimental and theoretical
uncertainties, covariance, and systematics.

Every survival target must state its death reach:

- `FORMULATION_LEVEL` — the exact ansatz or historical calculation dies;
- `TRACK_LEVEL` — the whole track with the same physical identity dies;
- `THEORY_LEVEL` — all QCTS dies only under a contradiction with its
  foundation or when the intersection of mandatory conditions is empty in
  every track of a demonstrably exhaustive top-level list.

If BBN, CMB, or another measurement is used to reconstruct `C_s`, branching,
or another unknown function, it is `CALIBRATION_DATA`. The same data layer
must not be counted again as independent confirmation. For the present
viability test all data may be used as constraints to seek an
`OBSERVATIONALLY_COMPATIBLE_EXISTENCE_WITNESS`; predictive power requires an
out-of-sample observable or microphysically fixed inputs.

Register `04` is the mandatory common index of all current values and
constraints. For P01–P11 it may not overwrite register `02`, but must link
to it. Exact laws are recorded without a free tolerance; measured
comparisons are recorded with dataset, model, CL, uncertainties, covariance,
and systematics. An item without a derived window remains
`OPEN_NO_KILL_WINDOW`; no number may be invented merely to make the table
look complete.

## 2. Birth, identity, and archiving of tracks

### K-BIRTH

A new track is created only if it:

1. addresses a subquestion of the anchor;
2. is not merely a technical repair of an existing track;
3. has its own mechanism, method, and at least one surface trace;
4. states how it differs from existing and dead tracks;
5. states what it does not address and gives its kill conditions.

If several physically distinct possibilities exist, create tracks `K1...Kn`.
One track dies when its own complete set of mandatory conditions is certified
empty in the frozen scope. A parent branch or the theory dies only after the
top-level alternative list is shown complete and every alternative dies in
its own scope; alternative tracks form an `OR`, not an `AND`.

### M-BIRTH and Q-BIRTH

A milestone needs an output, closure criterion, closure method, weight, and
duplication check. A new question needs a track, a surface trace, and a
decision gate; otherwise it is scaffolding.

### AR-DEAD-TRACK

Dead tracks are never deleted. Preserve their hypothesis, scope, law/test,
reason for death, inputs, scripts, raw output, audit, what the verdict does
not kill, and the reopening condition. Renaming a parameter, widening a
grid, or changing a solver does not create new physics. A technical timeout,
syntax error, or exhausted implementation batch is not a physical STOP.

## 3. Mandatory verification rules and known traps

### P1–P5

- `P1`: compare the pipeline with a reference model in the same run when
  such a comparator is semantically defined;
- `P2`: a stiff system needs a suitable solver and step-convergence audit;
- `P3`: solvers require physical bounds, null limits, finite guards, and checkpoints;
- `P4`: power-law fits first check boundary and truncation contamination;
- `P5`: no number without units, convention, sensitivity, and claim class.

### M1–M9

`M1` unbounded secant method — numerical root finding from the last two
points without using a derivative; without a physical bracket it may jump
into a forbidden region, across a singularity, or toward the wrong root.
`M2` reversed time fields; `M3` bisection without self-consistency; `M4` a
boundary distorting a power law; `M5` fixed Euler
for a bilinear source; `M6` interval comparison with different backgrounds;
`M7` box boundaries in a wave problem; `M8` unvalidated degree-of-freedom
counting; `M9` rigid mirrors producing a false ether.

### AR-LINEAGE

Before a downstream script carries physical weight, it must have a physics
contract: parent equation, gauge/frame, state space and ordering, background
coefficients, meaning of the Fourier mode, units, null limits, and
constraints. The audit verifies that every element reaches the
implementation or is marked as a controlled approximation. A missing degree
of freedom, changed direction of `Q_A^mu`, substitution of a series for an
exact background, or insertion of realized `k` into the FLRW background is
an implementation STOP and claim quarantine, not an ordinary solver error.

## 4. Evidence classes, constraints, and unknown functions

Each constraint has a class. The class does not say whether a result is
welcome; it records where its authority comes from and which decision it may
support. This prevents a helper benchmark, assumption, or agreement with a
reference model from being presented as an established law or direct
measurement:

- `E0_EXACT` — a mathematical identity or established physical law in the
  exactly stated scope. It acts as a hard internal guard: after the mapping of
  equations, units, and assumptions is verified, its violation may directly
  exclude that scope;
- `E1_DIRECT_MEASUREMENT` — observational or experimental data. It gains
  decision weight only with a complete model-to-observable map,
  uncertainties, covariance, systematics, and a declared statistical test;
  only then may it constrain or exclude a physical scope;
- `E2_REFERENCE_MODEL` — a comparator, benchmark, or null limit. It is used
  to check implementation, signs, units, and expected limiting behaviour.
  Disagreement with the reference model alone is not a physical STOP unless
  the compared property is separately mandatory as `E0` or a fully mapped
  `E1`;
- `E3_PROVISIONAL` — a working estimate, heuristic, or guide for selecting
  the next test. It helps narrow the search and set priorities, but has no
  exclusion weight and must not create PASS or STOP.

The same quantity may have different evidence classes in different uses.
For example, a number used for calibration is an input to reconstruction,
not simultaneously an independent `E1` confirmation; its concrete role must
therefore be registered before every test.

Only `E0` or a fully mapped `E1` may kill a physical scope. Disagreement
with an unproved prediction of a reference model is only
`REFERENCE_MISMATCH_ONLY`. An established law has no free tolerance; a
measured test uses its declared experimental uncertainty.

### FS-GATE-01 — behavior before formula

Before selecting an ansatz, state domain, codomain, units, regularity,
covariance, locality, symmetries/parity, conservation, causality, stability,
null and boundary limits, positivity, and observable maps. A scope excluded
before computation is `PRECHECK_EXCLUDED_SCOPE`, not `COMPUTED_STOP_SCOPE`.

If the concrete function is still unknown, FS-GATE-01 applies at the level
of behavior of the whole admissible class, not as a demand for a closed
analytic formula. Domain, units, symmetries, limits, and guards then define
`F_adm`; FS-GATE-02 subsequently asks whether this class contains at least
one function satisfying every mandatory constraint. The two gates are
sequential, not contradictory.

For the Lorentz sector the distinction is mandatory: in the audited scalar
cosine-Laplacian scope and in every branch invoking parity protection, the
odd linear term must be exactly zero. A general physical photon sector can
instead survive only with a derived coefficient and sign compatible with
the applicable experimental bound. A quadratic/Planck-suppressed term is
compared with its separate bound. For matter components a complete theory
must respect the equivalence principle, including compositional
universality; a scalar even operator does not prove this by itself.

### FS-GATE-02 — admissible set

If a function is unknown, do not silently guess one representative. Define

```text
A_t = {f in F_adm,t : all E0 identities and guards hold and all open E1
       observables lie in the preregistered tolerance region}.
```

Here `t` denotes one physical track and `A_t` its admissible set; it is not
the scalar background amplitude `A_f` from document `01`.
`RANGE_EXISTENCE_PASS` requires a witness in the complete common `A_t` over
the mandatory domain or an equivalent existence theorem; a local
function/output witness is insufficient.
`RANGE_CONDITIONAL_OPEN` means only that no contradiction has been proved.
A finite empty grid is not proof that a functional set is empty. At an
`AND` node the common intersection of one track's mandatory conditions
decides. At an `OR` node the admissible sets of physically alternative
tracks are united and the alternative list must be proved complete. The
theory is `GLOBAL_FEASIBILITY_INCOMPLETE` while a mandatory function or
observable map is missing; it dies in scope only after certification that
every set `A_t` in the exhaustive top-level list is empty. Alternative
tracks must never be intersected as if all were simultaneously mandatory.

A row-level kill window tests its declared formulation or track
(`FORMULATION_LEVEL` or `TRACK_LEVEL`). A result outside the window after a
complete observable map and likelihood excludes only that scope. FS-GATE-02
produces a `THEORY_LEVEL` verdict only when the top-level alternative list is
proved exhaustive and the admissible set of every alternative is certified
empty. A local kill therefore does not require global emptiness, but it must
not be silently promoted to death of the full theory.

An output-range relaxation may carry the whole admissible correspondence
into descendants, but may not replace it with a midpoint, zero direction,
or fitted representative. Its nonemptiness does not prove the existence of
one global smooth local function.

### FS-GATE-03 — finite frozen register of alternatives

For every release, the top-level list `T_top^(v)` is frozen as a finite,
author-approved register of physically distinct tracks. A
`LIVE_BACKUP / WAITING` track without a complete contract, admissible set,
and witness is not positive viability evidence; it only prevents an
unsupported `THEORY_STOP` and leaves the state
`GLOBAL_FEASIBILITY_INCOMPLETE`. A track introduced after the cutoff needs a
new ID, an exact mechanism difference, preregistered constraints, and an
author decision in a new release or audit delta. It must not retroactively
change the death of an older scope or be added merely because an adverse
result is already known. The theory has positive `RANGE_EXISTENCE_PASS` only
when at least one fully specified top-level track has a witness or existence
theorem; a list of imaginable alternatives is insufficient.

## 5. Compute, audit, and release workflow

`CONTRACT/DRAFT -> DEV_SANDBOX -> RC_FREEZE -> independent static audit ->
OFFICIAL RUN exactly once -> internal science audit -> orchestrator decision
-> MILESTONE_PROGRESS_REVIEW -> {ACCEPTED_CHECKPOINT_FREEZE only for an
accepted auditable milestone | NEXT_ATOM / WAIT}`.

The separate non-computational branch is `FROZEN_MANUAL_ANALYTIC_RESULT ->
MANUAL_ANALYTIC_RESULT_AUDIT -> ORCHESTRATOR_DECISION`. It contains no
Python, RC, or official run and must not be presented as any of them.

The arrow is the main successful path of one **scientific atom** — one
exactly bounded question or calculation. Its phases mean:

| Phase | Meaning | What opens it | What closes it and causes the next transition |
|---|---|---|---|
| `CONTRACT/DRAFT` | The scientific question is translated into an exact scope, equations, inputs, units, gauge/frame, expected result, thresholds, and `PASS/REVIEW/STOP` branches. It is not yet executable evidence. | A new physically independent question, an authorized next track step, or a return after an error in the contract/equation itself. | The contract is content-complete and the orchestrator permits technical implementation in `DEV_SANDBOX`. An unresolved physical choice first goes to the author. |
| `DEV_SANDBOX` | Technical workshop. The script author may implement and repair the working source and use only offline synthetic compile/help/unit/selftests. Its outputs have no physical weight. | A complete contract and capsule that exactly allowlists DEV files, tests, and write scope. | The full allowed DEV suite passes, creating `DEV_TESTS_PASS`, and the candidate may be frozen as an RC. A technical failure returns to the same DEV source; `10/10` opens a `TECHNICAL_PERMISSION_GATE`. |
| `RC_FREEZE` | The successful DEV candidate becomes an immutable calculation release candidate: contract SHA, exact source/base/runner/input hashes, absent-output guard, runtime dependency map, official command and timeout, thresholds, identity of the RC author, and distinct static auditor are frozen. | `DEV_TESTS_PASS` with no open technical failure. | The exact RC capsule is complete and handed to an independent static auditor. Any change to a frozen byte invalidates the RC and requires a new freeze. |
| `INDEPENDENT_STATIC_MATH_AUDIT` | A distinct auditor, without an official run, checks equations, signs, units, gauge, state order, provenance, guards, decision branches, and the runtime contract of the exact RC. This is not a physical verdict. | A hash-matching RC and verified separation between author and auditor. | A PASS recommendation allows the orchestrator to consider authorizing the official run. A code/transcription error returns to `DEV_SANDBOX`; a contract error to `CONTRACT/DRAFT`; a track-identity change goes to the author. |
| `OFFICIAL_RUN_AUTHORIZED / OFFICIAL RUN` | The orchestrator authorizes one bounded execution of the exact audited RC on official inputs. Output is published exactly once into a pre-absent target and becomes immutable raw after success. | Static PASS recommendation, matching hashes, RC absent from DNR, absent target, and `RUN_AUTHORIZED=true`. | Complete raw and execution receipt satisfy schema and hashes, opening internal science audit. Crash, timeout, dependency, or schema failure is technical with no physical verdict and returns to the earliest faulty upstream point. |
| `INTERNAL_SCIENCE_AUDIT` | For official raw, an independent physics auditor interprets the result against the contract: physical meaning, covariance, conservation, gauge, causality, stability, limits, convergence, observables, and exact claim/death reach. | Complete immutable raw, execution receipt, and a distinct internal physics auditor. | The audit recommends an action to the orchestrator. A material `S1–S4` finding activates `CLAIM_QUARANTINE` and finding-impact/identity review; a technical `T1` returns to the reachable technical point. |
| `FROZEN_MANUAL_ANALYTIC_RESULT / MANUAL_ANALYTIC_RESULT_AUDIT` | A separate non-RC branch for a manually derived analytic result. The exact proof body, inputs, claim scope, and record of one-time consumed authorization are frozen; a distinct `manual_analytic_result_auditor` checks equations, logic, provenance, and claim reach. This branch uses no project code, Python, network, RC, or official output and does not by itself create an observable claim. | Explicit one-time authorization, hash-frozen body and inputs, and a verified prohibition of self-audit. | The auditor provides only a recommendation to the orchestrator. The manual audit alone authorizes no checkpoint, external package, physical verdict, or observational verdict. |
| `ORCHESTRATOR_DECISION` | The main orchestrator combines the evidence of the applicable branch with its independent audit and alone records the authoritative exact-scope state: accepted `PASS`, `REVIEW/LIVE-WAITING`, or `STOP_SCOPE`. For the computational branch it reads the contract, RC/raw, and internal science audit; for the manual branch, the frozen analytic body and inputs, authorization record, and manual audit. It must not broaden evidence reach. | Completed internal or manual audit, or a closed finding decision record. A physics/identity change first requires Martin Jámbor's decision. | The authoritative scoped state and dependencies are recorded, opening milestone progress review. |
| `MILESTONE_PROGRESS_REVIEW` | Assesses information gain: whether a gate closed, blocker or route changed, work still serves the goal, and the smallest useful next scientific atom. It does not alter the physical verdict. | An accepted official/scientific result, authoritative blocker/route change, `10/10` permission gate, or explicit goal-drift concern. | Selects the next step, wait state, suitability for external audit, or — only for an accepted reproducibly auditable milestone, scoped STOP, or scientifically material blocker — `ACCEPTED_CHECKPOINT_FREEZE`. A `TECHNICAL_PERMISSION_GATE` alone creates neither a checkpoint nor an external package. Routine DEV repair, compile, or smoke testing does not trigger this phase. |
| `ACCEPTED_CHECKPOINT_FREEZE` | An accepted coherent milestone, scoped STOP, or important accepted blocker is bound to its parents and the evidence of the applicable branch in a reusable checkpoint. A computational checkpoint binds hashes of the contract, RC, inputs, raw, and internal audit; a manual analytic checkpoint binds hashes of the frozen analytic body, inputs, authorization record, and manual audit. A checkpoint does not broaden scientific reach. | The orchestrator accepted the exact result and progress review confirmed lasting informational or audit value. | The checkpoint is appended to the registry. It may seed the next scientific atom or a canonical external-audit package; without a new result it is not rewritten. |

The most important return and blocking branches are:

| Event | Mandatory consequence |
|---|---|
| Routine DEV failure | Repair the same working source, record one technical error and regression test; no physical `STOP` arises. |
| Ten technical errors in a batch | `TECHNICAL_PERMISSION_GATE`; further edit or run waits for Martin's explicit permission. |
| Static audit finds an implementation error | Return to `DEV_SANDBOX`, pass a new DEV suite, and freeze a new RC hash. |
| Static or science audit finds a contract/equation error while identity is preserved | Return to `CONTRACT/DRAFT`; repeat only the affected point and descendants. |
| Official run fails technically | No physical result; repair the earliest reachable technical cause and do not repeat the official run without new authorization. |
| Audit finds `S1–S4` | `CLAIM_QUARANTINE` of the earliest affected point and all transitive descendants -> one joint impact/identity decision record -> `MARTIN_DECISION_GATE` to choose same-track repair, a new track, or termination of the exact scope -> the orchestrator records the exact return point and authoritative state. The auditor only recommends. |
| Result is `LIVE / WAITING` | The track remains alive; the plan must name the exact missing input, reactivation condition, and what must not be repeated without new evidence. |

DEV uses synthetic tests and carries no scientific verdict. Every Python
process has internal and external time limits. Before an official run,
record in plain language what is calculated, the expected range, the
PASS/REVIEW/STOP branching, and what follows from a deviation. Preserve
scripts, inputs, environment, commands, raw output, and hashes. An unusable
script is marked in DNR/history and must not mislead a future auditor.

One implementation line has ten technical errors per batch. A technical
error is not a physical result. At `10/10` the author decides whether to
authorize another batch; a filename or agent change does not reset history.
Technical errors affect only the process — they stop further editing or a
run pending authorization — and never by themselves change a physical
PASS/REVIEW/STOP or the viability of the parent track.

Audit findings use `P0_PACKAGE_PROCESS_ONLY`,
`T1_TECHNICAL_NO_CLAIM_REACH`, `S1_LOCAL_CORRECTABLE_SAME_TRACK`,
`S2_TRACK_IDENTITY_AT_RISK`, `S3_FATAL_IN_SCOPE`, and
`S4_PARENT_THEORY_IMPACT`. `S1–S4` activate claim quarantine and one joint
decision record covering mathematical, physical, and philosophical/identity
reach. Only the main orchestrator records authoritative PASS/REVIEW/STOP.

### 5.1 Internal audit capsule and canonical external package

Internal audit does not create a newly copied evidence set after every step.
The auditor receives a hash-bound **internal capsule** that points to the
exact contract/preregistration, RC source and inputs, decision thresholds,
dependent checkpoints, and audit questions. The computational branch
contains immutable raw and an execution receipt; the manual analytic branch
contains the hash-frozen result body and inputs and the consumed one-time
authorization record. The artifact author, static mathematical auditor,
manual analytic auditor, and internal physics auditor must be distinct as
required by the applicable branch and separation-of-duties rules.

A separate **canonical external audit package** is created only after an
accepted coherent scientific milestone, a physical `STOP_SCOPE`, or a
material blocker worth independent assessment outside the project. It
contains at least:

1. scope and reading order;
2. a manifest and SHA-256 of every included file;
3. auditor instructions and exact questions;
4. expectations, reproduction command, and runtime/dependency map for a
   computational result;
5. checkpoint provenance and parent assumptions;
6. for the computational branch, the exact contract, RC, inputs, raw,
   internal audit, and only the required scripts; for the manual analytic
   branch, the frozen analytic body and inputs, authorization record, and
   manual audit without pretending that RC/raw exists.

After sealing, the package is immutable. The same bytes may be submitted to
several independent auditors; every submission has its own
`AUDIT_SUBMISSION_ID` and separate response path. A new auditor normally does
not read the other responses. The external package curator must not audit
their own package. Conflicting assessments open an
`AUDIT_DISCREPANCY_REVIEW`, not a majority vote. A DEV failure, syntax error,
or routine support step does not create a separate external package. An
error confined to the package control layer is
`P0_PACKAGE_PROCESS_ONLY`; if the scientific evidence hashes are unchanged,
only the package is repaired and resealed, not the scientific calculation.

Published versions are immutable. Each new version is a complete,
self-contained snapshot and also has a changelog, manifest, SHA-256, errata
links, and changed verdicts. The changelog must not carry a definition
needed to understand the current theory. SK is the semantic authority; EN
must preserve identical IDs, equations, numbers, statuses, and nonclaims.

## 6. Historical graveyard and current dead scopes

The full historical #1–#20 graveyard remains in the immutable archive as
optional provenance; it is not required to understand current v3.18. Its
labels must not automatically be read as death of broader modern tracks. In
particular, the old statements “S8 brakes excluded” and “the only lever is
lambda->0.10” have no universal force after later lineage audits. Reuse must
identify the exact old scope, evidence of death, and difference of the new
mechanism.

Current scientific scoped STOPs in A2 are:

- `A2-K1 / M-009`: exact tested fluid scope;
- `A2-K2 / M-008`: exact barotropic class;
- `A2-K3 / M-010`: exact tested transfer scope;
- `A2-K5 / M-012`: a specific conformal action;
- `A2-K6 / M-013`: the healthy interval of a specific operator.

These STOPs do not kill A2 as a whole. `A2-K4` is `LIVE_ACTIVE / 60/100`,
while `A2-K7`, `A2-K8`, `A2-K9`, `A2-K11`, and `A2-K12` are registered
waiting alternatives, not positive survival witnesses. `A2-K10` is
`SEPARATE_ROUTE / NOT_AUTHORIZED` under the background track `A1-K2`; it is
neither a dead track nor a backup of the active `A1-K1` route. The number
`60/100` is the cumulative weight of preregistered physical gates
authoritatively passed by A2-K4: G5 closed 50 points and G6 increased the
depth to 60. G6 applies only to the frozen nine-variable perfect-radiation
effective-fluid scope and its audited signs, characteristic speeds,
principal symbol, stiffness, and convergence. It is not a microscopic UV
no-ghost theorem, proof of global hyperbolicity, or proof of global stability
of all modes. It is not a probability of truth, posterior, fraction of all
requirements, or fraction of functions with a witness. An open or merely
technical subgate adds no points; the historical technical depth
`66.5/100` of the reduced runner is not part of this physical score. Its
reader-facing name is **registered depth of passed physical gates**; current
readiness is separately `A2_CLOSURE_NOT_ESTABLISHED / A3_ENTRY_BLOCKED`.

A3 is blocked in three senses at once: procedurally it is not authorized
before acceptance of one complete A2 track; physically A3 needs a closed
linear perturbation system, a production-transport operator, and regular
initial data; audit-wise no complete hash-bound A2 checkpoint yet exists.
This is a `WAITING` entry gate, not a physical STOP of A3.

## 7. Question register Q1–Q34

| ID | Question | v3.18 status and reason for restriction |
|---|---|---|
| Q1 | Does division keep the network stable? | `HISTORICAL / PARTIAL`. The v3.17 simulation is evidence for one model, not a continuum theorem. |
| Q2 | Is `delta` a local overhead derived from network degree? | `REVIEW`. `delta_mean=1/(<k>+C)=0.0229697828` is the frozen benchmark. If microphysics defines `delta_loc=<1/(k+C)>`, Jensen gives `delta_loc>=delta_mean`, strictly only for nondegenerate `P(k)`. No numerical correction or universal `delta(a)` follows without a frozen `P(k)`. |
| Q3 | What transfer form `Gamma/Q` follows from microdynamics? | `CONDITIONAL_BACKGROUND_ONLY`. The A1-K1 scalar ledger works at background level; it is neither full `Q_A^mu` nor a micro-operator. |
| Q4 | What scars follow from `xi->1` without the bilinear trap? | `OPEN`. A mechanism linking failure, scar, and products is missing. |
| Q5 | Does Newton's law grow from the entropic rule? | `HISTORICAL NUMERICAL SUPPORT`. High R2 in specific simulations is not a derivation of GR, PPN, lensing, or universal G. |
| Q6 | Does network growth have a preferred direction? | `PARTIAL`. The observed anisotropy decrease needs an analytic/continuum limit. |
| Q7 | Does genesis change the sound horizon? | `SCOPE_NARROWED`. Historical late scenarios do not close a new early source and full background. |
| Q8 | Are scar, collapse, and arrow of time one mechanism? | `OPEN`. The verbal identification has no microscopic operator. |
| Q9 | Do V-links reduce overhead into the required window? | `HISTORICAL / MODEL-DEPENDENT`. `C=28` is not an independent theorem. |
| Q10 | What creates and destroys V-links? | `HISTORICAL SUPPORT / OPEN MICROPHYSICS`. A simulated attractor is not a complete local action. |
| Q11 | Do the horizon and primordial spectrum arise without an inflaton? | `RECALCULATION_OPEN / ACTIVE_SCOPED_TARGETS`. P02 `n_s=0.9656 +/- 0.0016` and P03 `r<1e-10` remain current formulation-scoped survival conditions, but the gauge-invariant source, amplitude, and closed tensor source-to-observable dynamics are missing. The exact `n_s-w` relation belongs to withdrawn P08. |
| Q12 | Are the VCM-1 rules Lorentz-consistent? | `SCOPE_NARROWED`. Exact evenness is a local algebraic property of the audited scalar cosine-Laplacian operator, not a global Lorentz symmetry of the full system; full photon/boost/EP sectors remain open. |
| Q13 | Is the grown network a statistical manifold? | `STOP_SCOPE HISTORICAL` for exact reading 1; other definitions require a new track. |
| Q14 | Does the signal front sharpen? | `HISTORICAL NUMERICAL SUPPORT`. A KPZ-like exponent in a box is not by itself proof of a sharp Lorentz cone. |
| Q15 | Does digestion emit steam and what is `Delta N_eff`? | `CONDITIONAL_NUMERICAL_DERIVATION / OBSERVATIONAL_RANGE_NOT_YET_INFERRED`. The qualitative origin of steam in processing vacuum fuel is present; with `g_x=2`, `g_*s,dec=106.75`, `Delta N_eff=0.0535`. It is a survival commitment of exactly this P01/P11 thermal formulation, not a global prediction of the theory. Local `C_s^mu`, branching, timing, exit/reheating, and survival remain open. |
| Q16 | Can `C=28` be derived from domains? | `OPEN`. The `16+8+4` decomposition is a consistent bosonic degree count of the unbroken Standard Model; the four real Higgs directions already include the three would-be Goldstone directions. Missing is a derivation of why exactly this bosonic count equals cell capacity, why fermions are excluded, and why the identification is not ontologically circular or a look-elsewhere choice. |
| Q17 | What are the bispectrum and `f_NL`? | `OPEN`. A gauge-invariant conversion, shape, sign, and higher order are required. |
| Q18 | When is steam/the wave relic produced? | `CRITICAL OPEN / OBSERVATIONAL INVERSE PROGRAM`. Derive `dot(rho_s)+4H rho_s=C_s` through the early phase, exit, and reheating; BBN/CMB must constrain the admissible source band without double-counting data. Until this forward map exists, `Delta N_eff=0.0535` remains a scope-bound commitment of the declared thermal branch, not a posterior or theory-level kill window. |
| Q19 | Which matter component is produced by `Q`? | `BACKGROUND GATE PASS ONLY`. A1-K1 maps the product in the homogeneous account to a pressureless ash/CDM candidate and conserves baryons; clustering, particle identity, perturbations, and microphysics remain open. |
| Q20 | What is the complete gauge-invariant perturbation system? | `CRITICAL OPEN`. No A2 track is complete; A2-K4 is the deepest live track. |
| Q21 | What is `T` in `T proportional H`? | `CRITICAL OPEN`. An independent thermodynamic definition is required. |
| Q22 | How do `zeta`, `P_zeta`, `A_s`, and `n_s` arise from division? | `CRITICAL OPEN`. Realized Fourier `k` must not determine the FLRW background; this is the fundamental separation of homogeneous background from perturbations, not a new optional convention. Older expressions with `K_MPC=0.05` and implicit `Phi=1` were restricted precisely because they violated this separation. The common source and its spectrum are not derived. |
| Q23 | What ends the fuel era and reheats the universe? | `CRITICAL OPEN`. Exit, entropy, radiation domination, and BBN initial conditions are missing. |
| Q24 | Is the substrate 3D with a tick or a 4D causal structure? | `AUTHOR-LEVEL CONCEPTUAL OPEN`. Derive a Lorentzian limit or test a preferred frame. |
| Q25 | How does one capacity ensure universal coupling of fields? | `OPEN`. A shared metric, multiple spins, EP, and birefringence are required. |
| Q26 | Is cross-V weight quantum entanglement entropy? | `OPEN`. Classical weight without a Hilbert space and channel is insufficient. |
| Q27 | What is local overhead at fluctuating degree? | `OPEN`. Decide between `1/(<k>+C)` and `<1/(k+C)>`. For the latter, the former is the exact Jensen lower bound rather than the completed average; a numerical result requires the degree distribution `P(k)` of the growing network. |
| Q28 | What is the dynamical meaning of `C=28` independent of `n_s` data? | `OPEN`. A pre-data derivation from symmetry or action and an explicit map between the bosonic content of the emergent Standard Model and substrate capacity are required; the arithmetic `28` alone is insufficient. |
| Q29 | Does division satisfy the second law of thermodynamics? | `OPEN`. Entropies of all reservoirs and nonnegative total production are required. |
| Q30 | What are the kill conditions of predictions and other existence requirements? | `METHODOLOGY DEFINED / ROW-SCOPED`. Document 02 records the survival target, exact death scope, and meaning of agreement for P01–P11; document 04 is the complete EC01–EC43 index including exact laws, open windows, calibrations, and process exclusions. A result outside a window kills only the declared scope after a complete likelihood; a result inside keeps that same scope alive and does not exclude QCTS in that test, but by itself proves neither its global viability nor its truth. |
| Q31 | What is ash microphysics? | `OPEN`. Spin, mass, stability, distribution, phase space, and halo tests are not derived. |
| Q32 | What is the continuum limit of gravity? | `OPEN`. Einstein/Poisson limits, lensing, PPN, and polarizations are required. |
| Q33 | Does the network derive global curvature without H0 data? | `OPEN / SEPARATE TRACK`. Historical grids are not a pre-data derivation of `Omega_K`. |
| Q34 | Can division create covariant momentum exchange in the dark sector? | `CONDITIONED OPEN`. Full `F_A^mu`, counter-momentum, stability, and CMB/LSS mapping are required; a phenomenological drag fit is insufficient. |

## 8. Mandatory ledger of later-restricted formulations

| Older formulation | Original scope | Decisive test or constraint | v3.18 state and exact reach |
|---|---|---|---|
| `K_MPC=0.05` as a background or network scale | global FLRW background or fundamental network scale | the background must be invariant under change of the realized Fourier mode, so `partial H_FLRW(a)/partial k=0` | `WITHDRAWN INTERPRETATION`. Provenance identifies a mode/pivot; the value `0.05` is not itself a kill condition, but using it as a background scale invalidates that formulation. |
| `Phi=1` and `Phi z^p` as the global fuel term | global fuel normalization in the K4 background | exact mode cancellation `Phi(k) z^p=A_f a^p` | `CORRECTED`. The old global term is superseded; the correction does not by itself change the viability of the broader A2-K4 track. |
| `A_f` as an underived new parameter | fuel normalization in the frozen A1 background closure | lineage to declared A1 inputs and prohibition of a new silent fit | `CORRECTED / CONDITIONAL`. `A_f=7809.270101963506` is a bookkeeping result, not a microphysical constant; it has no standalone observational kill window. |
| `Delta N_eff=0.0535`, `0.905 K`, `53 GHz` | early two-polarization thermal P01/P11 formulation | complete `C_s^mu`, branching, exit/reheating, survival, and BBN/CMB forward map with likelihood | `CONDITIONAL_NUMERICAL_DERIVATION / SURVIVAL_TARGET`. Robust disagreement after the complete test kills this formulation, not automatically the full theory. |
| `n_s=0.9656 +/- 0.0016` and `r<1e-10` | exact `delta/m=1/2` scalar mechanism and exact thermal tensor formulation | complete gauge-invariant scalar and tensor system, source-to-observable map, normalization, and likelihood | `ACTIVE_FORMULATION_SCOPED_SURVIVAL_TARGETS / RECALCULATION_OPEN`. P02 and P03 remain current survival conditions; agreement only keeps them alive and is not confirmation of QCTS. |
| exact `n_s-w` relation | exact common scalar/background relation | new independent derivation of the relation | `WITHDRAWN / NO_CURRENT_DEATH_REACH`. P08 has no v3.18 survival target and must neither kill nor rescue the current track. |
| general Lorentz invariance from parity of one operator | full photon/boost/EP and multi-field sector | distinction between local operator evenness and global covariance/universality | `SCOPE_NARROWED`. Exact evenness of the scalar operator remains; general Lorentz invariance does not follow from it. |
| one scalar `Q_A` determines the production order of matter, ash, and steam | local causal production graph of all three components | complete covariant `Q_A^mu`, counter-momentum, local branchings, and `delta Q_A` | `SCOPE_NARROWED`. The background energy ledger remains usable, but parallel versus sequential ordering stays open. |
| three H0/S8 points as a new interval or fit | continuously interpreted observational interval or posterior | full likelihood, covariance, systematics, and continuous parameter map | `FORBIDDEN CLAIM`. The points remain only discrete conditional diagnostics against a synthetic anchor; the P04/P05 survival conditions are separate current commitments. Failure of the three points reaches the diagnostic, not automatically the theory. |

## 9. Live unresolved functions and return points at the content cutoff

The following table freezes the state as of 9 August 2026. Later working
results belong to the next release delta or a new version and must not
silently change this snapshot.

| ID | Function / route | Current state | What can close it |
|---|---|---|---|
| `UF-C01-RW1-KBRIDGE-001` | `A2-K4/P5`, local stress-work/current bridge | `RANGE_CONDITIONAL_OPEN / LIVE-WAITING` | global local-natural witness or existence theorem over complete face/bulk data and guards |
| `OR-C01-RW1-KOUT-001` | state-local output correspondence of the bridge | `CORRECTED RESULT ACCEPTED / OUTPUT_RANGE_CONDITIONAL_OPEN / RESERVOIR_INTERSECTION_CONDITIONAL_OPEN` | proof of nonemptiness, compatibility, and later realizability by one admissible function; acceptance of the conditional result does not prove a global `K_bridge` or witness existence |
| `UF-Q18-CG-001` | early steam/wave source `C_s` (historically `C_g`) | `OBSERVATIONAL_RANGE_NOT_YET_INFERRED / OPEN` | covariant source/reservoir, branching, exit, reheating, BBN/CMB forward map, and calibration/validation split |
| `UF-Q22-SOURCE-001` | common perturbation source from energy-demanding divisions | `OPEN` | local operator, `P_S(k)`, gauge-invariant conversion, and prohibition of a `k`-dependent background |

## 10. Release nonclaims

This register is not proof of the full theory, does not grant an A2 PASS,
does not change `A2-K4 / 60/100`, and does not open A3. It preserves only
explicitly identified conditional or formulation-scoped survival targets for
`H0`, `S8`, `N_eff`, `n_s`, `r`, `w0`, `wa`, temperatures, and frequencies
as falsification commitments with row-limited reach. P08 is withdrawn with
no current target, and P09 is only a benchmark with no active target or
target-based STOP. P01 and P11 form one joint thermal commitment and must not
be counted as independent confirmations. Agreement with a survival condition
only keeps the exact scope alive; these values are not automatically new
posterior intervals or confirmed theory-level predictions.
