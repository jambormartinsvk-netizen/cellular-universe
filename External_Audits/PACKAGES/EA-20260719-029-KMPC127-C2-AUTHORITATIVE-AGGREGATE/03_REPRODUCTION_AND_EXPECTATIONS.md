# Reprodukcia — EA-029

Všetky príkazy bežia z koreňa samostatnej čerstvej kópie `REPRO`.
Interný deadline je `4.8 s`; vonkajší limit má byť aspoň `10 s`.

## Negatívna vetva

Odstráňte:

`scripts/results/k_mpc_005/RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json`

Potom spustite:

```powershell
python scripts/371_script_KMPC_127_P5_3g7_C2_authoritative_atom_aggregate.py --aggregate --result-dir scripts/results/k_mpc_005 --output scripts/results/k_mpc_005/RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json --max-runtime-seconds 4.8
```

Očakáva sa exit `2`, presný missing-atom dôvod a žiadny aggregate raw.

## Success vetva

```powershell
python -m py_compile scripts/baseScripts/p5_general_synchronous/c2_authoritative_atom_aggregate.py scripts/371_script_KMPC_127_P5_3g7_C2_authoritative_atom_aggregate.py
python scripts/371_script_KMPC_127_P5_3g7_C2_authoritative_atom_aggregate.py --help
python scripts/371_script_KMPC_127_P5_3g7_C2_authoritative_atom_aggregate.py --smoke --max-runtime-seconds 4.8
python scripts/371_script_KMPC_127_P5_3g7_C2_authoritative_atom_aggregate.py --aggregate --result-dir scripts/results/k_mpc_005 --output scripts/results/k_mpc_005/RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json --max-runtime-seconds 4.8
```

Všetky štyri príkazy majú exit `0`. Official output má:

- candidate `PASS_C2_FOURIER_COVERAGE_10_OF_10_CANDIDATE_ONLY`;
- `read_only_no_physics_solve=true`;
- exact register a atómy `10/10`;
- všetky required gates a aggregate gate true;
- technical-failure outputs `0`;
- background spread PASS, worst
  `4.60781186570449e-16` na
  `a=1e-08:rho_ash_over_rho_r`;
- K4/score effect `NONE`.

Generated raw sa má field-level zhodovať s Evidence 004 po odstránení iba
`runtime_seconds`. Obídenie runnera, vloženie cieľového rawu, zmena
vstupného hashu alebo prahu je `DECLARED_DEVIATION`.

## Interný fresh-copy preflight pred zapečatením

Dňa 2026-07-19:

- štrukturálny preflight prešiel `130/130`;
- negatívna vetva skončila exit `2` za 0.390 s bez outputu;
- success compile/help/smoke/official mali `0/0/0/0`;
- success official trval 0.330 s;
- generated SHA bol
  `D84B4E3DBFAD64273DA6AEF549D61091503AD8ABEAB0F02C99C67987EB6B3A3B`;
- field-level parita po odstránení iba `runtime_seconds` prešla.

Prvý PowerShell orchestration príkaz zastal parserom pred vetvami aj
Pythonom; je zachovaný ako PF-116. Opravený test nemenil kód ani fyziku.
