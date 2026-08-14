# Výstup skriptov 73 a 74 — A2-K4.3b

**Dátum behov:** 2026-07-14  
**Stav celej K4.3b:** `NEUZAVRETÁ; A2-K4 OSTÁVA ŽIVÁ 60/100`  
**Dôvod:** hierarchy a nulové rekombinačné rozhranie prešli, ale chýba
sedem konečno-štartových radov v regulárnej gauge s podvedúcimi členmi K4.

## Skript 73

**Príkaz:** `python scripts\\73_script_A2_K4_3b_hierarchy_and_regular_mode_taxonomy_audit.py --max-runtime-seconds 20`  
**Vonkajší limit:** 30 s  
**Exit code:** 0  
**Hlásené trvanie:** 9,234 s  
**Execution:** `PASS`  
**Gate verdict:** `K4_3B_NEUZAVRETA_REGULAR_GAUGE_FINITE_START_SERIES_REQUIRED`

Všetkých 18 automatizovaných kontrol prešlo:

```json
{
  "checks": {
    "CAMB_neutrino_hierarchy_is_collisionless": true,
    "CAMB_photon_hierarchy_contains_opacity": true,
    "CAMB_polarization_hierarchy_contains_opacity": true,
    "CAMB_symbolic_hierarchy_inventory_4x3": true,
    "K4_interaction_vanishes_as_a_squared": true,
    "collective_density_isocurvature_compensated": true,
    "collective_velocity_isocurvature_compensated": true,
    "density_seed_has_Fl_order_y_to_l": true,
    "internal_density_isocurvature_compensated": true,
    "internal_mode_zero_total_source_all_multipoles": true,
    "internal_velocity_isocurvature_compensated": true,
    "nu_steam_collective_hierarchy_closes": true,
    "nu_steam_internal_hierarchy_decouples": true,
    "radiation_fractions_sum_to_one": true,
    "seven_standard_analytic_scalar_seeds_independent": true,
    "tight_coupling_collision_block_has_only_zero_equilibrium": true,
    "velocity_mode_not_finite_in_K4_1_Newtonian_U": true,
    "velocity_seed_has_expected_analytic_orders": true
  },
  "radiation_fractions": {
    "R_gamma": 0.5868901246903825,
    "R_nu_standard": 0.40597924832814813,
    "R_steam_DeltaNeff": 0.007130626981469443,
    "R_free_streaming_total": 0.41310987530961757
  },
  "standard_analytic_scalar_mode_count_S1": 7,
  "CAMB_version": "1.6.6",
  "CAMB_symbolic_equation_count_l2_to_l5": 12,
  "early_K4_lambda_over_E": {
    "x_minus_20": 6.520811657880213e-17,
    "x_minus_22": 1.1943283158718203e-18,
    "ratio": 54.598150033144236
  },
  "velocity_mode_Newtonian_U_scaling": "3/(4 k tau), exponent -1",
  "tight_coupling_collision_block_determinant": "-3/10"
}
```

Prvé koeficienty interného density seedu sú

```text
F0 = 1 - y^2/6 + y^4/120 + ...
F1 = y/3 - y^3/30 + ...
F2 = y^2/15 - y^4/210 + ...
```

a interného velocity seedu

```text
F0 = -y + y^3/10 + ...
F1 = 1 - 3y^2/10 + y^4/56 + ...
F2 = 2y/5 - 2y^3/35 + ...
F3 = 3y^2/35 - y^4/126 + ...
```

kde `y=k tau`.

## Skript 74

**Príkaz:** `python scripts\\74_script_A2_K4_3b_CAMB_recombination_interface_reference.py --max-runtime-seconds 50 --samples 1200`  
**Vonkajší limit:** 60 s  
**Exit code:** 0  
**Hlásené trvanie:** 0,063 s  
**Execution:** `PASS_NULL_RECOMBINATION_INTERFACE_REFERENCE`  
**Gate verdict:** `NEUZAVRETA_EXACT_K4_BACKGROUND_BACKEND_STILL_REQUIRED`

```json
{
  "CAMB_version": "1.6.6",
  "checks": {
    "all_reference_arrays_finite": true,
    "baryon_temperature_and_sound_speed_physical": true,
    "early_tight_coupling_for_k_0p2_Mpc": true,
    "finite_tight_coupling_switch_exists": true,
    "ionization_fraction_nonnegative_and_helium_bounded": true,
    "opacity_and_visibility_nonnegative": true,
    "visibility_normalization_controlled": true,
    "visibility_peak_in_recombination_window": true
  },
  "diagnostics": {
    "early_TCA_epsilon_k_0p2_Mpc": 4.796141700579197e-06,
    "early_z_for_epsilon": 1000000.0,
    "first_z_descending_with_epsilon_ge_0p1": 2184.9904407280255,
    "opacity_max_per_Mpc": 45229129.11554979,
    "visibility_integral_deta": 1.0000192112403723,
    "x_e_max": 1.1648364177716797,
    "x_e_min": 0.00020991699936393488,
    "z_visibility_peak": 1088.1712506287604
  }
}
```

## Audítorské obmedzenie

Skript 74 používa konštantný `w=-0.97703` CAMB surrogate a nezmenenú
štandardnú atómovú fyziku. Nedokazuje rekombináciu na presnom A1-K1
backgrounde a neobsahuje K4 poruchy. Je iba zmrazeným nulovým interface
testom pre budúci modifikovateľný backend.

