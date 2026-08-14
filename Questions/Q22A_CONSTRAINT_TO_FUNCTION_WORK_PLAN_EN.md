# Q22a/Q18 — proposed procedure: from constraints to a steam source

**Goal:** decide without free fitting whether a local covariant early-steam
source function exists and, if it does, whether constraints determine it
uniquely or leave a bounded family.  
**Starting point:** the effective FLRW class is not excluded; a fundamental M0
clock and reservoir are not currently defined.  
**Out of scope:** does not alter A1/K4 or invent new microphysics.

## Decision tree

```text
existing variables and ledgers
        |
        v
P1: closed inventory of sources/states
        |-- no local state + reservoir --> A4 fundamentally BLOCKED
        v
P2: M0–M2 algebraic operator and null limits
        |-- violates ledger/positivity --> corresponding branch DEAD
        v
P3: M3–M6 timing, thermodynamics, BBN, relic budget
        |-- empty set --> mechanism DEAD
        v
P4: M7–M8 perturbations and stability
        |-- instability/isocurvature --> mechanism DEAD
        v
P5: M9 free-parameter count + preregistered observational test
        |-- free profile remains --> CONDITIONAL FAMILY, not prediction
        `-- no free function remains --> DERIVED PREDICTION
```

## P1 — complete inventory without a new hypothesis

**Question:** which already-defined object can be a local state `chi`, and
which can energetically pay for steam?

| Candidate in present documentation | What must be checked | Known current risk |
|---|---|---|
| fuel `rho_f` and A1 `Gamma rho_f` | whether a derived local threshold/state naturally ends the source | constant late `F->C` alone does not make an early steam pulse; direct `F->R` encounters M-015 |
| scar/domain I | define `n_I,xi`, their evolution, energy, and `T_I^(mu nu)` | Q4/Q8 have no operator or ledger; it must not become a hidden reservoir |
| exit/reheating reservoir | find an already-existing component and its local transfer | Q18/Q23 state the question, not yet the object |

**P1 PASS:** table of every existing candidate with exact sources, units, and
the decision whether it meets the minimal M0 input.  
**P1 STOP:** no existing candidate has local state, energy, and paired ledger
together. The conclusion is “v3.18 does not yet contain a fundamental A4
function,” not “early steam is physically impossible.”

## P2 — operator closure and two null limits

For each P1 candidate that passes, write without a numerical fit

```text
S_s^mu(Y),  S_e^mu(Y),  sum_A Q_A^mu=0,
rho_A>=0.
```

Verify the switched-off-mechanism limit and the post-event `rho_s -> a^-4`
limit. P2 passes only for a local, dimensionally correct, balanced operator
with no new fitted time or branching ratio.

## P3–P5

P3 turns M2–M6 into energy, timing, entropy, and relic boundary conditions
and reports whether `F_allowed` is empty, unique, or a family. P4 derives
`delta S_s^mu`, frame, noise, and isocurvature from that same operator before
testing stability. P5 freezes the surviving family and data: BBN, CMB, and
lensing may reject or narrow it, but may not supply the missing formula.

## Immediate executable step

**P1.1 — source map of existing variables.** A read-only audit of Q4, Q8,
Q18/Q23, and the A2 ledger. It creates no script and no new physical track.
It returns a table: “variable → local state? → energy? → evolution? → paired
ledger? → verdict.” It either opens the one authorised P2 track or confirms
P1 STOP, ending function-guessing in both cases.

## Links

- `Q22A_EARLY_STEAM_FUNCTION_CONSTRAINT_LEDGER_SK.md`
- `Q22A_CONSTRAINT_TO_FUNCTION_DERIVATION_PROTOCOL_EN.md`
- `Audit/Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md`
- `00_GATE_AND_STATION_CONSTRAINT_LEDGER_EN.md`

