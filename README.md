# The Cellular Universe (v3.17)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21286129.svg)](https://doi.org/10.5281/zenodo.21286129)

**An emergent, non-equilibrium causal network model of spacetime.** This repository hosts the complete theoretical derivation, methodology registers, and numerical verification pipelines for the Cellular Universe theory (v3.17).

> **Central hypothesis:** Is observed physics the surface trace of the energy dissipation and cell-division dynamics of a discrete Planckian space network?

**Archival record & timestamp:** all predictions are registered on Zenodo — https://doi.org/10.5281/zenodo.21286129 (v1, 7 July 2026). The Zenodo record is the citable, timestamped version; this repository is its living mirror. *(For version-independent citation, use the "Cite all versions" DOI shown on the Zenodo page.)*

## 🚀 Registered predictions

Derived from the topology of a random 3D Poisson–Voronoi/Delaunay network (⟨k⟩ = 15.54) and the Standard Model boson count (C = g_B = 28), with **one fitted parameter** (λ = 0.10–0.15):

| Observable | This model | Standard / current data | Decided by |
|---|---|---|---|
| **N_eff** | **3.09–3.10** (thermal graviton relic; no inflaton) | 3.045 | CMB-S4 / Simons Obs. |
| **n_s** | **0.9656 ± 0.0016** — derived: n_s − 1 = −(3/2)δ | 0.9649 ± 0.0042 (fitted) | CMB-S4 |
| **Primordial r** | **< 10⁻¹⁰ — no B-modes, ever** | many models hope 10⁻³–10⁻² | LiteBIRD |
| **H₀** | **66.4 km/s/Mpc** | 67.4 (CMB) vs ~73 (local) | ladder systematics; S4 |
| **S₈** | **0.86–0.87** | KiDS-Legacy 2025: 0.815 (+0.016/−0.021) | Euclid / LSST |
| **w₀, wₐ** | **−0.92…−0.94, −0.4…−0.6** (accounting shadow; NEC intact) | −1, 0 | DESI final |
| **DM direct detection** | **permanently null** (gravity-only "ash") | WIMP signals expected | LZ / XENONnT |
| **Consistency relation** | the **same δ** sets the primordial tilt and w(z) | no such link | joint fits |

## ⚰️ Kill conditions (falsifiability)

Any single one of the following immediately falsifies the model:
1. Detection of primordial B-modes, r ≥ 10⁻³ (LiteBIRD / CMB-S4)
2. A confirmed non-gravitational dark-matter interaction (LZ / XENONnT / DARWIN)
3. S₈ ≤ 0.78 **and** wₐ ≤ −0.6 confirmed simultaneously (Euclid/LSST + DESI)
4. Local H₀ ≥ 72 km/s/Mpc with distance-ladder systematics fully accounted for
5. Discovery of a new fundamental carrier boson (changes g_B = 28, hence n_s)
6. CMB-S4: n_s outside 0.9656 ± 0.004

## 📂 Repository structure

```
cellular-universe/
├── LICENSE            (MIT for scripts, CC-BY-4.0 for text)
├── README.md
├── theory/
│   ├── SK/            Slovak originals (AUTHORITATIVE)
│   │   ├── 01_Introduction_and_Philosophy_SK.md
│   │   ├── 02b_Predictions_Table_v3.17_SK.pdf
│   │   ├── 03b_Predictions_Table_v3.17_SK.csv
│   │   ├── 04_Main_Document_Theory_Equations_Values_v3.17_SK.md
│   │   └── 05_Methodology_Rules_and_Question_Register_SK.md
│   └── EN/            Faithful English translations (verifiable against SK)
│       ├── 00_README_EN.md
│       ├── 01b_Introduction_and_Philosophy_EN.md
│       ├── 02_Predictions_Table_v3.17_EN.pdf
│       ├── 03_Predictions_Table_v3.17_EN.csv
│       ├── 04b_Main_Document_Theory_Equations_Values_v3.17_EN.md
│       └── 05b_Methodology_Rules_and_Question_Register_EN.md
└── scripts/
    ├── 06_script_Q14_light_cone_front_sharpening.py
    ├── 07_script_Q12_dispersion_Lorentz_test.py
    ├── 08_script_Q7_sound_horizon_H0.py
    ├── 09_script_K3_cosmology_pipeline.py
    └── 10_script_Q10_Vlinks_dowry_rule.py
```

## 🛠️ Verification & run guide

Requirements: Python 3.10+, `numpy`, `scipy`. No network access needed; minutes on a laptop.

**Before trusting any output, check the validation values** (details in `00_README_EN.md`):
- Q14: Poisson network mean degree **⟨k⟩ ≈ 15.54–15.58**; front exponent χ ≈ 0.26–0.32
- Q12: periodic stitching must give **⟨k⟩ = 15.535** (≈16.1 ⇒ ghost-edge filtering failed, pitfall M7); linear dispersion term must vanish
- Q7: ΛCDM validation **r_s = 144.32 Mpc, h = 0.6730**
- K3: ΛCDM **h = 0.673, Ω_m = 0.316**; the no-steam point must reproduce (65.6, 0.359, −0.91, −0.60, 0.888)
- Q10: saturation attractor (std/mean ≈ 0.13); area-law exponent **p ≈ 1.97**

```bash
python scripts/09_script_K3_cosmology_pipeline.py      # cosmology: H0, w0, wa, S8, chi2
python scripts/07_script_Q12_dispersion_Lorentz_test.py # dispersion & Lorentz suppression
python scripts/10_script_Q10_Vlinks_dowry_rule.py       # dowry rule, saturation, area law
```

## 🧭 Methods note

Calculations and adversarial review were performed in collaboration with an AI system (Claude, Anthropic) under the author's direction, using a pre-registered falsification protocol: **20 dead branches, 9 documented methodological pitfalls, zero reversals** (full registers in `theory/`). The derivations of δ and n_s were additionally cross-checked by a second, independent AI system — a consistency check, *not* peer review. **Independent human replication is explicitly invited**; issues and pull requests are welcome.

## 📄 Citation

```bibtex
@misc{jambor2026cellular,
  author    = {Jambor, Martin},
  title     = {The Cellular Universe: Theory and Numerical Verification Pipelines (v3.17)},
  month     = jul,
  year      = 2026,
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.21297228},
  url       = {https://doi.org/10.5281/zenodo.21297228}
}
```
