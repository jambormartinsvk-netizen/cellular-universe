# Výstup skriptu 72 — A2-K4.3a

**Dátum behu:** 2026-07-14  
**Príkaz:** `python scripts\\72_script_A2_K4_3a_species_ledger_and_anisotropic_stress_audit.py --max-runtime-seconds 10`  
**Vonkajší limit:** 15 s  
**Exit code:** 0  
**Trvanie výpočtu hlásené skriptom:** 0,25 s  
**Rozsudok:** `PASS_K4_3A_LEDGER`

```json
{
  "checks": {
    "Thomson_enthalpy_weighted_momentum_cancellation": true,
    "background_dark_energy_transfer_sum": true,
    "dark_momentum_transfer_sum": true,
    "perturbed_dark_energy_transfer_sum": true,
    "radiation_continuity_aggregation": true,
    "radiation_euler_aggregation_without_collisions": true,
    "steam_S1_declared_zero_hierarchy_limit": true,
    "zero_anisotropic_stress_implies_Psi_equals_Phi": true,
    "zero_slip_0i_interface_recovers_K4_2": true
  },
  "next_required_gate": "K4.3b full hierarchies, regular IC, tight coupling and recombination",
  "runtime_limit_seconds": 10.0,
  "runtime_seconds": 0.25,
  "scope": "algebraic formulation only; not a full Einstein-Boltzmann evolution",
  "simplified_residuals": {
    "Thomson_enthalpy_weighted_momentum_cancellation": "0",
    "background_dark_energy_transfer_sum": "0",
    "dark_momentum_transfer_sum": "0",
    "perturbed_dark_energy_transfer_sum": "0",
    "radiation_continuity_aggregation": "0",
    "radiation_euler_aggregation_without_collisions": "0",
    "steam_S1_declared_zero_hierarchy_limit": "0",
    "zero_anisotropic_stress_implies_Psi_equals_Phi": "0",
    "zero_slip_0i_interface_recovers_K4_2": "0"
  },
  "test": "A2-K4.3a species ledger, anisotropic stress and null limits",
  "track_state": "A2-K4 remains LIVE at 60/100",
  "verdict": "PASS_K4_3A_LEDGER"
}
```

## Audítorská interpretácia

Ide o exaktný algebraický nulový a konzervačný test rozhrania, nie o úplný Einsteinov–Boltzmannov výpočet. Výsledok preto nemení sekvenčné skóre K4. Plná brána G7 ostáva otvorená.

