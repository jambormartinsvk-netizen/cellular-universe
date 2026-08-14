# Reprodukcia — EA-008

Z koreňa čerstvej kópie `REPRO/`:

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/nid_order7_m3_provenance_v2_rank_filter.py
python -m py_compile scripts/294_script_KMPC_050_P5_3g7_NID_order7_M3_provenance_rank_filter.py
python scripts/294_script_KMPC_050_P5_3g7_NID_order7_M3_provenance_rank_filter.py --help
python scripts/294_script_KMPC_050_P5_3g7_NID_order7_M3_provenance_rank_filter.py --max-runtime-seconds 4.8 --smoke
python scripts/294_script_KMPC_050_P5_3g7_NID_order7_M3_provenance_rank_filter.py --max-runtime-seconds 4.8 --audit --output scripts/results/k_mpc_005/RUN_KMPC_050_P5_3G7_NID_ORDER7_M3_PROVENANCE_RANK_FILTER.json
```

Pred auditom musia byť KMPC-050 success/failure/temp výstupy neprítomné.
Očakávanie:

```text
candidate               = REVIEW_NID_ORDER7_NONNUMERICAL_CORE_UNCLOSED
regression_pass         = true
provenance_pass         = true
matrix_pass             = true
capture_counts          = passthrough 1 / target 1 / holdout 1
correction_pattern_pass = false
after_driver_pass       = true
after_holdout_pass      = false
```

Reference SHA je
`8D527E822959D861EB33994233D22BDF752C368025AC66F28C6F820DEF479F65`.
Generated JSON dostane vlastný hash. V dvoch zahoditeľných kópiách odstráňte
samostatne KMPC-048 prerequisite a KMPC-049 failure prerequisite; smoke musí
v oboch prípadoch fail-closed bez fyzikálneho verdictu.
