# THE CELLULAR UNIVERSE — REGISTRATION EDITION (v3.17)
## All formulas with their logic, computation of the values, and comparison with standard explanations

**Author of the theory:** Martin Jambor | **Adversarial reviewer and controller:** Claude (Anthropic) | **Date:** 7 July 2026
**Intended for prediction registration (Zenodo/OSF) — a timestamp prior to CMB-S4, LiteBIRD, Euclid/LSST and the final DESI release.**
*(Faithful English translation of file 04; the Slovak original is authoritative.)*

## CURRENT DATA STATE (data watch as of 7 July 2026)
- **Lensing:** the final KiDS-Legacy (DR5, 2025): S₈ = 0.815 (+0.016/−0.021), only ~0.7σ from Planck — the lensing side has moved UP (from KiDS-1000's 0.759), toward our stake S1. The score recomputed with this data point: **model χ² ≈ 19.6–19.9 vs ΛCDM ≈ 30.0** (3 fronts: DESI w₀, wₐ + S₈; without RSD and correlations — an indicator). Our tension in S₈: 2.4–3.3σ.
- **DESI:** DR2 in force (2025, strengthened hints of evolving dark energy; w₀ = −0.75±0.06, wₐ = −0.86±0.25); sky mapping completed April 2026, final analysis to come — stakes S1/S3 live.
- An external independent audit (July 2026) confirmed the consistency of the δ derivation and the n_s prediction.
**Verification scripts (attached):** q14 (front) | q12 (dispersion) | q7 (sound horizon) | k3 (cosmology pipeline) | q10 (V-links)

---

# PART A — FORMULAS, THEIR LOGIC, AND THE COMPUTATION OF VALUES

## A1. Network geometry: ⟨k⟩ = 48π²/35 + 2 = 15.54
**Logic:** space = points scattered at random (a Poisson process); neighbourhood = Delaunay triangulation (cells that share a face of the Voronoi tessellation). The mean number of neighbours in 3D is a known constant of stereology — independent of density, set by randomness alone.
**Verification:** simulation with 30k–300k points → ⟨k⟩ = 15.58 (Poisson), 15.32–15.54 (grown by division; drift −1.3 % under 3× growth). Periodic network: 15.535.

## A2. Division overhead: δ = 1/(⟨k⟩ + C)
**Logic:** upon division a cell rebuilds its bonds — 1 new interface arises out of the cell's total number of connections (⟨k⟩ surface + C interior). Overhead = the rebuilt fraction = fuel burned to no effect. Hence w_fuel = −1+δ: the fuel dilutes at exactly the overhead rate.
**Subtlety (Jensen):** the mean of the reciprocal ⟨1/k⟩ = 0.0701 > 1/⟨k⟩ = 0.0647 (+8 %) — degree fluctuations are measured, not neglected (measured in the VCM: δ_sim = 0.0697 = ⟨1/k⟩ ✓).
**Value:** δ = 1/(15.54 + 28) = **0.02297**.

## A3. Interior capacity: C = g_B = 28
**Logic:** a V-link = a shared domain of two cells; the sharing is carried by the CARRIERS of the domains — and the carriers are bosons. Link capacity = the number of independent carrier states.
**Count:** gluons 8×2 = 16 | photon 2 | W⁺W⁻Z 3×3 = 9 | Higgs 1 → **28** (equivalently before symmetry breaking: 8 gauge + 4 Higgs + 16 gluons = 28; pitfall M8: beware double-counting the Goldstones).
**Court of alternatives (executed by the data):** fermions 90 → n_s = 0.986 (5σ †) | all d.o.f. 106.75 → 0.988 (5.4σ †) | 17 particles → 0.954 (2.6σ †) | 8 domains → 0.936 (6.8σ †). Only the bosonic carrier count survived (0.15σ). Look-elsewhere effect acknowledged: the weight is carried by the mechanism plus the fact that 28 existed in the theory a day before the question was posed.

## A4. The emergent light cone: σ(R) ∝ R^χ
**Logic:** a signal hops across the random network; randomness smears the front, but if the width grows more slowly than the radius (χ < 1), the front sharpens in relative terms → out of chaos in the small, a sharp c emerges in the large.
**Measurement:** BFS from a source; for each tick, the mean radius R(t) and the width σ(t); fit of log σ vs log R. **χ = 0.32→0.26 (Poisson, 30k→300k), 0.32±0.02 (network grown by division).** Validations: R(t) linear; speed ∝ N^(−1/3); octant anisotropy 3.4 %→2.0 %. External support: the shape theorem, KPZ (χ_KPZ = 1/3 in 2D, ~0.24 in 3D).

## A5. Wave dispersion: ω²(k) = (2/N)·Σ_edges [1 − cos(k·δ⃗)]
**Logic of the formula:** substituting a plane wave e^{ik·x} into the graph Laplacian (⟨u|L|u⟩/⟨u|u⟩) — a variational frequency estimate. For small k: ω ≈ c·k (the sound of the network); deviations = the imprint of granularity.
**Why the linear term does NOT exist:** the operator is real and symmetric → the spectrum is even in k (k → −k identical) → odd terms are forbidden by parity, not merely "small".
**Values:** β = −0.060 (quadratic softening); isotropy of c: 0.06 % (formula) / 0.2 % (evolution); cubic lattice: 1.33 % (21× worse), β varying ±3× with direction. Scattering: Γ ∝ k^(3–3.5) (Rayleigh) → photon mean free path ≫ the universe.
**Suppression:** the deviation ∝ (l_P/λ)²: optical λ ~ 10⁻⁶ m, l_P ~ 10⁻³⁵ m → (10⁻²⁹)² = **10⁻⁵⁸** — 38 orders of magnitude below the tests (10⁻²⁰).
**Methodological note (M7):** the formula overestimates ω by 7–9 % (spectral mean vs peak) — symmetries from the formula, numbers from time evolution; periodic stitching must be validated against ⟨k⟩.

## A6. One c for all fields (U-1)
**Logic:** two natural couplings of fields to the network (equal contacts vs FEM ∝ facet area) BOTH yield Newton (R² 0.9991/0.9996) and isotropy, yet different c (ratio 15.95). Mixing w(α), we measure the sensitivity: **d ln c/dα = −0.27**. GW170817 (Δc/c < 10⁻¹⁵) ⇒ the couplings of all fields must agree to **4×10⁻¹⁵** ⇒ only IDENTITY survives: a contact has a single property (its capacity), the domains are layers of one and the same cell, and there is no second number for another field to read.
**Consequence (Bell's decomposition of Michelson–Morley):** a sharp isotropic cone (A4, A5) + one c (U-1) + Bell's theorem (bodies made of network waves contract by themselves) ⇒ motion through the network is unmeasurable ⇒ Z1 = 1.

## A7. Background equations (V1) — derived term by term
 dΩ_f/dx = −3δ·Ω_f − λ·(H₀/H)·Ω_f
 dΩ_m/dx = −3·Ω_m + λ·(H₀/H)·Ω_f ; dΩ_r/dx = −4Ω_r ; E² = ΣΩ (x = ln a)
**Logic of the terms:**
- **−3δΩ_f:** expansion = division (N ∝ a³ → 3 divisions/cell/e-fold), each costing the overhead δ (A2) → fuel loss of 3δ per e-fold. THIS IS the micro-origin of w = −1+δ.
- **λ(H₀/H)Ω_f:** digestion runs on the cell's INTERNAL clock (the interior is its own dimension and knows nothing of H) → conversion at the constant rate λH₀ per unit of fuel. The factor H₀/H is merely the conversion to e-folds. This is why Γ∝H (#4) and globally constant Γ (#5) died.
- **Fuel↔matter exchange:** enforced by the Bianchi identity (∇T = 0, law Z3 satisfied actively) — energy is not lost, it is transferred.
**Value λ = 0.15:** the theory's only fit. Microscopically λ = ε_eff/(H₀·t_P): **ε_eff = 0.15·H₀·t_P = 1.74×10⁻⁶²** per attempt. Remarkably: ε_eff² = 3×10⁻¹²⁴ ≈ the failure yield 10⁻¹²³ (P7) — the nucleation reading: waste = the COINCIDENCE of a failure and a scar, each ~10⁻⁶¹·⁵ (a scaffolding-level observation).

## A8. The accounting shadow (V2): why we see "phantom" dark energy
 ρ_DE,eff(x) = E² − Ω_m0·e⁻³ˣ − Ω_r0·e⁻⁴ˣ ; w_eff = −1 − (1/3)·d ln ρ_DE,eff/dx
**Logic:** the observer ASSUMES matter dilutes exactly as a⁻³. In our universe matter accumulates (creation from fuel) → subtracting it leaves an apparent component with w_eff < −1 in the past (wₐ < 0) — **the phantom is an accounting illusion; the NEC is not violated**. CPL fit w = w₀ + wₐ(1−a), weighted by ρ_DE,eff, over 0 < z < 1 (where DESI measures).
**Values (pipeline, working point v4):** w₀ = −0.92, wₐ = −0.61.

## A9. Growth of structure (V3) and S₈
 δ_m′ = −Θ ; Θ′ = −(2 + E′/E)·Θ − (3/2)·(Ω_m/E²)·δ_m ; from z = 1000, growing mode δ ∝ a
**Logic:** lumps grow by gravity (the last term) and are braked by expansion (Hubble friction). σ₈ = 0.811·D/D_ΛCDM (identical primordial amplitude — the CMB anchor); S₈ = σ₈√(Ω_m/0.3).
**Value:** S₈ = **0.874**.

## A10. The CMB anchor (V4) and the sound horizon
 r_s = ∫_{z*}^∞ c_s dz/H ; c_s = c/√(3(1+R_b)) ; R_b = (3ω_b/4ω_γ)·a ; θ* = r_s/D_M fixed
**Logic:** θ* is the most precisely measured number in cosmology (the acoustic angular scale). It pins the ratio of the ruler to the distance → for a given early universe it determines H₀. A double loop: inside, self-consistent ω_m0(h) (matter accumulates in our model!); outside, bisection on h.
**Validation:** ΛCDM → h = 0.6730, Ω_m = 0.3157, r_s = 144.32 Mpc ✓; the no-steam model reproduced the audited point (65.6/0.359/−0.91/−0.60/0.888) ✓✓.

## A11. Why genesis cannot rescue H₀ (Q7) — the logic of the sign
Matter "waiting" inside the fuel does NOT blueshift when looking into the past (w ≈ −1), whereas real matter does (a⁻³). Late creation ⇒ less early energy ⇒ slower early expansion ⇒ a LONGER ruler r_s ⇒ at fixed θ*, a LOWER H₀. **Measured: ΔH₀ = −1.5 (f=0.1, z_c=3000) down to −4.5 (f=0.3).** The only direction that works = extra radiation (the steam).

## A12. The steam: ΔN_eff = (8/7)·(10.75/g*)^{4/3}
**Logic (the "cake"):** the steam (2 polarizations of network ripples) took its slice at genesis and left the table; the remaining g* channels gradually handed their heat to the photons (annihilations). Temperature ratio: T_steam/T_ν = (10.75/g*)^{1/3} (entropy conservation; 10.75 = the channels present at neutrino decoupling). Energy ∝ T⁴ and the fermion/boson factor 8/7 → the formula.
**Value:** g* = 106.75 (the Standard Model complete — the domain table!) → **ΔN_eff = 0.0535 → N_eff = 3.10**. The relic today: T = 2.725·(3.91/106.75)^{1/3} = 0.905 K, peak at 53 GHz.
**Thermalization (Q15a):** the per-event ripple production efficiency ~ (E_event/E_P)²; at genesis f = 1 → ~1 → detailed balance → exactly the thermal share 2/106.75 (independent of unknown O(1) factors). Decoupling: Γ/H = (T/T_P)³ → instantaneous. Today: E/cell ~ 10⁻¹²³E_P → efficiency 10⁻²⁴⁶ → the corresponding term is legitimately absent from V1 (it would be 10⁻²⁴⁸).

## A13. The primordial spectrum: n_s − 1 = −(3/2)·δ
**Step 1 (scale invariance from area):** the energy fluctuation of a region ⟨δE²⟩ = T²C_V; the holographic capacity C_V = γ(R/l_P)² (the area law — MEASURED from the dowry rule: p = 1.97). The lump's potential Φ = δE/R = √γ·T/T_P — **R drops out** → n_s = 1 from geometry.
**Step 2 (the background):** the fuel era w = −1+δ ⇒ quasi-de Sitter; ε ≡ −Ḣ/H² = (3/2)(1+w) = (3/2)δ. Modes exit at k = aH; d ln H/d ln k = −ε.
**Step 3 (the exponent m):** a saturated V-channel (energy creates links rather than heat — a Hagedorn-like regime): δE ∝ √(T·E_P)·√N ⇒ amplitude ∝ √T ∝ √H ⇒ m = ½.
**Result:** n_s − 1 = 2·(½)·d ln H/d ln k = −ε = −(3/2)δ = **−0.0345** (Planck: −0.0351 ± 0.0042; 0.15σ).
**Amplitude:** A_s = 2.1×10⁻⁹ ⇒ freeze-out temperature ~ 2–7×10⁹ GeV. **E-folds:** N = ln(ρ_i/ρ_f)/(3δ) ≈ 1280 (about 60 are needed) — the horizon is covered by the fuel era.
**Court of alternatives:** uncorrelated noise → n_s = 4 († #19); a critical point → ~2 (†); equipartition of channels → −3δ (δ = 0.0117, below the fit window).

## A14. Tensors: r ≈ 0
**Logic:** tensors come from the Rayleigh–Jeans tail of the thermal ripples: Δ²_h ≈ 0.4·H·T (occupation n_k = T/k at k = H). The scalar ∝ T, the tensor ∝ H·T, and H = O(T²) in Planck units at T ~ 10⁻¹⁰ T_P ⇒ **r realistically 10⁻²¹–10⁻¹⁹, absolute ceiling < 6×10⁻¹¹**. The sign of the tilt is blue (the stiff saturated network suppresses anisotropic stress earlier) — academic.
**Prediction:** primordial B-modes do not exist; a detection of r ≳ 10⁻³ = the death of the model.

## A15. The half-dowry rule (R4) and its measurements
**Logic:** the daughters were one interior → they are born mutually entangled with half of their capacity; the parent's links are split between them (monogamy forbids duplication — registered as reading R2). The map n′ = n/2 + C/2 ⇒ fixed point **n_V = C; saturation is an attractor**.
**Measurements (VCM, ~10k cells):** convergence from above and from below ✓; sharpness std/mean = 0.13 ✓; **V-weight across a sphere ∝ R^1.97 (the area law)** ✓. The modest dowry (s=1) → n_eq = 2 († #20).

---

# PART B — WHERE WE SPEAK DIFFERENTLY FROM THE STANDARD (and why)

| phenomenon | standard explanation | our explanation | why ours / what decides |
|---|---|---|---|
| **dark energy** | a fundamental constant Λ (unexplained; QFT off by 10¹²²) | NO fundamental Λ: the accounting shadow of matter creation + fuel dilution (w = −1+δ, F5) | explains both the magnitude (Λ is not an input) and the DESI signal wₐ<0; decided by the final DESI |
| **"phantom" w < −1** | new fields (quintom) or systematics | an illusion of a fitter assuming a⁻³ matter dilution; the NEC is intact | no pathology; a prediction of the exact shape of w(z) |
| **dark matter** | a new particle (WIMP, axion) interacting at least weakly | ash — fully digested waste, GRAVITATIONAL ONLY (the G domain), m ≳ keV | **we predict permanently null direct detections**; a confirmed non-gravitational DM interaction = a problem for the model |
| **inflation** | a scalar inflaton field (ad hoc potential) | the fuel era w = −1+δ: quasi-dS without an inflaton, ~1280 e-folds; ε = (3/2)δ DERIVED | no new field; the tilt n_s is tied to δ from geometry and the boson count |
| **origin of primordial seeds** | quantum vacuum fluctuations of the inflaton | thermal holographic fluctuations of the saturated V-layer (area law measured) | n_s = 0.9656 DERIVED; the unique n_s ↔ w(z) relation; decided by S4 |
| **primordial B-modes** | the hope of many models, r ~ 10⁻³–10⁻² | **they do not exist** (r < 10⁻¹⁰) | an asymmetric executioner: a LiteBIRD detection = our death |
| **N_eff** | 3.045 (inflation erases the gravitons) | **3.10** — a genesis without an inflaton keeps its steam | the theory's sharpest own number; CMB-S4 |
| **the Hubble tension** | systematics or early dark energy | a hard prediction of H₀ = 66.4 + steam; the local ladder carries a systematic | stake S4; losing it = serious trouble |
| **the S₈ tension** | an open problem of ΛCDM | we predict S₈ = 0.86–0.87 (HIGHER) — a bet that lensing will move up | **the bet is moving our way:** the final KiDS-Legacy (2025) shifted S₈ from 0.759 to 0.815 (+0.016/−0.021); our tension fell from ~5σ to 2.4–3.3σ; decided by Euclid/LSST |
| **baryogenesis** | Sakharov/leptogenesis (unconfirmed) | digestion failures nucleating on scars; yield 10⁻¹²³ = ε² | the mechanism yes, the number ε underived (P7 — identical to the Λ mystery) |
| **gravity** | a fundamental force / graviton exchange | an entropic gradient (Jacobson); the graviton as a FORCE carrier does not exist; ripples of the network (GWs) do | Newton emerged twice independently (R² 0.999); GW speed = c via U-1 |
| **Lorentz invariance** | a fundamental symmetry (a postulate) | emergent: randomness + the capacity identity; violations parked at 10⁻⁵⁸ | undecidable by instruments — honestly: a philosophical difference, not a measurable one |
| **entanglement** | abstract nonlocality of Hilbert space | V-links (shared domains); ER=EPR; signalling forbidden (#12), gravitationally inert (VS-1) | monogamy FOR FREE from capacity; the area law measured |
| **collapse / the arrow of time** | an interpretational problem of QM | an irreversible scar in the network (the I domain) | open (Q8) — honestly: verbal, the mechanism is missing |
| **cosmic rotation / chirality** | — | a REJECTED reading of our own: strong rotation dead (deficit of 6–40 orders, #13) | an example of self-falsification by the protocol |
| **constancy of constants** | an assumption of immutability | DERIVED: cells do not grow (#17), δ is constant (n_V = C is an attractor) | a drift of δ would be trace E1 |

**Where we say an unambiguous NO (the model's list of prohibitions):** no inflaton | no graviton force-carrier | no fundamental Λ | no NEC violation | no non-gravitational dark-matter interaction | no primordial B-modes | no measurable Lorentz violation | no fifth force | no growth of cells / change of G | no signal through the interior.

---

# PART C — OBSERVATION PROGRAMME AND IMPACTS
(See the Predictions Table: six decisive tests with dates; the consistency relation n_s↔w(z); the timestamped preprint as priority no. 1; the dowry rule as a real network protocol; the VCM toolkit and the methodology as scientific products.)

# PART D — WHAT WE ADMIT
One underived number (ε ~ 10⁻⁶² ≡ P7 ≡ the Λ mystery) | the S₈ front remains risky: our 0.874 (λ=0.15) or 0.859 (λ=0.10) vs KiDS-Legacy 0.815+0.016/−0.021 = tension of 3.3σ or 2.4σ — softened from ~5σ, not gone; in-model brakes examined and excluded (ash: free-streaming length 0.04 Mpc ≪ 8 Mpc; steam perturbations ~0.1 %; the only lever is λ→0.10) | m = ½ and C = 28 are readings with a mechanism, not theorems (death conditions on record) | a single pipeline of a single reviewer (W4 — half repaid by our own reproduction + an external audit confirmed the consistency of δ and n_s) | the I domain and Gaussianity remain open | the look-elsewhere effect for C acknowledged.

# THE KEY SENTENCE
Every formula in this document has its logic, every number its procedure, and every claim its named way of dying — the theory says "no" to eight standard building blocks, and for each "no" it offers a mechanism, a number, and an experiment that can execute it.
