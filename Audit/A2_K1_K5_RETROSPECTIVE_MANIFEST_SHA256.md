# A2-K1 až A2-K5 — manifest retrospektívneho auditu

**Dátum:** 2026-07-13  
**Rozsah:** rovnice, výpočty, max. hĺbka a rozsudok K1–K5  
**Kanonická zmena:** M-011 pozastavená; K4 znovu otvorená na K4.1

## Reprodukčné príkazy

```powershell
python scripts\21_script_A2_barotropic_fuel_gradient_instability.py
python scripts\23_script_A2_K1_superhorizon_velocity_instability_converged.py
python scripts\24_script_A2_K1_equation_sign_and_null_limit_audit.py
python scripts\25_script_A2_K3_superhorizon_velocity_instability.py
python scripts\26_script_A2_K3_equation_sign_and_null_limit_audit.py
python scripts\27_script_A2_K4_equation_sign_null_and_eigenvalue_audit.py
python scripts\30_script_A2_K4_full_superhorizon_relative_mode_converged.py
python scripts\63_script_A2_K1_K5_retrospective_depth_equation_verdict_audit.py
python scripts\64_script_A2_K4_retrospective_adiabatic_convergence.py
python scripts\45_script_A3_K5_K1_CAMB_anchor_and_growth_bound.py
python scripts\46_script_A3_K5_K1_required_primordial_amplitude.py
```

Skript 64 sa zámerne skončí nenulovým návratovým kódom, kým tesná
`k`-konvergencia zostáva nad prahom. Ide o zachovaný výsledok
`REQUIRES_NUMERICAL_REVIEW`, nie o zlyhanie spustenia.

## Prostredie rozhodujúcej K5 brány

```text
OS       Windows 10.0.26200
Python   3.11.3
CAMB     1.6.6
NumPy    2.4.6
```

## SHA-256 skriptov

| Súbor | SHA-256 |
|---|---|
| `scripts/21_script_A2_barotropic_fuel_gradient_instability.py` | `D620AFDB6C0175D5AAC593131ABEDE2036090D8C04B53AEB540B1E5B91A04817` |
| `scripts/23_script_A2_K1_superhorizon_velocity_instability_converged.py` | `6AD94F01C7FCDDFB0C4481AC2003EEA0202481DB484C28572215287E92535FC6` |
| `scripts/24_script_A2_K1_equation_sign_and_null_limit_audit.py` | `2D95E4DFB7FDCAB632B22C1080B3AE9BEF1A487B2B2720E92CEC7EEACEAC7FCE` |
| `scripts/25_script_A2_K3_superhorizon_velocity_instability.py` | `7AECD362FE7106114D737163A70DD9AC059A4158E4465F8023CDB8FEFF6C1C9F` |
| `scripts/26_script_A2_K3_equation_sign_and_null_limit_audit.py` | `F41560EC69C75CF5FB1D60F0F659F0B348BEBE683FBAF1C3A24E54379E39FA7C` |
| `scripts/27_script_A2_K4_equation_sign_null_and_eigenvalue_audit.py` | `7D416EAAFD149D9D046D3372126D7B6126C9D92DC4EE0697E1C8C67FCA6D58AB` |
| `scripts/30_script_A2_K4_full_superhorizon_relative_mode_converged.py` | `1225473EA0302E12682A3DA4CDDF279941CE45AA901772E6F44745225F28DC4A` |
| `scripts/63_script_A2_K1_K5_retrospective_depth_equation_verdict_audit.py` | `42E6E408D8B38740A37054B3CEBE8EA711E265908EC7B80A9DC47E22E2760A78` |
| `scripts/64_script_A2_K4_retrospective_adiabatic_convergence.py` | `2B37184273374F78EC641EF184D3F690AFE05D1CAF1D65D97CAC5B0E2FD9A694` |
| `scripts/45_script_A3_K5_K1_CAMB_anchor_and_growth_bound.py` | `F0DE5BD1C801F86441F03861F1539980FB1CA36552D82E2D16BF9F2FF873689A` |
| `scripts/46_script_A3_K5_K1_required_primordial_amplitude.py` | `9F86BF5B35D66C96E9BD46A6242F6D4104977AE9FFADA1166991B2AC0B03DD15` |

## SHA-256 dokumentov

| Súbor | SHA-256 |
|---|---|
| `Audit/A2_K1_K5_RETROSPEKTIVNY_AUDIT_MAX_HLBKY_ROVNIC_VYPOCTOV_A_ROZSUDKOV.md` | `D5F04C1C3C7913F5DE838F79A9CBF314CC58F3D17C0624E54922D4A026BC38D5` |
| `Audit/A2_K1_K5_NUMERICAL_OUTPUT_63_64.md` | `0BDFC637281086D5693254883D26898929EB53ECBE507C84ECBCACDC836CA48E` |
| `Audit/ERRATUM_M011_K4_REFERENCE_GAIN_VS_ABSOLUTE_TRANSFER.md` | `9F5B07952129528DCF249CCB70FC3D33955E9BC0871D8B1323B933B282D18DB7` |
| `Audit/A2_K1_K5_KANONICKY_STAV_A_MAX_HLBKA_PO_RETROSPEKTIVE.md` | `B0FC4B2379E6EB2FF4416C2B81DC4ABA2C9A35C52D7E3083B37F55837BEF4F4E` |
| `Audit/REGISTER_MRTVYCH_KOLAJI_ADDENDUM_RETROSPEKTIVA_M011.md` | `CC5DD7C08CC1E3D34D517D3DB15B9C14DFE2FBBDE8F88F2F925F6BB8E5B4143F` |
| `Audit/A2_KATALOG_STAV_SKORE_A_DOVOD_SMRTI_K1_AZ_K11.md` | `C865F65CF536CEFDDC2FE00AFA9F20D9353105DE08088368B4728E38D0991767` |
| `Questions/A2_K1_K5_STAV_A_DALSI_POSTUP_PO_RETROSPEKTIVE.md` | `594B4EB26CECE40190D9E506346DF66EDF6556E4F652F9AD9CA13AB84BB17D57` |
| `Questions/A3_STAV_A_AKCNY_PLAN_PO_K1_K5_RETROSPEKTIVE.md` | `8E5CF5EFF75F07A7AB691A1BCEE89396305389A8A376FD719772CD28C0CA917B` |
| `Questions/00_READ_FIRST_A2_Q20_CURRENT_STATE_AFTER_K1_K5_RETROSPECTIVE.md` | `8A1B63A8E7A551B21FE1922137B38AE69540BE652AC9A51C008499C03CE76D3B` |
| `Questions/00_READ_FIRST_A2_Q20_CURRENT_STATE.md` | `B90B41582FC97B4FA9C615507D4A764D9D6BD38224AA123AA057307FA309BC4F` |
| `theory/SK/05x_Methodology_Rules_and_Question_Register_A2_K1_K5_Retrospective_SK.md` | `75217FC10212301D7EB2C28A4B2AA7185B03530A3FFC4D4935ABB9CB6FD09278` |
| `theory/EN/05x_Methodology_Rules_and_Question_Register_A2_K1_K5_Retrospective_EN.md` | `1A512885F9C5AB1331817C323466F81EEC1357C42D1F0F842496844E972697BB` |

Hash tohto manifestu sa má pridať až do nadradeného release manifestu, aby
nevznikla sebareferencia.

