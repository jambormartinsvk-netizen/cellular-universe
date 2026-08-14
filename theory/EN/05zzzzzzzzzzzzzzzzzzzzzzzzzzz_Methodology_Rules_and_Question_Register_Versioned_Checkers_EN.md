# Methodology Rules and Question Register — Versioned Checkers and Segmented Evidence (EN)

Date: 2026-07-15  
Scope: additive; earlier rules are unchanged

## AR56 — A corpus checker is an immutable numbered snapshot

The expected file count and quarantine dictionary belong to a specific checker hash revision. After scripts are deliberately added, the old checker is not silently rewritten: it is marked `SUPERSEDED`, its reason and hash are retained, and a new numbered successor is created. `NOT_IN_QUARANTINE` is neither a technical nor a physical PASS.

## AR57 — Independent cases are checkpointed before the next case

When a monolithic aggregate contains multiple independent scientific or negative-control cases and a timeout could discard completed evidence, every case is run with its own internal and external limit and its immutable output, process exit, and hash are stored before the next case. Final combination is performed by an offline aggregate with no child processes. A timeout places only that case in REVIEW and does not erase completed results from other cases.

## Q81 — Which corpus checker is current after K7b P0?

**Answer:** script 196. It audited 200 other Python files, records 68 quarantined entries, found syntax failures only in 118/119, found only 186 incomplete, and executed no target script. Older 188, 191, and 194 remain reproducible `SUPERSEDED` snapshots.

## AR58 — A relevant error-ledger preflight is mandatory before every command

Before composing or launching a Python or shell command, the rows relevant to its syntax and purpose must be actively identified in `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md`, and their prevention must be implemented in the command. Updating the ledger only after an error is not sufficient. Repeating a known error receives a new row linked to the original error and no physical verdict. PowerShell `foreach` output is first stored in a variable and only then piped; exact numbered-script paths are obtained from a filtered `.py` inventory excluding `__pycache__`.

## Q82 — What exactly did K7c P1 prove, and what remains open?

**Answer:** clean script 197, with the legacy adaptive block absent, reproduced the 100/200 difference `1.44327268769215e-6`, the 200/400 difference `3.93123964056996e-6`, the ratio `0.367129155088317`, and dominance by `M`. Reproduction is PASS, but physical convergence remains REVIEW because the difference did not fall below `1e-6` and the RK4 ratio is outside `8–32`. K4 remains alive at `66.5/100`; P2 must distinguish summation error in the `M'` terms from algebraic conditioning, stiffness, and working precision. Checker 198 is the current snapshot: 202 other `.py` files and 69 quarantined entries.

## AR59 — Stations, route prefixes, and multi-round audits must not be conflated

A1, A2, A3, ... are shared verification stations. A track is a mechanism choice at a specific station, and a route prefix is the ordered path of track choices already made. A result conditioned on an upstream track belongs to that route prefix and must not be generalized without a new audit to the same-named track on a different background. PASS of one track permits progress to the next station; STOP of one track does not kill the station while another track remains alive. If every track at a station dies, the route prefix terminates with the last reached station stated exactly.

An audit discussion is an immutable multi-round thread. The original audit and response are not overwritten; every further objection, response, evidence package, or reaudit receives a new round number. Conflicting audits remain preserved and are resolved by a separate adjudication thread. The current summary points to the immutable rounds and the latest valid decision.

## Q83 — Which directory model is authoritative for future stations and audits?

**Answer:** the primary tree is the nested route `A1/A1Kx/A2/A2Ky/A3/...`; internal subtracks remain under `SUBTRACKS` at the station where they are tested. Every station, track, and subtrack has `PASS`, `REVIEW`, `STOP`, `HISTORY`, `AUDIT_THREADS`, and `ARTIFACTS`. Every audit thread preserves the sequence `audit → response → evidence → open points → reaudit`. The detailed design is `Questions/DIRECTORY_STRUCTURE_AND_MIGRATION_PROPOSAL_V2_STATIONS_ROUTES_AND_AUDIT_THREADS_2026-07-15.md`; physical migration starts only after a path/SHA manifest and Git baseline exist.

## AR60 — Result weight is frozen before execution and correlated checks are not double-counted

Every scientific result is assigned before execution to one versioned gate
with a physical weight. Weights within one scorecard sum to 100. After a
result they may not change without a new version, a reason, and recalculation
of every sibling. Multiple rows, monitors, or reproduction checks of the same
claim cannot receive duplicate weight. The scorecard separately reports
validated PASS support, blocking FAIL evidence, open or technical weight, and
audited PASS+FAIL coverage. Failure of a high-weight gate has high decision
value but does not support the theory. A score is not a probability of truth.

## AR61 — HISTORY is a mandatory append-only event ledger

Every station, track, subtrack, audit thread, and shared-core version has
HISTORY/00_EVENT_LEDGER.md. A change of state, score, scope, path, name,
limitation, or supersession receives a new immutable event containing the old
and new values, reason, triggering audit, affected claims, and evidence
hashes. An older event is not edited; a correction uses a CORRECTS link. A
navigational current summary may display the latest state but does not
replace historical evidence.

## AR62 — The shared Python core is versioned and every result pins its exact version

Shared physics, numerics, and audit gates may be extracted into
scripts/baseScripts/vNNN, but an authoritative version is immutable after
use. Every run manifest records the version and SHA-256 of imported modules.
A correction creates a new version, changelog, new result, and differential
audit; the old result is marked LIMITED or SUPERSEDED, never silently
overwritten. A shared core must not transfer PASS across different
backgrounds without a separate route-conditioned audit.

## Q84 — Why are we at K7c, and why is there no K1c?

**Answer:** K1 through K6 were alternative numerical formulations of the
same C7.7c gate, not uniform a/b/c stages. Only the seventh formulation was
split into K7a (projected algebra/Jacobian), K7b (initial coefficients and
constraints without an ODE), K7c (evolution and convergence), and planned
K7d (complete activity/constraints). K1 stopped at 28 unresolved activity
checks before this subdivision existed. Uniform gate IDs C7-G0 through G9
will now show tests that were not reached; historical names remain unchanged.

## Q85 — What weight does the current K7c P1 result carry?

**Answer:** under scorecard C7-W1, K7 conservatively has 40/100 validated
support (G0 through G3), 20/100 blocking evidence (G5 convergence), 40/100
open weight, and 60/100 audited coverage. The human count “8 of 10 PASS” is
not 80%, because several rows reproduced the same claim or were monitors
only. The C7 scorecard is not added to the historical whole-track depth of
A2-K4 66.5/100.

## Q86 — How will the failed RK4 ratio be externally audited?

**Answer:** a route-conditioned package freezes script 197, the 100/200/400
checkpoints, equations and conventions, norm, pre-run expectations, raw
output, dependency and SHA manifest, known limitations, and open questions.
The audit must examine ratio orientation, asymptotic regime, norm suitability,
grid closure, M dominance, non-tautological constraints, and an independent
implementation. Discussion proceeds in immutable rounds audit → response →
evidence → reaudit.
## AR63 — Local P0/P1/P2 labels require a namespaced ID in central registers

A short P0, P1, or P2 label is allowed only in a document whose header
uniquely identifies the route and node. Central plans, route registers,
external audits, and HISTORY use purpose prefixes: SCI for scientific
execution, ORG for organization, BASE for the shared core, AUD for an audit,
and ZEN for publication. The legacy scientific K7c P2 has stable ID
SCI-A2K4-C7G5-K7C-P2-MLEDGER; ORG-V2-P2 must neither replace nor alter it.

## Q87 — Where is the authoritative abbreviation and identifier register?

**Answer:** the Slovak register is
Questions/00_ABBREVIATION_AND_IDENTIFIER_REGISTER_SK.md and its English
mirror is Questions/00_ABBREVIATION_AND_IDENTIFIER_REGISTER_EN.md. They
define stations, route prefixes, K1–K7/K7a–d, C7-G0 through G9, namespaced
P0/P1/P2, physics and numerical abbreviations, and status codes. A precise
physics derivation takes precedence if it conflicts with the navigation
glossary.

## Q88 — Did the reorganization change the legacy scientific P2?

**Answer:** no. SCI-A2K4-C7G5-K7C-P2-MLEDGER remains a new numbered,
diagnostic-only decomposition of the nine M-prime terms on identical stored
checkpoints, comparing the original float64 sum, math.fsum, and an 80-dps
reference, with no RHS change and no score. Script 186 remains
DO_NOT_RUN_TECHNICAL. The scope and source hashes are frozen in
Questions/A2_K4_K7C_P2_SCOPE_FREEZE_AND_ORG_NAMESPACE_2026-07-15.md.
## AR64 — An exact algebraic identity takes precedence over a numerical residual

Before a small or growing numerical residual is interpreted physically, the
corresponding coefficient must be checked for an algebraic identity implied
by the registered definitions. A float64 remainder produced by subtracting
terms that must cancel exactly is not a new physical effect. An expression
may be replaced by exact zero only after a separate symbolic, provenance,
and high-precision audit; the subsequent evolution remains a separate gate
with every original threshold unchanged. This does not revive the dead
summation-only track.

## Q89 — What did K7c P2 close?

**Answer:** script 199 preserved bitwise parity with P1 states and RHS and
found only `1×` improvement from `math.fsum` at all three checkpoints.
Therefore `K7c.3e fsum-only` is dead. P2 also localized the discrepancy to
two coefficients that should be exactly zero under the registered
background definitions. K4 remains REVIEW at `66.5/100`; P2 carries no
score.

## Q90 — What step is permitted after P2?

**Answer:** only P3a-A without an ODE: exact algebraic proof, an 80-dps
numerical check, and a provenance audit of both coefficients. Only a PASS
permits P3a-B, which sets only these two identities to zero and repeats RK4
100/200/400 with the unchanged gates `8–32` and `diff200/400 < 1e-6`.

## Q91 — What are the results of P3a-A and P3b?

**Answer:** P3a-A proved both coefficient identities exactly over the
rationals and at 80 dps with a maximum normalized residual of `2.5069e-81`.
After a source-delta proof of the sole permitted change, P3b obtained
`diff200/400 = 3.0308221211e-14` and a classical RK4 ratio of `16.004121`.
Both preregistered step gates passed. Depth remains `66.5/100`, and the full
C7-G5 remains PARTIAL PASS/REVIEW because method and tolerance convergence
have not yet been tested.

## Q92 — Which older claim did P3b limit, and what step is permitted next?

**Answer:** P1 remains a valid reproduction of the legacy float64
representation, but it is no longer evidence of physical non-convergence of
the canonical equations. The fsum-only branch remains dead. A new
preregistration may next complete the method and tolerance parts of G5,
followed by non-tautological G4 and finally NID/NIV × deep/shallow G6. P3b
alone permits neither CMB/S8 work nor award of the full G5 weight.

## Q93 — What is P4a, and what is its current state?

**Answer:** P4a is the preregistered but not yet executed method and
tolerance part of C7-G5. It separately compares DOP853 at two tolerances and
Radau against the P3b RK4-grid400 endpoint; four differences must be
`<=1e-8`. Each case has its own limit and JSON, and aggregation is offline.
Source-delta 210, formal preflight, and versioned corpus checker 211 must pass first.

## AR65 — An active route must have a finite finish line and iteration budget

Every active track must state its finite list of remaining gates, a work
progress measure separate from scientific score, and the maximum number of
technical corrections per gate. A technical error creates neither a new
central Q nor a new physical subtrack. After the initial implementation and
at most two technical corrections, the outcome must be PASS, physical STOP,
or REVIEW_BLOCKED with an architectural decision. Changing the finish line,
script/Q cap, or budget requires a new addendum and HISTORY event; it may not
happen by silently adding suffixes.

## Q94 — How far is A2-K4 from completion?

**Answer:** fine depth is `66.5/100`, strict C7-W1 support is `40/100`, and
WBS-1 work progress is `48/100`. Six packages remain: completion of G5,
then G4, G6, G7, G8, and G9. The realistic estimate is 25–40 working days,
the optimistic estimate is 15–20, and the risk case is 2–3 months. Script
208 is currently the highest existing ID; 209–212 are only planned. Q99 and
flat script 240 cap the current A2-K4 unless a separate review or new
physical branch authorizes a change.
