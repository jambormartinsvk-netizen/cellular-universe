# Výstup A2-K4.1 — skripty 66 a 67

**Dátum:** 2026-07-14  
**Účel:** reprodukovateľný textový záznam rozhodujúcich výsledkov; úplný JSON
sa znovu vytvorí spustením uvedených skriptov.

## Príkazy

```powershell
python scripts\66_script_A2_K4_1_complete_regular_mode_basis.py
python scripts\67_script_A2_K4_1_independent_fixed_RK4_crosscheck.py
```

## Skript 66 — hlavný DOP853 audit

```text
test = A2-K4.1 complete regular constrained superhorizon basis
verdict = PASS_K4_1_REGULAR_SUPERHORIZON_BASIS

characteristic_polynomial =
p^3 (p+2)^2 (p+3) [p^2+(5-3 delta)p+12-6 delta]

regular_mode_count = 3
regular_modes = adiabatic, cdm_density_isocurvature,
                baryon_density_isocurvature
old_velocity_seed_projection_residual = 0.9789492202249631
old_velocity_seed_in_regular_span = false

global_relative_00_constraint_residual = 2.190976441956265e-12
max_regular_subspace_absolute_singular_transfer = 26.43690732226979
primordial_1e_minus_5_max_audit_norm = 0.0002643690732226979

mode max absolute norm transfers:
adiabatic = 2.467224670513985
cdm_density_isocurvature = 23.19873760693366
baryon_density_isocurvature = 4.3981188463378755

deep_start_matrix_difference = 5.8472165509997765e-06
q_matrix_difference = 1.4860591568582408e-09
solver_matrix_difference = 1.6189777392400475e-07
background_matrix_difference = 9.410060697437228e-07

ratios to Gamma=0 are reported separately and are not absolute growth:
adiabatic max ratio = 1.65258
cdm density isocurvature max ratio = 16.1559
baryon density isocurvature max ratio = approximately 4.3981
```

Kontroly skriptu 66:

```text
symbolic_characteristic_factorization = PASS
exactly_three_regular_modes = PASS
old_velocity_seed_not_regular = PASS
all_runs_finite = PASS
initial_constraints_controlled = PASS
global_constraint_controlled = PASS
deep_start_converged = PASS
superhorizon_q_converged = PASS
solver_tolerance_converged = PASS
background_step_converged = PASS
primordial_1e_minus_5_remains_linear = PASS
```

## Skript 67 — nezávislý fixed-RK4 audit

```text
test = A2-K4.1 independent fixed-RK4 and indicial-basis cross-check
verdict = PASS_INDEPENDENT_CROSSCHECK

indicial exponents:
0, 0, 0, -2, -2,
-2.4655450000000005 +/- 2.404842583824356 i,
-3

regular_kernel_dimension = 3
regular_basis_residual = 2.7755575615628914e-17

coarse step = 5.0e-4
coarse points = 40002
coarse global relative 00 residual = 3.420233137675572e-14
coarse DOP853 reference difference = 3.9462702622928906e-07

fine step = 2.5e-4
fine points = 80002
fine global relative 00 residual = 2.490601607427337e-15
fine DOP853 reference difference = 3.7117295136117254e-07

coarse/fine fixed-RK4 matrix difference = 2.3454368710518858e-08
```

Kontroly skriptu 67:

```text
independent_nullity_three = PASS
explicit_regular_basis_in_kernel = PASS
five_irregular_exponents = PASS
coarse_and_fine_finite = PASS
fixed_RK4_constraint_controlled = PASS
fixed_RK4_step_converged = PASS
DOP853_reference_reproduced = PASS
```

## Zachované diagnostické errata

- `ERRATUM_66_A2_K4_1_NUMPY_INT_JSON.md`: NumPy integer nebol JSON
  serializovateľný; fyzikálny výpočet sa nemenil.
- `ERRATUM_66B_A2_K4_1_SYMPY_CHARPOLY_SYMBOL.md`: rovnaké meno symbolu s
  inými assumptions spôsobilo falošné textové zlyhanie; determinant sa
  vyhodnocuje s pôvodným symbolom.
- `ERRATUM_67_A2_K4_1_NUMPY_BOOL_JSON.md`: NumPy boolean nebol JSON
  serializovateľný; fyzikálny výpočet sa nemenil.
- `ERRATUM_67B_A2_K4_1_BACKGROUND_MIDPOINT_ORDER.md`: aritmetický priemer
  backgroundových koncov degradoval nezávislý RK4 na druhý rád; midpoint sa
  teraz počíta samostatným polkrokom RK4.

Prvý neúspešný výstup skriptu 67 sa nevykladá ako smrť fyzikálnej koľaje:
constraint, jadro a spektrum prešli, zlyhala presnosť kontrolného integrátora.
Oprava bola zapísaná pred opakovaním a finálny test prešiel všetkými siedmimi
bránami.

## Rozsah

Výstup uzatvára iba úplnú regulárnu superhorizontovú bázu deklarovaného
perfect-radiation systému. Neobsahuje high-k test, úplnú fotónovú/neutrínovú
hierarchiu, CMB normalizáciu ani likelihood.

