# Reprodukcia — EA-009

Z koreňa čerstvej kópie `REPRO/`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/nid_support_closure.py
python -m py_compile scripts/297_script_KMPC_053_P5_3g7_NID_support_closure.py
python scripts/297_script_KMPC_053_P5_3g7_NID_support_closure.py --help
python scripts/297_script_KMPC_053_P5_3g7_NID_support_closure.py --max-runtime-seconds 4.8 --smoke
python scripts/297_script_KMPC_053_P5_3g7_NID_support_closure.py --max-runtime-seconds 4.8 --audit --output scripts/results/k_mpc_005/RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json
```

Pred auditom musia byť KMPC-053 success/failure/temp výstupy neprítomné.
Očakávanie:

```text
candidate      = PASS_NID_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY
reference_pass = true
core_pass      = true
common_pass    = true
tail_pass      = true
```

Reference SHA je
`625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD`.
Generated JSON dostane vlastný hash. V dvoch zahoditeľných kópiách odstráň
samostatne KMPC-052 a KMPC-048 prerequisite; smoke musí fail-closed bez
fyzikálneho verdictu.
