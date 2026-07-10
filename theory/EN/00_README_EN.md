The Cellular Universe (v3.17)

An emergent, non-equilibrium causal network model of spacetime. This repository hosts the complete theoretical derivation, ontological rules, and numerical validation pipelines for the Cellular Universe theory (v3.17).

🌌 Central Hypothesis: Is observed physics the surface trace of the energy dissipation and cell-division dynamics of a discrete Planckian space network?

🚀 Key Predictions & Cosmological Bounds

Without adding unconstrained free parameters, the model derives cosmological parameters from the topology of a random 3D Poisson-Voronoi Delaunay network ($\langle k \rangle = 15.54$) and the Standard Model gauge boson degrees of freedom ($C = g_B = 28$):

Scalar Spectral Index:

$n_s = 0.9656 \pm 0.0016$ (Derived analytically via $n_s - 1 = -1.5\delta$).

Dark Energy Dynamics:

Predicts a distinct evolutionary track for dark energy ($w_0 \approx -0.92$, $w_a \approx -0.61$), serving as an accounting shadow of localized matter nucleations.

Matter Clustering:

$S_8 \approx 0.859 - 0.874$ (Our tension compared to the final KiDS-Legacy 2025 measurement of $S_8 = 0.815$ stands at a manageable $2.4\sigma - 3.3\sigma$, a significant softening from the earlier KiDS-1000 mismatch).

Early Universe Relic:

Predicts a hot "steam" graviton background contributing $\Delta N_{\text{eff}} = 0.0535$ ($N_{\text{eff}} = 3.10$).

Tensor-to-Scalar Ratio:

$r < 10^{-10}$ (primordial B-modes are strongly suppressed).

📂 Repository Structure

cellular-universe/
│
├── LICENSE.md               <-- Combined license file (MIT for scripts, CC-BY-4.0 for text)
├── README.md                <-- This file
│
├── theory/                  <-- Core theoretical frameworks, tables, and registers
│   ├── SK/                  <-- Slovak Original Records (Authoritative)
│   │   ├── 00_uvod_a_filozofia.md
│   │   ├── bunkovy_vesmir_v3_17_REGISTRACIA.md
│   │   └── 03_Predictions_Table_v3.17_SK.csv               <-- NEW: Translated Slovak predictions
│   └── EN/                  <-- English Translations for Peer-Review
│       ├── 01b_Introduction_and_Philosophy_EN.md
│       ├── 03_Predictions_Table_v3.17_EN.csv               <-- Original English predictions
│       ├── 04b_Main_Document_Theory_Equations_Values_v3.17_EN.md
│       └── 05b_Methodology_Rules_and_Question_Register_EN.md
│
└── scripts/                 <-- Executable verification Python pipelines
    ├── 06_script_Q14_light_cone_front_sharpening.py
    ├── 07_script_Q12_dispersion_Lorentz_test.py
    ├── 08_script_Q7_sound_horizon_H0.py
    ├── 09_script_K3_cosmology_pipeline.py
    └── 10_script_Q10_Vlinks_dowry_rule.py


🛠️ Verification & Run Guide

To run the cosmological and network simulations, ensure you have numpy, scipy, and matplotlib installed.

1. Execute the Cosmology & Growth Pipeline

Reproduces the back-integration of background equations, CPL parameters, and growth equations:

python scripts/09_script_K3_cosmology_pipeline.py


2. Verify Spacetime Dispersion Relations and Lorentz Test

Fits the discrete graph Laplacian dispersion and checks for Lorentz invariance suppression:

python scripts/07_script_Q12_dispersion_Lorentz_test.py


3. Run the Spatial Connection (Dowry Rule) Simulation

Validates the convergence of network capacity to the $n_V = C$ attractor and measures the area law exponent ($p \approx 1.97$):

python scripts/10_script_Q10_Vlinks_dowry_rule.py


⚰️ Kill Conditions (Falsifiability)

In accordance with strict Popperian methodology, the model is designed to be fully falsifiable. Any of the following measurements will immediately falsify the current formulation:

LiteBIRD/CMB-S4 detection of primordial B-modes ($r \ge 10^{-3}$).

Confirmed non-gravitational dark matter interaction (e.g., direct detection of WIMPs by LZ or XENONnT).

Local Hubble parameter confirmed at $H_0 \ge 72$ km/s/Mpc without any remaining cosmic distance ladder systematics.

CMB-S4 scalar spectral index verified outside the $0.9656 \pm 0.004$ margin.

📄 Citation & Open Access

If you analyze, test, or build upon this model, please cite the registered Zenodo record:

@misc{jambor2026cellular,
  author       = {Jambor, Martin},
  title        = {The Cellular Universe: Theory and Numerical Verification Pipelines (v3.17)},
  month        = jul,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21286129},
  url          = {https://doi.org/10.5281/zenodo.21286129}
}
