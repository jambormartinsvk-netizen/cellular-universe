# P5 — index immutable výsledkov

Tento index zoskupuje výsledky P5 bez ich presunu alebo prepisu. Rozhoduje
stav v `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/00_WORK_PLAN.md`.

| JSON | Status | Použitie |
|---|---|---|
| `RUN_KMPC_003_P5_1_GENERAL_SYNCHRONOUS_STATIC_LEDGER.json` | autoritatívny P5.1 PASS | exact-A1/static ledger |
| `RUN_KMPC_004_P5_2_FULL_CONSTRAINT_LEDGER.json` | historický PF-041 STOP | iba spätný audit chyby |
| `RUN_KMPC_004_P5_2_FULL_CONSTRAINT_LEDGER_RERUN1.json` | autoritatívny P5.2 PASS | structural constraint ledger |
| `RUN_KMPC_005_P5_3A_SEED_PROVENANCE_AUDIT.json` | autoritatívna mapa medzery | nie regularity PASS |
| `RUN_KMPC_006_P5_3B_ADIABATIC_LEADING_SEED_RERUN1.json` | P5.3b PASS | iba adiabatický leading seed |
| `RUN_KMPC_007_P5_3C_ADIABATIC_FINITE_STARTS.json` | P5.3c PASS | iba adiabatické dve plochy |
| `RUN_KMPC_008_P5_3D_STANDARD_MODE_LEADING_SEEDS.json` | P5.3d PASS | päť štandardných leading módov |
| `RUN_KMPC_009_P5_3E_INTERNAL_REGULARITY.json` | P5.3e PASS | interné leading módy |
| `RUN_KMPC_010_P5_3F_GAUGE_HIERARCHY_AUDIT.json` | P5.3f PASS_MAPY | gauge-invariantná relatívna rýchlosť; lokalizuje chýbajúce standard `l>=2` |
| `RUN_KMPC_011_P5_3G1_F1_NORMALIZATION_PROVENANCE.json` | historický PF-043 REVIEW | neúplný marker BR2-90; nepoužiť na verdict |
| `RUN_KMPC_012_P5_3G1_F1_NORMALIZATION_PROVENANCE_RERUN1.json` | P5.3g1 mapa | priradenia sú správne, most uzatvára až 013 |
| `RUN_KMPC_013_P5_3G2_F1_QNU_NORMALIZATION_BRIDGE.json` | P5.3g2 formula PASS | `F1=qnu` v BR2/CAMB konvencii |
| `RUN_KMPC_014_P5_3G3_STANDARD_NEUTRINO_L2_SERIES.json` | PF-044 DO_NOT_USE | použil pomocné `tn`, nie návratové `qn` |
| `RUN_KMPC_015_P5_3G3A_SEED84_VELOCITY_SEMANTICS.json` | PF-045 DO_NOT_USE_STOP | príliš prísna `eta` podmienka |
| `RUN_KMPC_016_P5_3G3A_RETURNED_QN_SEMANTICS_RERUN1.json` | P5.3g3a PASS_SCOPE | návratové NIV `qn` je pri fixnom `y` invariantné |
| `RUN_KMPC_017_P5_3G3_STANDARD_NEUTRINO_L2_QN_RERUN1.json` | P5.3g3 RERUN1 derivation PASS | regulárny neutrínový `l=2` kandidát; nie plný seed |
| `RUN_KMPC_018_P5_3G4_PHOTON_TCA_FIRST_ORDER.json` | formula PASS iba s 021 | photon TCA algebra; synchronné mapovanie `shear` uzatvára až immutable 021 |
| `RUN_KMPC_019_P5_3G5_EARLY_OPACITY_AND_EINSTEIN_LEDGER.json` | P5.3g5 formula PASS, early scope | skorá plne-ionizovaná opacity a povinné `U_c,U_b,U_f` v `0i`; nie dynamický reziduálny test |
| `RUN_KMPC_020_P5_3G6_SYNCHRONOUS_PHOTON_GAUGE_BRIDGE.json` | PF-054 DO_NOT_USE verdict | správne identity, ale chybná markerová cesta; iba historická technická stopa |
| `RUN_KMPC_021_P5_3G6_RERUN1_SYNCHRONOUS_PHOTON_GAUGE_BRIDGE.json` | P5.3g6 RERUN1 formula PASS | uzatvára synchronný `sigma` ↔ `h,eta` most pre 018 |
| `RUN_KMPC_023_P5_3G7_M3_TCA0_RERUN1.json` | `RUNNABLE_REVIEW_ONLY` | exact k-cancel prešiel, ale štandardný M1 seed ostal neukotvený `76/77`; nie P5 seed |
| `RUN_KMPC_024_P5_3G7_M3_TCA0_RERUN2.json` | `M1_ANCHOR_PASS / DO_NOT_USE_PHYSICS_M3` | štandard `76/76` a constrainty PASS; frakčný palivový coefficient/row contract neuzavretý (PF-058), leading-power test nie je dva ODE štarty |
| `RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_AD_K0p05_NOMINAL.json` | `REVIEW_TRUNCATION_EXTENSION_REQUIRED` | J4 sentinel; rovnice/rank/holdout PASS, support nedostatočný |
| `RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J6.json` | `PASS_SUPPORT_SOLVE_ATOM` | J6 plnorankový support atóm |
| `RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J8.json` | `REVIEW_SUPPORT_SOLVE_ATOM` | jediný driver residual `fuel_Euler[8]` nad prahom |
| `RUN_KMPC_030_P5_3G7_M3_FULL_RA_J8_ONE_REFINEMENT_AUDIT.json` | `TECHNICAL_COMPLETE / REVIEW_TAIL_METRIC_SEMANTICS` | jedna korekcia uzavrela driver/holdout/guards; raw deep tail mieša common drift s added powers; SHA `8CB706...3C6F` |
| `RUN_KMPC_031_P5_3G7_M3_FULL_RA_DEEP_TAIL_BRANCH_PROVENANCE.json` | `PASS_SUPPORT_TRUNCATION_J4_SENTINEL_SCOPE` | no-solve rozklad; added tails PASS iba AD/k=.05/nominal; SHA `C547F8...92FF6`, nie celý P5.3/G8 |
| `RUN_KMPC_032_P5_3G7_S_C0_COEFFICIENT_PASSPORT_TECHNICAL_FAILURE.json` | PF-069 technical failure | numpy scalar konverzia zastala pred fyzikou; SHA `51C7B3...1EA03` |
| `RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1.json` | `PASS_S_C0_LOWER_MOMENT...ONLY` | 20/20, 10/10 fixtures; SHA `4CED9D...CFE8C`; higher multipoles/S-M/coverage open |
| `RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json` | core/common PASS; `[0,1]` insufficient; vtedajší `[0,3]` remainder open | SHA `37FB44...DCE20`; docs 57–59; neskorší KMPC-035 obmedzil `[0,3]` na insufficient/REVIEW |
| `RUN_KMPC_035_P5_3G7_CDI_C2_SUPPORT_03_05_LADDER.json` | scoped core/common PASS; `[0,3]` remainder REVIEW | SHA `A9BD51...E42A01`; docs 60–62; `delta_f` a `sigma_fs` tail fail pri `z=.01`; historický `C2` nie je Fourier C2 |
| `RUN_KMPC_036_P5_3G7_M1_ORDER7_PROVENANCE_GATE.json` | scoped provenance PASS; power7 driver precision REVIEW | SHA `39BB38...B7B497`; docs 63–65; 18 holdoutov PASS, tri driver[7] residualy `~1e-15`; support step 3 BLOCKED |
| `RUN_KMPC_039_P5_3G7_M1_ORDER7_CONTEXT_OWNER.json` | CDI same-matrix numerical boundary PASS | SHA `BDF331...CE016`; jedna bounded correction a 80-dps QR uzavreli 121+18 bez regresie |
| `RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07.json` | CDI `[0,5]` adequate iba `.05/nominal` | SHA `69C78F...BD219`; tail 6,7 PASS; bez automatického `[0,9]` |
| `RUN_KMPC_041_P5_3G7_BI_C1_PRIMARY_EXTENDED_COVERAGE.json` | BI core/common PASS; `[0,1]` insufficient | SHA `8BB006...AE183`; BI step 2 nasledoval samostatne |
| `RUN_KMPC_042_P5_3G7_BI_SUPPORT_STEP_2_03_05.json` | BI core/common PASS; `[0,3]` insufficient | SHA `E5F18D...8CA61`; BI order-7 gate nasledovala samostatne |
| `RUN_KMPC_043_P5_3G7_BI_M1_ORDER7_PROVENANCE_GATE.json` | BI lower/structural PASS; driver+holdout precision REVIEW | SHA `B02D1D...61EB0`; 5/121 driver a 1/18 holdout relative FAIL pri absolute `~1e-16`; BI same-matrix closure NEXT |
| `RUN_KMPC_044_P5_3G7_BI_M1_ORDER7_NUMERICAL_BOUNDARY.json` | BI same-matrix numerical boundary PASS | SHA `C3BD73...F1C36`; jedna correction `2.498e-15` a 80-dps QR uzavreli 121+18 aj projekciu bez regresie |
| `RUN_KMPC_045_P5_3G7_BI_SUPPORT_STEP_3_05_07_TECHNICAL_FAILURE.json` | PF-074, bez fyzikálneho verdictu | SHA `FFFF06...330C01`; wrong S-C0 owner + missing stderr `sys`; nahradil iba owner/stderr KMPC-046 |
| `RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json` | BI `[0,5]` adequate iba `.05/nominal` | SHA `60EC5A...15FB1`; regression/core/S-C0/common/tail 6,7 PASS; bez `[0,9]` |

Žiadny z výsledkov neotvára G8 samostatne. Najbližší krok je
samostatne predregistrovať NID primary `[0,3]` vs extended `[0,5]`, leading
`j=0`, s NID-specific combined-`R_fs` kompenzáciou. Potom ostáva NIV,
`k×variant` coverage, skutočné vyššie multipóly/S-M a až potom finite-opacity
P5.4, recombination a dvojštartová validácia.

KMPC-024 nemení túto finish line. Pred novým runnerom navyše vyžaduje
`Phi^0/Phi^1 × z^j` palivový ledger a total Bianchi/left-null mapu.
