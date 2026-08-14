# Reprodukcia KMPC-036 — M1 order-7 precision gate

**Revízia balíka:** `R3_REFREEZE_AFTER_EXTERNAL_TECHNICAL_STOP`  
**Reprodukčný strom:** `REPRO/`  
**Interný timeout:** presne `4.8 s`  
**Externý timeout:** `10 s` na proces  
**Pôvodné prostredie:** `C:\Python311\python.exe`, NumPy; presná verzia
NumPy nebola v pôvodnom raw výsledku uložená. Auditor zaznamená vlastné
verzie. Ide o environmentálnu medzeru, nie fyzikálny STOP.

## Povinný prerequisite

Runner pred výpočtom fail-closed overuje súbor:

`REPRO/scripts/results/k_mpc_005/RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json`

Jeho zmrazený SHA-256 je
`A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`.
R2 ho neobsahovala, preto oficiálny audit skončil technickým STOP-om.
R3 dopĺňa iba tento prerequisite a dokumentáciu; nemení výpočet KMPC-036.

## Čo sa počíta

Ten istý ukotvený M1 seed sa predĺži z order 5 na order 7. Kontroluje sa
stabilita starších koeficientov, plný rank a 139 driver/initial/holdout
rovníc. Reference prešiel rankom, anchorom, regresiou a všetkými holdoutmi.
Presne tri `power=7` driver riadky neprešli relatívnym `1e-10`, hoci ich
absolútne rezíduá sú približne `3e-16` až `1e-15`.

## Očakávané výsledky

| Kontrola | Reference |
|---|---|
| rank | `98/98` |
| hard-anchor absolute difference | `<=1e-14` |
| inverse condition | `>=1e-10` |
| order5→7 drift | hybrid `1e-14` absolute / `1e-12` relative |
| holdouty | 18/18 PASS; najhorší `Einstein_0i[7] ≈ 3.84e-11` |
| review riadky | `gamma_Euler[7] ≈ 2.87e-10`; `cdm_continuity[7] ≈ 4.66e-10`; `tight_coupling[7] ≈ 1.17e-9` relatívne |
| scope | `PASS...HOLDOUT_ONLY / REVIEW...PRECISION_FLOOR_UNCLOSED` |

## Reprodukčné príkazy

Spúšťať z koreňa čerstvej kópie balíka.

```bash
timeout 10s python REPRO/scripts/280_script_KMPC_036_P5_3g7_M1_order7_provenance_gate.py --smoke --max-runtime-seconds 4.8
timeout 10s python REPRO/scripts/280_script_KMPC_036_P5_3g7_M1_order7_provenance_gate.py --audit --max-runtime-seconds 4.8 --output REPRO/scripts/results/k_mpc_005/RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json
```

Windows PowerShell audit s externým watchdogom:

```powershell
$args = @('REPRO\scripts\280_script_KMPC_036_P5_3g7_M1_order7_provenance_gate.py','--audit','--max-runtime-seconds','4.8','--output','REPRO\scripts\results\k_mpc_005\RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json')
$p = Start-Process -FilePath 'C:\Python311\python.exe' -ArgumentList $args -PassThru -NoNewWindow
if (-not $p.WaitForExit(10000)) { $p.Kill($true); throw 'EXTERNAL_TIMEOUT_10S' }
if ($p.ExitCode -ne 0) { throw "PYTHON_EXIT_$($p.ExitCode)" }
```

Smoke používa rovnaký watchdog s argumentmi
`--smoke --max-runtime-seconds 4.8` a bez `--output`.

## Vyhodnotenie

- Rovnaké tri relatívne odchýlky pri absolútnom machine floor podporujú
  existujúci `REVIEW_PRECISION_FLOOR_UNCLOSED`.
- Iná podmnožina floor-level failov na odlišnej platforme nie je sama osebe
  PASS ani formula mismatch. Auditor porovná absolútne rezíduá, lokálne
  `term_norm`, rank, anchor, regresie a holdouty a zaznamená Python, NumPy
  a BLAS/LAPACK prostredie. Projektový verdikt zostáva `REVIEW`, kým
  predregistrovaný refinement formálne neuzavrie terminálne riadky.
- Zlyhanie ranku, anchoru, regresie alebo holdoutu znamená formula/platform
  mismatch; nejde automaticky o fyzikálny STOP.
- Ak všetko prejde, auditor musí vysvetliť platformový/precision rozdiel;
  projektový verdict sa nemení automaticky.
- Exception alebo timeout je `TECHNICAL_STOP`, fyzika `NOT_RUN`.

Generated JSON sa porovnáva s `EVIDENCE/010__KMPC036_RAW_RESULT.json` podľa
polí a prahov. Bitový hash generated JSON nemusí byť identický.
