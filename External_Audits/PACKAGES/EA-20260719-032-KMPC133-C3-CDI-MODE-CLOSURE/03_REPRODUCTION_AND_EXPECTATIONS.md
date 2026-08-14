# Reprodukcia a očakávania

Vo fresh copy `REPRO/` spúšťajte každý proces s vonkajším limitom 10 s:

```powershell
python -m py_compile scripts\baseScripts\p5_general_synchronous\c3_zero_variant_parallel_v5_cdi_k0p15_same_matrix_refinement.py
python -m py_compile scripts\377_script_KMPC_133_P5_3g7_C3_CDI_k0p15_same_matrix_refinement.py
python scripts\377_script_KMPC_133_P5_3g7_C3_CDI_k0p15_same_matrix_refinement.py --help
python scripts\377_script_KMPC_133_P5_3g7_C3_CDI_k0p15_same_matrix_refinement.py --smoke --mode CDI --k 0.15 --max-runtime-seconds 4.8
```

Očakávanie: exit `0/0/0/0`; smoke `4/4`, bez fyzikálneho solve.

## Negatívny guard

V osobitnej fresh copy odstráňte KMPC-127 aggregate a priložený KMPC-133
generated raw. Smoke musí skončiť nonzero na missing/hash guarde a nesmie
vytvoriť generated JSON.

## Official KMPC-133

V success fresh copy odstráňte iba priložený KMPC-133 generated raw:

```powershell
python scripts\377_script_KMPC_133_P5_3g7_C3_CDI_k0p15_same_matrix_refinement.py --audit --mode CDI --k 0.15 --max-runtime-seconds 4.8
```

Očakávanie: exit `0`, pair a refinement PASS. Gamma0 driver má klesnúť z
`8.199227816e-10` približne na `1.0563e-16`; af0 z
`3.844141885e-10` približne na `1.1150e-16`. Tail ostáva približne
`7.1837e-9 < 1e-6`.

## Field parity

Generated a priložený raw musia mať exact parity po odstránení iba polí s
názvom obsahujúcim `runtime`. Jediná ďalšia dovolená odchýlka je absolútny
koreň poľa `frozen_B1_left_null_Bianchi/frozen_algebra_source`; relatívny
suffix a source hash musia zostať identické. Vedecké polia, identity, prahy
a hashe sa nenormalizujú.
