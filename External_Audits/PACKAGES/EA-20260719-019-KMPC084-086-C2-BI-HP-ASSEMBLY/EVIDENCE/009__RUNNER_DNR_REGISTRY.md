# P5 — manifest runnerov

| Rozsah | Kanonické runnery | Poznámka |
|---|---|---|
| P5.1–P5.3f | `scripts/236_script_KMPC_003*` až `scripts/247_script_KMPC_010*` | čítať celé názvy, nie iba čísla |
| P5.3g1–g3 | `scripts/248_script_KMPC_011*` až `scripts/254_script_KMPC_017*` | obsahuje opravené reruny; stav v artifact indexe |
| P5.3g4 | `scripts/255_script_KMPC_018_P5_3g4_photon_l2_tca_seed.py` | prefix 255 koliduje s Q22A runnerom |
| P5.3g5 | `scripts/256_script_KMPC_019_P5_3g5_early_opacity_and_einstein_ledger.py` | prefix 256 koliduje s Q22A runnerom |
| P5.3g6 STOP | `scripts/257_script_KMPC_020_P5_3g6_synchronous_photon_gauge_bridge.py` | PF-054, neautoritatívny |
| P5.3g6 RERUN1 | `scripts/260_script_KMPC_021_P5_3g6_synchronous_photon_gauge_bridge_rerun1.py` | autoritatívny scope-limited výsledok |
| P5.3g7 KMPC-022 | `scripts/261_script_KMPC_022_P5_3g7_mode_resolved_full_seed_audit.py` | PF-055 `DO_NOT_RUN_TECHNICAL`; JSON nevznikol |
| P5.3g7 KMPC-023 | `scripts/261_script_KMPC_023_P5_3g7_mode_resolved_full_seed_audit_rerun1.py` | `RUNNABLE_REVIEW_ONLY`; M1 neukotvená |
| P5.3g7 KMPC-024 | `scripts/261_script_KMPC_024_P5_3g7_mode_resolved_full_seed_audit_rerun2.py` | M1 anchor PASS, ale PF-058 `DO_NOT_USE_PHYSICS` pre úplný M3 |
| P5.3g7 R-A attempt 4 | `scripts/264_script_KMPC_025_P5_3g7_m3_full_ra_b1_preflight.py` | `PASS_ALGEBRA_SCOPE / STOP_CONTRACT_GUARD_PF064`; zachovať, contract PASS neudeľuje |
| P5.3g7 R-A attempt 5 | `scripts/265_script_KMPC_026_P5_3g7_m3_full_ra_b1_contract_guard_rerun1.py` | `PASS_R_A_B1_CONTRACT_GUARD_ONLY`; bez solve/ODE, bez bodov |
| P5.3g7 R-A attempt 6 | `scripts/271_script_KMPC_027_P5_3g7_m3_full_ra_seed_attempt6.py` | `DO_NOT_RUN_FULL_MODE / SMOKE_REGRESSION_ONLY`; PF-068 timeout, dokumenty 37–39 |
| P5.3g7 R-A attempt 7 | `scripts/272_script_KMPC_028_P5_3g7_m3_full_ra_atomic_attempt7.py` | sentinel dobehol; J2/J4 truncation REVIEW, ostatné atómy NOT_RUN |
| P5.3g7 R-A attempt 8 | `scripts/273_script_KMPC_029_P5_3g7_m3_full_ra_support_ladder_attempt8.py` | J6 PASS; J8 numerical driver REVIEW |
| P5.3g7 R-A attempt 9 | `scripts/274_script_KMPC_030_P5_3g7_m3_full_ra_j8_refinement_attempt9.py` | SHA `81D777...16FD`; TECHNICAL_COMPLETE, tail semantics REVIEW |
| P5.3g7 R-A attempt 10 | `scripts/275_script_KMPC_031_P5_3g7_m3_full_ra_deep_tail_branch_provenance_attempt10.py` | SHA `A222F9...C15B2`; `TECHNICAL_COMPLETE / ARCH_A CLOSED`, no-solve tail PASS |
| P5.3g7 S-C0 passport | `scripts/276_script_KMPC_032_P5_3g7_s_c0_coefficient_passport.py` | SHA `B6D108...FBC76E`; PF-069 `DO_NOT_RUN_AUDIT_TECHNICAL`, physics not reached |
| P5.3g7 S-C0 RERUN1 | `scripts/277_script_KMPC_033_P5_3g7_s_c0_coefficient_passport_rerun1.py` | SHA `9FC086...6C8B0F`; `RUNNABLE_REGRESSION_ONLY / IMMUTABLE_RESULT_EXISTS`, scoped PASS |
| P5.3g7 CDI C1 | `scripts/278_script_KMPC_034_P5_3g7_CDI_C1_primary_extended_coverage.py` | SHA `E8C267...0695A4`; docs 57–59; `RUNNABLE_REGRESSION_ONLY`, result SHA `37FB44...DCE20`; vtedajší `[0,3]` remainder open neskôr uzavrel KMPC-035 ako insufficient/REVIEW |
| P5.3g7 CDI support step 2 | `scripts/279_script_KMPC_035_P5_3g7_CDI_C2_support_03_05_ladder.py` | SHA `09F86A...76649E3`; docs 60–62; immutable result SHA `A9BD519F...E42A01`; `RUNNABLE_REGRESSION_ONLY`; scoped core/common PASS + `[0,3]` remainder REVIEW |
| P5.3g7 M1 order-7 provenance | `scripts/280_script_KMPC_036_P5_3g7_M1_order7_provenance_gate.py` | SHA `EBA6F6...2A204B`; docs 63–65; result SHA `39BB3886...B7B497`; scoped PASS + power7 driver precision REVIEW; regression-only |
| P5.3g7 M1 order-7 numerical successors | `scripts/281_script_KMPC_037*` až `scripts/283_script_KMPC_039*` | docs 67,68,74; 281/282 sú PF-072/PF-073; 283 immutable PASS result SHA `BDF331...CE016`; všetky už iba lineage/regression |
| P5.3g7 CDI support step 3 | `scripts/284_script_KMPC_040_P5_3g7_CDI_support_step3_05_07.py` | SHA `AF9CDF...65258`; docs 75–76; immutable result SHA `69C78F...BD219`; CDI `[0,5]` adequate iba `.05/nominal`; regression-only |
| P5.3g7 BI C1 | `scripts/285_script_KMPC_041_P5_3g7_BI_C1_primary_extended_coverage.py` | SHA `078C67...A059C`; docs 77–78; immutable result SHA `8BB006...AE183`; core/common PASS, `[0,1]` insufficient; regression-only |
| P5.3g7 BI support step 2 | `scripts/286_script_KMPC_042_P5_3g7_BI_support_step2_03_05.py` | SHA `F1C068...FEDD1`; docs 79–80; immutable result SHA `E5F18D...8CA61`; core/common PASS, `[0,3]` insufficient; regression-only |
| P5.3g7 BI M1 order-7 provenance | `scripts/287_script_KMPC_043_P5_3g7_BI_M1_order7_provenance_gate.py` | SHA `DB7650...1D358`; docs 81–82; immutable result SHA `B02D1D...61EB0`; structural/lower PASS, 5 driver + 1 holdout precision REVIEW; regression-only |
| P5.3g7 BI M1 order-7 boundary | `scripts/288_script_KMPC_044_P5_3g7_BI_M1_order7_numerical_boundary.py` | SHA `AE319B...DF37A`; docs 83–84; immutable result SHA `C3BD73...F1C36`; same-matrix numerical boundary PASS; regression-only |
| P5.3g7 BI support step 3 V1 | `scripts/289_script_KMPC_045_P5_3g7_BI_support_step3_05_07.py` | SHA `B3CCBA...0CECB`; PF-074, failure SHA `FFFF06...330C01`; `DO_NOT_RUN_AUDIT_TECHNICAL` |
| P5.3g7 BI support step 3 owner successor | `scripts/290_script_KMPC_046_P5_3g7_BI_support_step3_owner_successor.py` | SHA `E20F21...D1EDB`; docs 85–86; result SHA `60EC5A...15FB1`; BI `[0,5]` adequate `.05/nominal`; regression-only |
| P5.3g7 NID closure | `scripts/291_script_KMPC_047*` až `scripts/297_script_KMPC_053*` | KMPC-049/PF-075 je `DO_NOT_RUN`; KMPC-053 autoritatívne uzavrel NID `[0,5]` `.05/nominal` po M1 depth-7 a KMPC-052 boundary; ďalší mód NIV |
| P5.3g7 NIV closure | `scripts/298_script_KMPC_054*` až `scripts/300_script_KMPC_056*` | KMPC-054 odmietol `[-1,2]`; 299/PF-076 je `DO_NOT_RUN_AUDIT_TECHNICAL`; KMPC-056 uzavrel NIV `[-1,4]` `.05/nominal` pri M1 depth 6; ďalší krok `k×variant` coverage |
| P5.3g7 C2 first atom | `scripts/301` až `305` | 301–303 sú PF-077 až PF-079 `DO_NOT_RUN`; 304 je read-only diagnostic; 305/KMPC-061 SHA `DF48D8...54F28`, docs 104–109; AD/`.005` immutable REVIEW tail a ďalší je nový support-ladder runner |
| P5.3g7 C2 AD `.005` support 04→06 | `scripts/306_script_KMPC_062*` | SHA `0A0D83...39CF5`; docs 110–111; immutable REVIEW, tail `5,6` prešiel na `z=1e-4`, nie `.01`; ďalší nový depth-8 runner |
| P5.3g7 C2 CDI `.005` closure | `scripts/311` až `317` | 312/313 sú PF-081/082 timeout DNR; 314/KMPC-070 je checkpoint bez verdiktu; 315/PF-083 `DO_NOT_USE_PHYSICS`; 316/PF-084 smoke DNR; 317/KMPC-073 SHA `B7779F...1A350`, result SHA `B7B2B7...E8498`, support `[0,7]` PASS |
| P5.3g7 C2 CDI `.15` closure | `scripts/318` a `319` | 318/KMPC-074 SHA `80DD26...0FB67` je immutable M3 driver REVIEW; 319/KMPC-075 SHA `7E8281...E5F8E`, result SHA `19F5F0...999B9`, same-matrix refinement PASS; CDI mód uzavretý |

Pred spustením rozhoduje karanténny register a konkrétna preregistrácia.
RERUN3 legacy KMPC-022/023/024 nie je povolený. R-A pokus 4 je algebraický
oracle obmedzený PF-064; pokus 5 je autoritatívny B1 contract guard PASS.
Pokusy 9 a 10 sú immutable uzavreté a nesmú sa opakovať na rovnaký output.
ARCH-A sa skončila úspešne historickým balíkom 10; nevznikne attempt 11.
Podľa nového pravidla je aktívny counter po vecnom KMPC-031 `0/10`, pričom
historických 10 balíkov zostáva v ledgeri. Ďalší proces musí patriť S1/mode
coverage kontraktu 51. Skript 262 zostáva rezervovaný výhradne P5.4 a nesmie
sa spustiť pred plným P5.3 seedom.

KMPC-032 nie je ARCH-A attempt 11. Má vlastný technický ledger a smie sa
spustiť iba podľa dokumentov 52–53, s immutable výstupom a bez zvýšenia
skóre pri samotnom algebraickom PASS.

Po PF-069 je 276 `DO_NOT_RUN_AUDIT_TECHNICAL`; jediný povolený nástupca je
277 podľa dokumentov 54–55. Nesmie meniť rovnice, iba numpy scalar bridge.

KMPC-034 až KMPC-040 sú immutable a nesmú prepísať existujúce outputy.
KMPC-040 uzavrel CDI support step 3 bez triggera pre `[0,9]`; ďalší módový
coverage krok musí dostať nový runner a samostatnú predregistráciu.
KMPC-041 je immutable BI C1 REVIEW primary supportu; nesmie sa opakovať.
KMPC-042 je immutable BI step-2 REVIEW; BI `[0,7]` blokuje samostatná
order-7 provenance brána. KMPC-043 je už immutable a nesmie sa opakovať;
KMPC-044 ju uzavrel bez zmeny rovníc/prahov. BI `[0,5]→[0,7]` je iba
odblokovaný pre nový runner a samostatnú predregistráciu. KMPC-045 skončil
PF-074 a nesmie sa opakovať; jediný owner/stderr nástupca KMPC-046 uzavrel
BI support bez `[0,9]`. KMPC-047 až 056 sú immutable. Ďalší runner patrí
samostatnej `k×variant` coverage a nesmie prevziať módový correction vector.
KMPC-061 je immutable po prvom C2 atóme; 305 sa nesmie opakovať na rovnaký
output. Deväť ďalších C2 atómov čaká na nový AD/`.005` support-ladder krok.
KMPC-062 je tiež immutable; ďalší runner smie testovať iba `[0,6]→[0,8]`.
KMPC-063 je immutable PASS candidate pre AD/k=.005 support `[0,6]`; runner
307 sa nesmie opakovať. Ďalší runner smie testovať iba AD/k=.15 nominal
s atom-local supportom `[0,2]→[0,4]` a bez prenosu correction vectora.
KMPC-064/runner 308 je po PF-080 `DO_NOT_RUN`; nevznikol raw. KMPC-065/
runner 309 je immutable REVIEW pre AD/k=.15 `[0,2]→[0,4]`. Ďalší runner
smie testovať iba `[0,4]→[0,6]`, depth 6, pri nezmenených prahoch.
KMPC-066/runner 310 je immutable PASS candidate pre AD/k=.15 support
`[0,4]`. KMPC-067 až 075 sú immutable CDI lineage; výsledkové autority sú
iba KMPC-073 pre k=.005 a KMPC-075 pre k=.15. Ďalší runner patrí iba
BI/k=.005 nominal `[0,5]→[0,7]` bez prenosu CDI refinement vektora.
KMPC-076 až 080 sú immutable BI lineage. Autoritatívny PASS je KMPC-078
pre k=.005; KMPC-079/080 pri k=.15 ostávajú REVIEW iba na nezávislom
holdout numerical boundary. Runner 324 sa nesmie opakovať; ďalší runner
smie iba high-precision auditovať ten istý systém bez pridania holdout riadkov.
Runnery 325/KMPC-081 a 326/KMPC-082 sú PF-086/PF-087 `DO_NOT_RUN`; nič
nevypočítali. Runner 327/KMPC-083 je immutable 80-dps REVIEW a vylúčil
solve-roundoff. Ďalší runner smie iba exact/high-precision zostaviť rovnaké
driver/holdout rovnice; holdout sa nesmie pridať do solve.
Runner 328/KMPC-084 je po PF-089 `DO_NOT_RUN_AUDIT_TECHNICAL`; zlyhal iba
smoke hash-ownera pred fyzikou. KMPC-085 smie opraviť iba oddelenie
algebraického ownera a hash ownera pri nezmenenom high-precision holdout
assembly rozsahu.
Runner 329/KMPC-085 je po PF-090 `DO_NOT_RUN_AUDIT_TECHNICAL`; owner oprava
prešla, ale zlyhal iba nesprávny decimal-exact affine smoke fixture.
KMPC-086 smie opraviť výlučne tento fixture a zachovať výpočet.
Runner 330/KMPC-086 je immutable REVIEW. PF-091 bolo iba prvé CLI volanie
bez outputu; corrected official dobehol a vylúčil posledné holdout-assembly
zaokrúhlenie. Ďalší runner smie iba 80-dps zostaviť rovnakú 104x104 driver
maticu a potom nezávislý holdout; nesmie meniť rovnice, support ani prahy.
