# Quantum Cellular Theory of Space: A Testable Cosmological Model of a Dividing Causal Network

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21915608.svg)](https://doi.org/10.5281/zenodo.21915608)

**Also known as:** The Cellular Universe<br>
**Author:** Martin Jámbor<br>
**Slovak name:** Kvantová bunková teória priestoru<br>
**Scientific status:** open research programme with audited partial results;
not experimentally confirmed and not peer-reviewed

Quantum Cellular Theory of Space (`QCTS`) investigates whether observed
spacetime can emerge from a discrete, evolving causal network whose cells
process energy and divide. The programme asks whether one local microscopic
process could connect cosmic expansion and its acceleration, propagating
waves and the invariant limiting speed, the formation of matter-like
products, a nonrelativistic residue (“ash”), a thermal wave relic (“steam”),
persistent network scars, and the arrow of time.

> **Central question:** Can observed physics be the macroscopic trace of
> energy processing, transport, and cell division in an underlying causal
> network—without violating established relativity, conservation laws,
> cosmological observations, or their measured tolerances?

The current homogeneous ledger contains a fuel-to-ash energy transfer. Which
additional channels physically exist, whether they arise in parallel or in a
sequence, and how they share energy and momentum remain open questions. The
main unresolved bridge is therefore a complete local covariant
production-and-transport law, not merely another numerical fit.

The [Zenodo record](https://doi.org/10.5281/zenodo.21915608) is the fixed,
citable snapshot. This repository adds selected reproduction scripts, sealed
external-audit packages, audit responses, and immutable history needed to
check how the current claims were obtained.

## 🚀 Registered predictions

The numerical entries below are registered **survival targets**. Agreement
keeps only the stated formulation alive; it does not confirm the cellular
mechanism or prove QCTS. Exclusion requires the complete model-to-observable
map and the uncertainties, covariance, nuisance parameters, and systematics
specified for that row.

One central mean-field construction starts from the known stereological
ensemble mean degree of ideal three-dimensional Poisson–Delaunay geometry,

```text
<k> = 15.53545746435112,
delta_mean = 1 / (<k> + C).
```

For the investigated capacity identification `C = 28`, this gives

```text
delta_mean = 0.022969782752802058.
```

The arithmetic is reproducible, but the physical identification `C = 28`
remains a hypothesis with acknowledged look-elsewhere exposure. It still
requires a microscopic explanation of the bosonic selection and fermionic
exclusion. If the physical overhead is instead the local average
`<1/(k+C)>`, Jensen's inequality makes it larger for a non-degenerate degree
distribution; that correction cannot be evaluated without the appropriate
degree distribution or controlled moments.

| Observable or property | Current scoped survival target | Essential limitation |
|---|---|---|
| `Delta N_eff`, `N_eff` | `Delta N_eff = 0.0535`, `N_eff ≈ 3.10` | Conditional early-decoupled two-polarization thermal relic; branching, exit, reheating, and survival remain open. |
| scalar tilt `n_s` | `0.9656 ± 0.0016` | Exact `delta/m = 1/2` scalar mechanism; the width is a frozen target, not a derived posterior uncertainty. |
| tensor ratio `r` | sharp target `r < 1e-10`; broader practical exclusion marker `r >= 1e-3` | A tensor operator, normalization, pivot convention, and B-mode likelihood are still required. |
| Hubble constant `H0` | approximately `66.4 ± 0.4 km/s/Mpc` | Frozen-background survival boundary, not a completed posterior or a claimed solution of the Hubble tension. |
| clustering `S8` | approximately `0.86–0.87` | Simplified-growth survival boundary, not a completed Einstein–Boltzmann fit or proof that the tension is solved. |
| effective `w0`, `wa` | `w0 = -0.919`, `wa = -0.612` | Joint accounting-shadow target, not independent Gaussian measurements or a fundamental fuel equation of state. |
| sterile ash | null nongravitational signal | Conditional on a future ash particle model and detector response; there is no numerical detector kill window yet. |
| scalar dispersion | exactly zero odd linear term in the audited trial variable `q` | Proven only for the scalar cosine–Laplacian operator, not for full Lorentz invariance, photons, boosts, or the equivalence principle. |
| thermal steam/wave relic | `T ≈ 0.905 K`, peak `≈ 53 GHz`, jointly with `Delta N_eff = 0.0535` | The same thermal commitment as the first row; identification with gravitons is not derived. |

Two former or provisional quantities are deliberately not active targets:

- the former exact `n_s-w` consistency relation is **withdrawn** and has no
  current evidential or exclusion weight;
- constant `delta = 0.02297` is a calibration benchmark only. No
  `delta(a)` law, measurable drift interval, or drift-based kill window has
  been derived.

The authoritative row-by-row statements, evidence, exclusions, and mandatory
nonclaims are in
[`theory/EN/02_Prediction_Status_Table_EN.csv`](theory/EN/02_Prediction_Status_Table_EN.csv).

## ⚰️ Kill conditions (falsifiability)

QCTS uses scope-aware falsification. A failed necessary condition kills the
exact operator, mechanism, or formulation that requires it. It kills the
whole theory only if the contradiction reaches a shared fundamental
principle, or if the declared top-level alternatives are proven exhaustive
and every admissible set is empty.

The current registered exclusion tests include:

1. robust exclusion of `Delta N_eff = 0.0535` after a complete BBN/CMB map
   excludes the exact two-polarization early-thermal steam formulation;
2. robust exclusion of `n_s = 0.9656 ± 0.0016` after a complete primordial
   source map excludes the exact `delta/m = 1/2` scalar mechanism;
3. after a complete tensor-to-B-mode map, `r >= 1e-10` excludes the sharp
   tensor estimate, while a robust `r >= 1e-3` detection excludes the broader
   registered thermal tensor realization;
4. robust incompatibility with `H0 ≈ 66.4 ± 0.4 km/s/Mpc` under one joint
   likelihood excludes the frozen background formulation;
5. robust incompatibility with `S8 ≈ 0.86–0.87` after a full
   Einstein–Boltzmann and lensing/growth analysis excludes the corresponding
   simplified-growth formulation;
6. joint exclusion of `(w0, wa) = (-0.919, -0.612)` under the same CPL
   projection excludes the exact effective-accounting formulation;
7. a reproducible nongravitational signal attributable to the same derived
   ash species would exclude the sterile-ash formulation;
8. a nonzero odd linear term in the exact audited scalar operator would
   exclude that operator;
9. failure to derive `C = 28` excludes the exact capacity identification and
   results that necessarily depend on it, not automatically every cellular
   model;
10. a proof that no admissible common local production-and-transport law
    exists within `A2-K4` would end that track. The track is currently
    waiting for such a law or an existence witness; absence of a found
    witness is not itself a no-go theorem.

Calibration data cannot be reused as independent confirmation. Dead tracks,
failed scripts, inputs, and reasons are preserved so the same failed route is
not silently retried. The exact decision reach of every condition is recorded
in
[`theory/EN/04_Theory_Existence_Conditions_Register_EN.csv`](theory/EN/04_Theory_Existence_Conditions_Register_EN.csv).

## 📂 Repository structure

```text
cellular-universe/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── MANIFEST.sha256
├── RELEASE_STAGING_MANIFEST.tsv
├── theory/
│   ├── SK/                         # Slovak semantic authority
│   │   ├── 00_README_SK.md
│   │   ├── 01_Bunkovy_Vesmir_SK.md
│   │   ├── 02_Prediction_Status_Table_SK.csv
│   │   ├── 03_Methodology_and_Question_Register_SK.md
│   │   └── 04_Theory_Existence_Conditions_Register_SK.csv
│   └── EN/                         # Audited English translations
│       ├── 00_README_EN.md
│       ├── 01_The_Cellular_Universe_EN.md
│       ├── 02_Prediction_Status_Table_EN.csv
│       ├── 03_Methodology_and_Question_Register_EN.md
│       └── 04_Theory_Existence_Conditions_Register_EN.csv
├── External_Audits/               # Selected sealed packages and responses
└── HISTORY/v3.17/                 # Immutable earlier public snapshot
```

Recommended reading order:

1. [`theory/EN/00_README_EN.md`](theory/EN/00_README_EN.md) — document map;
2. [`theory/EN/01_The_Cellular_Universe_EN.md`](theory/EN/01_The_Cellular_Universe_EN.md)
   — physical account, equations, milestones, limits, and open questions;
3. [`theory/EN/02_Prediction_Status_Table_EN.csv`](theory/EN/02_Prediction_Status_Table_EN.csv)
   — exact survival targets and exclusion reach;
4. [`theory/EN/03_Methodology_and_Question_Register_EN.md`](theory/EN/03_Methodology_and_Question_Register_EN.md)
   — verification rules, track logic, and Q1–Q34;
5. [`theory/EN/04_Theory_Existence_Conditions_Register_EN.csv`](theory/EN/04_Theory_Existence_Conditions_Register_EN.csv)
   — EC01–EC43 existence conditions.

If an English translation and the Slovak original differ in meaning, the
Slovak document controls. Executable code is MIT-licensed; theory and
documentation are CC BY 4.0. See [`LICENSE`](LICENSE).

## 🛠️ Verification & run guide

Verify the hierarchical Git snapshot from the repository root:

```bash
sha256sum -c MANIFEST.sha256
```

Zenodo stores 13 attachments in one flat directory. The GitHub-root
`README.md` and the HTML used for the Zenodo Description field are not file
attachments. In a flat download, map each release path to its uploaded name
and verify the 11 non-control attachments plus the staging manifest:

```bash
awk -F '\t' 'NR>1 && $8=="yes" && $6!="SELF_EXCLUDED" {print $6 "  " $2}' RELEASE_STAGING_MANIFEST.tsv | sha256sum -c -
grep 'RELEASE_STAGING_MANIFEST.tsv$' MANIFEST.sha256 | sha256sum -c -
```

The manifest cannot hash itself; its checksum is bound by the repository
commit and Zenodo record.

The active verification route is

```text
A1-K1  ->  A2-K4  ->  A3
```

`A2-K4` is the most advanced live linear-perturbation track. Its regular
superhorizon basis passed the registered `G5` gate. In the frozen
nine-variable perfect-radiation effective-fluid scope, all three regular
modes also passed the scoped `G6` kinetic-sign, gradient,
characteristic-causality, null-limit, constraint, high-`q`, and numerical
convergence checks. This gives a registered depth of `60/100`—a cumulative
gate weight, not a probability, posterior, or percentage of all work
completed. It is not a microscopic UV no-ghost theorem or a proof of global
stability.

Before `A3`, the programme still needs a common local
production-and-transport law, full covariant perturbations with dynamic
Bianchi/constraint preservation, separate photon and neutrino Boltzmann
hierarchies, CMB-normalised spectra and growth, and joint likelihoods.

Selected reproducible milestones are sealed under
[`External_Audits/PACKAGES`](External_Audits/PACKAGES). Start each package
with its `00_SCOPE_AND_READ_ORDER.md`, verify its manifest, and use only the
commands and expected outputs declared there. Auditor responses are kept
separately under [`External_Audits/RESPONSES`](External_Audits/RESPONSES).
Useful entry points include:

- [`EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO`](External_Audits/PACKAGES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/00_SCOPE_AND_READ_ORDER.md);
- [`EA-20260719-029-KMPC127-C2-AUTHORITATIVE-AGGREGATE`](External_Audits/PACKAGES/EA-20260719-029-KMPC127-C2-AUTHORITATIVE-AGGREGATE/00_SCOPE_AND_READ_ORDER.md);
- [`EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE`](External_Audits/PACKAGES/EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE/00_SCOPE_AND_READ_ORDER.md);
- [`EA-20260801-047-V318-PT1-H0-S8-C2C3-THREE-POINT-LEGACY-SENSITIVITY`](External_Audits/PACKAGES/EA-20260801-047-V318-PT1-H0-S8-C2C3-THREE-POINT-LEGACY-SENSITIVITY/00_SCOPE_AND_READ_ORDER.md).

A successful script run is not automatically scientific evidence. Use only
the result, scope, and verdict bound by the corresponding sealed package or
accepted checkpoint.

## 🧭 Methods note

The project separates mathematical identities, direct measurements,
reference-model comparisons, and provisional guidance. It also separates
technical failures from physical exclusions: a syntax error, timeout, solver
failure, or unavailable runtime never becomes a physical STOP.

Unknown functions are first constrained by domains, units, symmetries,
limits, conservation, causality, stability, and observables. A track remains
alive while its complete admissible set has not been shown empty. Alternative
tracks are not positive evidence, but they prevent an unjustified
theory-level death verdict until their taxonomy is frozen and exhaustive.

The work was developed by Martin Jámbor with extensive AI-assisted
calculation, adversarial checking, documentation, and independent-agent
audits. AI agreement is not peer review. The repository preserves equations,
scripts, raw outputs, hashes, scoped verdicts, dead ends, and external-audit
responses so human and machine auditors can reproduce or challenge each
result directly.

Independent calculations, issues, and carefully scoped pull requests are
welcome.

## 📄 Citation

```bibtex
@misc{jambor2026quantumcellular,
  author    = {Jámbor, Martin},
  title     = {Quantum Cellular Theory of Space: A Testable Cosmological Model
               of a Dividing Causal Network},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.21915608},
  url       = {https://doi.org/10.5281/zenodo.21915608}
}
```

The citation reproduces the exact title of the deposited Zenodo work. The
informal alias **The Cellular Universe** refers to the same theory and is not
a separate framework. When citing a numerical target, also cite its
row-specific scope and mandatory nonclaim from the prediction register.
