# A2-K5.1 — reprodukčný manifest, verdikt a nové koľaje

**Dátum:** 2026-07-13  
**Koľaj:** A2-K5/K1  
**Verdikt:** `PREŽÍVA A2-K5.1 — 60/100; A3 RASTOVÁ BRÁNA ČERVENÁ`  
**Nové ID smrti:** žiadne; M-012 zatiaľ nevzniká

## 1. Rozhodovacie výsledky

```text
equation/null checks = 13/13 PASS

relative superhorizon mode:
  coupled transfer = 6.977880288e-6
  lambda=0 transfer = 1.469347225e-5
  coupled/null gain = 0.474896619
  global 00 residual = 1.47543e-9

adiabatic mode:
  max generated relative ratio = 9.44204e-8
  global 00 residual = 1.21728e-10
  step difference = 2.86030e-7

full/QS coefficient differences = 0.0
Geff/G today = 5.5654 to 5.6735 for q=30 to 300

delta->0 limit:
  beta proportional delta^(-1/2)
  varphi_x proportional delta^(+1/2)
  beta varphi_x constant to spread 1.11e-16
```

## 2. Povinne zachované neúspešné behy

| Skript | Stav | Dôvod | Nástupca |
|---|---|---|---|
| 38 | exit `1` | zdvojené `X_f` v skalárnej entalpii; 00 rezíduum `0.1066` | 39 |
| 40 | exit `1` | krokový rozdiel `1.1441e-6` nad prahom `1e-6` | 41 |
| 43 | exit `1` | neexportované API; `AttributeError` pred fyzikálnym výpočtom | 44 |

Skripty 39, 41 a 44 nemenia fyziku ani rozhodovacie prahy. Presné opravy sú
v troch súboroch `ERRATUM`.

## 3. Analýza úmrtí a nové koľaje

Spoločné korene smrti/rizika sú:

1. malá entalpia `rho_f+p_f=delta rho_f` vo fluidnom prenose hybnosti;
2. záporný barotropický gradientový člen;
3. konštantný neskorý tok;
4. dvojzložkový ledger bez nosiča;
5. uzamknutie backgroundového toku s príťažlivou piatou silou;
6. zámena backgroundového fitu za perturbačný dôkaz.

Nové alebo spresnené smery v poradí sú K5/K3a, K5/K4a, K5/K2a, K5/K6 a
nová backgroundová vetva A1-K2/A2-K6a. Definície a vstupné steny sú v
`Questions/A2_nove_kolaje_po_analyze_pricin_smrti.md`.

## 4. SHA-256

| Súbor | SHA-256 |
|---|---|
| `scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py` | `7FB9E3BF82ABE1A1985E426AA37F00B40329EEA9781B4334B20359A99898BA6E` |
| `scripts/33_script_A2_K5_K1_quasistatic_growth_gate.py` | `D05F7A548D9E4050102A8EAB298F83059AD164C55F284CD0FCB4C0D3721337C3` |
| `scripts/37_script_A2_K5_1_action_equations_sign_null_audit.py` | `BF6EC14A2FFD89F6F36DB55A7C843D5106BA639CC466EFD4290F371C12761566` |
| `scripts/38_script_A2_K5_1_full_superhorizon_relative_mode.py` | `6B1CC10440C233327658C4804FBF736CF71C8F2E538B63695D0DF3DAED7BB4D5` |
| `scripts/39_script_A2_K5_1_full_superhorizon_relative_mode_enthalpy_fixed.py` | `2F2B4FE75EDDF48FDE8EC3F8E584A4F81E6297A7A16735617E4539CB9438F0C5` |
| `scripts/40_script_A2_K5_1_regular_adiabatic_mode.py` | `9F62A3DFA02B9FB2BA6D3AC4C80D624C4443625F6B753A93006CDC73D48E2A8B` |
| `scripts/41_script_A2_K5_1_regular_adiabatic_mode_converged.py` | `A4EBF8E8993FA246ED09E3F4342F72A0CA8BF5FF523C8EF1CE435123011FA694` |
| `scripts/42_script_A2_K5_1_quasistatic_limit_crosscheck.py` | `34349C68E65CDD3846EA52E1EA7365AAFD8BE6734853ECDFEDB07BCB5FA94C84` |
| `scripts/43_script_A2_K5_1_delta_zero_singular_limit.py` | `8AF163FBD4C005FC1ACD0C66E2E17E41BA41F962DFFCFA1F99D735B68D5F5B83` |
| `scripts/44_script_A2_K5_1_delta_zero_singular_limit_fixed.py` | `27FD67F2814594772596D5D06BB96CA5D4DC303C6AF3E599C220737B1B4003B5` |
| `scripts/ERRATUM_38_39_A2_K5_1_SCALAR_ENTHALPY.md` | `50A56EB41B4556641EB0D265E3A8174565D301411F807C73498A0294D6132AE9` |
| `scripts/ERRATUM_40_41_A2_K5_1_ADIABATIC_CONVERGENCE.md` | `11201829257981CFB3DB6E1F0370B005486A5B1A69B265F5206F73EEF37FA451` |
| `scripts/ERRATUM_43_44_A2_K5_1_DELTA_LIMIT_API.md` | `DDAAFA5B019E7ECDFF5AD61BC4413E3D8DE14D301C803EDF9FBAE42B3EA4905E` |
| `scripts/README_AUDIT_SCRIPTS_37-42.md` | `08CACD0F5B736CA83DA29D4FF81BD817F80ECBC3D9E03B1CF55F18F888249D6D` |
| `scripts/OUTPUT_A2_K5_1_37-42.md` | `278D21734D94E44D632FB1A9B66B59F7056349E9C226E4C372EF5E0F550AFBAE` |
| `scripts/README_AUDIT_SCRIPTS_43-44.md` | `B7FCBBC9D08E727B7937DB60FDEF6D0960774870B0F3CEC2D7C0A0C047EB5D71` |
| `scripts/OUTPUT_A2_K5_1_43-44.md` | `2497FA0628D5F5C6E6F9C16467289124BD75193AAD652D9075A2C922C4A17A9F` |
| `Audit/A2_K5_1_uplne_relativisticke_perturbacie_a_superhorizontovy_test.md` | `5DD3064AA7C2DA0C51DB06F92355699E69F6D4884607E0F7D6456BDCB3447F03` |
| `Audit/A2_analyza_hlavnych_pricin_smrti_kolaji.md` | `669816EA7B52C0A0AF02BF9D7B725C6FA9E7104896DEB67267654E501E141439` |
| `Audit/00_READ_FIRST_A2_AFTER_K5_1.md` | `5B4F048AAFCEA4D66B888DA17C7F783A5A654A4FAC15C1C2225130A92D9573E2` |
| `Questions/A2_nove_kolaje_po_analyze_pricin_smrti.md` | `F06AF4503C4F7FC32F8D8676972F4A1A4ADD5F8E75E9E6249CA71433CF787E8F` |
| `Questions/A2_STAV_A_AKCNY_PLAN_PO_K5_1.md` | `70D7E8952F2D4C8B68D2076A0B9416F525C3968380F588DB427C9E162370C389` |
| `Questions/00_READ_FIRST_A2_Q20_AFTER_K5_1.md` | `B9B8D18C0BEC9998E17C2B891791099FAF6414FA9793947F0E97DDCCE1D7EC3F` |
| `theory/SK/05h_Methodology_Rules_and_Question_Register_A2_K5_1_SK.md` | `255DC84147C31AFE4E9ADE50561950F444F2DC0318561A45C12B3AB5A8547936` |
| `theory/EN/05h_Methodology_Rules_and_Question_Register_A2_K5_1_EN.md` | `076E52F62E3B42B6BB4121F6059786C9C58E9210FFFAB0CF8BFAA74A6E67714B` |

Hash tohto manifestu sa zapisuje v samostatnej pečati, aby nevznikla
sebareferencia.

## 5. Nasledujúci rozhodovací krok

Najprv A3-K5/K1: plná CLASS/CAMB implementácia a CMB-normalizované spektrá.
Súčasne je pripravená definícia nasledujúcej akčnej koľaje K5/K3a, ale nesmie
sa použiť na tiché zachraňovanie K5/K1. Každá koľaj dostane vlastný parameter
ledger, skripty a rozsudok.
