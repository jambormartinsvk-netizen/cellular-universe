# Register vlastníctva zdieľaných modulov

**Snapshot:** `BASE-OWNERSHIP-2026-07-30-07`  
**Pravidlo:** jeden modul má jedného vlastníka; ostatné koľaje ho iba
odkazujú. Hash identifikuje presnú revíziu, nie fyzikálny PASS.

## Fyzikálne moduly

| Modul | SHA-256 | Vlastník | Importujúce runnery | Stav/dosah |
|---|---|---|---|---|
| `a2_k4_g8/structural.py` | `162DD5B88E3B78F27F8AC6CC40B46FD42FE86A8852FD6FF4423A6CC937B8EAEF` | A2-K4/C7/K7/G8 | 221 | historický štrukturálny screen |
| `a2_k4_g8/structural_pf034.py` | `E3E0FF899F07BD3EEE0ECA487D1EED9D243CA61E0BF6838F7EC95CB2771B005B` | A2-K4/C7/K7/G8 | 233 | PF-034 oprava; historický scope |
| `a2_k4_g8/s2_tca_direct.py` | `2BAC33B24B365A4DCD1C3913F9A94F9F519E0D58C6528B26C688D2FAC3197E79` | A2-K4/C7/K7/G8 | 222 | starý TCA screen |
| `a2_k4_g8/s3_hierarchy_sweep.py` | `2F579CE54FCE7AABEE1FE9794E7E8D3C2299CAB5FD67470B60580CA8B61D4B04` | A2-K4/C7/K7/G8 | 223 | starý hierarchy sweep |
| `a2_k4_g8/background_universality.py` | `EB3B1F3A5FB39982723E9DD2B9DD12F9A9106977DA31A1557A8FB25BF34ADBC3` | A1-K1/P4 | 224 | audit fixed-`K_MPC`; výsledok obmedzený P4/P5 |
| `k_mpc_005/af_from_a1_background.py` | `72B750EE5ECA77122389841021A80433DD6C417778BF23C768FF51417A80C8E1` | A1-K1/P4 | 234, 235, Q22A-255 | presný A1 background helper; `A_f` pôvod REVIEW |
| `p5_general_synchronous/coefficient_identities.py` | `CE5E9465F48B32AE5823C9697BF90F0027A64C4992CF452EBB657D4917629FBD` | A2-K4/P5.1 | 236 | formulačný P5.1 scope |
| `p5_general_synchronous/constraint_identities.py` | `51EF807412940D8FAE9DBC77613F952124294487E767A2250D1E01DA38400C6E` | A2-K4/P5.2 | 241 | štrukturálny constraint scope |
| `p5_general_synchronous/adiabatic_seed_identities.py` | `C96F67996B5DDB22AF61150E591524A9379A55D9C974A336445794D672D7BD32` | A2-K4/P5.3b | 243 | leading-radiation seed scope |
| `p5_general_synchronous/photon_tca_first_order.py` | `1CAA5A3520378894E5A1DABA512D658B4AABC42D90327CD107E960F392695BC1` | A2-K4/P5.3g4 | 255-KMPC | prvý TCA koeficient; nie plný seed |
| `p5_general_synchronous/early_opacity_ledger.py` | `F35B2D0DBA10E32CE7B9FD29970201464867CC138E0E068DDC4CAF4E7FFAB13A` | A2-K4/P5.3g5 | 256-KMPC | skorý opacity/Einstein formula scope |
| `p5_general_synchronous/mode_resolved_puiseux.py` | `5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE` | A2-K4/P5.3g7-M3 | 261-KMPC-022/023 | exact k-cancel a 11-zložková diagnostika; `V1_INCOMPLETE_FUEL_STATE / DO_NOT_USE_PHYSICS` |
| `p5_general_synchronous/mode_resolved_puiseux_v2_m1_anchored.py` | `5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455` | A2-K4/P5.3g7-M3 | 261-KMPC-024 | `M1_ANCHOR_ONLY`; úplný M3 REVIEW, PF-059 guard obmedzenie |
| `p5_general_synchronous/full_ra_m3_seed.py` | `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` | A2-K4/P5.3g7-M3-FULL/R-A | 271–274 | frozen physics base; KMPC-030 numerical sentinel complete, support-tail semantics REVIEW; bez P5.3/K4 verdictu |
| `p5_general_synchronous/full_ra_m3_seed_attempt9_refinement.py` | `A8E2EA26B6960F23298259EFBECFFC9806ECF10F0207AE4D2B2AD0C2713DA0AB` | A2-K4/P5.3g7 technical audit | 274-KMPC-030 | presne jedna numerická korekcia a no-equation ladder audit; immutable výsledok SHA `8CB706...3C6F` |
| `p5_general_synchronous/full_ra_m3_seed_attempt10_tail_provenance.py` | `A7C06D4C16AF5429319DFF307ADB4A2FCF72542AA65E92B1D6EA1B229387CA55` | A2-K4/P5.3g7 technical audit | 275-KMPC-031 | no-solve added-tail provenance; J4 support PASS iba AD/k=.05/nominal; ARCH-A closed 10/10 |
| `p5_general_synchronous/s1_collective_contract.py` | `F535EE15137BBD6F9C0379821C9CC94DED8EC56037B6105B75BEF65A5884EE68` | A2-K4/P5.3g7/S-C0 contract | 276-KMPC-032 | nezávislý ordered mode/support/moment contract; bez solvera a bez fyzikálneho PASS |
| `p5_general_synchronous/s_c0_coefficient_passport.py` | `C370B610815AFAC345C990E3CFE516D616873F39598F468A5ADBF2C65A2A6B95` | A2-K4/P5.3g7/S-C0 passport | 276-KMPC-032 | PF-069 `DO_NOT_RUN_AUDIT`; conditional algebra zachovaná, physics not reached |
| `p5_general_synchronous/s_c0_coefficient_passport_v2_numpy_scalar.py` | `06EE03C939FBCCFA6FA130421EEF98D0B8CC7571937EF02A7A46A57367534C11` | A2-K4/P5.3g7/S-C0 PF-069 overlay | 277-KMPC-033 | scalar-only oprava; scoped PASS result SHA `4CED9D...CFE8C`; equations/weights/supports/thresholds unchanged |
| `p5_general_synchronous/cdi_c1_coverage.py` | `D57CA8CA5571A07440A987F4FB0DDA08A40DAF7EA8C95AF929FC5C936F2FCE0F` | A2-K4/P5.3g7/CDI-C1 | 278-KMPC-034 | no new equations; immutable SHA `37FB44...DCE20`; vtedajší `[0,3]` remainder open neskôr KMPC-035 obmedzil na insufficient/REVIEW |
| `p5_general_synchronous/cdi_support_ladder.py` | `A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068` | A2-K4/P5.3g7/GLOBAL_C1-CDI-support-step-2 | 279-KMPC-035 | executed immutable SHA `A9BD519F...E42A01`; scoped core/common PASS, `[0,3]` remainder REVIEW; no new equations |
| `p5_general_synchronous/m1_order7_provenance.py` | `0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7` | A2-K4/P5.3g7/GLOBAL_C1-M1-order7-provenance | 280-KMPC-036 | immutable result SHA `39BB3886...B7B497`; scoped PASS + terminal power7 precision REVIEW; no new equations |
| `p5_general_synchronous/m1_order7_numerical_refinement.py` | `CE29222FCE45DAA99A7B8E1FFCC06E9471D648A2B61C14DA05F653DBA9E7A80C` | A2-K4/P5.3g7/M1-order7-boundary V1 | 281-KMPC-037 | PF-072 `DO_NOT_RUN_TECHNICAL`; immutable failure, same-matrix design preserved |
| `p5_general_synchronous/m1_order7_numerical_refinement_v2_householder.py` | `81D7EA664677158E98340E39F395DE2EE0DAB6EEFCFFA785089F51E62434193A` | A2-K4/P5.3g7/M1-order7 Householder overlay | 282-KMPC-038 | PF-073 `DO_NOT_RUN_TECHNICAL`; zero-tie formula, wrong runtime owner |
| `p5_general_synchronous/m1_order7_numerical_refinement_v3_context_owner.py` | `1E35D147049F981F901B9A2B72C76EBE5705F5D19A04447E742AE978A9BC5278` | A2-K4/P5.3g7/M1-order7-boundary V3 | 283-KMPC-039 | result SHA `BDF331...CE016`; authoritative same-matrix numerical boundary PASS |
| `p5_general_synchronous/cdi_support_step3.py` | `79677797314CA8D5E5D8622ED55A07E083953D1049DA164E9871D8E97C4FFD87` | A2-K4/P5.3g7/GLOBAL_C1-CDI-support-step-3 | 284-KMPC-040 | result SHA `69C78F...BD219`; `[0,5]→[0,7]` scoped CDI `.05/nominal` PASS; no `[0,9]` |
| `p5_general_synchronous/bi_c1_coverage.py` | `303515C80945905BFC537B8FFDB94F1F126B73EB939679D46A95DD4BDE384BF6` | A2-K4/P5.3g7/GLOBAL_C1-BI | 285-KMPC-041 | result SHA `8BB006...AE183`; core/common PASS, primary `[0,1]` insufficient; BI step 2 next |
| `p5_general_synchronous/bi_support_step2.py` | `08A8071D5D3DC8A1A0D58CB76CAF08548ADC6D85F067D51151CE78129CC1F19F` | A2-K4/P5.3g7/GLOBAL_C1-BI-support-step-2 | 286-KMPC-042 | result SHA `E5F18D...8CA61`; `[0,3]→[0,5]` core/common PASS, tail REVIEW; BI order-7 next |
| `p5_general_synchronous/bi_m1_order7_provenance.py` | `69C65F408635E71B455FBF2135FB5057E0DA01B8E4895B5B5D96733AC4AF03C2` | A2-K4/P5.3g7/GLOBAL_C1-BI-M1-order7 | 287-KMPC-043 | result SHA `B02D1D...61EB0`; BI structural/lower PASS, driver+holdout precision REVIEW; same-matrix closure next |
| `p5_general_synchronous/bi_m1_order7_numerical_boundary.py` | `FBB920976CAF5FAF2DDA87D1286573E91155A0688C23EB8E2A5AB0EE3B70BFAD` | A2-K4/P5.3g7/GLOBAL_C1-BI-M1-order7-boundary | 288-KMPC-044 | result SHA `C3BD73...F1C36`; same BI matrix, one correction + one 80-dps QR PASS; BI support step 3 next |
| `p5_general_synchronous/bi_support_step3.py` | `1ABB16A886432C4A2B908CE802598D4970567030C2E7CCAFE6FA1A37A4C36CC8` | A2-K4/P5.3g7/GLOBAL_C1-BI-support-step-3 V1 | 289-KMPC-045 | PF-074 `DO_NOT_RUN_AUDIT_TECHNICAL`; equations preserved, wrong S-C0 helper owner |
| `p5_general_synchronous/bi_support_step3_v2_owner.py` | `EB434319DA1E07AAE23B2CE76F6287934B941FF5A7835AF9CDE702AECA6E5EDB` | A2-K4/P5.3g7/GLOBAL_C1-BI-support-step-3 owner overlay | 290-KMPC-046 | result SHA `60EC5A...15FB1`; BI `[0,5]→[0,7]` PASS `.05/nominal`; NID next |
| `a2_k11_cs2/full_multispecies_constrained_dae.py` | `19263A674E1F342E06E6D0D3999E65E58687CCFF20E5EE083A05D06D7BB107FF` | A2-K11/K11-CS2-S0 | 262, 263 | `PASS_FORMULA_IDENTITIES_ONLY / STOP_STATE_REGISTER_V001`; PF-062: extra `E_0,E_1`, správne `4l+9`; full propagátor neimplementovaný |
| `a2_k11_cs2/finite_hierarchy_contract_v002.py` | `30610E17EA247B035962439EBF40467F33ACDBAB26298E3CBD47EC57DA48B42E` | A2-K11/K11-CS2-full | 266–270 auditná línia | exact ordered 25/33/41 state/RHS contract; closure metadata výslovne non-exact |
| `a2_k11_cs2/finite_hierarchy_source_ast_preflight_v003.py` | `58385E957E379AA1BFFB6F97453F58DD33682CAB05FFF097C9D8D7DC616B5203` | A2-K11/K11-CS2-full | 269, 270 | pinned CAMB source-AST, attempt 5 autoritatívne 55/55 structural PASS |
| `a2_k11_cs2/full_multispecies_constrained_dae_v002.py` | `NOT_CREATED` | A2-K11/K11-CS2-full | runner zatiaľ nepridelený | rovnaký fyzický suffix; exact-A1 thermal/full DAE, numerický top + konvergencia, regular basis a independent holdouts; ďalší balík ARCH-A 6/10 |
| `release_v318_h0_s8_legacy_sensitivity_dev.py` | `74AE3B0BC31FA1AE4BB9FDB3339C84869DA38131440795BD0C7B2B82677F30D9` | RELEASE/v3.18/PT1_H0/C2-C3 | 393 | V5 RC2 segmented `10+10+9`; DEV 31/31; 9 final grid rawov a dual audit prijaté iba ako sampled conditional legacy sensitivity; `RUN_AUTHORIZED=false`; bez current-K4/G8/G9 claimu |

`a2_k4_g8/__init__.py` má hash
`F4CA236BF250E6EE7F9FCAB6E085737411382B716EABBC3E03964DE7183730C8`;
neobsahuje samostatný fyzikálny claim.

`a2_k11_cs2/__init__.py` má lazy revíziu hash
`C3C739B916745581B8AEA8C698DFA82FFA441A8E9FF7F57FDAEDE32DAEF39391`;
legacy heavy exporty zachováva cez `__getattr__`, aby ľahké contract audity
nenačítavali CAMB/SymPy.

## Globálne nefyzikálne utility

| Modul | SHA-256 | Účel |
|---|---|---|
| `000_extract_pdf_text_bounded.py` | `99CD64089689B914D6AB3163F8641F15BA677E2B1F18820C85230066C2562811` | ohraničená extrakcia PDF textu |
| `001_render_pdf_pages_bounded.py` | `BABD15A5BF2A234B5EFB31A975FEFF2056400C7EE0AB5BC62D40DCAA47440526` | ohraničený Fitz render; známe zlyhanie v HISTORY |
| `002_render_pdf_pages_bounded_pdfium.py` | `C54098FFDDABB5778D13560ECA7C327D0D6FBEFC28FDA1E4DFDB893A14C0ED58` | ohraničený PDFium render |

## Dosah opravy

Pri zmene modulu sa podľa tohto registra vytvorí zoznam všetkých
importujúcich runnerov. Potom sa vyhľadajú ich výsledky a audity v manifeste
vlastníckej koľaje. Žiadny z týchto výsledkov sa neprepisuje; oprava vytvorí
nový runner alebo novú hash/verziu a rozdielový audit.

`__pycache__/*.pyc` sú odvodené súbory a nie sú súčasťou verzie ani dôkazu.
