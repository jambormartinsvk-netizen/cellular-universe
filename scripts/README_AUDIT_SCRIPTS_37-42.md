# Reprodukcia A2-K5.1 — skripty 37 až 42

**Dátum:** 2026-07-13

## Aktívne rozhodovacie skripty

1. `37_script_A2_K5_1_action_equations_sign_null_audit.py` — algebraické
   znamienka, hlavný symbol, identita `delta_c`, nulový limit;
2. `39_script_A2_K5_1_full_superhorizon_relative_mode_enthalpy_fixed.py` —
   finálny relatívny superhorizontový mód;
3. `41_script_A2_K5_1_regular_adiabatic_mode_converged.py` — finálny
   constrained adiabatický mód;
4. `42_script_A2_K5_1_quasistatic_limit_crosscheck.py` — porovnanie úplných
   koeficientov s kvázistatickým skriptom 33.

## Povinne zachované neúspešné skripty

- `38_script_A2_K5_1_full_superhorizon_relative_mode.py` — nesprávna skalárna
  entalpia; 00 rezíduum `0.1066`, výsledok nepoužívať;
- `40_script_A2_K5_1_regular_adiabatic_mode.py` — fyzikálne brány prešli, ale
  krokový rozdiel `1.1441e-6` nesplnil prah `1e-6`.

## Errata

- `ERRATUM_38_39_A2_K5_1_SCALAR_ENTHALPY.md`;
- `ERRATUM_40_41_A2_K5_1_ADIABATIC_CONVERGENCE.md`.

## Poradie spustenia

```powershell
python scripts\37_script_A2_K5_1_action_equations_sign_null_audit.py
python scripts\38_script_A2_K5_1_full_superhorizon_relative_mode.py
python scripts\39_script_A2_K5_1_full_superhorizon_relative_mode_enthalpy_fixed.py
python scripts\40_script_A2_K5_1_regular_adiabatic_mode.py
python scripts\41_script_A2_K5_1_regular_adiabatic_mode_converged.py
python scripts\42_script_A2_K5_1_quasistatic_limit_crosscheck.py
```

Očakávané návratové kódy sú `0, 1, 0, 1, 0, 0`. Kódy `1` skriptov 38 a 40
sú reprodukciou zachovaných odmietnutých behov, nie chybou aktuálneho balíka.
