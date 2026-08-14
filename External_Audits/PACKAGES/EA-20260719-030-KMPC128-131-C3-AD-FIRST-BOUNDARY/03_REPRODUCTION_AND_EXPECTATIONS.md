# Reprodukcia a očakávania

Pracujte v kópii adresára `REPRO`. Najprv overte Python a spustite procesy
oddelene s vonkajším limitom 10 s:

```powershell
python -m py_compile scripts\baseScripts\p5_general_synchronous\c3_zero_variant_parallel_v3_support_shards.py
python -m py_compile scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py
python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --help
python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --smoke --mode AD --k 0.005 --max-runtime-seconds 4.8
```

Očakávanie: exit `0`; smoke `4/4`, `physics_executed=false`.

### Negatívny guard

V druhej fresh copy odstráňte iba kópiu KMPC-127 aggregate prerequisite a
spustite rovnaký smoke. Očakávanie: nonzero exit, hlásenie missing/hash guard,
žiadny generated JSON. Zapečatený balík sa nemení.

### Official `.005`

Vo fresh copy najprv odstráňte iba priloženú generated raw kópiu s názvom
`RUN_KMPC_131...AD_K0p005...json`, potom:

```powershell
python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --audit --mode AD --k 0.005 --max-runtime-seconds 4.8
```

Očakávanie: exit `0`, pair PASS, `gamma0` PASS, `af0` PASS.

### Official `.05`

V ďalšej fresh copy odstráňte iba priloženú `.05` generated raw kópiu a
spustite:

```powershell
python scripts\375_script_KMPC_131_P5_3g7_C3_four_support_shards.py --audit --mode AD --k 0.05 --max-runtime-seconds 4.8
```

Očakávanie: exit `0`, technicky úplný pair REVIEW; oba varianty majú
core/common/background/null/af0-bridge PASS a iba tail FAIL. Najhorší M3
tail na `z=.01` je približne `3.281732115e-3 > 1e-6`.

`.15` sa v tomto balíku nespúšťa. Package T2 neznamená fyzikálny C3 PASS.

### Field parity

Oba fresh-copy official JSON sa porovnajú po odstránení iba polí s názvom
obsahujúcim `runtime`. Jediná ďalšia dovolená environmentálna odchýlka je
absolútny koreň poľa
`frozen_B1_left_null_Bianchi/frozen_algebra_source`; relatívny suffix
`scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py` a jeho
manifestovaný SHA-256 musia zostať identické. Všetky fyzikálne polia,
identity, gate hodnoty, prahy a source hashe musia mať exact parity.
