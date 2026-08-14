# P5 — zdieľané moduly

| Brána | Modul | Runner |
|---|---|---|
| P5.1 | `p5_general_synchronous/coefficient_identities.py` | `236_script_KMPC_003_P5_1_general_synchronous_static_ledger.py` |
| P5.2 | `p5_general_synchronous/constraint_identities.py` | `241_script_KMPC_004_P5_2_full_constraint_ledger.py` |
| P5.3b | `p5_general_synchronous/adiabatic_seed_identities.py` | `243_script_KMPC_006_P5_3b_adiabatic_leading_seed_ledger.py` |
| P5.3g4 | `p5_general_synchronous/photon_tca_first_order.py` | `255_script_KMPC_018_P5_3g4_photon_l2_tca_seed.py` |
| P5.3g5 | `p5_general_synchronous/early_opacity_ledger.py` | `256_script_KMPC_019_P5_3g5_early_opacity_and_einstein_ledger.py` |
| P5.3g7-M3 V1 | `p5_general_synchronous/mode_resolved_puiseux.py` | `261_script_KMPC_022...`, `261_script_KMPC_023...RERUN1` |
| P5.3g7-M3 V2 | `p5_general_synchronous/mode_resolved_puiseux_v2_m1_anchored.py` | `261_script_KMPC_024...RERUN2` |
| P5.3g7-M3 FULL/R-A core | `p5_general_synchronous/full_ra_m3_seed.py`, SHA-256 `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` | attempts 6–10 historicky uzavreté; KMPC-031 uzavrel iba AD J4 sentinel support |
| P5.3g7 S-C0 contract | `p5_general_synchronous/s1_collective_contract.py`, SHA-256 `F535EE15137BBD6F9C0379821C9CC94DED8EC56037B6105B75BEF65A5884EE68` | KMPC-032; nezávislý fail-closed register, bez solvera |
| P5.3g7 S-C0 passport V1 | `p5_general_synchronous/s_c0_coefficient_passport.py`, SHA-256 `C370B610815AFAC345C990E3CFE516D616873F39598F468A5ADBF2C65A2A6B95` | KMPC-032 PF-069; lower moments, physics not reached |
| P5.3g7 S-C0 PF-069 overlay | `p5_general_synchronous/s_c0_coefficient_passport_v2_numpy_scalar.py`, SHA-256 `06EE03C939FBCCFA6FA130421EEF98D0B8CC7571937EF02A7A46A57367534C11` | KMPC-033 scoped PASS; iba scalar conversion RERUN1; result `4CED9D...CFE8C` |
| P5.3g7 CDI C1 coverage | `p5_general_synchronous/cdi_c1_coverage.py`, SHA-256 `D57CA8CA5571A07440A987F4FB0DDA08A40DAF7EA8C95AF929FC5C936F2FCE0F` | KMPC-034/runner 278; executed immutable SHA `37FB44...DCE20`; core/common PASS, `[0,1]` insufficient, no new equations |
| P5.3g7 CDI support ladder | `p5_general_synchronous/cdi_support_ladder.py`, SHA-256 `A8257E2195E2AB61B5C4195B80EA44EE7669B5A52F9C8440BA5F5244190E3068` | KMPC-035/runner 279 executed; immutable SHA `A9BD519F...E42A01`; scoped core/common PASS, `[0,3]` remainder REVIEW; M1 order-7 gate before step 3 |
| P5.3g7 M1 order-7 provenance | `p5_general_synchronous/m1_order7_provenance.py`, SHA-256 `0B1EB4C76A7388D6A8F6D1E5DD933549043337381DEF6DE77539D3F84CA7BAC7` | KMPC-036/runner 280 executed; result SHA `39BB3886...B7B497`; scoped PASS + power7 precision REVIEW; no new equations |
| P5.3g7 BI M1 order-7 provenance | `p5_general_synchronous/bi_m1_order7_provenance.py`, SHA-256 `69C65F408635E71B455FBF2135FB5057E0DA01B8E4895B5B5D96733AC4AF03C2` | KMPC-043/runner 287; BI-local RHS/state, result SHA `B02D1D...61EB0`; structural/lower PASS + driver/holdout precision REVIEW; no CDI correction |
| P5.3g7 BI M1 order-7 boundary | `p5_general_synchronous/bi_m1_order7_numerical_boundary.py`, SHA-256 `FBB920976CAF5FAF2DDA87D1286573E91155A0688C23EB8E2A5AB0EE3B70BFAD` | KMPC-044/runner 288; result SHA `C3BD73...F1C36`; BI same-matrix boundary PASS, bez CDI stavu/korekcie |
| P5.3g7 BI support step 3 V1 | `p5_general_synchronous/bi_support_step3.py`, SHA-256 `1ABB16A886432C4A2B908CE802598D4970567030C2E7CCAFE6FA1A37A4C36CC8` | KMPC-045 PF-074; `DO_NOT_RUN_AUDIT_TECHNICAL`, failure SHA `FFFF06...330C01` |
| P5.3g7 BI support step 3 owner overlay | `p5_general_synchronous/bi_support_step3_v2_owner.py`, SHA-256 `EB434319DA1E07AAE23B2CE76F6287934B941FF5A7835AF9CDE702AECA6E5EDB` | KMPC-046/runner 290; owner-only oprava, result SHA `60EC5A...15FB1`; BI `[0,5]` adequate |

Hashe sa čítajú z jediného registra
`scripts/baseScripts/00_MODULE_OWNERSHIP_REGISTER.md`. Ostatné P5 runnery
zatiaľ obsahujú route-specific algebra alebo mapovanie; pred opakovaným
použitím sa najprv rozhodne, či patrí do nového base modulu.

## PF-058 obmedzenie mode-resolved vetvy

| Modul | SHA-256 | Autoritatívny rozsah |
|---|---|---|
| `mode_resolved_puiseux.py` | `5a89cf82006cb5ecc1d8b4be1fd56a463453ee3d6261968cb64de8ccf2c8b7ae` | presné k-cancel/background identity a historická 11-zložková diagnostika; `DO_NOT_USE_PHYSICS` pre úplný M3 |
| `mode_resolved_puiseux_v2_m1_anchored.py` | `5de2c280b0e9daf528a9e3011368361b37ae53de38827fb6f6ce4ab2019a4455` | tvrdá M1 eliminácia; `REVIEW_ONLY_M3`, PF-059 tautologický identity guard |

Úplný seedový modul bol použitý v historických balíkoch 6–10. Importuje
frozen contract, rieši samostatnú `Phi^0` fuel vežu a viaže sa na frozen
coefficient-wise energy/momentum/Bianchi guard. Legacy V1/V2 sa
neprepisuje; ich frakčný solver sa nesmie volať. Po vecne úspešnom KMPC-031
je `historical_packages_total=10` a aktívny counter po sebe idúcich
technických zlyhaní `0/10`. Ďalší krok nie je attempt 11, ale nový
mode-coverage atóm nad uzavretou architektúrou a kontraktom 51.

PF-063 navyše obmedzuje frakčný pressure/trace scope oboch legacy modulov:
`fuel_pf` má trojnásobnú neadiabatickú časť oproti kovariantne
konzervovanému scriptu 88. Budúci R-A modul nesmie tento výraz importovať;
M1 hard-anchor helper možno preniesť iba s nezávislým frozen hash guardom.

## R-A B1 moduly

| Modul | SHA-256 | Stav |
|---|---|---|
| `full_ra_b1_preflight.py` | `62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D` | algebraický oracle PASS; PF-064 contract guard STOP |
| `full_ra_contract.py` | `F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464` | autoritatívny exact ordered state/driver/holdout contract |
| `full_ra_b1_preflight_v2.py` | `27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C` | `PASS_R_A_B1_CONTRACT_GUARD_ONLY`; importuje frozen algebra a nezávislý contract |

Budúci seedový modul musí importovať `full_ra_contract.py`; nesmie vytvoriť
lokálnu kópiu tuple alebo použiť iba count.

`full_ra_m3_seed.py` túto podmienku implementuje; hash je zmrazený vyššie a
v ownership registri. Historická budúca formulácia z dokumentu 37 bola
splnená pred balíkom 6 a je superseded výsledkami 39–50.

KMPC-032 nemení 13-state solver. `s1_collective_contract.py` vlastní
očakávané supporty a negatívne fixtures; implementácia ich iba importuje.
Vyššie `F_l>=3` coefficient dictionaries sa v tomto balíku nevyrábajú.
