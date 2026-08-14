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
Runner 331/KMPC-087 je immutable REVIEW. Exact 80-dps driver assembly
prešiel, no non-fit `Einstein_0i[7]` ostal nad prahom. Ďalší runner smie iba
read-only rozložiť tento holdout na úplný coefficient/term ledger a oddeliť
M1, F0/fuel, background a exact-driver príspevky; nesmie meniť rovnice,
support, prahy ani pridať holdout do solve.
Runner 332/KMPC-088 je po PF-092 `DO_NOT_RUN_AUDIT_TECHNICAL`. Frozen solve
prebehol, ale success raw nevznikol, pretože `1e-70` reconstruction gate bola
prísnejšia než 50-ciferný referenčný decimal export. KMPC-089 smie opraviť
iba túto round-trip bránu na dynamické dve serializované ulp a pridať presnú
false-check diagnostiku; fyzika, term ledger aj prahy ostanú nezmenené.
Runner 333/KMPC-089 je po PF-093 `DO_NOT_RUN_AUDIT_TECHNICAL`. Compile/help
prešli, ale syntetický smoke porovnal 80-dps operand s pravou stranou znovu
vypočítanou pri default dps; official sa nespustil. KMPC-090 smie opraviť iba
fixture precision scope. V2 serialization formula, term ledger, rovnice a
fyzikálne prahy sa nesmú meniť.
Runner 334/KMPC-090 je po PF-094 `DO_NOT_RUN_AUDIT_TECHNICAL`. Corrected
smoke prešiel; official izoloval oba reconstruction checky. V1 fuel ledger
násobil bridged operandy pri 80 dps namiesto bridge už vykonaného binary64
produktu `1.5*delta`. KMPC-091 smie opraviť iba tento ledger faktor; frozen
holdout, solve, rovnice, support a prahy ostávajú nezmenené.
Runner 335/KMPC-091 je po PF-095 `DO_NOT_RUN_AUDIT_TECHNICAL`. Všetky
matematické smoke checks prešli; false bol iba vnorený V2 owner restore,
ktorý porovnával pôvodný callable s outer-dočasnou referenciou. KMPC-092
smie opraviť iba owner expectation; V1–V4 výpočet sa nesmie meniť.
Runner 336/KMPC-092 je immutable diagnostic REVIEW. Owner-only successor
prešiel a úplný 73-term ledger lokalizoval dominantný blok na fractional
background × M1; aktívny technický counter resetoval na `0/10`. Runner sa
nesmie opakovať. Ďalší runner smie izolovať iba jednu upstream stranu tohto
bilineárneho bloku pri nezmenenom F0/M3 systéme, prahoch a non-fit holdoute.
Runner 337/KMPC-093 je po PF-096 `DO_NOT_RUN_AUDIT_TECHNICAL`. Compile/help
a nové HP-M1 smoke fixtures prešli; false bol iba zdedený attribution owner
restore počas legitímneho outer M1 overlayu. Official sa nespustil a raw
nevznikol. KMPC-094 smie opraviť iba owner expectation; frozen M1 reassembly
matematika, support, rovnice a prahy sa nesmú meniť.
Runner 338/KMPC-094 je po PF-097 `DO_NOT_RUN_AUDIT_TECHNICAL`. Owner smoke
prešiel, ale official unscaled 80-dps QR skončil `matrix is numerically
singular`; success raw nevznikol. KMPC-095 smie zmeniť iba stĺpcovú
ekvilibráciu reduced M1 systému pri zachovaní unweighted residualu; žiadne
riadkové váhy, rovnice, background hodnoty, support ani prahy sa nemenia.
Runner 339/KMPC-095 je po PF-098 `DO_NOT_RUN_AUDIT_TECHNICAL`. Zlyhal iba
syntetický `1e40` scale fixture s neuskutočniteľnou `1e-60` absolútnou
solution bránou; official sa nespustil. KMPC-096 smie opraviť iba fixture
rozsah/toleranciu a numerické ratio porovnanie; V3 solver sa nemení.
Runner 340/KMPC-096 je po PF-099 `DO_NOT_RUN_AUDIT_TECHNICAL`. Corrected
smoke prešiel; official column-equilibrated QR však zopakoval numerical
singularity a raw nevznikol. KMPC-097 musí byť iba matrix-provenance
diagnostic s rank/singular/difference ledgerom; nesmie skúšať ďalší
fyzikálny solver ani udeliť C2 PASS.
Runner 341/KMPC-097 je po PF-101 `DO_NOT_RUN_AUDIT_TECHNICAL`. Matrix
provenance a binary64 diagnostic bridge prebehli, ale HP-M1 overlay potom
nahradil 13-stavový combined register 11-stavovým M1 registrom a atribúcia
skončila `KeyError: delta_f`; failure SHA `9B1B1031...2F19E5`. KMPC-098 smie
opraviť iba explicitné zlúčenie M1 stavov so zachovaním `delta_f,U_f`;
V5 diagnostika, rovnice, support, bridge a prahy sa nemenia.
Runner 342/KMPC-098 je po PF-102 `DO_NOT_RUN_AUDIT_TECHNICAL`. Combined
13-state merge a fuel preservation prešli, ale zdedená KMPC-088 atribučná
brána vyžadovala starý KMPC-087 residual, ktorý po diagnostickej M1
substitúcii nie je invariant. Failure SHA `3CD0C73D...9CBBD6`. KMPC-099 musí
spustiť iba standalone M1 assembly/provenance rez; atribučná brána a jej
tolerancie ostávajú nezmenené.
Runner 343/KMPC-099 je po PF-103 `DO_NOT_RUN_IMMUTABLE_TARGET_EXISTS`.
Standalone diagnostika a exclusive publish raw SHA `93780C85...E96ECD9`
prešli, ale post-publish terminálny summary očakával legacy `atom_id` a
vrátil nonzero. Raw je diagnostický evidence artefakt; KMPC-100 smie iba
read-only overiť jeho SHA/schema/contract a publikovať summary-compatible
receipt bez opakovania výpočtu.
Runner 344/KMPC-100 je immutable read-only diagnostic receipt. Exit 0 a
všetky SHA/source/rank/no-PASS kontroly prešli; raw SHA
`2581BC15...D9CC1A`. Vecný KMPC-099/100 resetuje aktívny technický counter
na `0/10`. Ďalší runner smie iba rank-revealing HP audit tej istej natívnej
M1 matice; downstream fyzika je až samostatný následný krok.
Runner 345/KMPC-101 je po PF-104 `DO_NOT_RUN_AUDIT_TECHNICAL`. Compile/help
a oba CPQR smoke fixtures prešli, ale official sa zastavil v output-path
garde pred M1 assembly, pretože CLI uviedlo basename namiesto canonical
`scripts/results/k_mpc_005/...` cesty. Failure SHA `378A4FC7...A119CA`;
aktívny technický counter je `1/10`. KMPC-102 smie iba opraviť routing nad
byteovo nezmeneným V9, bez zmeny metódy, prahov alebo scope.
Runner 346/KMPC-102 je immutable routing successor nad byteovo nezmeneným
V9 CPQR. Compile/help/smoke/official exit 0; raw SHA
`49187BB8...CDE0CB`, natívny rank `98/98` a všetky numerické contract checks
prešli. Vecný výsledok resetuje aktívny counter na `0/10`. Ďalší runner smie
iba downstream insertion cez zachovaný 13-state register; V9 solver, M1
matica, rovnice a prahy sa nesmú meniť.
Runner 347/KMPC-103 je po PF-105 `DO_NOT_RUN_AUDIT_TECHNICAL`. Compile
prešiel, ale help/smoke ešte pred CLI parserom odhalili side effect pri
importe runnera 346: top-level konfigurácia KMPC-102 znemožnila jednorazovú
konfiguráciu KMPC-103. V11 ani fyzika nebežali; counter je `1/10`.
KMPC-104 smie zmeniť iba contract-loader na SHA-guarded statický AST read.
Runner 348/KMPC-104 je po PF-106 `DO_NOT_RUN_AUDIT_TECHNICAL`. AST loader
a všetkých 17 smoke checks prešli, no payload identity ostala hardcoded
`KMPC-103`. Official sa nespustil; counter je `2/10`. KMPC-105 smie pridať
iba V12 identity wrapper nad byteovo nezmeneným V11.
Runner 349/KMPC-105 je po PF-107 `DO_NOT_RUN_AUDIT_TECHNICAL`. V12 identity,
compile/help a 19 smoke checks prešli, ale official monolit HP-M1 plus dva
support solve plus exact boundary prekročil interných `45 s`; failure SHA
`DAF1A456...239EC3`. Čiastkové stavy v pamäti nemajú fyzikálny verdikt a
counter je `3/10`. KMPC-106 smie vytvoriť iba verdict-free immutable
checkpoint HP-M1 + accepted/audit support; KMPC-107 ho musí načítať cez
exact SHA a samostatne vykonať audit-matrix/exact-driver/holdout. Runtime ani
fyzikálne prahy sa nezvyšujú.
Runner 350/KMPC-106 je po PF-108 `DO_NOT_RUN_AUDIT_TECHNICAL`. Compile
prešiel, no help/smoke ešte pred CLI odmietli neliterálny AST assignment
`dict(_prior_sources)` v runneri 349; V13 ani fyzika nebežali a raw
nevznikol. Counter je `4/10`. KMPC-107 smie byť iba routing successor nad
byteovo nezmeneným V13: načíta pinned priamy literal contract z runnera 346
a explicitne pridá hashované V11/V12/V13 a raw KMPC-102/PF-107.
Runner 351/KMPC-107 je po PF-109 `DO_NOT_RUN_AUDIT_TECHNICAL`. Routing,
compile/help a 28+3 smoke checks prešli; celý CPQR + accepted/audit support
prefix dobehol, ale publish odmietol diagnostický JSON scalar typu `mpf`.
Failure SHA je `ADB8D2A1...92F89C`, success raw nevznikol a counter je
`5/10`. KMPC-108 smie iba rekurzívne serializovať každý zostávajúci `mpf`
na 90-digit decimal string, reportovať jeho presnú payload cestu a zachovať
byteovo nezmenený V13 checkpointový výpočet, registre, SHA, prahy a runtime.
Runner 352/KMPC-108 publikoval immutable raw SHA `683D867D...9D995` a
terminálny summary, potom host shell vrátil external timeout 124 (`PF-110`).
Raw má runtime `41.875 s`, šesť presne reportovaných `mpf` konverzií a žiadny
C2 PASS; audit support je false iba cez `M3_driver`. Runner sa pre existujúci
cieľ nesmie opakovať. Counter je do read-only KMPC-109 receiptu `6/10`;
receipt musí overiť SHA, schema, checkpoint fingerprint a presnú false-check
množinu pred povolením exact resume.
Runner 353/KMPC-109 je immutable read-only receipt, raw SHA
`21EF9A9B...28118F9`. Compile/help/smoke/official exit 0; overil raw
KMPC-108 SHA, vnútorný register SHA `402B42E1...5EBF40`, 13-state poradie,
round-trip, šesť `mpf` ciest a presné false množiny. Povolil iba exact
driver/holdout resume a resetoval counter na `0/10`; C2/P5/K4 bez zmeny.
Runner 354/KMPC-110 je po PF-111 `DO_NOT_RUN_AUDIT_TECHNICAL`. Compile/help
prešli, ale smoke pred solve použil alfabetické JSON dict poradie namiesto
explicitného checkpoint `m1_state_order`; raw ani exact fyzika nevznikli a
counter je `1/10`. KMPC-111 smie iba order-reconstruction overlay nad
byteovo nezmeneným V17.
Runner 355/KMPC-111 je po PF-112 `DO_NOT_RUN_AUDIT_TECHNICAL`. Compile/help
a 19 smoke checks prešli; official dobehol po exact boundary, ale fail-closed
parity porovnanie postavilo živé integer-key/tuple typy proti JSON
string-key/list typom. Failure SHA `1ADCB30A...BD95E40`; fyzikálny payload
nevznikol a counter je `2/10`. KMPC-112 smie pridať iba publish-canonical
parity overlay nad byteovo nezmenenými V17/V18.
Runner 356/KMPC-112 je immutable vecný výsledok. Compile/help, 29 smoke
checks, tri publish fixtures a official exit 0 prešli; raw SHA
`FAF52256...A6507A1`. Exact driver aj non-fit holdout PASS, interný audit
dokument 179 uzavrel BI/k=.15 a resetoval counter na `0/10`. Runner sa pre
existujúci immutable target nesmie opakovať.
