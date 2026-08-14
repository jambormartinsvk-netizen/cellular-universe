# Reprodukcia a očakávania — EA-006

Všetky príkazy sa spúšťajú z koreňa čerstvej kópie `REPRO/`. Na Windows
PowerShell použite pre každý proces samostatný externý timeout najviac 10 s.

## Official poradie

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/nid_c1_coverage.py
python -m py_compile scripts/291_script_KMPC_047_P5_3g7_NID_C1_primary_extended_coverage.py
python scripts/291_script_KMPC_047_P5_3g7_NID_C1_primary_extended_coverage.py --help
python scripts/291_script_KMPC_047_P5_3g7_NID_C1_primary_extended_coverage.py --max-runtime-seconds 4.8 --smoke
python scripts/291_script_KMPC_047_P5_3g7_NID_C1_primary_extended_coverage.py --max-runtime-seconds 4.8 --audit --output scripts/results/k_mpc_005/RUN_KMPC_047_P5_3G7_NID_C1_PRIMARY_EXTENDED_COVERAGE.json
```

Pred official auditom musí byť generated output, failure output a `.tmp-`
output neprítomný. Smoke nesmie vytvoriť výsledkový súbor.

## Očakávaný official výsledok

```text
execution_status = TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT
candidate         = REVIEW_NID_C1_SUPPORT_EXTENSION_REQUIRED
core_pass         = true
common_pass       = true
combined_R_fs     = true
tail_pass         = false
```

Cross-platform floating hodnoty nemusia mať bitovú identitu reference JSON.
Projektové prahy však ostávajú presne zmrazené a candidate pattern sa musí
reprodukovať bez ich zmeny. Každú nezhodu konkrétnej metriky zapíšte spolu s
platformou, absolútnym/relatívnym rozdielom a dopadom na vetvenie.

## Runtime-dependency negatívny test

V druhej zahoditeľnej kópii `REPRO/` dočasne odstráňte jeden prerequisite
JSON a spustite `--smoke`. Očakáva sa fail-closed nonzero exit s
`TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`; fyzika sa nesmie interpretovať.
Zapečatený balík ani official pracovnú kópiu týmto testom nemeňte.

## Reference

Reference raw result je `EVIDENCE/005__KMPC047_REFERENCE_RESULT.json`, SHA
`EED63396DB99C0818306C581413572BE647630CFD0433A8F05A1DCE704DC696A`.
Generated result musí dostať vlastný SHA-256 v odpovedi auditora.

