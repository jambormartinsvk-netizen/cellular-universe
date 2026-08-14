# Reprodukcia — EA-010

Z koreňa čerstvej kópie `REPRO/`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/niv_support_step2_v2_finite_owner.py
python -m py_compile scripts/300_script_KMPC_056_P5_3g7_NIV_support_step2_finite_owner_successor.py
python scripts/300_script_KMPC_056_P5_3g7_NIV_support_step2_finite_owner_successor.py --help
python scripts/300_script_KMPC_056_P5_3g7_NIV_support_step2_finite_owner_successor.py --max-runtime-seconds 4.8 --smoke
python scripts/300_script_KMPC_056_P5_3g7_NIV_support_step2_finite_owner_successor.py --max-runtime-seconds 4.8 --audit --output scripts/results/k_mpc_005/RUN_KMPC_056_P5_3G7_NIV_SUPPORT_STEP_2_FINITE_OWNER_SUCCESSOR.json
```

Pred auditom musia byť KMPC-056 success/failure/temp výstupy neprítomné.
Očakávanie:

```text
candidate       = PASS_NIV_SUPPORT_STEP_2_SUPPORT_MINUS1_4_ADEQUATE_CANDIDATE_ONLY
owner_restored  = true
regression_pass = true
M1_depth6_pass  = true
core_pass       = true
common_pass     = true
tail_pass       = true
```

Reference SHA je
`9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332`.
Generated JSON dostane vlastný hash. V zahoditeľnej kópii odstráň KMPC-054
prerequisite; smoke musí fail-closed bez fyzikálneho verdictu. V druhej
kópii zmeň jeden import hash; preimport guard ho musí odmietnuť.

