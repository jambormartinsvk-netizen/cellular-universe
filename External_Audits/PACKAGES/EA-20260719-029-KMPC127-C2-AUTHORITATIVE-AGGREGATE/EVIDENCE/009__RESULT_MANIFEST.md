# P5 — manifest výsledkov

Kanonický adresár je `scripts/results/k_mpc_005/`. Súbor
`00_RESULTS_INDEX_P5_SK.md` je podrobný index. Tento route manifest iba
určuje vlastníctvo:

- `RUN_KMPC_003` až `RUN_KMPC_021` patria P5;
- pôvodný `RUN_KMPC_004...json` je PF-041 STOP, autoritatívny je `RERUN1`;
- `RUN_KMPC_020...json` je PF-054 technický STOP, autoritatívny je
  `RUN_KMPC_021...RERUN1`;
- `RUN_KMPC_023_P5_3G7_M3_TCA0_RERUN1.json` je immutable diagnostika
  neukotveného M1, hash
  `4c925d10627a69430f2d3ac59f2609423a8743165d518644ffb1ec9bba869469`;
- `RUN_KMPC_024_P5_3G7_M3_TCA0_RERUN2.json` potvrdzuje M1/štandardný seed,
  ale je iba incomplete-contract diagnostika PF-058, hash
  `0613ad04cfafcb4414247cdc9fecbcbafa1288520eba51fc5bbde7a37b1c3ee8`;
- `RUN_KMPC_025_P5_3G7_M3_FULL_RA_B1_PREFLIGHT.json` zachováva presné
  algebraické nuly, ale celý contract PASS obmedzila PF-064;
- `RUN_KMPC_026_P5_3G7_M3_FULL_RA_B1_CONTRACT_GUARD.json` je autoritatívny
  `PASS_R_A_B1_CONTRACT_GUARD_ONLY`, 9/9 checks a 9/9 negatívnych fixtures;
  nie je seed solve ani fyzikálny PASS;
- `RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_AD_K0p05_NOMINAL.json` je jediný
  vykonaný atóm pokusu 7, SHA-256
  `2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83`;
  rovnice/ranky/holdouty prešli, ale J2/J4 truncation je
  `REVIEW_TRUNCATION_EXTENSION_REQUIRED`; nejde o fyzikálny STOP;
- `RUN_KMPC_029...SUPPORT_J6.json` (SHA `658495...C4636A`) je plnorankový
  support PASS artefakt; `...SUPPORT_J8.json` (SHA `1EE3FC...D51AB8`) je
  numerický REVIEW iba pre driver residual `1.5577e-10`; ladder agregát
  nevznikol a production support ešte nebol udelený;
- `RUN_KMPC_030_P5_3G7_M3_FULL_RA_J8_ONE_REFINEMENT_AUDIT.json` má SHA
  `8CB706223C43EB4E72F2B56BE266C73E07349F2E0D6B32212E280AB64F803C6F`;
  všetkých 22 numerical checks PASS, ale raw independent-solve deep tail je
  `REVIEW_TAIL_METRIC_SEMANTICS`; nejde o P5.3 ani K4 PASS;
- `RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json` má SHA
  `C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6`;
  `PASS_SUPPORT_TRUNCATION_J4_SENTINEL_SCOPE`, iba AD/k=.05/nominal;
- lineage výsledky patria auditnému threadu, nie P5 fyzikálnemu skóre;
- žiadny existujúci výsledok nie je P5.4, G8 ani G9 PASS.
- `RUN_KMPC_032...TECHNICAL_FAILURE.json` má SHA
  `51C7B32B84F498ACD9CEFD7BC72D546D87F1DDCBC4C2BC189A02E1036991EA03`;
  audit zastal na numpy-scalar konverzii pred fyzikálnou identitou. Nie je
  to S-C0 ani K4 verdikt.
- `RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1.json` má SHA
  `4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C`;
  autoritatívny rozsudok je iba
  `PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY`.
  Vyššie multipóly, S-M, CDI remainder/coverage, G8 a skóre ostávajú
  otvorené/bez zmeny.
- `RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json` má SHA
  `37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20`;
  autoritatívne prešiel iba CDI core/common-coefficient scope. Support
  `[0,1]` je nedostatočný a remainder `[0,3]` ešte nebol testovaný.
  Výsledok nemení P5/K4 skóre ani G8.
- `RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json` má SHA
  `A9BD519F9124B80E648EE327A3C2175A5E9DC3D65B02EB1CFD7F119333E42A01`;
  historický token `C2` nie je Fourier C2. Autoritatívny rozsudok je
  `PASS_CDI_SUPPORT_STEP_2_CORE_AND_COMMON_03_05_STABILITY_ONLY /
  REVIEW_CDI_SUPPORT_03_REMAINDER_UNCLOSED`. Pri `z=.01` neprešli iba F0
  `delta_f` a M3 `sigma_fs`; M1 order-7 provenance gate blokuje step 3.
  Výsledok nemení P5/K4 skóre ani G8.
- `RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json` má SHA
  `39BB388669E74C9368BD823C5FF5C68A487B7FC1CD4F74EACBF64D9A08B7B497`;
  regression/shape/rank/anchor/condition/state a všetkých 18 holdoutov PASS,
  ale tri terminal power-7 driver riadky ostávajú precision-floor REVIEW.

- `RUN_KMPC_037_P5_3G7_M1_ORDER7_NUMERICAL_REFINEMENT_TECHNICAL_FAILURE.json`
  má SHA `7F1B5B...315E1`; PF-072, bez fyzikálneho payloadu.
- `RUN_KMPC_038_P5_3G7_M1_ORDER7_HOUSEHOLDER_ZERO_TIE_TECHNICAL_FAILURE.json`
  má SHA `E85E6C...DA64F`; PF-073 smoke, full audit NOT_RUN.
- `RUN_KMPC_039_P5_3G7_M1_ORDER7_CONTEXT_OWNER.json` má SHA
  `BDF3317235FEDEA23EDF8C23563423014F2E98A461C6E638C474DF94471CE016`;
  jeden refinement aj jeden 80-dps same-matrix QR uzavreli `121/121` driver+
  initial a `18/18` holdoutov bez lower/anchor regresie. Autoritatívny verdict
  je `PASS_M1_ORDER7_PROVENANCE_NUMERICAL_BOUNDARY_CLOSED_SAME_MATRIX_ONLY`.
  Support step 3 tým bol odblokovaný; výsledok nemení skóre ani G8.
- `RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07.json` má SHA
  `69C78F70ECD851D8B8A48E4E09445181C0D4559E9BD2E90A7BA19933351BD219`;
  autoritatívne `PASS_CDI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_WITHIN_CDI_K005_NOMINAL_ONLY`.
  Regresie `[0,3]/[0,5]`, core `[0,7]`, common `0…5`, S-C0 a tail obálka
  iba `6,7` prešli; najhorší tail je `8.71681e-9 < 1e-6`. `[0,9]` sa
  nespúšťa; ďalší krok je samostatný BI fail-fast atóm. Skóre a G8 bez zmeny.
- `RUN_KMPC_041_P5_3G7_BI_C1_PRIMARY_EXTENDED_COVERAGE.json` má SHA
  `8BB006EF6606476D85168FBDCD913249E9EDE024C1017473376A33CF4C7AE183`;
  autoritatívne `PASS_BI_C1_CORE_AND_COMMON_COEFFICIENT_STABILITY_ONLY /
  REVIEW_BI_C1_PRIMARY_01_INSUFFICIENT_EXTENDED_03_REMAINDER_NOT_YET_TESTED`.
  Core/S-C0/common `0,1` prešli, ale envelope tail `2,3` zlyhal pre F0 aj
  M3; dokázaná je iba nedostatočnosť `[0,1]`. Ďalší krok je samostatný BI
  `[0,3]→[0,5]`; skóre a G8 bez zmeny.
- `RUN_KMPC_042_P5_3G7_BI_SUPPORT_STEP_2_03_05.json` má SHA
  `E5F18DA4DE5A718C4448D095804F6D41FE88445A95FB99645EFBCCB48D48CA61`;
  autoritatívne `PASS_BI_SUPPORT_STEP_2_CORE_AND_COMMON_03_05_STABILITY_ONLY /
  REVIEW_BI_SUPPORT_03_REMAINDER_UNCLOSED`. Regresia/core/S-C0/common `0…3`
  prešli, ale tail `4,5` pri `.01` zlyhal pre F0 `delta_f` a M3 `sigma_fs`.
  BI `[0,3]` je nedostatočný; ďalší krok je vlastná BI M1 order-7 provenance
  brána, nie priamy `[0,7]`. Skóre a G8 bez zmeny.
- `RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE.json` má SHA
  `B02D1D16CFAE4331378B68F12258142F84A424419BB9D3A52AAEE87D0CC61EB0`;
  autoritatívne `PASS_BI_M1_ORDER7_REGRESSION_SHAPE_RANK_ANCHOR_CONDITION_STATE_ONLY /
  REVIEW_BI_M1_ORDER7_DRIVER_AND_HOLDOUT_PRECISION_BOUNDARY_UNCLOSED`.
  Shape/rank/anchor/condition/lower regresie prešli; formálne zlyhalo 5/121
  driver a 1/18 holdout pri absolute residualoch `4.1e-17…8.4e-16`.
  Nasleduje BI same-matrix closure, nie support `[0,7]`; skóre a G8 bez zmeny.
- `RUN_KMPC_044_P5_3G7_BI_M1_ORDER7_NUMERICAL_BOUNDARY.json` má SHA
  `C3BD732C9F3FB402E4143DA6EF149E6C2830F5F5C96D17D21D314BC5B82F1C36`;
  autoritatívne
  `PASS_BI_M1_ORDER7_PROVENANCE_NUMERICAL_BOUNDARY_CLOSED_SAME_MATRIX_ONLY`.
  V0 reprodukoval 5+1 KMPC-043 odchýlok; jedna korekcia `2.498e-15` a jeden
  80-dps QR uzavreli `121/121 + 18/18` aj spätnú projekciu bez lower/anchor
  regresie. BI support step 3 je iba odblokovaný pre samostatný run; skóre
  a G8 bez zmeny.
- `RUN_KMPC_045_P5_3G7_BI_SUPPORT_STEP_3_05_07_TECHNICAL_FAILURE.json` má
  SHA `FFFF061651A06F3FD097F5C6622C42084643F41D98C2C3B2B0C141A54C330C01`;
  PF-074 wrong S-C0 owner + missing stderr `sys`; bez canonical fyzikálneho
  payloadu, `DO_NOT_RUN_AUDIT_TECHNICAL`.
- `RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json` má SHA
  `60EC5A801FDDBAFFBA6CE184EBB3BC154879928385E6E37FB118781118615FB1`;
  autoritatívne
  `PASS_BI_SUPPORT_STEP_3_SUPPORT_05_ADEQUATE_WITHIN_BI_K005_NOMINAL_ONLY`.
  Regresia/core/S-C0/common a tail `6,7` prešli; worst tail M3
  `8.71681e-9 < 1e-6`. BI `[0,5]` je uzavretý iba `.05/nominal`; bez
  `[0,9]`, skóre a G8 bez zmeny.
- NID lineage `RUN_KMPC_047` až `RUN_KMPC_050` uzavrela fail-fast support,
  PF-075 a order-7 provenance; KMPC-050 vylúčil jednoduchý roundoff, ale
  lokalizoval chýbajúcu M1-depth kompatibilitu.
- `RUN_KMPC_051_P5_3G7_NID_M1_DEPTH_5_7.json` má SHA
  `AF088030BA709F08D40D825B9477C9A84BA330705CDDFB1C12C52B0DD3FC1E5E`;
  M1 depth 7 odstránil Einstein holdout rozpor a zachoval common koeficienty.
  `RUN_KMPC_052...NUMERICAL_BOUNDARY.json` má SHA
  `FDEE962EED16EDF459D7D8504833AB1206AEF1BFC8178A356A88A121CF196C4C`;
  V2 aj V3 uzavreli jediný `fuel_Euler[7]` float64 boundary.
- `RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json` má SHA
  `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD`;
  autoritatívne `PASS_NID_SUPPORT_05_ADEQUATE_AT_K005_NOMINAL`. Regresia,
  refined core, combined-`R_fs`, S-C0, common a tail `6,7` prešli; `[0,9]`
  sa nespúšťa. Ďalší mód bol NIV; skóre a G8 bez zmeny.
- `RUN_KMPC_054_P5_3G7_NIV_C1_PRIMARY_EXTENDED_COVERAGE.json` má SHA
  `0CF322A7BA5964B78BBF9180B29FA8BBBE43A646ECEB05D444B6250568ECFB1E`.
  Core/common/combined-`R_fs` prešli, ale tail `3,4` jasne zlyhal; NIV
  `[-1,2]` je nedostatočný.
- `RUN_KMPC_055_P5_3G7_NIV_SUPPORT_STEP_2_MINUS1_4_MINUS1_6_TECHNICAL_FAILURE.json`
  má SHA `93906783C433800CB9609A7D3F735F01C504840B323EA981E95BDE79CF7576EC`;
  PF-076, bez fyzikálneho verdiktu.
- `RUN_KMPC_056_P5_3G7_NIV_SUPPORT_STEP_2_FINITE_OWNER_SUCCESSOR.json` má
  SHA `9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332`;
  autoritatívne `PASS_NIV_SUPPORT_MINUS1_4_ADEQUATE_AT_K005_NOMINAL`.
  M1 depth 6, core/common/tail aj owner restore prešli; `[-1,8]` sa
  nespúšťa. Ďalší scope je `k×variant` coverage; skóre a G8 bez zmeny.
- `RUN_KMPC_061_P5_3G7_C2_AD_K0p005_NOMINAL.json` má SHA
  `0952AF08B1DE291D015F71396954F70EAE2F78A962E1EE1D3A08ECA48A1F5DCD`;
  autoritatívne `REVIEW_C2_AD_K0p005_SUPPORT_EXTENSION_REQUIRED`. M1,
  accepted/audit core, S-C0, common a background prešli, ale F0/M3 tail
  rádov `3,4` je `2.81e-4…3.35e-2 > 1e-6`. Zvyšných 9 C2 atómov sa
  nespustilo; ďalší krok je AD `[0,4]→[0,6]`; skóre bez zmeny.
- `RUN_KMPC_062_P5_3G7_C2_AD_K0p005_SUPPORT_04_06.json` má SHA
  `640057CB6AC3F059988D6BD6C0CBE65ABAC1712F18961A2FEAFA5E1341EA6760`;
  autoritatívne `REVIEW_C2_AD_K0p005_SUPPORT_06_08_REQUIRED`. Core/common/
  background prešli; tail `5,6` prešiel na `z=1e-4`, ale na `.01` je
  F0 `8.21e-6` a M3 `1.57e-5`. Ďalší je `[0,6]→[0,8]`, depth 8.
- `RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json` má SHA
  `CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD`;
  autoritatívne `PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY`.
  M1/core/common/background aj tail `7,8` prešli; na `z=.01` je F0
  `1.83e-9` a M3 `5.07e-9 < 1e-6`. C2 je `1/10 PASS`; ďalší AD/`.15`.
- `RUN_KMPC_065_P5_3G7_C2_AD_K0p15_NOMINAL.json` má SHA
  `987E467EA2F36EA8F061F665A33AE1F6DC9AB6E2EFE9FB710E23CE0C50171636`;
  autoritatívne `REVIEW_C2_AD_K0p15_SUPPORT_04_06_REQUIRED`. M1/core/
  common/background prešli, no tail `3,4` je už na `z=1e-4` F0 `9.37e-6`
  a M3 `1.09e-5`. Ďalší je `[0,4]→[0,6]`, depth 6; skóre bez zmeny.
- `RUN_KMPC_066_P5_3G7_C2_AD_K0p15_SUPPORT_04_06.json` má SHA
  `81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816`;
  autoritatívne `PASS_C2_AD_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY`.
  Všetky brány prešli; tail `.01` F0 `9.14e-9`, M3 `1.52e-8`. C2 `2/10`.
- `RUN_KMPC_073_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_PHASE_ORDER_SUCCESSOR.json`
  má SHA `B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498`;
  autoritatívne `PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`.
  Common/tail/core aj 13-state production order prešli. KMPC-068/069 sú
  timeout DNR, KMPC-070 checkpoint bez verdiktu, KMPC-071 `DO_NOT_USE_PHYSICS`
  a KMPC-072 smoke DNR.
- `RUN_KMPC_074_P5_3G7_C2_CDI_K0p15_NOMINAL.json` má SHA
  `7771610FC77C2F3AA3FD9EA7D9BDE01F9C9D8F6751AC5BCD1075E67B9FBBB1A0`;
  immutable REVIEW izoloval iba `gamma_Euler[7]` M3 driver
  `3.84414e-10 > 1e-10`.
- `RUN_KMPC_075_P5_3G7_C2_CDI_K0p15_SAME_MATRIX_REFINEMENT.json` má SHA
  `19F5F0B38CFE62C6E2ECA277EE5F959D866967027C5AF721CF4B2E1A30B999B9`;
  autoritatívne `PASS_C2_CDI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.
  Tá istá 104×104 matica po troch corrections znížila driver maximum na
  `1.11499e-16`; všetky brány prešli.
- KMPC-078 BI/k=.005 checkpoint-resume má SHA `F24894A0...18A359` a PASS
  `[0,7]` voči `[0,9]`; M3 tail `.01` je `4.76773e-9`.
- KMPC-080 BI/k=.15 same-matrix raw má SHA `028BE28F...83DD1F`; main driver
  klesol na `1.35219e-16`, ale nezávislý `Einstein_0i[7]` holdout ostáva
  `3.01976e-9 > 1e-9`.
- KMPC-083 80-dps raw má SHA `A8CB50F9...D729C9`; driver tej istej
  float64-zostavenej matice je `9.82e-82`, no nezávislý holdout ostal
  `3.019756782e-9`. Solve-roundoff je vylúčený; ďalší exact-assembly audit.
  C2 ostáva `5/10`.
- KMPC-086 high-precision holdout-assembly raw má SHA `54F9A116...B65649E`.
  Znovuzostavený 16x104 holdout (non-fit) dal `Einstein_0i[7] =
  3.0197567116e-9`, prakticky identicky s KMPC-083. Posledné holdout
  zostavenie/odčítanie teda nie je príčina; ďalší krok je 80-dps assembly
  tej istej driver matice. C2 ostáva `5/10`.
- KMPC-087 high-precision driver-assembly raw má SHA
  `EA0B4403318516D4503379246A882222E64681CB0248A4EFB00F10201CCE2144`.
  Exact 104x104 driver prešiel na `8.72028e-82`; exact holdout ostal non-fit
  a `Einstein_0i[7]=3.0197565776e-9 > 1e-9`. Driver assembly roundoff je
  vylúčený; autoritatívne REVIEW smeruje na binary64 upstream M1/F0/background.
  C2 ostáva `5/10`.
- KMPC-092 coefficient-attribution raw má SHA
  `73C3F00B7969291C7EF89E3FEAB56591D0FDEB8A1D65B0D2050B88360D300606`.
  Úplný 73-term ledger zrekonštruoval `Einstein_0i[7]` do `2.30e-67` a
  odhalil cancellation factor `8.91e8`. Dominantný upstream blok je
  fractional background × M1 (`-7.04819e-9`); F0 je iba `-1.80023e-11`.
  Výsledok je diagnostic REVIEW, nie PASS/STOP; ďalší test izoluje M1 od
  background generátora. C2 ostáva `5/10`.
- KMPC-099 standalone M1 matrix-provenance raw má SHA
  `93780C85488F17831562238D61FF2ADA70182163B488687BAB49BA9A6E96ECD9`.
  Natívna 80-dps assembly po binary64 projekcii aj nezávislý frozen rebuild
  majú shape `121×98`, rank `98/98`, condition `634.52` a najmenšiu singular
  value `0.537408`. RHS je identická; 26 matrix prvkov sa líši najviac o
  `1.776e-15`, relatívna Frobeniova odchýlka je `6.085e-18`. Výsledok je
  diagnostic REVIEW, nie C2 PASS.
- KMPC-100 read-only receipt má SHA
  `2581BC157F0CBA08D91654A9BCE9976D93429D9DB6AA0FA2AE4765F05AD9CC1A`.
  Overil KMPC-099 SHA, source ledger, ranky, diagnostic-only rolu, nulový
  autoritatívny HP-M1 solve a `pass_c2_atom_candidate=false` bez opakovania
  matice. QR blokér je lokalizovaný; C2 ostáva `5/10`.
- KMPC-102 native 80-dps M1 CPQR raw má SHA
  `49187BB85B8C59559A23EF6741DFB64F0015C2F0CC458D5C9D284FF2CECDE0CB`.
  Pri shape `121×98` priamo potvrdil rank `98/98`; ortogonalita je
  `3.21e-81`, relatívna faktorizácia `1.00e-82` a normálový reziduál
  `7.85e-85`. Lokálne M1 driver aj non-fit holdout prešli, ale fyzikálny
  PASS bol správne potlačený. Ďalší krok je 13-state downstream insertion;
  C2 ostáva `5/10`.
- KMPC-108 HP-M1 support checkpoint raw má SHA
  `683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995`.
  Lossless register SHA je `402B42E1...5EBF40`; M1, accepted `[0,5]`, F0,
  common, tail, S-C0, background a audit holdout prešli. Jediný audit false
  check je float64 `M3_driver`, worst `tight_coupling[7] = 2.77159e-10`
  voči `1e-10`. Raw je checkpoint-only bez C2 PASS.
- KMPC-109 read-only receipt má SHA
  `21EF9A9BF8D6E437CC848BD76EC026C5621534F35C0D88F99D2BFAFAD28118F9`.
  Bez solve prepočítal file/register SHA, poradie, round-trip a presnú false
  množinu; povolil jediný exact-driver/non-fit-holdout resume. C2 ostáva
  `5/10`.
- KMPC-112 checkpoint exact-resume raw má SHA
  `FAF52256489BA7C105F9125C1ED9A68358C0187E5F7B8B1164E1BA036A6507A1`.
  Exact 104×104 driver prešiel na `8.61476e-82`; nezávislý 16×104 holdout
  bez fit riadkov prešiel na `7.07119e-15` a `Einstein_0i[7]` na
  `3.39654e-15`. Interný audit 179 prijal scoped BI/k=.15 PASS; C2 je
  `6/10`, K4 ostáva `60/100`.
- KMPC-113 NID/k=.005 nominal raw má SHA
  `DD5B3075AB7581C4DC590CFE668952217B58C969B07FEC1CCDE5FA02C7B3B533`.
  M1/core/common/background prešli, no tail `6,7` na `.01` bol F0
  `1.1184e-5` a M3 `2.4037e-5`, preto autoritatívne REVIEW otvorilo
  `[0,7]→[0,9]` bez zmeny prahu.
- KMPC-114 accepted `[0,7]` checkpoint raw má SHA
  `339FD13BE750060793FCE04698BA5726AFD58DCB08BBDD3DB7B1FDFE76B35195`.
  Má výlučne rolu `NO_PHYSICS_VERDICT`, M1 depth 9 a 9/9 preconditions PASS.
- KMPC-115 checkpoint-resume raw má SHA
  `7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851`.
  Accepted `[0,7]`, audit `[0,9]`, M1/core/common/tail/S-C0/background a
  independent `00/0i` holdouty prešli; najhorší `.01` tail je
  `8.94188e-9 < 1e-6`. Interný audit 183 prijal scoped NID/k=.005 PASS;
  C2 je `7/10`, K4 ostáva `60/100`.
- KMPC-116 NID/k=.15 nominal raw má SHA
  `0965E3D1F7726CC851B3D1B6043468169ADEBED44096B010565F768DBD8E25AB`.
  Accepted/common/tail/background a holdout prešli; audit false iba
  `M3_driver`, worst `gamma_Euler[7]=4.18656e-10 > 1e-10`.
- KMPC-117 same-matrix raw má SHA
  `F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4`.
  Na presne tej istej 104×104 matici tri corrections znížili driver na
  `1.35140e-16`; independent holdout `1.43732e-11`, tail aj background
  prešli. Interný audit 186 prijal scoped NID/k=.15 PASS a uzavrel NID mód;
  C2 je `8/10`, K4 ostáva `60/100`.
- KMPC-118 NIV/k=.005 nominal raw má SHA
  `FDB2DF9C0AA1620F2ABF76F1704735DD1848F8C8D861BD959B5F81EC6873B78F`.
  Netail brány prešli; `.01` tail F0/M3 ostal nad `1e-6` a otvoril
  predregistrované rozšírenie `[-1,6]→[-1,8]`.
- KMPC-119 verdict-free checkpoint raw má SHA
  `0E87C19C706D2D8AE9FA1FF2771B46FEEF308327C5B459024175566BAF4ECEE9`.
  Accepted `[-1,6]`, audit `[-1,8]`, M1 depth 8 a 9/9 preconditions PASS;
  samostatne nemení verdict.
- KMPC-120 checkpoint-resume raw má SHA
  `D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136`.
  Všetky brány prešli; `.01` tail F0 `3.66649e-9`, M3 `7.69530e-9` a M3
  holdout `4.77975e-14`. Interný audit 190 prijal scoped NIV/k=.005 PASS;
  C2 je `9/10`, K4 ostáva `60/100`.
- KMPC-121 NIV/.15 nominal raw SHA
  `8E5E8107833C9F2858BA180F9DBC3DFA4037566CCC2F7D30AF819B1FC94C0BEE`
  izoloval core `fuel_Euler[6]=1.62542e-10` a tail REVIEW.
- KMPC-122 same-matrix raw SHA
  `BAC68E1D85802852EEBF4B1AC2E277EC15FD32264E166F673D486FD747869419`
  uzavrel core na `1.51686e-16`; tail ostal nad `1e-6`.
- KMPC-123 checkpoint attempt raw SHA
  `D3B31093D84156D05BF4EE8EC707D53B5D653DE5700289E6EA68627674898DC8`
  má `checkpoint_complete=false`; KMPC-124 success raw nevznikol (PF-114).
- KMPC-125 má iba technical failure raw SHA
  `1ED339AE9FBA7BA27C066A659926B0B822029F8BC3CF0AE4844DF4845E3A31D0`
  (PF-115), bez fyzikálneho verdiktu.
- KMPC-126 widened multi-rank raw SHA
  `1D46AFD1CDEB650A7787A5E6FE9E2304A5212FF1FE9AA47657BEAAAA557B8AA0`
  prešiel všetkými bránami; accepted/audit driver `1.72471e-16/2.13943e-16`,
  holdout `9.60602e-11`, tail `2.80666e-12/3.40284e-12`. Interný audit 197
  uzavrel NIV mód. C2 má 10/10 scoped PASS atómov; aggregate je NOT_RUN a
  K4 ostáva `60/100`.
- KMPC-127 read-only C2 aggregate raw SHA
  `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F`
  overil exact SHA/identity/candidate/brány registra `10/10`, bez
  technical-failure outputu. Najhorší cross-mode/cross-k background spread
  je `4.60781e-16 < 1e-12`. Interný audit 199 uzavrel C2 gate a odblokoval
  C3; K4 ostáva `60/100`.

KMPC-023/024 nie sú úplný P5 seed ani fyzikálny STOP K4.

Výsledok sa nikdy neprepisuje; oprava dostane nové RUN ID alebo `RERUNn`.
