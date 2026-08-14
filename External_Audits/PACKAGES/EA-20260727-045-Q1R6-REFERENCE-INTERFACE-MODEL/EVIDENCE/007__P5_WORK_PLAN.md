# A1-K1 → A2-K4 → P5 — živý kontrakt úplného stavového priestoru

**Aktualizované:** 2026-07-26  
**Stav:** `ŽIVÁ / active technical counter 0/10 / C3 45/45 / B6B1_ANALYTIC_ENVELOPE_CONTRACT_PASS / B6B2_PASSPORT_SCHEMA_PASS_PHYSICAL_CONTENT_REVIEW_BLOCKED / B6B2_6_FORMAL_FIRST_PASSAGE_MANTLE_PASS / INPUT_INCOMPLETE / P5.4 NOT RUN`  
**Rodičovský mechanizmus:** `Q_f^mu=-Gamma rho_f u_d^mu`, `Q_c^mu=+Gamma rho_f u_d^mu`, `Gamma=lambda H0`  
**Účel:** nahradiť redukovanú K7 bázu plným general-synchronous species-first stavom; nejde o nový mechanizmus ani novú A2 koľaj.

## Čo P5 presne testuje

P5 musí ukázať, že A2-K4 možno implementovať bez potlačenia hybnosti popola.
Povinný stav je minimálne:

```text
metric: h, eta
photons: delta_gamma, U_gamma, multipóly
neutrinos/para: delta_nu, U_nu, sigma_nu, L3_nu, ...
baryons: delta_b, U_b
ash/CDM: delta_c, U_c
fuel: delta_f, U_f
energy frame: U_d=(1-beta)U_c+beta U_f
```

`U_c` ani `U_b` sa nesmú odstrániť projekciou či gauge podmienkou. `k` je
Fourierov perturbatívny mód; nesmie sa vložiť ako pevný background parameter.

## Brány a aktuálny stav

| Brána | Čo musí platiť | Stav | Dôkaz / ďalší krok |
|---|---|---|---|
| P5.1 | exact-A1 background, `gamma=lambda/E`, `beta`, `U_d`, species RHS identity | **PASS** | 9/9 presných núl; `RUN_KMPC_003_P5_1_GENERAL_SYNCHRONOUS_STATIC_LEDGER.json` |
| L2-B2.1 | BR2 89/90 obsahuje rovnaké jadro | **PASS, scope-limited** | 16/16 source kontrol; nie je to constraint ani ODE PASS |
| P5.2 | `00`, `0i`, slip a trace constrainty obsahujú `U_c`,`U_b`,`U_f` a majú nulové limity | **PASS, structural-only** | 13/13 kontrol; dynamické zachovanie zostáva otvorené |
| P5.3 | regulárne general-synchronous seedy v plnom stave | **ČIASTOČNÝ PASS / C3 45/45 / S-M D03 PARTIAL CANDIDATE BRIDGE BEHAVIORAL OPEN / B6B-1 ENVELOPE PASS / B6B-2 SCHEMA PASS + PHYSICAL REVIEW BLOCKED / B6B-2.2 PROTOCOL PASS / B6B-2.3 MATRIX PASS / B6B-2.4 P4-V1 REVIEW BLOCKED BEFORE WITNESS / B6B-2.5 H_D03-MF1-V1 EVENT-MEASURE BRIDGE PASS / B6B-2.6 H_RDIV-MF1-V1 FORMAL FIRST-PASSAGE MANTLE PASS / B6B-2.7 C01-C10 AUTHOR-INPUT MAP ACCEPTED / B6B-2.8 H_BIO-ECHO-V1 HEURISTIC MAP PASS + PHYSICAL REVIEW / B6B-2.9 C01-RW1 CONTRACT-ONLY PASS / B6B-2.10 Q1R3 + Q1R5 TERMINAL EVIDENCE-INCOMPLETE / Q1R6 REFERENCE-INTERFACE-ONLY REVIEW** | C01 ostáva `AUTHOR_SELECTED_E3_TEST_BRANCH / NO_PHYSICAL_WITNESS`; Q1R3 je `24/24_TERMINAL`, Q1R5 `15/15_TERMINAL`; [result280](P5_3_SEEDS/280_B6B2_10_H_RDIV_C01_RW1_V1_Q1R6_LOCAL_REPROCESS_S0_S13_RESULT_SK.md) prijal Q1R6 `1/1_TERMINAL` ako `PASS_Q1R6_REFERENCE_INTERFACE_MODEL_ONLY / REVIEW_Q1R6_NOT_A_COMPLETE_W10_WITNESS`, S0/S10/S13 PASS a S1–S9/S11–S12 MISSING. Nie je to complete W10 ani refutácia. `A_RW1=FORMALLY_NOT_PROVEN_EMPTY / PHYSICAL_NONEMPTINESS_NOT_PROVEN`. P4 work atoms `3`, physical witness attempts `0`; blocker ostáva `PHYSICAL_RW1_CARRIER_POWER_THRESHOLD_CONSERVATION_CELL_MEASURE_AND_RESET_NOT_DERIVED`. Progress review prijal `SCIENTIFIC_GATE_PROGRESS / NO_GOAL_DRIFT`; nasleduje externý Q1R6 closure balík a potom audited ordered transition Q1R7; bez nového source operation a Pythonu. |
| P5.4 | krátka species-first evolúcia: constrainty, linearita, dva štarty a kroková konvergencia | NOT RUN | po P5.3 |
| G8 | plná photon/neutrino hierarchia a `lmax` convergence | BLOCKED_BY_P5 | až po P5.1–P5.4 |
| G9 | CMB/S8 likelihood na zmrazenej fyzike | NOT RUN | až po platnom G8 |

## PASS, STOP a zakázané skratky

- PASS P5.2 potrebuje nezávislé constraint identity aj nulové limity.
- STOP P5 implementácie je chýbajúci alebo znamienkovo rozporný povinný člen;
  nie je to automatická smrť A2-K4.
- P5.3/P5.4 môžu dať `REVIEW_BLOCKED` pri technickom limite, nie fyzikálny
  STOP bez invariantného dôkazu.
- Nesmie sa patchovať K7/213, pripísať K7 body P5, zlúčiť baryón s fotónom
  mimo explicitného TCA limitu ani zaviesť parameter len na potlačenie `U_c`.
- Podľa AR66.2 textový audit smie byť iba `PASS_MAPY`; P5.1/P5.2 sú
  `STRUCTURAL PASS` a P5.3b–e sú `FORMULA PASS — leading radiation scope`.
  P5.4 nesmie bežať bez formula-provenance ledgeru a nezávislých residualov.

## Ukazovatele

| Ukazovateľ | Hodnota | Význam |
|---|---:|---|
| fyzikálna hĺbka A2-K4 | `60/100` | K7 `66.5/100` je iba technická hĺbka redukovanej RHS |
| P5 bránový progress | `3.5/6 oporných bodov; C3 45/45, fyzická S-M para ešte nie` | `A1_K1_A2_K4_P5_3_SM_v1` je zvolený iba ako mechanizmová trieda; input contract, full hierarchy a finite opacity sú otvorené; scoped PASS nepridáva bod |
| vedecká podpora P5 | neurčená | nesmie sa odvodiť z počtu skriptov ani z K7 supportu |

## Rozsah, ktorý zatiaľ nie je dokázaný

P5.1, L2-B2.1 a P5.2 neprešli dynamické zachovanie constraintov, regulárne
seedy, gauge mapovanie, numeriku, plnú hierarchiu ani dáta.
K7 G0–G7 sa na P5 neprenášajú.

## Aktuálny jediný krok

Autor 2026-07-22 zvolil kanonický variant
`A1_K1_A2_K4_P5_3_SM_v1 = exit/reheating reservoir`. Paralelný
`...SM_v2 = scar/event` nie je nástupca v1 a zostáva nevybraný. Aktuálny
stav je `AUTHOR_BRANCH_SELECTED / INPUT_CONTRACT_INCOMPLETE / NO_CODE`.
Autor schválil `V1-R1` a stavovú triedu `V1-S1`; `V1-D01` je uzavretý a
po reviewed manteloch autor schválil `V1-P1` s `V_min=0`; `V1-D02` je
uzavretý vo formálnom rozsahu. Jediný vybraný blok je `V1-D03`.
Constraint-first mapa hmota–para–popol má `PASS_MAPY` (reviewer `PASS_MAP`)
a analytický backward screen B0 `PASS_SCREEN` iba v scope
`ANALYTIC_CONDITIONAL_SCREEN`; `y_e` je `DIAGNOSTIC_ONLY`, T1 ani rate funkcie nie
sú zvolené. B1 má scoped `CONDITIONAL_FUNCTION_FAIL` pre spoločnú A13
1280-e-foldovú mapu; B2 audit `PASS_B2` vyžaduje v diskrétnej vetve oddeliť
`R_J(Y)` a `E_J(Y)`. EA-040 T1 audit `AGREE_WITH_LIMITATION` je prijatý;
event-energy distribution F-001 je zapracovaný. B3 má `PASS_B3` iba ako
`FINITE_HYPOTHESIS_MAP`: deterministické `F1–F3` majú spoločný hypotetický
drain, ale nijaký event operator ani T1 nebol zvolený. B4 má
`PASS_FORMULA_LINEAGE`: A2 `delta` patrí efektívnej tlakovej/sieťovej práci;
`F1–F3` ako energia réžie majú iba `STOP_CURRENT_CORPUS_ONLY`. B5 má
`PASS_DEFINITION_INVENTORY`, Q4-P0 `0/8` a Q22a-G0 zostáva definične
blokované. EA-041 tento stav prijal `AGREE_IN_SCOPE / T1` bez nálezov.
Autor potom schválil B6-C0 `LOCAL_CELLULAR_DIGESTION_FIRST_PASSAGE` pre
`e -> s+M` a následné `M -> C`; interný re-audit po troch formulačných
opravách dal `PASS_B6_C0_TOPOLOGY`. `V1-D03=PARTIAL_AUTHOR_INPUT`: C0
zúžil topológiu, ale neznížil otvorenú funkčnú voľnosť. B6a odmietol
energetickú frakciu ako clock a odvodil PH1 phase mantle
`D_u theta_D=m_e-(Theta/2)sin(2theta_D)` s pointwise hranicou
`2m_e>Theta`; re-audit dal `PASS_B6A_PH1_CONDITIONAL_MANTLE`. Autor potom
určil, že pred detailnou mikrofyzikou sa má nájsť množina reálnych
možností. B6b mapa MF1–MF4 po opravách dostala `PASS_B6B_FAMILY_MAP`.
One-winding brána už nie je jediný ďalší krok a PH1 zostáva iba MF2
 kandidátom. B6b-1 po deviatich lokálnych opravách a čistom delta re-audite
dostal `PASS_B6B1_ANALYTIC_ENVELOPE_CONTRACT`; žiadna rodina nebola vybraná
ani vyradená. B6b-2 po nezávislom audite dostal
`PASS_B6B2_PASSPORT_SCHEMA / REVIEW_B6B2_PHYSICAL_CONTENT_BLOCKED_D03_D11`.
Zmrazil kovariantné P0–P8 požiadavky, immutable search record a E3 S8 outer
envelope `[0.777,0.831]` iba pod E2 flat-LambdaCDM mapovaním; DESI je
necertifikovaný quasi-holdout a nesmie rankovať. B6b-3a smie neskôr hľadať
množinu kompatibilnú so S8 pásmom, ale pôjde o feasibility/kalibráciu;
nezávislé potvrdenie patrí B6b-3b. Eventová energia, `n_act`, causal region,
mark/cohort mapy a `omega_C` zostávajú otvorené. Autor spresnil, že tieto
nepozorovateľné fakty nemá vybrať odhadom. Dokument 248 je preto prekonaný
ako aktívny questionnaire. B6b-2.2 protokol má
`PASS_B6B2_2_POSSIBILITY_SPACE_PROTOCOL`; B6b-2.3 má
`PASS_B6B2_3_P0_P3_COMPATIBILITY_MATRIX`; B6b-2.4/P4-v1 má
`REVIEW_P4_V1_DEPENDENCY_FREEZE_BLOCKED_BEFORE_WITNESS`. Autorom schválená
E3 rodina H_D03-MF1-v1 následne prešla B6b-2.5 ako
`PASS_H_D03_MF1_V1_EVENT_MEASURE_BRIDGE_BEHAVIORAL_OPEN`. `pi_0∈[0,1]`
je celý exact matematický interval; formálny mapping witness existuje, ale
fyzická hodnota `pi_0`, generátor `R_div(Y)` a physical P4 witness nie.
Autor potom schválil H_RDIV-MF1-v1. Jeho zmrazené R0–R11 po nezávislom
audite uzavreli B6b-2.6 ako
`PASS_H_RDIV_MF1_V1_FORMAL_FIRST_PASSAGE_MANTLE_BEHAVIORAL_OPEN`: formal
regular crossing measure/compensator, once-only genealogy, kovariancia,
pozitivita a exact v1 exclusions sú konzistentné. B6b-2.7 prijal mapu
C01–C10 iba ako author-input navigáciu. B6b-2.8 prijal
`PASS_H_BIO_ECHO_V1_HEURISTIC_CONSTRAINT_MAP_ONLY /
REVIEW_PHYSICAL_ECHO_CARRIER_IDENTITY_CAUSAL_BRIDGE_CONSERVATION_AND_RESET_OPEN`;
biologická analógia je inšpirácia a constraint filter, nie fyzikálny dôkaz.
Autor následne explicitne zvolil C01-RW1 ako testovaciu E3 vetvu. B6b-2.9
[prereg 259](P5_3_SEEDS/259_B6B2_9_H_RDIV_C01_RW1_V1_AUTHOR_SELECTION_AND_PHYSICAL_FEASIBILITY_PREREGISTRATION_SK.md)
a [result 260](P5_3_SEEDS/260_B6B2_9_H_RDIV_C01_RW1_V1_CURRENT_CORPUS_W0_W12_RESULT_SK.md)
uzavreli `PASS_RW1_PHYSICAL_FEASIBILITY_CONTRACT_ONLY /
REVIEW_RW1_PHYSICAL_CARRIER_POWER_THRESHOLD_CONSERVATION_CELL_MEASURE_AND_RESET_OPEN`.
C01 je `AUTHOR_SELECTED_E3_TEST_BRANCH / NO_PHYSICAL_WITNESS`; C02–C10 sú
`INACTIVE_RETAINED_BACKUPS / NO_ACTUAL_QUOTIENT_PROVEN`.
`A_RW1=FORMALLY_NOT_PROVEN_EMPTY / PHYSICAL_NONEMPTINESS_NOT_PROVEN`.
`F_D0410_SCHEMA` je zmapovaná, ale physical nonemptiness/emptiness nie je
dokázaná. B6b-2.10 [result272](P5_3_SEEDS/272_B6B2_10_H_RDIV_C01_RW1_V1_Q1R3_TERMINAL_COVERAGE_RESULT_SK.md)
prijal `REVIEW_Q1R3_TERMINAL_COVERAGE_EXHAUSTED_EVIDENCE_INCOMPLETE_NO_PHYSICAL_INFERENCE`.
S0/S13 PASS, S1–S12 `NOT_ASSESSABLE`; Q1R3 nie je complete W10,
reference-only prijatie ani candidate-local vylúčenie. Exact lineage je
`24/24_TERMINAL`; ďalšie Q1R3 source operations a reset sú zakázané.
Ordered transition zachoval Q1R3 a Q1R4 duplicate. [Q1R5 result276](P5_3_SEEDS/276_B6B2_10_H_RDIV_C01_RW1_V1_Q1R5_S0_S13_PHYSICS_SCREEN_RESULT_SK.md)
s task238 erratom prijal
`REVIEW_Q1R5_SCREEN_EVIDENCE_INCOMPLETE_NO_PHYSICAL_INFERENCE`.
Q1R5 je `15/15_TERMINAL`; S0–S12 sú `NOT_ASSESSABLE`, S13 PASS. Nie je
complete W10, prijatý ani vylúčený a ďalšie Q1R5 source operations/reset sú
zakázané. [Q1R6 result280](P5_3_SEEDS/280_B6B2_10_H_RDIV_C01_RW1_V1_Q1R6_LOCAL_REPROCESS_S0_S13_RESULT_SK.md)
po obsahovom lokálnom reprocessingu prijal úplný 11-entry source universe a
vetvu `PASS_Q1R6_REFERENCE_INTERFACE_MODEL_ONLY /
REVIEW_Q1R6_NOT_A_COMPLETE_W10_WITNESS`. S0/S10/S13 sú PASS;
S1–S9/S11–S12 MISSING. Q1R6 je `1/1_TERMINAL`, nie complete W10 ani
refutácia a ďalší fetch/reset je zakázaný. P4 work atoms sú `3`, physical witness
attempts `0`; physical
blocker ostáva
`PHYSICAL_RW1_CARRIER_POWER_THRESHOLD_CONSERVATION_CELL_MEASURE_AND_RESET_NOT_DERIVED`.
Progress review prijal `SCIENTIFIC_GATE_PROGRESS / NO_GOAL_DRIFT`.
Najbližší krok je externý Q1R6 closure balík a potom independently audited
ordered transition Q1R7.
Dovtedy `C_x`, `Pi_J`, ďalší source operation, steam, completion, druhý
ansatz ani Python nie sú povolené.
`V1-D04` až `V1-D11` sú následné blokované kroky.
Nižšie
uvedený numerický sled je história, nie nový
run príkaz.

**P5.3g7 architektonický ledger:** dokumenty 32–50 uzavreli ARCH-A pri
historickom balíku 10; aktívny counter po vecnom úspechu je `0/10`.
KMPC-031 oddelil common drift od added powers a udelil scope PASS J4 supportu
iba pre AD/k=.05/nominal. S1 branch contract je dokument 51. KMPC-033
udelil iba conditional S-C0 lower-moment passport. KMPC-039 uzavrel CDI
order-7 numerical boundary a KMPC-040 následne potvrdil CDI `[0,5]` support
iba pre `.05/nominal`. KMPC-041/042 vyvrátili BI `[0,1]` aj `[0,3]`.
KMPC-043 (docs81–82, runner287) uzavrel BI lower/structural provenance, ale
5 driver a jeden holdout ostali precision REVIEW. KMPC-044 (docs83–84,
runner288) ich na tej istej BI matici uzavrel jedinou correction aj 80-dps
QR bez lower/anchor regresie. KMPC-045 PF-074 nevydal fyzikálny payload;
KMPC-046 owner-only nástupca uzavrel BI `[0,5]` voči `[0,7]`. KMPC-047 až
053 uzavreli NID `[0,5]`. KMPC-054 odmietol NIV `[-1,2]`; PF-076 zachoval
technický failure KMPC-055 a owner-only KMPC-056 uzavrel NIV `[-1,4]` voči
`[-1,6]` s M1 depth 6. Všetky sekvenčné módy sú tým uzavreté iba pre
`.05/nominal`. KMPC-057 až 060 potom odstránili tri support-guard smoke chyby
bez fyzikálneho atómu. KMPC-061 prešiel preflight, ale prvý C2 atóm
AD/`.005` odmietol `[0,2]` pre tail `3,4`. KMPC-062 `[0,4]→[0,6]` ešte
neprešiel na `.01`; KMPC-063 `[0,6]→[0,8]` uzavrel tento atóm s tailom
`1.83e-9/5.07e-9`. KMPC-064 skončil PF-080 bez fyziky; KMPC-065 opravil
iba smoke scope a pri AD/`.15` odmietol `[0,2]` pre tail `3,4`. Druhý C2
atóm bol REVIEW; KMPC-066 ho uzavrel candidate supportom `[0,4]`. KMPC-067
až 073 uzavreli CDI/`.005` na `[0,7]` voči `[0,9]`; technické timeout a
checkpoint-order pokusy PF-081 až PF-084 nepridali fyzikálny výsledok.
KMPC-074 izoloval CDI/`.15` M3 driver boundary a KMPC-075 ho uzavrel
same-matrix refinementom bez zmeny prahu. KMPC-078 uzavrel BI/`.005` cez
hashovaný checkpoint. KMPC-080 opravil BI/`.15` main driver, ale nezávislý
  holdout ostal REVIEW. KMPC-083 vylúčil solve-roundoff, KMPC-086 posledné
  float64 zostavenie/odčítanie holdoutu a KMPC-087 aj float64 zostavenie
  drivera. KMPC-092 zrekonštruoval všetkých 73 členov `Einstein_0i[7]`,
  potvrdil cancellation factor `8.91e8` a lokalizoval dominantný upstream
  blok na fractional background × M1; F0 je iba `-1.80e-11`. KMPC-099/100
  následne ukázali, že natívna M1 assembly po binary64 projekcii aj frozen
  rebuild majú rank `98/98`, condition `634.52`, identickú RHS a relatívny
  matrix rozdiel `6.09e-18`. KMPC-102 natívnym 80-dps CPQR potvrdil rank
  `98/98`, faktorizáciu `1.00e-82`, normálový reziduál `7.85e-85` a lokálny
  M1 driver/holdout PASS bez udelenia fyzikálneho verdiktu. KMPC-108/109
  potom uzavreli lossless 13-state checkpoint a receipt: M1, accepted, F0,
  common, tail, S-C0, background a audit holdout prešli; jediný false check
  je float64 audit M3 driver `2.7716e-10 > 1e-10` na
  `tight_coupling[7]`. KMPC-112 ho exact-driver/non-fit-holdout resumeom
  z checkpointu bez opakovania CPQR uzavrel a interný audit 179 udelil
  BI/.15 scoped PASS. KMPC-113 pri NID/`.005` odmietol `[0,5]` iba pre
  tail na `.01`; KMPC-114/115 cez hashovaný checkpoint uzavreli `[0,7]`
  voči `[0,9]`, pričom najhorší tail bol `8.94e-9 < 1e-6`. Interný audit
  183 udelil scoped PASS. KMPC-116 potom na NID/`.15` izoloval iba
  `gamma_Euler[7]` driver boundary `4.1866e-10`; KMPC-117 ju na presne tej
  istej matici uzavrel tromi corrections na `1.3514e-16`, bez regresie
  holdoutu, tailu alebo backgroundu. Interný audit 186 uzavrel celý NID
  mód. KMPC-118 potom izoloval pri NIV/`.005` tail-only truncation;
  KMPC-119/120 cez verdict-free checkpoint uzavreli `[-1,6]` voči
  `[-1,8]` a interný audit 190 udelil scoped PASS. KMPC-121/122 pri NIV/.15
  uzavreli nominal core a otvorili tail support; PF-114/115 zachovali
  incomplete checkpoint a rank-104-only chybu bez verdiktu. KMPC-126
  explicitne refinoval ranky 104/130 a uzavrel `[-1,6]` voči `[-1,8]`.
  Interný audit 197 uzavrel NIV mód. KMPC-127 potom bez nového solve overil
  exact register `10/10` a background spread; interný audit 199 uzavrel C2
  aggregate a odblokoval C3. KMPC-148, audit 243 a EA-039 potom uzavreli
  autoritatívny C3 register na `45/45`. S-C zostáva conditional a fyzická
  S-M para otvorená.
Súčasne ešte musí prejsť K4-spätne viazaný,
gauge jednoznačný `h,eta` seed a K4 mapovanie
a musí byť uzavretý zvolený S-M variant
`A1_K1_A2_K4_P5_3_SM_v1` (mikrofyzikálne odvodená para z Q18/Q22). Samotná
po voľbe `V1-P1` je aktívny iba `V1-D03`; `V1-D04` až `V1-D11` sú
blokované. Mapa a STOP hranice sú
`P5_3_SEEDS/25_P5_3G7_INPUT_RAILS_SK.md` a
`Audit/A2_K4_P5_G7_FULL_SEED_INPUT_CLOSURE_AUDIT_2026-07-16.md`. Bez týchto
vstupov sa `00`, `0i`, trace, traceless residual nesmie počítať.

Presný výsledok RERUN1/RERUN2 a contract STOP sú v `P5_3_SEEDS/28–31`;
`00`,`0i` zostávajú nezávislé holdout rezíduá a nesmú byť pridané do
driver matice. Dokument 37 a numbering-cap erratum sú historické vstupy
balíkov 6–10, nie aktuálny príkaz. Autoritatívny S-C0 výsledok je dokument
56 a counter pravidlo je séria po sebe idúcich technických zlyhaní.
Historické balíky a aktívny counter po sebe idúcich zlyhaní sú v
`P5_3_SEEDS/P5_3G7_M3_FULL_R_A_TECHNICAL_ATTEMPT_LEDGER.md`.

## Odkazy a údržba

- rodič: `tracks/A1/A1K1/A2/A2K4/00_WORK_PLAN.md`;
- historický K7 stop: `../C7_7c/K7/00_WORK_PLAN.md`;
- P5 predregistrácia: `Independent_Audits/K_MPC_0_05/14_P5_FULL_GENERAL_SYNCHRONOUS_SUCCESSOR_PREREGISTRATION_SK.md`;
- prenosový audit: `Independent_Audits/Implementation_Lineage/09_L2_B2_1_BR2_EQUATION_RESULT_SK.md`.
- P5.2 výsledok: `P5_2_CONSTRAINT_LEDGER/01_RESULT_SK.md`.
- P5.3a výsledok: `P5_3_SEEDS/01_PROVENANCE_RESULT_SK.md`.
- P5.3b výsledok: `P5_3_SEEDS/03_P5_3B_RESULT_SK.md`.
- P5.3d výsledok: `P5_3_SEEDS/06_P5_3D_RESULT_SK.md`.
- P5.3e výsledok: `P5_3_SEEDS/08_P5_3E_RESULT_SK.md`.
- P5.3f výsledok: `P5_3_SEEDS/10_P5_3F_RESULT_SK.md`.
- P5.3g1 výsledok: `P5_3_SEEDS/14_P5_3G1_RESULT_SK.md`.
- P5.3g2 výsledok: `P5_3_SEEDS/15_P5_3G2_RESULT_SK.md`.
- P5.3g3 obmedzenie: `P5_3_SEEDS/18_P5_3G3_LIMITATION_SK.md`.
- P5.3g3 RERUN1 výsledok: `P5_3_SEEDS/21_P5_3G3_RERUN1_RESULT_SK.md`.
- P5.3g4 výsledok: `P5_3_SEEDS/22_P5_3G4_RESULT_SK.md`.
- P5.3g5 výsledok: `P5_3_SEEDS/23_P5_3G5_RESULT_SK.md`.
- P5.3g6 RERUN1 výsledok: `P5_3_SEEDS/24_P5_3G6_RERUN1_GAUGE_BRIDGE_RESULT_SK.md`.
- P5.3g7 vstupné vetvy: `P5_3_SEEDS/25_P5_3G7_INPUT_RAILS_SK.md`.
- P5.3g7-M1 štandardná metrická mapa: `P5_3_SEEDS/26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md`.
- P5.3g7 RERUN2 contract STOP: `P5_3_SEEDS/31_P5_3G7_M3_TCA0_RERUN2_RESULT_AND_CONTRACT_STOP_SK.md`.
- P5.3g7 R-A B1 coefficient/species/Bianchi ledger: `P5_3_SEEDS/32_P5_3G7_M3_FULL_R_A_B1_COEFFICIENT_SPECIES_BIANCHI_LEDGER_SK.md`.
- P5.3g7 R-A B1 výsledok a PF-064 oprava: `P5_3_SEEDS/34_P5_3G7_M3_FULL_R_A_ATTEMPT4_RESULT_AND_PF064_AUDIT_SK.md`, `P5_3_SEEDS/36_P5_3G7_M3_FULL_R_A_ATTEMPT5_CONTRACT_GUARD_RESULT_SK.md`.
- P5.3g7 S-C0 contract/passport/result: `P5_3_SEEDS/51_P5_3G7_S1_BRANCH_AND_SUPPORT_TRANSFER_CONTRACT_SK.md`, `P5_3_SEEDS/52_P5_3G7_S_C_COEFFICIENT_PASSPORT_PREREGISTRATION_SK.md`, `P5_3_SEEDS/56_KMPC_033_S_C0_COEFFICIENT_PASSPORT_RERUN1_RESULT_AND_AUDIT_SK.md`.
- P5.3g7 C2 aggregate result: `P5_3_SEEDS/199_KMPC_127_C2_AUTHORITATIVE_ATOM_AGGREGATE_RESULT_AND_INTERNAL_AUDIT_SK.md`.
- P5.3g7 CDI C1 result: `P5_3_SEEDS/59_KMPC_034_CDI_C1_PRIMARY_EXTENDED_COVERAGE_RESULT_AND_AUDIT_SK.md`.
- P5.3g7 CDI support step 2 result: `P5_3_SEEDS/62_KMPC_035_GLOBAL_C1_CDI_SUPPORT_STEP_2_RESULT_AND_AUDIT_SK.md`.
- index bezstratového poriadku: `00_ARTIFACT_INDEX_SK.md`.
- AR66.2 checklist: `Independent_Audits/Implementation_Lineage/10_FORMULA_PROVENANCE_CHECKLIST_SK.md`.

Aktualizuje sa iba pri verdikte P5 brány, zmene povinného stavu, fyzikálnom
STOP/REVIEW, otvorení G8 alebo release snapshote. Šablóna:
`tracks/00_TRACK_CONTRACT_STANDARD_SK.md`.
