# A2-K4.3b skripty 73–76 — manifest a SHA-256

**Dátum:** 2026-07-14  
**Kanonický rozsudok:** `K4.3b NEUZAVRETÁ; A2-K4 ŽIVÁ 60/100`  
**Nový dôvod smrti:** nevydáva sa

## Verifikačný súhrn

- skript 73: execution PASS, 18/18 kontrol;
- skript 74: nulový CAMB rekombinačný interface PASS, 8/8 kontrol;
- skript 75: zachovaný auditný FAIL pre nezamenené aliasy `J2/G2`;
- erratum 75: fyzikálny FAIL nevydaný;
- skript 76: 22/22 exact CAMB symbolic koeficientov s rezíduom `0`;
- syntax skriptov 73–76: PASS; po TIMEOUTe hromadného príkazu boli 75 a 76
  overené osobitne, pričom 73 a 74 už prešli skoršou syntaxovou kontrolou;
- hromadný hash/syntax príkaz bol po 15 s ukončený ako technický TIMEOUT;
  všetky hashe sa následne získali v troch dávkach s limitom 10 s.

## Súbory

| Súbor | Bajty | SHA-256 |
|---|---:|---|
| `scripts/73_script_A2_K4_3b_hierarchy_and_regular_mode_taxonomy_audit.py` | 12664 | `efe2795778be9b0511a982330ce40117cf945063bb598ac229491bbcded5b070` |
| `scripts/74_script_A2_K4_3b_CAMB_recombination_interface_reference.py` | 6031 | `3c7c9187da8bf2a9cde5d5a2ca386f273267b4168ffa55d10aa8c27783ebffdd` |
| `scripts/75_script_A2_K4_3b_exact_CAMB_hierarchy_coefficient_crosscheck.py` | 4130 | `1ad8b2b59efd649d089e6adbd38f850eae09b77cd8c70a5e996ab8509a56c228` |
| `scripts/ERRATUM_75_A2_K4_3b_CAMB_L3_ALIAS_MAPPING.md` | 997 | `77e29d8832e1becf77a2655b35521967c2e16ee2572afe54423af9a1a3d55ef9` |
| `scripts/76_script_A2_K4_3b_exact_CAMB_hierarchy_coefficients_alias_fixed.py` | 4325 | `e65aca51fad0c37f5688ad83610df65dedc46b4729091927207569a5527f382f` |
| `scripts/OUTPUT_A2_K4_3B_73_74.md` | 4141 | `00bac0c9481602d50b9cbc21a86b566bfe3755226d7899de05be22a4d41b22e1` |
| `scripts/OUTPUT_A2_K4_3B_75_76.md` | 1611 | `c4aebefb5265031ca3fc4eed7e3755d3d17a21f360434a76e6761850acf64c87` |
| `Audit/A2_K4_3B_HIERARCHY_MODE_TAXONOMY_RECOMBINATION_AUDIT.md` | 10089 | `8b1b336553f821f37fe9eb64c142a50eeac355b7605825244470ab2abedf846d` |
| `Audit/A2_K4_3B_EXACT_CAMB_COEFFICIENT_CROSSCHECK_ADDENDUM.md` | 996 | `78efb34746662ca616898ff7228c682150a654dc170ccb2175e610f8fe45c141` |
| `Audit/A2_K4_3B_SCORE_AND_K4_1_SCOPE_ADDENDUM.md` | 1510 | `5e6ac30b3707e920a80386a7f7e0b9157e294b01dab3a2555b572575d052d554` |
| `Questions/00_READ_FIRST_A2_Q20_AFTER_K4_3B_73_74.md` | 1573 | `b88f92f4466427c084aa06512eb3da094370a00e94a5d8fb70f84023573100f4` |
| `Questions/A2_K4_3B_STAV_A_DALSI_KROK_PO_73_74.md` | 1465 | `bb53dd5d029177702c9a696a9a08923582d9bc7cd76cfb70094cc0ec0a1279b9` |
| `theory/SK/05zzzzz_Methodology_Rules_and_Question_Register_A2_K4_3b_SK.md` | 2427 | `ef6a851df8cc90bfa611c0d9e5cf4962993921f1882961f1f9d7ef0380564e59` |
| `theory/EN/05zzzzz_Methodology_Rules_and_Question_Register_A2_K4_3b_EN.md` | 2338 | `823fe9e1eedc900e833ad4f27f4172aaf9e70b07df560aaeba0350b1ee19ff8a` |

## Nemennosť

Pôvodný skript 75 a jeho nesúlad sa nemažú. Budúce K4.3b-RG skripty musia
dostať nové čísla, výstupy a nový manifest alebo explicitný changelog.

