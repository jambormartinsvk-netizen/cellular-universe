# README — The Cellular Universe (Cellular Space Theory), record v2

**Author:** Martin Jambor (Independent Researcher) | ORCID on record
**Adversarial review & computations:** Claude (Anthropic AI), under the author's direction; consistency cross-check by a second AI system (Gemini). This constitutes consistency checking, **not peer review**. Independent human replication is explicitly invited.
**Language note:** the record is fully bilingual. Files tagged `_SK` are the authoritative Slovak originals; files tagged `_EN` (01b, 04b, 05b and the predictions tables) are faithful English translations, verifiable against the originals.
**Living mirror:** https://github.com/jambormartinsvk-netizen/cellular-universe (issues and replication PRs welcome; this Zenodo record is the citable timestamp).

## What this record is
A pre-registration of exact, falsifiable cosmological predictions of a model in which space is a random causal network of Planck-scale cells whose "metabolism" (digestion of vacuum fuel + cell division) generates expansion, matter and dark-sector phenomenology. **One fitted parameter** (lambda = 0.10–0.15); delta = 1/(<k> + g_B) = 0.02297, DeltaN_eff = 0.0535 and n_s = 0.9656 are derived, not fitted.

## File guide (read in this order)
| # | file | content |
|---|------|---------|
| 01 / 01b | Introduction_and_Philosophy (SK / EN) | the story, core metaphors introduced step by step, philosophical principles F1–F5, why to trust the method |
| 02 / 02b | Predictions_Table_v3.17 (EN / SK pdf) | one page: every prediction vs. standard value, deciding experiment, kill condition |
| 03 / 03b | Predictions_Table_v3.17 (EN / SK csv) | machine-readable versions (compare to future data by script) |
| 04 / 04b | Main_Document_Theory_Equations_Values_v3.17 (SK / EN) | all equations with their logic, computation of every value, terminology mapping, field-theoretic framework note, phenomenon-by-phenomenon comparison, data state at registration |
| 05 / 05b | Methodology_Rules_and_Question_Register (SK / EN) | anchor, falsification protocol, verification rules P1–P5, 9 methodological pitfalls (M1–M9), 20 dead branches with reasons, 16 resolved questions with verdicts |
| 06–10 | script_*.py | reproducible pipelines (see below) |

## Headline predictions (details in 02/03)
N_eff = 3.09–3.10 | n_s = 0.9656 ± 0.0016 (derived) | primordial r < 1e-10 (any detection r >= 1e-3 falsifies the model) | H_0 = 66.4 km/s/Mpc | S_8 = 0.86–0.87 | w_0 ≈ −0.92, w_a ≈ −0.4…−0.6 | permanently null direct dark-matter detection | consistency relation: the same delta sets n_s − 1 = −(3/2)delta and the shape of w(z).

## Scripts: requirements & validation
**Requirements:** Python 3.10+, numpy, scipy. No network access needed. Each run should take seconds–minutes on a laptop (largest: 300k-node Delaunay).

**Before trusting any output, check the validation values:**
- `06_..Q14..` (front sharpening): Poisson network must give mean degree **<k> ≈ 15.54–15.58**; verdict output chi ≈ 0.26–0.32.
- `07_..Q12..` (dispersion): periodic stitching must validate **<k> = 15.535** (if you get ~16.1, ghost-edge filtering failed — pitfall M7); linear dispersion term must vanish; isotropy of c at the 0.1 % level; cubic-lattice contrast ~21x worse.
- `08_..Q7..` (sound horizon): LCDM validation must return **r_s = 144.32 Mpc, h = 0.6730**; late matter creation must LOWER H_0 (−1.5 to −4.5) — that sign is the point.
- `09_..K3..` (full cosmology): LCDM validation **h = 0.673, Omega_m = 0.316**; the no-steam model point must reproduce **H_0 = 65.6, Omega_m = 0.359, w_0 = −0.91, w_a = −0.60, S_8 = 0.888** before you trust the steam runs.
- `10_..Q10..` (V-links): dowry rule must converge to saturation (std/mean ≈ 0.13) and cross-boundary weight exponent **p ≈ 1.97** (area law).

If a validation value fails on your machine, do not use the run — consult pitfalls M1–M9 in file 05.

## Kill conditions (any single one falsifies the model)
1. Detection of primordial B-modes, r >= 1e-3 (LiteBIRD / CMB-S4)
2. Confirmed non-gravitational dark-matter interaction (LZ / XENONnT / DARWIN)
3. S_8 <= 0.78 AND w_a <= −0.6 confirmed simultaneously (Euclid/LSST + DESI)
4. Local H_0 >= 72 km/s/Mpc confirmed with systematics fully accounted for
5. Discovery of a new fundamental carrier boson (changes g_B = 28, hence n_s)
6. CMB-S4: n_s outside 0.9656 ± 0.004

## Data state at registration (7 July 2026)
DESI DR2: w_0 = −0.75 ± 0.06, w_a = −0.86 ± 0.25 (survey mapping completed April 2026; final analysis pending). KiDS-Legacy (DR5, 2025): S_8 = 0.815 (+0.016/−0.021). Planck 2018: n_s = 0.9649 ± 0.0042, N_eff = 2.99 ± 0.17.

## License
Text and documents: CC-BY 4.0. Scripts: MIT.
