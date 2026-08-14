# A2-K5.0 — reprodukčný manifest a stav K5/K1

**Dátum:** 2026-07-13  
**Koľaj:** A2-K5/K1  
**Verdikt:** `PREŽÍVA IBA K5.0 — 45/100; RASTOVÁ BRÁNA ČERVENÁ`  
**Nasleduje:** A2-K5.1 — úplné relativistické lineárne perturbácie

## 1. Rozhodovacie výsledky

```text
Q reconstruction max error = 6.66e-16
ln A mass-identity max error = 5.06e-9
beta_0 = 1.528833197434
massless Geff/G today = 5.67466189115
min mphi^2/H0^2 = 2.66242555419
min meff^2/H0^2 = 21.5384259282
weighted matter growth ratio = 1.051965 to 1.053042
diagnostic projected S8 = 0.919943 to 0.920885
all scripts 32-36: compile=0, run=0
```

Kladné hmotnostné štvorce sú iba backgroundovou tachyonickou bránou. Rast a
`S8` sú kvázistatická diagnostika, nie CMB-normalizovaný likelihood.

## 2. Zachovaná oprava bez mazania histórie

Skript 34 zostáva zachovaný. Vypočítal obe asymetrické šírky KiDS správne,
ale širšiu hodnotu `0.021` pomenoval nejednoznačne ako konzervatívny
„high-side“ výsledok. Skript 36 superseduje iba názvy:

- horná formálna šírka pre model nad centrálnou hodnotou je `+0.016`;
- `0.021` zostáva iba konzervatívna širšia mierka.

Žiadny z pomerov nie je platná likelihoodová signifikancia. Pozri
`scripts/ERRATUM_34_36_A2_K5_K1_KIDS_ASYMMETRIC_LABELS.md`.

## 3. SHA-256

| Súbor | SHA-256 |
|---|---|
| `scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py` | `7FB9E3BF82ABE1A1985E426AA37F00B40329EEA9781B4334B20359A99898BA6E` |
| `scripts/32_script_A2_K5_K1_canonical_scalar_reconstruction.py` | `F062F471E14295EE74E1D224D6235173279A2582984A65173A8CABEC79E2CDF4` |
| `scripts/33_script_A2_K5_K1_quasistatic_growth_gate.py` | `D05F7A548D9E4050102A8EAB298F83059AD164C55F284CD0FCB4C0D3721337C3` |
| `scripts/34_script_A2_K5_K1_weighted_matter_growth_and_S8_projection.py` | `49EA3776128CF49107D03502ABC1CCB77E8DF8AFC60EFB92AE5EA693D34CB409` |
| `scripts/35_script_A2_K5_K1_mass_stability_crosscheck.py` | `9D7D79B8EB4011D92ED8257E7010064055D71628FA1DD55EFFB0C4BDE5B70138` |
| `scripts/36_script_A2_K5_K1_weighted_matter_growth_and_S8_projection_corrected_labels.py` | `FDF4CCE10CEE607803B9D3DD7FA2F6C20E3E610B0EBBC9065ED02FF4809485A6` |
| `scripts/ERRATUM_34_36_A2_K5_K1_KIDS_ASYMMETRIC_LABELS.md` | `2ECA667B2234C01C7EB882D7E0DEE465B25B8C86F67B630C23B3F666AC396E5C` |
| `scripts/README_AUDIT_SCRIPTS_32-36.md` | `01373A99FEE794DDFDCD6246A9ADFA2BD68CE037B53F7B1F69053C32F725E5B4` |
| `scripts/OUTPUT_A2_K5_K1_32-36.md` | `0AE49158A9963A48526A4D3CBEED912315F643DCCA31C3CE2B2D53B36D941049` |
| `Questions/00_READ_FIRST_A2_Q20_CURRENT_STATE.md` | `3951CF96B46D511B9D411F2B85D016FAB10A801EE56602A77F011C303B8D018D` |
| `Questions/A2_K5_problem_mikrofyziky_a_kolaje.md` | `1C84460BF87FF4E3B698703B46272CC47B9368CC9D8B882A06A88D8B9309B12D` |
| `Questions/A2_K5_STAV_A_DALSI_POSTUP.md` | `B691F11B25F5D282E6A3E9B04956EE604175EB7D468048454DB73A295E0E9644` |
| `Audit/A2_K5_00_canonical_scalar_action_reconstruction_and_growth_risk.md` | `E950FFCE32C21993D25FFD114B4A1AD40AECECFD820A1CAF930500636602FC80` |
| `Audit/00_READ_FIRST_A2_K5.md` | `523A840DE24DA7E6A0BEF85E4E33C99E7076F4B64ABEDAE38B5E8FCF0D9B55B7` |
| `theory/SK/05g_Methodology_Rules_and_Question_Register_A2_K5_00_SK.md` | `90B2A52327F0696369A9B7C1425204875CD6A732D0B2ADEC5258E375E6A71B75` |
| `theory/EN/05g_Methodology_Rules_and_Question_Register_A2_K5_00_EN.md` | `48C4FE3D64A4E90E72EF44AF804023DE8E181F3C15AAAF862A8D8AE26BEA31BE` |

Hash tohto manifestu sa má zapísať v nadradenom release manifeste, aby
nevznikla sebareferencia.

## 4. Stavová interpretácia

K5/K1 zatiaľ neporušila lokálnu kovariantnosť, celkové zachovanie energie a
hybnosti ani testované ghost/gradient/tachyonické podmienky. Nemá však
pozitívny rastový výsledok: tá istá väzba, ktorá vytvára žiadaný background,
vytvára aj silnú príťažlivú piatu silu.

Koľaj sa neoznačí za mŕtvu iba na základe kvázistatickej projekcie. A2-K5.1 a
plná CMB normalizácia majú predregistrovanú povinnosť rozhodnúť, či vznikne
`MŔTVA M-012`. Ak áno, tento balík ani jeho skripty sa nemažú.
