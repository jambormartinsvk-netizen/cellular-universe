# Working Methodology Rules and Question Register — EN

**Layer:** `tracks/` — working layer, not the release corpus  
**Updated:** 2026-08-01  
**Status:** authoritative working navigation; consolidated into `theory/` only for a release candidate

## Duplication check

The frozen base contains AR1–AR8 and the historical addenda contain AR9–AR69.
AR5 protects published versions, AR7 requires SK/EN parity, AR66 governs live
plans, and AR69 governs artifact ownership. None of them defines where a
working candidate originates and when it may enter `theory/`.

## AR70 — boundary between the working register and release corpus

1. A new working question, status change, rule candidate, limitation, audit
   discussion, or preregistration originates at the lowest applicable
   `tracks/<route>/` node.
2. Ordinary track state is maintained in `00_WORK_PLAN.md`,
   `00_CURRENT_DECISION.md`, `HISTORY/00_EVENT_LEDGER.md`, a manifest, or
   `AUDIT_THREADS/`; it does not create a new `theory/*/05...` file.
3. If a node genuinely needs a local AR/Q/L delta register, it may use the
   optional pair `05_RULE_AND_QUESTION_CANDIDATES_SK.md` and
   `05_RULE_AND_QUESTION_CANDIDATES_EN.md`. It contains deltas only, not a
   copy of the full register, and is marked `WORKING / NOT_RELEASED`.
4. A candidate shared by several tracks is maintained in this global working
   register under `tracks/METHODOLOGY/`, again as a content-matched SK/EN pair.
5. `theory/SK` and `theory/EN` contain released or release-ready consolidated
   content. An intermediate runner, technical erratum, open question, or
   `REVIEW` state is not added there as a new thematic addendum.
6. Only the main orchestrator may promote content to `theory/` while a release
   candidate is open, after duplication, evidence-chain, SK/EN parity,
   changelog, release-trigger, and SHA-256 manifest checks.
7. Existing historical `theory/*/05*` files are neither deleted nor physically
   moved without a Git baseline, a complete `OLD_PATH -> NEW_PATH` map, link
   checks, and hash checks. From 2026-07-16 they are frozen as a historical or
   release layer and are not a live working-write location.

## Replacement for the old workflow

The old instruction “a new rule gets a new paired addendum in `theory`” is
replaced by:

> A new rule first receives a paired working record at the applicable depth
> under `tracks`. It is consolidated into `theory/SK` and `theory/EN` only
> after acceptance by the main orchestrator and opening a release candidate.

## FS-GATE-01 — constrain behavior before choosing the function

Before selecting a concrete function, action, or kernel, create a behavioral
and then physical constraint passport under
`tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_EN.md`.

1. First record inputs, outputs, signs, trends, thresholds, zeros,
   saturation, and energy bounds known from physical laws or observation.
2. If these necessary behaviors contradict one another, the subfamily gets
   `BEHAVIORAL_EMPTY_SCOPE`; the exact function need not be known.
3. A non-empty behavioral envelope gives only `BEHAVIORAL_OPEN`, not a
   physics PASS. One explicit local witness must then be found.
4. A failed grid or missing ansatz does not prove emptiness.
5. A death reason is recorded as certified non-existence of a common output
   set in the stated scope, not “we did not find the function.”
6. This working gate adds no score and creates no new AR/Q number while the
   identifier register is locked.

### FS-GATE-01a — evidence force and distinction of a pre-computation no-go

**Accepted by the user:** 2026-07-17  
**Status:** binding clarification of existing FS-GATE-01; no new AR/Q ID.

1. Every future function/kernel constraint is labelled `E0_EXACT`,
   `E1_DIRECT_MEASUREMENT`, `E2_REFERENCE_MODEL`, or `E3_PROVISIONAL`
   under `00_CONSTRAINT_FEASIBILITY_GATE_EN.md`.
2. Only `E0` and a completely mapped `E1` may exclude a subclass before
   constructing a function. `E2` is a mandatory comparator/null limit, not
   an automatic STOP; its standalone mismatch is `REFERENCE_MISMATCH_ONLY`.
   `E3` is guidance, not a death reason.
3. An `E1` record must state confidence level, statistical and systematic
   error, sector/sign, units, and the model-to-observable mapping.
4. Such a pre-computation exclusion receives `PRECHECK_EXCLUDED_SCOPE` and
   `NO_CANDIDATE_RUN`. It is valid only in the certified space, adds no
   canonical depth, and may not be summarised as `COMPUTED_STOP_SCOPE`.
5. Only a complete preregistered physical calculation is
   `COMPUTED_STOP_SCOPE`; only a complete model -> observable -> likelihood
   chain is `OBSERVATIONAL_STOP_SCOPE`. A technical incident remains
   `TECHNICAL_STOP`.

## FS-GATE-02 — an unknown function is carried as a feasible set

**Author decision:** Martin Jambor, 2026-08-01

When a concrete function, kernel, or local transport law is not yet known,
the workflow does not arbitrarily select one representative. It first builds
the feasible set

```text
A_f={f in F_adm:
     every exact physical identity holds,
     every inequality/regularity/causality/stability guard holds,
     every open measured observable lies inside its preregistered
     tolerance region}.
```

1. `F_adm` states the domain, codomain, regularity, locality, covariance,
   units, allowed jet, null limits, and forbidden new fields/scales.
2. Exact laws (`E0`) apply without tolerance. Measured compatibility is
   tested only through a frozen observable map, dataset provenance,
   uncertainties, covariance/systematics, and an explicit confidence or
   coverage region; vague “plus or minus an error” is not a decision bound.
3. A valid scientific result may be an entire non-empty set or interval; a
   unique function is not required, and a null or minimum-norm direction is
   not selected without another physical principle.
4. `RANGE_EXISTENCE_PASS` requires an explicit witness or an existence
   theorem. A list of conditions alone is `RANGE_CONDITIONAL_OPEN`.
5. If existence is undecided, the function receives a durable
   `UNRESOLVED_FUNCTION_ID`, exact constraints, dependent gates, and a
   reactivation input. The track remains `LIVE / WAITING`, and a deeper
   audit can return to this identifier.
6. `EMPTY_SCOPE_CERTIFIED` is allowed only after a proof that the feasible
   set is empty in the exact scope. Finding zero ansatzes, grid points, or
   explicit formulas does not prove emptiness.
7. The theory-level feasible set is maintained on the common state space:

   ```text
   A_theory = A_exact
              intersect A_observational
              intersect intersection_i pullback_i(A_i).
   ```

   The theory has at least one feasible whole in the tested scope only when
   this common set is non-empty. While a mandatory function or observable
   map is missing, the state is `GLOBAL_FEASIBILITY_INCOMPLETE`, neither
   PASS nor STOP.
8. Every accepted interval propagates into descendants as a set-valued
   constraint; it may not be silently replaced by its center, a
   minimum-norm point, or a fitted representative.

### FS-GATE-02a — return to an unresolved function and death logic

1. Every unresolved mandatory function has a durable record in the lowest
   route-local `00_STATUS.md` or work plan: `UNRESOLVED_FUNCTION_ID`,
   domain/codomain, admissible class, every E0/E1/E2/E3 constraint, current
   allowed output ranges, witness/certificate state, dependent gates, and
   the exact reactivation input. Parent plans carry only a summary and link.
2. `RANGE_CONDITIONAL_OPEN` means that no contradiction has yet been
   certified; it does not prove existence. `RANGE_EXISTENCE_PASS` means that
   at least one common range or function witness passed every currently open
   E0 and fully mapped E1 constraint. It is not by itself a PASS of later G
   gates.
3. At an `AND` node every child is mandatory and the intersection of their
   pullbacks decides feasibility. The node dies only after a certificate
   that this common intersection is empty. At an `OR` node children are
   alternative tracks; the node dies only when the alternative list is
   proven exhaustive and every alternative has `EMPTY_SCOPE_CERTIFIED` in
   the same scope.
4. A track remains `LIVE / CONDITIONED` or `LIVE / WAITING` while at least
   one alternative has a non-empty witness or an open, uncertified feasible
   set. Failure to find a formula, an empty finite grid, or incomplete
   constraint mapping does not kill it.
5. The theory is `GLOBAL_FEASIBILITY_INCOMPLETE` while a mandatory function
   or model-to-observable map is missing, or at least one declared
   alternative is unresolved. `THEORY_PHYSICALLY_DEAD_IN_SCOPE` is allowed
   only after proving that the global common feasible set is empty and every
   top-level alternative in a proven-exhaustive partition has died. Reasons
   and certificates are never deleted.
6. Measurement errors are not a free tolerance. An E1 region states the
   dataset, confidence/coverage, statistical and systematic uncertainties,
   covariance, and exact model-to-observable map. A proven E0 law has no
   measurement tolerance unless the theorem itself explicitly contains an
   approximation.

### Register of unresolved functions

| ID | Route / function | Admissible class and current result | Missing item | Reactivation / dependent gates |
|---|---|---|---|---|
| `UF-C01-RW1-KBRIDGE-001` | `A2-K4/P5/B6b-2.12`, `K_bridge^CT` | task504 is quarantined for an evaluation/operator-type mismatch; the corrected D2SW5 task506 `RANGE_CONDITIONAL_OPEN` candidate awaits audits | the pointwise geometric obstruction is characterized, but existence of one global local-natural operator, combined kernel compatibility, and exact cap/current-side/traction data are not evaluated; the observational intersection is not open | explicit same-track operator witness or local-natural relative-horizontal existence theorem; blocks unique physical `P_boundary`, state-sufficient reservoir set, D2I/D3-D6, and P5.4 |

## WORKING-TECH-INCIDENT-NONCONSUMPTION — a technical failure does not consume a physics attempt

**Accepted by the user:** 2026-07-16  
**Status:** binding working rule without a new AR identifier while the
identifier register remains locked.

Duplication check: the error ledger already separates parser, import,
timeout, serialization, and tool failures from a physics result. AR67
forbids killing a track from a timeout or parser alone. What was missing was
the explicit rule that these incidents consume no physics attempt and cannot
exhaust the track.

A physics attempt is counted only when a run or analytic package:

1. implements the preregistered physics, complete mandatory state, and rows;
2. completes technically with valid provenance, a finite output, and no
   known formal defect;
3. has sufficient holdouts and convergence to interpret a physical
   PASS/STOP criterion;
4. passes or fails a physical law, invariant mathematical condition, or
   preregistered observational range.

Syntax, import, timeout, missing dependency, marker, wrong register,
state/RHS parity, serialization, unit, adapter, cache, path, transcription,
or other implementation failures are technical incidents. Record them in
the error ledger, preserve and label the defective artifact, and require the
repair to pass preflight. They consume no physics attempt, may issue no
physical STOP, and may neither kill nor permanently block the parent track.

There is no hard count of technical repairs. Repetition of the same failure
class triggers an architectural review, shared-base test, or replacement of
the technical path, not death of the physics. To prevent runner
proliferation, prefer one versioned base, one stable runner, and new immutable
run IDs; create a new physical suffix only when equations, mechanism, or
physical scope change.

This working rule limits the historical AR66/AR67 wording “at most two
technical corrections.” The original remains as history. Its budget may now
be read only as at most two preregistered **physical** variants/attempts in a
package, not as a cap on syntax, runtime, or implementation repairs.

### Later user clarification — technical cap of 10

The sentence “there is no hard count of technical repairs” was refined later
on 2026-07-16: one concrete technical implementation branch has at most
**10 technical attempts**. Every attempt needs an ordinal number, input,
result, and failure cause in a route-local technical ledger.

After the tenth technical failure, only that implementation branch receives
`TECHNICAL_STOP`. Its record must identify at least one cause:

- `SCRIPT_IMPLEMENTATION_FAILURE` — no script passed preflight and completed
  reliably;
- `PYTHON_OR_DEPENDENCY_FAILURE` — interpreter, package, or runtime;
- `SANDBOX_OR_ENVIRONMENT_FAILURE` — sandbox, permission, or host issue;
- `BUILD_OR_ADAPTER_FAILURE` — compilation, binding, or external backend.

`TECHNICAL_STOP` is not a physical STOP. The parent physical track remains
`REVIEW_TECHNICAL_UNRESOLVED`; its mechanism may not be marked dead. Work may
continue through a different preregistered technical architecture with its
own new `0/10` ledger, without changing the physical suffix unless the
equations, mechanism, or scope change. This clarification supersedes only
the earlier unlimited-repair sentence; the remainder of the rule stays in
force.

Every launched preregistered technical package occupies one ordinal slot
`n/10`, whether it ends in a technical FAIL or a scoped PASS. Compile and
`--help` commands inside that package are not separate attempts. If the
tenth package does not close the technical branch, that branch receives
`TECHNICAL_STOP`; the reason must distinguish earlier failures and the state
of the tenth package.

Renaming a runner, base, or technical suffix may not reset the counter. A
new `0/10` ledger is allowed only after a differential audit demonstrates
that the architecture does not address the same implementation problem
lineage and does not inherit its defective contract. K4 R-A therefore
conservatively inherited attempts 1–3; K11 full-v002 started at `0/10`
because old S0-v001 was a distinct formula-regression register and the
differential audit froze a new multispecies/thermal/TCA/DAE contract.

### Latest user clarification — count consecutive technical failures

**Accepted:** 2026-07-16. This clarification supersedes only the older
sentences under which every substantive package permanently occupied an
`n/10` slot and success could not reset the counter.

The active counter is the number of **consecutive technical failures** in
the same track/subtrack and implementation-problem lineage. After every
substantive calculation that completes technically, has valid provenance,
contains no known formal defect, and delivers at least a partial
interpretable result, reset the active counter to `0/10`. This holds whether
the physical outcome is scoped PASS, REVIEW, or invariant STOP; a successful
calculation is technically successful even when it falsifies the physics.

`py_compile`, `--help`, smoke, parser/CLI checks, hash-only checks, empty
diagnostic runs, or test scripts without a new partial result do **not**
reset the counter. Nor does merely renaming a file or architecture. Every
route-local ledger must therefore keep two distinct quantities:

```text
historical_packages_total      — immutable audit history,
consecutive_technical_failures — active cap 0..10.
```

At `10/10` consecutive technical failures, the implementation lineage gets
`TECHNICAL_STOP`. Earlier failures are never deleted after a reset; their
causes remain in history. Physics attempts and physical death continue to be
governed only by lines 78–93 above.

## WORKING-TASK-AND-AGENT-BOUNDARY — split tasks without losing authority

**Accepted by the user:** 2026-07-16 as a working organizational rule
without a new AR identifier.

Create a separate main task for a physically independent work package, not
automatically for every suffix, mode, parameter, or technical repair. A new
task is justified when the package has its own state/equation contract, its
own PASS/REVIEW/STOP point, is mostly independently auditable, and is
expected to produce multiple substantive runs or extensive documentation.

Atoms that use the same equations and differ only by mode, `k`, variant,
tolerance, or support remain in one task. The orchestrator owns the
authoritative registers and verdicts and transfers between tasks only a
frozen handoff: objective, mandatory inputs/hashes, constraints, current
state, and the exact done condition.

Use subagents primarily for bounded read-only work: hashes and manifests,
link/ID checks, indexing, log/JSON triage, source-lineage, and independent
reviews. Physical derivation, formula changes, mechanism selection, and
PASS/REVIEW/STOP remain with the main reasoning agent. Avoid parallel
write-heavy work when agents could edit the same files.

## Open working items

- complete the classification of historical `05` pairs without changing them;
- resolve confirmed collisions AR8, AR9, AR37–39, Q20, Q64–67, and Q72 under
  `tracks/METHODOLOGY/00_IDENTIFIER_COLLISION_LEDGER.md`; do not allocate
  another global AR/Q number until then;
- prepare the exact migration map after a Git baseline exists;
- before v3.18, build one consolidated SK/EN release register instead of a
  chain of thematic addenda.
