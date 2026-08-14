# Abbreviation and Identifier Register — EN

Date: 2026-07-15  
Status: authoritative navigation register; physical definitions remain in their derivations

## Path and branch identifiers

| Token | Meaning |
|---|---|
| `A1`, `A2`, `A3` | verification stations, not tracks |
| `K1`, `K2`, ... | track or local subtrack; its full path determines meaning |
| `A2-K4` | fourth track tested at station A2 |
| `A1K1 → A2K4` | route prefix through the stations |
| `C7.7c` | legacy ID of the evolution species/mode activity-completeness gate in A2-K4; not a station |
| `C7.7c-K1...K7` | alternative numerical formulations of the same C7.7c gate |
| `K7a/K7b/K7c/K7d` | projected algebra/Jacobian; initial constraints without ODE; evolution/convergence; planned full activity gate |
| `J...`, `BR...`, `RG...` | local diagnostic/reformulation branches defined by the node's `00_CURRENT_STATE.md` |

Bare `K4` is forbidden in a decision document because it can mean A2-K4 or
C7.7c-K4. Use the full path.

### Stable station and track identifiers

In reader-facing prose, `A1/A2/A3` mean **verification stations** and `K`
means a **track**. The identifiers themselves are not renamed:

- `S1` is already the finding class `S1_LOCAL_CORRECTABLE_SAME_TRACK`;
- `T1` is already `T1_TECHNICAL_NO_CLAIM_REACH`, while `T` is also used for
  tensor/time objects;
- renaming A/K would break historical hashes, route paths, and audit
  packages without adding scientific information.

## Namespaced phases

| Stable ID | Legacy alias | Meaning |
|---|---|---|
| `SCI-A2K4-C7G5-K7C-P0` | P0 | fail-closed K7b provenance/regression gate |
| `SCI-A2K4-C7G5-K7C-P1-RK4` | P1 | clean fixed RK4 reproduction at 100/200/400 steps |
| `SCI-A2K4-C7G5-K7C-P2-MLEDGER` | P2, K7c.3d | diagnostic ledger of nine `M'` terms; next scientific step |
| `ORG-V2-P1/ORG-V2-P2` | organization phases | non-invasive indexing / later physical migration |
| `BASE-V001-PARITY-197` | base pilot | candidate shared-core extraction and parity audit of script 197 |
| `AUD-C7G5-K7C-P1-RK4` | external RK4 audit | independent review of the non-RK4 ratio and norm |
| `ZEN-v3.18` | Zenodo v3.18 | publication package, not scientific P2 |

Short P0/P1/P2 is allowed only when the document header contains the full
route. Central plans, route registers, and external audits use stable IDs.

## C7-W1 gates

`C7-G0...G9` denote respectively provenance (5), state/initial data (10),
algebra/signs/null limits/initial constraints (15), bounded evolution (10),
trajectory activity and non-tautological constraints (15), numerical
convergence (20), mode/surface coverage (10), full interval/endpoints (5),
full photon/neutrino hierarchy (5), and downstream CMB/S8 likelihood (5).

## Physics and numerics

| Token | Meaning |
|---|---|
| `D`, `M` | projected compensated density and momentum sources used by K7 |
| `M'` | derivative of `M`; target of scientific P2 |
| `δ_A`, `U_A`, `Ω_A` | density perturbation, dimensionless velocity/momentum, and background fraction of species A |
| `c`, `f`, `b`, `γ`, `fs` | ash/CDM, fuel, baryons, photons, and free-streaming radiation |
| `NID/NIV` | neutrino isocurvature density/velocity modes |
| `deep/shallow` | deep/shallow superhorizon initial surfaces of a specified audit |
| `RHS`, `ODE` | right-hand side; ordinary differential equation/system |
| `RK4`, `DOP853`, `Radau` | classical fourth-order Runge–Kutta; explicit adaptive high-order solver; implicit solver |
| `FD`, `HP`, `dps` | finite difference; high precision; decimal working digits |
| `rtol/atol`, `nfev` | relative/absolute solver tolerance; RHS evaluation count |
| `CMB`, `S8`, `H0`, `ΛCDM` | microwave background; clustering amplitude; Hubble constant; standard cosmological model |

## Status and evidence codes

`PASS` means the named gate passed only in its stated scope. `REVIEW` is open
or insufficient. `STOP/DEAD` closes a specific track while preserving its
reason and evidence. `NOT_REACHED` was not run due to an earlier blocker.
`INHERITED` earns no score without its own audit. `TIMEOUT_UNCLOSED` is a
technical result, not automatically a physical failure. `DO_NOT_RUN_TECHNICAL`
marks retained but unsafe/incomplete code. `PROVENANCE_FAIL` is a missing or
wrong source/hash/manifest. `LIMITED`, `SUPERSEDED`, and `CORRECTS` preserve
the relationship between old and new evidence.

Physical depth measures whole-track progress through physically accepted
station gates; the current A2-K4 value is `60/100` and is not a probability
of truth. A historical technical depth such as K7 `66.5/100` is a diagnostic
value and does not transfer into the track's physical depth. Gate weight is
preregistered decision importance. Support is passed weight, blocker is
failed weight, open weight is unresolved/unreached weight, and coverage is
PASS+FAIL weight—not a probability. `PRERUN`, checkpoint, manifest, lineage,
audit thread, `HISTORY`, and `baseScripts` respectively mean frozen pre-run
expectations, immutable intermediate evidence, provenance inventory,
artifact ancestry, immutable multi-round audit, append-only event ledger,
and an immutable versioned shared core.


## K7c diagnostic identifiers after P2

| ID | Meaning and status |
|---|---|
| `SCI-A2K4-C7G5-K7C-P2-MLEDGER` | completed nine-term `M'` ledger; simple `math.fsum` explanation STOP |
| `K7c.3e fsum-only` | dead subtrack: more accurate final summation improved 3/3 checkpoints by only `1×` |
| `SCI-A2K4-C7G5-K7C-P3A-ZERO-IDENTITY` | live audit of two algebraically zero coefficients; P3a-A has no ODE, P3a-B only after PASS |
| `P3a-A` | symbolic, 80-dps, and provenance identity audit; no score |
| `P3a-B` | historical preregistration name for the evolution handoff; implemented as route node `P3b`, PASS only for the isolated step gate |
| `SCI-A2K4-C7G5-K7C-P3B-ZERO-IDENTITY-RK4` | authoritative P3b run; `diff200/400=3.0308e-14`, ratio `16.004121`, full G5 still REVIEW |
| `P4a` | preregistered but not yet run node: method and tolerance breadth of C7-G5 before G4/G6 |
| `SCI-A2K4-C7G5-K7C-P4A-METHOD-TOLERANCE` | stable P4a ID; DOP853 medium/tight and Radau tight, offline aggregate |
