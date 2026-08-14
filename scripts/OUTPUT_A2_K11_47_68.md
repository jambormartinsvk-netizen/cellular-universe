# A2-K11 — výstup reprodukcie skriptu 47 a auditu 68

**Dátum:** 2026-07-14

## Identita

```text
script47 SHA-256 = 3CFFD6E9977BD8A4619362BBD0BDDCC2436BBEF468EC47B00DADD8F6F0E056BC
script68 SHA-256 = 8EE1ED58E2D2CE0A8212729A78FA17E01511DE805B5F4CE2DCF6D3D60AABAD42
```

## Príkazy

```powershell
python scripts\47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py
python scripts\68_script_A2_K11_script47_physics_and_constraint_audit.py
python scripts\24_script_A2_K1_equation_sign_and_null_limit_audit.py
```

Návratový kód skriptu 68 je zámerne `1`, pretože jeho auditný rozsudok je
zamietnutie neplatného PASS.

## Skript 47 — reprodukovaný výstup

```text
test = A2-K11 S8_K1b Rigorous Amplitude Scaling and Constraint Audit
background_steps = 139897
background_integration_step = 5e-5
rtol = 1e-12
atol = 1e-16

A=1:
transfer_ratio = 2.9220968892602475e-20
max_absolute_residual = 3.8566042202543255e-14
max_term_norm = 3.856614635307602e-14
final_relative_residual = 0.5186005312471957
solver_steps = 3201

A=1e6:
transfer_ratio = 1.4124826676161818e-20
max_absolute_residual = 3.8566037041252005e-8
max_term_norm = 3.8566141191843345e-8
final_relative_residual = 0.9999999998712594
solver_steps = 6601

A=1e8:
transfer_ratio = 1.4124483852661196e-20
max_absolute_residual = 3.856604211584749e-6
max_term_norm = 3.856614626643053e-6
final_relative_residual = 0.9999999998712525
solver_steps = 8199

printed verdict = PASS_RIGOROUS_S8_K1b_AUDIT
linear scaling difference A=1e6 vs A=1e8 = 2.43e-5
```

## Skript 68 — nezávislý audit

Skript 68 použil backgroundový krok `1e-4`; jeho úlohou nebolo reprodukovať
posledné cifry transferu, ale nezávisle testovať koeficienty a význam
constraintovej metriky.

```text
delta = 0.02297
w = -0.97703

expected cs^2=1 Hubble coefficient = +2.0
script47 coefficient = -3.93109
barotropic cs^2=w coefficient = -3.93109

script47 pressure coefficient = +43.535045711798
barotropic pressure coefficient = -42.535045711798

start a = 0.0009166743056192137
script47/correct proper-time rate = 1090.9
script47 lambda/(aE) = 0.006935346496092873
required lambda/E = 6.3574539335345805e-6

script47 fuel energy map [uc,uf]
= [+0.30193062673456134,-0.30193062673456134]
required map
= [-0.00027677204760707795,+0.0005535440952141559]

fuel continuity map relative difference = 0.9999996672948676
RHS homogeneity residual = 2.197544865327609e-16

independent A=1 final relative 00 residual = 0.7248532884376271
independent A=1e6 final relative 00 residual = 0.9999999998713835
normalised max-residual ratio = 0.9999999970658254
```

Výsledky vypočítaných brán:

```text
cs1_null_limit_hubble_coefficient = FAIL
proper_time_rates_are_lambda_over_E_not_lambda_over_aE = FAIL
parallel_energy_transfer_has_no_CDM_Euler_force = FAIL
fuel_energy_recoil_matches = FAIL
fuel_continuity_complete = FAIL
canonical_0i_sign = FAIL
canonical_00_density_sign = FAIL
implemented_rhs_is_linear_homogeneous = PASS
large_amplitude_pointwise_00_constraint = FAIL
absolute_residual_is_amplitude_independent_noise = FAIL

verdict = REJECT_SCRIPT47_PASS_INVALID_EVIDENCE
```

## Skript 24 — zachovaný znamienkový nulový limit

Všetkých osem symbolických kontrol kanonickej A2-K1 energetickej časti
prešlo. Referencia je arXiv:1109.6234, rovnice (32), (33), (35) a (38), s
mapovaním `Gamma_ref=-Gamma_cell`, `1+w=delta>0`.

## Interpretácia

Numerický výstup skriptu 47 je reprodukovateľný. Jeho fyzikálny PASS je
zamietnutý. Skript 47 sa zachováva; A2-K11 zostáva na `15/100` a M-015 sa
nevydáva.

