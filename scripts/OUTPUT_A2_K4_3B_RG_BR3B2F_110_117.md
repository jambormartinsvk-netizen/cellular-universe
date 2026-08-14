# A2-K4.3b-RG BR3B-2f — výstup skriptov 110 až 117

Dátum: 2026-07-14  
Kanonický stav: **K4 ŽIVÁ, 60/100 = G6**  
G7: **NEUZAVRETÁ**

## Behy

| Skript | Stav | Auditný význam |
|---|---|---|
| 110 | `REVIEW_UNCLOSED` | Jednobehová CAMB regresia je stabilná pre AD/CDI/BI, nie pre vysoké NID/NIV koeficienty. |
| 111 | `REVIEW_UNCLOSED` | Baryónová diferencia zrušila závislosť od veľkosti kroku, ale nie od časového okna. |
| 112 | `EXTERNAL_TIMEOUT_UNCLOSED` | Symbolické `series()` bolo ukončené vonkajším limitom 35 s. |
| 113 | `REVIEW_UNCLOSED` | Vedúce koeficienty a rezíduá PASS; plná hodnosť a `k`-nezávislosť boli príliš prísne brány. |
| 114 | `NOT_EXECUTED_DUPLICATE_PRESERVED` | Technický duplikát po chybe Windows patch helpera; bez dôkaznej váhy. |
| 115 | `PASS_STANDARD_NID_NIV_FROBENIUS_TARGET_UNIQUE` | Jediný nulový smer nezasahuje cieľové koeficienty. |
| 116 | `PASS_MISSING_MATTER_DRESSED_SECTORS_PROVEN` | Dokázal chýbajúce NID `p+1` a NIV `p` sektory. |
| 117 | `PASS_MANIFEST_CREATED` | SHA-256 manifest skriptov 110–116. |

## Kľúčové čísla skriptu 115

- tvar matice: `62 x 60`;
- hodnosť: `59`, deficit presne jeden;
- podmienenosť vyriešeného podpriestoru: `17.42–17.46`;
- škálované rezíduá: `1.14e-15` až `1.39e-15`;
- dominantný nulový smer: `eta5=0.78087`, `sigma5=0.62470`;
- maximálna absolútna projekcia nulového smeru do cieľa: `8.32e-16`;
- publikované vedúce NID/NIV koeficienty: relatívna chyba najviac približne
  `2.7e-13`.

## Kľúčový výsledok skriptu 116

Pri `epsilon_m != 0` nestačí čistý radiačný zoznam mocnín. Povinné poradie je:

- NID: `3.93109 -> 4.93109 -> 5.93109 -> 6.93109`;
- NIV: `2.93109 -> 3.93109 -> 4.93109 -> 5.93109`.

Skripty 104 a 108 sa nemažú ani neoznačujú ako chybné výpočty. Ich PASS sa
obmedzuje na vypočítané čisté radiačné sektory; úplnosť poradia bola neskorším
auditom vyvrátená.

## Reprodukčný manifest

| Súbor | SHA-256 |
|---|---|
| `scripts/110_script_A2_K4_3b_RG_BR3B2f_CAMB_mode_coefficients_in_a.py` | `97e4f522077f418cac3053269cb5c24a1058eef80b171d88f73fc78bce259ff3` |
| `scripts/111_script_A2_K4_3b_RG_BR3B2f2_NID_NIV_baryon_fraction_difference.py` | `c8a91e41fdf5c05c44fc69a459c1755c1e311580bafb4fccf736d1dbcfcaf19d` |
| `scripts/112_script_A2_K4_3b_RG_BR3B2f3_exact_Frobenius_standard_NID_NIV.py` | `8b32ae418e8baa7fe6f232097d1b00c58fad7a0e0385088d900c39ddf33cf46f` |
| `scripts/113_script_A2_K4_3b_RG_BR3B2f3_Frobenius_bounded_coefficients.py` | `53541b338834bf58b8ad9090f51f9e24bd45363c92d04a1f27c27a2ba415b5f9` |
| `scripts/114_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit.py` | `c94a01fe69048c91e80d10cec9364524ebf7e89007f6b9f19fdb2fe7bb8dffcd` |
| `scripts/115_script_A2_K4_3b_RG_BR3B2f3_Frobenius_null_direction_audit_fixed.py` | `8e5b6e925653473c5d905b14636fa5a049dd002447beedb257e68e05a8896006` |
| `scripts/116_script_A2_K4_3b_RG_BR3B2f4_missing_matter_dressed_sector_audit.py` | `591cce9728670895d14ee83e582a658f5a7b4144de494a1d21f6b18aa6dfbe93` |

