The Cellular Universe (v3.17)
An emergent, non-equilibrium causal network model of spacetime. This repository hosts the complete theoretical derivation, ontological rules, and numerical validation pipelines for the Cellular Universe theory (v3.17).
Central Hypothesis: Is observed physics the surface trace of the energy dissipation and cell-division dynamics of a discrete Planckian space network?
🚀 Key Predictions & Cosmological Bounds
Without adding unconstrained free parameters, the model derives cosmological parameters from the topology of a random 3D Poisson-Voronoi Delaunay network () and the Standard Model gauge boson degrees of freedom ():
Scalar Spectral Index:  (Derived analytically via ).
Dark Energy Dynamics: Predicts a distinct evolutionary track for dark energy (, ), serving as an accounting shadow of localized matter nucleations.
Matter Clustering:  (Our tension compared to the final KiDS-Legacy 2025 measurement of  stands at a manageable , a significant softening from the earlier KiDS-1000 mismatch).
Early Universe Relic: Predicts a hot "steam" graviton background contributing  ().
Tensor-to-Scalar Ratio:  (primordial B-modes are strongly suppressed).
📂 Repository Structure
cellular-universe/
│
├── LICENSE.md               <-- Combined license file (MIT for scripts, CC-BY-4.0 for text)
├── README.md                <-- This file
│
├── theory/                  <-- Core theoretical frameworks and registers
│   ├── SK/                  <-- Slovak Original Records (Authoritative)
│   │   ├── 00_uvod_a_filozofia.md
│   │   └── bunkovy_vesmir_v3_17_REGISTRACIA.md
│   └── EN/                  <-- English Translations for Peer-Review
│       ├── 01b_Introduction_and_Philosophy_EN.md
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
Validates the convergence of network capacity to the  attractor and measures the area law exponent ():
python scripts/10_script_Q10_Vlinks_dowry_rule.py


⚰️ Kill Conditions (Falsifiability)
In accordance with strict Popperian methodology, the model is designed to be fully falsifiable. Any of the following measurements will immediately falsify the current formulation:
LiteBIRD/CMB-S4 detection of primordial B-modes ().
Confirmed non-gravitational dark matter interaction (e.g., direct detection of WIMPs by LZ or XENONnT).
Local Hubble parameter confirmed at  km/s/Mpc without any remaining cosmic distance ladder systematics.
CMB-S4 scalar spectral index verified outside the  margin.
📄 Citation & Open Access
If you analyze, test, or build upon this model, please cite the registered Zenodo record:
@misc{jambor2026cellular,
  author       = {Jambor, Martin},
  title        = {The Cellular Universe: Theory and Numerical Verification Pipelines (v3.17)},
  month        = jul,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://doi.org/10.5281/zenodo.XXXXXXX}
}

