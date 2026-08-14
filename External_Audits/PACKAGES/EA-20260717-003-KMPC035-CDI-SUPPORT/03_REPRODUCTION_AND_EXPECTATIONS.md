# Reprodukcia KMPC-035 — CDI support `[0,3]` verzus `[0,5]`

**Revízia balíka:** `R2_PRE_DELIVERY_REFREEZE`  
**Reprodukčný strom:** `REPRO/`  
**Interný timeout:** presne `4.8 s`  
**Externý timeout:** `10 s` na proces  
**Pôvodné prostredie:** `C:\Python311\python.exe`, NumPy; presná verzia
NumPy nebola v raw výsledku uložená. Auditor zaznamená vlastné verzie.

## Čo sa počíta

Porovnajú sa CDI riešenia so supportmi `[0,1]`, `[0,3]` a `[0,5]`.
Kontroluje sa stabilita spoločných koeficientov `0..3` a obálka nových
členov `4,5` na dvoch plochách. Token `C2` v názve runnera nie je globálna
Fourierova C2 brána.

## Očakávané výsledky

| Kontrola | Reference |
|---|---|
| immutable regresia | PASS |
| core rank/driver/holdout | PASS |
| common bridge F0 | max relative drift `≈1.1548e-14` |
| common bridge M3 | max relative drift `≈6.6107e-13` |
| tail pri `z=1e-4` | F0 aj M3 PASS |
| tail pri `z=1e-2` | FAIL presne F0 `delta_f ≈2.5240e-5` a M3 `sigma_fs ≈3.2167e-3` |
| scope | `PASS_CORE_AND_COMMON... / REVIEW_REMAINDER_UNCLOSED` |

Tail FAIL je očakávaný vecný výsledok. Nie je technický pád ani smrť K4.

## Reprodukčné príkazy

```bash
timeout 10s python REPRO/scripts/279_script_KMPC_035_P5_3g7_CDI_C2_support_03_05_ladder.py --smoke --max-runtime-seconds 4.8
timeout 10s python REPRO/scripts/279_script_KMPC_035_P5_3g7_CDI_C2_support_03_05_ladder.py --audit --max-runtime-seconds 4.8 --output REPRO/scripts/results/k_mpc_005/RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json
```

Windows PowerShell audit s externým watchdogom:

```powershell
$args = @('REPRO\scripts\279_script_KMPC_035_P5_3g7_CDI_C2_support_03_05_ladder.py','--audit','--max-runtime-seconds','4.8','--output','REPRO\scripts\results\k_mpc_005\RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json')
$p = Start-Process -FilePath 'C:\Python311\python.exe' -ArgumentList $args -PassThru -NoNewWindow
if (-not $p.WaitForExit(10000)) { $p.Kill($true); throw 'EXTERNAL_TIMEOUT_10S' }
if ($p.ExitCode -ne 0) { throw "PYTHON_EXIT_$($p.ExitCode)" }
```

Smoke používa rovnaký watchdog s argumentmi
`--smoke --max-runtime-seconds 4.8` a bez `--output`.

## Vyhodnotenie

- Reprodukcia reference patternu podporí scoped core/common PASS a
  remainder REVIEW.
- Ak tail prejde, neudeľovať automatický PASS; porovnať koeficienty,
  platformu a metriky.
- Zlyhanie core/ranku/regresie/holdoutu je formula alebo platform mismatch,
  nie automaticky fyzikálny STOP.
- Exception alebo timeout je `TECHNICAL_STOP`, fyzika `NOT_RUN`.

Generated JSON sa porovnáva s `EVIDENCE/010__KMPC035_RAW_RESULT.json` podľa
polí a prahov, nie povinne bitovým hashom.
