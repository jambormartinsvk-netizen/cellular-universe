# Reprodukcia a očakávania

Pracujte v kópii adresára `REPRO`. Každý proces má vonkajší limit 10 s:

```powershell
python -m py_compile scripts\baseScripts\p5_general_synchronous\c3_zero_variant_parallel_v4_ad_k0p05_support_04_06.py
python -m py_compile scripts\376_script_KMPC_132_P5_3g7_C3_AD_k0p05_support_04_06.py
python scripts\376_script_KMPC_132_P5_3g7_C3_AD_k0p05_support_04_06.py --help
python scripts\376_script_KMPC_132_P5_3g7_C3_AD_k0p05_support_04_06.py --smoke --mode AD --k 0.05 --max-runtime-seconds 4.8
```

Očakávanie: exit `0/0/0/0`; smoke `6/6`,
`physics_executed=false`.

## Negatívny guard

V osobitnej fresh copy odstráňte KMPC-127 aggregate prerequisite aj
priložený KMPC-132 generated raw. Spustite rovnaký smoke. Očakávanie:
nonzero exit, missing/hash guard a žiadny generated JSON.

## Official KMPC-132

V success fresh copy odstráňte iba priložený
`RUN_KMPC_132...SUPPORT_04_06.json` a spustite:

```powershell
python scripts\376_script_KMPC_132_P5_3g7_C3_AD_k0p05_support_04_06.py --audit --mode AD --k 0.05 --max-runtime-seconds 4.8
```

Očakávanie: exit `0`, nominal checkpoint PASS, gamma0/af0 pair PASS a
najhorší tail na `z=.01` približne `4.6829e-8 < 1e-6`.

## Field parity

Generated a priložený raw musia mať exact parity po odstránení iba názvov
polí obsahujúcich `runtime`. Jediná ďalšia environmentálna odchýlka je
absolútny koreň poľa
`frozen_B1_left_null_Bianchi/frozen_algebra_source`; relatívny suffix
`scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py` a
source hash musia zostať identické. Fyzikálne polia, identity, prahy a hashe
sa nenormalizujú.

AD/.15 raw sa v tomto balíku nereprodukuje; jeho tier je T1 a SHA-256 má byť
`FFEB802BADF663F812023914C1B8C34AA150070A763BBF123E41A55E7BFE4C47`.
