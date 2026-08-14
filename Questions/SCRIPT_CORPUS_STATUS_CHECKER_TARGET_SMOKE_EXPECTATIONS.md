# Checker 188 — očakávania target smoke-testu

Dátum: 2026-07-15  
Stav: zapísané pred target smoke-testami

## Test A — známy karantenizovaný skript

Cieľ: `118_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py`  
Očakávanie: checker nič z cieľa nespustí, vráti `status=DO_NOT_RUN_TECHNICAL`, `routine_run=BLOCKED` a exit code `2`.

## Test B — nekarantenizovaný autoritatívny agregátor

Cieľ: `176_script_A2_K4_C7_7c_K7b_final_four_surface_gate.py`  
Očakávanie: checker nič z cieľa nespustí, vráti `status=NOT_IN_QUARANTINE` a exit code `0`. Tento výsledok neznamená fyzikálny PASS; iba neprítomnosť v známom blokovacom registri.

Každý checker beh má interný limit 5 s a externý limit 10 s. Cieľový skript sa neimportuje ani nespúšťa.
