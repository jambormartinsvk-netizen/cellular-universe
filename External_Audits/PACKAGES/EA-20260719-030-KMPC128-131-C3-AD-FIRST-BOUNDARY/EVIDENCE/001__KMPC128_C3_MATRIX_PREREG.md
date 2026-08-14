# KMPC-128 — C3 matica nulových variantov, párové receipts

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Východiskový stav:** C1 uzavreté; C2 exact aggregate `10/10 PASS`; C3
odomknuté; K4 `60/100`; P5 `3.5/6`.

## 1. Jediná otázka

Prejde už uzavretý kartézsky register pätnástich `mode × k` nominálnych
seedov aj vlastnými nulovými mostami `gamma→0` a `A_f→0`, bez zmeny rovníc,
supportov, plôch alebo prahov?

Tento výpočet testuje iba conditional `S-C0 / Phi1 / M3-TCA0` seed. Neodvodzuje
fyzickú paru `S-M`, finite opacity, plnú hierarchiu, P5.4, G8, G9, CMB ani
`S8`. Ani `45/45` preto samo nezvýši K4 nad `60/100`; podľa dokumentu 51
uzavrie iba matematickú C3 coverage a odkryje fyzický blocker `S-M`.

## 2. Zachovanie 45 logických atómov s menšou réžiou

Zmrazený kontrakt 51 vyžaduje

```text
5 módov × 3 k × (nominal, gamma0, af0) = 45 logických atómov.
```

Pätnásť `nominal` atómov už existuje ako immutable C1/C2 dôkaz. KMPC-128 ich
nepočíta znovu: pri každom `mode × k` fail-closed overí presný súbor, SHA-256,
identitu, support a nadradenú PASS autoritu. Potom vypočíta jeho dve chýbajúce
logické vetvy `gamma0` a `af0`.

Na disk sa zapisuje jeden párový receipt na `mode × k`, teda najviac 15 nových
raw JSON namiesto 30. Každý receipt zachová dve samostatné logické identity,
checks, kandidátske interpretácie a runtime. Ide iba o technickú granularitu;
počet fyzikálnych atómov, rovnice a rozhodovacie kritériá sa nemenia.

Immutable názov:

```text
RUN_KMPC_128_P5_3G7_C3_{MODE}_K{0p005|0p05|0p15}_ZERO_VARIANT_PAIR.json
```

Poradie closure je `AD → CDI → BI → NID → NIV`; v každom móde
`k=.005 → .05 → .15`. Po troch receipts vznikne jeden interný audit módu a
jeden kompaktný externý balík. Partial výsledok sa zachová, ale neextrapoluje.

## 3. Zmrazené nulové varianty

Význam sa preberá bez zmeny z `full_ra_m3_seed.py`:

- `gamma0`: `FrozenInputs(lam=0.0)`; ostatné vstupy nominálne;
- `af0`: `FrozenInputs(af=0.0)`; ostatné vstupy nominálne;
- M1 standard seed sa v oboch vetvách počíta z nominálnych vstupov, tak ako v
  KMPC-028; zdieľa sa v párovom procese, ale jeho plný guard a metadata sa
  zapíšu do receipt;
- každý variant nanovo rieši F0 aj M3 na accepted aj audit supporte.

`gamma0` musí navyše dať do absolútneho `1e-12`:

```text
max|ash_j| = 0,
max|transfer_gr,j| = 0,
max|gamma_j| = 0,
|fuel_0 - 1| = 0.
```

`af0` musí mať konečné netriviálne solve (`rows>0`, `unknowns>0`), fyzický
`Phi1` príspevok k seedu nulový do `1e-12`, fuel/ash background nulový do
`1e-12` a jeho F0/M3 koeficienty na accepted aj audit supporte zhodné s
príslušným immutable nominal atómom podľa zmrazeného coefficient bridge
`relative 1e-8`, `absolute fallback 1e-12`.

## 4. Presný support register

| mód | `k` | accepted → audit | M1 depth | nominal autorita |
|---|---:|---|---:|---|
| AD | .005 | `[0,6]→[0,8]` | 8 | KMPC-063 |
| AD | .05 | `[0,2]→[0,4]` | 5 | KMPC-028 coefficients + KMPC-031 closure |
| AD | .15 | `[0,4]→[0,6]` | 6 | KMPC-066 |
| CDI | .005 | `[0,7]→[0,9]` | 9 | KMPC-073 |
| CDI | .05 | `[0,5]→[0,7]` | 7 | KMPC-040 |
| CDI | .15 | `[0,5]→[0,7]` | 7 | KMPC-075 |
| BI | .005 | `[0,7]→[0,9]` | 9 | KMPC-078 |
| BI | .05 | `[0,5]→[0,7]` | 7 | KMPC-046 |
| BI | .15 | `[0,5]→[0,7]` | 7 | KMPC-112 HP-exact |
| NID | .005 | `[0,7]→[0,9]` | 9 | KMPC-115 |
| NID | .05 | `[0,5]→[0,7]` | 7 | KMPC-053 |
| NID | .15 | `[0,5]→[0,7]` | 7 | KMPC-117 |
| NIV | .005 | `[-1,6]→[-1,8]` | 8 | KMPC-120 |
| NIV | .05 | `[-1,4]→[-1,6]` | 6 | KMPC-056 |
| NIV | .15 | `[-1,6]→[-1,8]` | 8 | KMPC-126 |

Support sa po výsledku nesmie zmenšiť. Ak nulový variant potrebuje väčší
support, výsledok je `REVIEW_C3_SUPPORT_EXTENSION_REQUIRED`; prípadný
nástupca musí dostať novú predregistráciu ešte pred novým solve.

## 5. Immutable nominal vstupy

Všetky cesty sú pod `scripts/results/k_mpc_005/`.

| atóm | súbor | SHA-256 |
|---|---|---|
| AD/.005 | `RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json` | `CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD` |
| AD/.05 | `RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_AD_K0p05_NOMINAL.json` | `2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83` |
| AD/.15 | `RUN_KMPC_066_P5_3G7_C2_AD_K0p15_SUPPORT_04_06.json` | `81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816` |
| CDI/.005 | `RUN_KMPC_073_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_PHASE_ORDER_SUCCESSOR.json` | `B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498` |
| CDI/.05 | `RUN_KMPC_040_P5_3G7_CDI_SUPPORT_STEP_3_05_07.json` | `69C78F70ECD851D8B8A48E4E09445181C0D4559E9BD2E90A7BA19933351BD219` |
| CDI/.15 | `RUN_KMPC_075_P5_3G7_C2_CDI_K0p15_SAME_MATRIX_REFINEMENT.json` | `19F5F0B38CFE62C6E2ECA277EE5F959D866967027C5AF721CF4B2E1A30B999B9` |
| BI/.005 | `RUN_KMPC_078_P5_3G7_C2_BI_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json` | `F24894A043B531825DD36A424637D1E70244F89B66678AF945EA6C135918A359` |
| BI/.05 | `RUN_KMPC_046_P5_3G7_BI_SUPPORT_STEP_3_OWNER_SUCCESSOR.json` | `60EC5A801FDDBAFFBA6CE184EBB3BC154879928385E6E37FB118781118615FB1` |
| BI/.15 | `RUN_KMPC_112_P5_3G7_C2_BI_K0p15_HP_M1_CHECKPOINT_EXACT_RESUME_JSON_PARITY_SUCCESSOR.json` | `FAF52256489BA7C105F9125C1ED9A68358C0187E5F7B8B1164E1BA036A6507A1` |
| NID/.005 | `RUN_KMPC_115_P5_3G7_C2_NID_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json` | `7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851` |
| NID/.05 | `RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json` | `625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD` |
| NID/.15 | `RUN_KMPC_117_P5_3G7_C2_NID_K0p15_SAME_MATRIX_REFINEMENT.json` | `F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4` |
| NIV/.005 | `RUN_KMPC_120_P5_3G7_C2_NIV_K0p005_SUPPORT_06_08_CHECKPOINT_RESUME.json` | `D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136` |
| NIV/.05 | `RUN_KMPC_056_P5_3G7_NIV_SUPPORT_STEP_2_FINITE_OWNER_SUCCESSOR.json` | `9AF6410513C2B0A6142DA9B08E8A1D115670C644171B102683568E64D645C332` |
| NIV/.15 | `RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json` | `1D46AFD1CDEB650A7787A5E6FE9E2304A5212FF1FE9AA47657BEAAAA557B8AA0` |

Globálna C2 autorita je
`RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json`, SHA
`CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F`.
Pre AD/.05 je dodatočná support autorita KMPC-031, SHA
`C547F818E3918CD844CA06BEA32814279A9D4A20D662A9166114410645792FF6`.

## 6. Nezmenené brány a prahy

Každá nová logická vetva musí prejsť:

1. frozen R-A/state/driver/holdout a B1 left-null/Bianchi guard;
2. production TCA0 bridge a M1 anchor;
3. exact F0/M3 shape, rank, driver, independent `00/0i` holdout,
   forbidden-layer/stress a production contract;
4. common coefficient bridge accepted→audit;
5. cancellation-safe tail na `z=1e-4,1e-2`;
6. actual S-C0 a combined-`R_fs` guard;
7. background k-independence;
8. vlastný nulový limit; pri `af0` aj nominal coefficient bridge.

Prahy zostávajú: driver `1e-10`, holdout `1e-9`, common `1e-8`, tail
`1e-6`, absolute fallback `1e-12`, background relative `1e-12`. Vnútorný
limit celého párového procesu je `4.8 s`; každý `compile`, `help`, `smoke` a
official run je samostatný proces s vonkajším limitom najviac `10 s`.

## 7. Predregistrované vetvy

- všetky core/common/tail/background/null/af0-bridge checks true:
  `PASS_C3_ZERO_VARIANT_PAIR_CANDIDATE_ONLY`;
- M1/core/holdout/Bianchi/S-C0 fail bez technickej výnimky:
  `REVIEW_C3_CORE_GATE_UNCLOSED`;
- common alebo nominal-af0 bridge fail:
  `REVIEW_C3_COEFFICIENT_BRIDGE_UNCLOSED`;
- tail fail: `REVIEW_C3_SUPPORT_EXTENSION_REQUIRED`;
- background leak: `STOP_C3_BACKGROUND_K_OR_MODE_LEAK_CANDIDATE_ONLY`;
- nulový limit fail: `REVIEW_C3_NULL_LIMIT_UNCLOSED`, pokiaľ nezávislá
  reprodukcia nepreukáže invariantný formulačný rozpor;
- syntax/import/CLI/hash/schema/timeout/serializácia: iba technická chyba,
  immutable failure receipt a žiadny fyzikálny verdikt.

Módový closure je dovolený iba pri `3/3` párových receipts = `9/9` logických
atómov vrátane troch už uzavretých nominal. C3 aggregate až pri `15/15`
receipts = `45/45` logických atómov.

## 8. Predbehový source freeze

Pred prvým Python procesom musia byť doplnené a overené SHA-256:

| artefakt | SHA-256 |
|---|---|
| `full_ra_m3_seed.py` | `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` |
| `c2_fourier_coverage.py` | `757F97E14657CC7046177C2D33115CA87639B9C92E89BDABE2BFF3B4380DF3FC` |
| nový base `c3_zero_variant_pair.py` | `45AE0B848819A56F690953A15D1722C266FD55D02E07D67F4115103CFA5AE9C0` |
| runner `372/KMPC-128` | `32A4B3D6504DCD9A0B7C40F2947721CBF3DA07733F2A1DA4A28483120A7B6C0C` |

Žiadny `PENDING_BEFORE_FIRST_PYTHON` nezostal; source freeze je dokončený.
Odteraz sa tento dokument nemení; výsledok a interný audit patria do nového
dokumentu.

## 9. Súborový rozpočet R5

Pre prvé ucelené AD closure sa plánujú nové live artefakty: `1` spoločná
predregistrácia, `1` base, `1` runner, `3` raw receipts a `1` interný audit.
Nie sú potrebné tri skripty ani tri preregistrácie. Centrálne registre sa
aktualizujú jedným batchom až po closure. Externý balík použije single-copy
runtime closure a musí zostať pod `40` fyzickými súbormi, inak sa pred
kopírovaním vyžaduje explicitná budget výnimka.
