# A2-K4.3b-RG BR3B-2f-5 — výstup skriptov 118 až 125

Dátum: 2026-07-14  
Kanonický stav: **K4 ŽIVÁ, 60/100 = G6**  
BR3B-2f-5: **PASS**  
G7: **NEUZAVRETÁ**

## Behy a dôkazná váha

| Skript | Stav | Dôvod/stav dôkazu |
|---|---|---|
| 118 | `SYNTAX_ERROR_UNCLOSED_PRESERVED` | Chýbala zátvorka v `solve_fuel`; fyzika sa nespustila. |
| 119 | `SYNTAX_ERROR_UNCLOSED_PRESERVED` | Prvá oprava stále neuzavrela vonkajší zoznam; fyzika sa nespustila. |
| 120 | `JSON_SERIALIZATION_ERROR_UNCLOSED_PRESERVED` | Rovnice sa vykonali, ale `numpy.bool_` zlyhal pri JSON zápise. |
| 121 | `REVIEW_LEGACY_ORACLE_ERROR_LOCALIZED` | 24/26 brán PASS; dve nezhody iba voči chybnému shear oraclu 108. |
| 122 | `PASS_DIAGNOSTIC` | Vystavil nulovo-matter štandardné koeficienty; potvrdil správny základ. |
| 123 | `PASS_DIFFERENCE_LOCALIZED_TO_NU_SHEAR` | Celý rozdiel lokalizovaný iba do `nu_shear` zdroja. |
| 124 | `PASS_FULL_MIXED_CHAIN_THROUGH_COMMON_FUEL` | Opravený oracle, 26/26 brán PASS; fyzikálna sústava nezmenená. |
| 125 | `PASS_MANIFEST_CREATED` | SHA-256 ledger skriptov 118–124. |

## Kľúčové výsledky skriptu 124

- NID a NIV: matice `44 x 36`, hodnosť `36/36`;
- čísla podmienenosti `94.06` a `99.09`;
- fyzikálne škálované rezíduá `1.55e-15` a `9.56e-16`;
- maximum z 11 riadkov `7.62e-16` a `1.50e-15`;
- povinné matter vrstvy majú normu `1.191e-2` a `2.985e-2`, ale pri `mu=0`
  klesnú pod `3.8e-16`;
- corrected nulový matter shear oracle používa `U_fs`, nie `U_gamma`;
- common fuel je konečný pre oba módy a bez nového fitu.

## Prečo sa skript 108 obmedzuje

Jeho `J_ns=(8/15)(U_gamma,e-U_gamma,l)` zamieňa druh častice. Správne je
`J_ns=(8/15)(U_fs,e-U_fs,l)`. Preto jeho plná hodnosť a malé rezíduum ostávajú
algebraicky pravdivé, ale jeho staré shear koeficienty nie sú fyzikálny oracle.
Skript 108 sa nemaže.

## Reprodukčný manifest

| Súbor | SHA-256 |
|---|---|
| `scripts/118_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` | `e5ea459aef997b593fc1fc192d5d3c300bd97cee5efa198c60432122f097950f` |
| `scripts/119_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` | `f4e82c3d717600f02748646ac89f85d3838f26872efdeb4377323d8fa195dc8c` |
| `scripts/120_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` | `f466f39dfb435cc20c7ce3f04eb2c622889d979385db12376737d6fd109efe70` |
| `scripts/121_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain.py` | `b088d27114e2628afd7a322c20947e81226d23c1cccf119b5dc21cc289c75f84` |
| `scripts/122_script_A2_K4_3b_RG_BR3B2f5_zero_matter_reference_diagnostic.py` | `02c7716a671f591eea2b06ad4babb2937dcec435bb53ca3521a1680004898ee7` |
| `scripts/123_script_A2_K4_3b_RG_BR3B2f5_script108_source_difference_audit.py` | `e59b44c868ad1720470ba746a41551b68df17fb1c819447a8b49827430d3b124` |
| `scripts/124_script_A2_K4_3b_RG_BR3B2f5_full_mixed_Puiseux_chain_audited.py` | `681f2e6b1398d593f235adb34dd9fbe94e69e788838575bf5f5918ce74e97ab4` |

