# KMPC-127 — C2 autoritatívny register atómov: predregistrácia

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C2 Fourier aggregate`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / INTERNAL_AUDIT_PASS / C2_GATE_CLOSED`  
**K4:** `LIVE / 60/100`; zmena skóre `NONE`

## 1. Otázka

Po scoped PASS všetkých desiatich C2 mode×k atómov sa vykoná povinný
read-only aggregate zo frozen dokumentu 104. Smie iba:

1. načítať desať immutable JSON súborov;
2. overiť exact meno, SHA-256, identitu a povolený PASS candidate;
3. fail-closed overiť boolean brány `core/common/tail/background`;
4. overiť exact kartézsky register bez duplicity;
5. z už uložených background hodnôt vypočítať cross-mode/cross-k spread
   `D,H,rho_f,rho_ash` na `a=1e-8,3e-8`;
6. zapísať jeden immutable agregovaný raw.

Agregát nesmie importovať fyzikálny solver, zostaviť maticu, fitovať,
korigovať koeficient ani meniť atómový verdikt.

## 2. Frozen register

| Mode | k | Run | Súbor | SHA-256 | Povolený candidate |
|---|---:|---:|---|---|---|
| AD | .005 | 063 | `RUN_KMPC_063_P5_3G7_C2_AD_K0p005_SUPPORT_06_08.json` | `CB0CEA5DD92BF85F0F0066FAD8DE77D5F8247B02B864FACF92FA374E0FBC85BD` | `PASS_C2_AD_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY` |
| AD | .15 | 066 | `RUN_KMPC_066_P5_3G7_C2_AD_K0p15_SUPPORT_04_06.json` | `81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816` | `PASS_C2_AD_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY` |
| CDI | .005 | 073 | `RUN_KMPC_073_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_PHASE_ORDER_SUCCESSOR.json` | `B7B2B7231E20D90D7EA71F1934B795296B7B0C2772148988C0FCFB2CF96E8498` | `PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY` |
| CDI | .15 | 075 | `RUN_KMPC_075_P5_3G7_C2_CDI_K0p15_SAME_MATRIX_REFINEMENT.json` | `19F5F0B38CFE62C6E2ECA277EE5F959D866967027C5AF721CF4B2E1A30B999B9` | `PASS_C2_CDI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY` |
| BI | .005 | 078 | `RUN_KMPC_078_P5_3G7_C2_BI_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json` | `F24894A043B531825DD36A424637D1E70244F89B66678AF945EA6C135918A359` | `PASS_C2_BI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY` |
| BI | .15 | 112 | `RUN_KMPC_112_P5_3G7_C2_BI_K0p15_HP_M1_CHECKPOINT_EXACT_RESUME_JSON_PARITY_SUCCESSOR.json` | `FAF52256489BA7C105F9125C1ED9A68358C0187E5F7B8B1164E1BA036A6507A1` | `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY` |
| NID | .005 | 115 | `RUN_KMPC_115_P5_3G7_C2_NID_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json` | `7D7B9BC1F2874A20E0CB8116D657F7C0419D03B284D0161CFFDF89112B4E0851` | `PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY` |
| NID | .15 | 117 | `RUN_KMPC_117_P5_3G7_C2_NID_K0p15_SAME_MATRIX_REFINEMENT.json` | `F9BE1AC95575B0A71E73596384360ADC382C651EE4C8BA067DD4313C4BE6C7C4` | `PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY` |
| NIV | .005 | 120 | `RUN_KMPC_120_P5_3G7_C2_NIV_K0p005_SUPPORT_06_08_CHECKPOINT_RESUME.json` | `D6350636F9BA27C541EF8CDC2585ED370E2F1E2EB35495E01198A8BAA47AB136` | `PASS_C2_NIV_K0p005_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY` |
| NIV | .15 | 126 | `RUN_KMPC_126_P5_3G7_C2_NIV_K0p15_SUPPORT_06_08_MULTI_RANK_REFINEMENT.json` | `1D46AFD1CDEB650A7787A5E6FE9E2304A5212FF1FE9AA47657BEAAAA557B8AA0` | `PASS_C2_NIV_K0p15_SUPPORT_06_ADEQUATE_CANDIDATE_ONLY` |

Exact identity každého rawu je
`{"mode": MODE, "k_Mpc_inverse": K, "variant": "nominal"}`.
Povolený execution status je iba
`TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR_AUDIT`.

## 3. Frozen brány a prah

- expected/observed register: presne `5×2=10`, bez duplicity;
- každý raw: exact SHA, identity, candidate a execution status;
- každý raw: `core_pass is True`, `common_pass is True`,
  `tail_pass is True`, `background_guard.pass is True`;
- oba `by_a` riadky a všetky štyri observed background veličiny musia
  existovať, byť číselné a konečné;
- relatívny spread je
  `(max(values)-min(values))/max(max(abs(values)),1e-300)`;
- frozen limit každej z ôsmich spread metrík je `<=1e-12`;
- žiadny vybraný názov, status ani candidate nesmie byť technical failure.

## 4. Rozhodovací strom

- chýbajúci súbor/kľúč, zlá SHA/identity/candidate, duplicita alebo
  nekonečná hodnota → technický exit `2`, bez aggregate rawu a bez fyziky;
- technicky platný register, ale niektorá atómová brána alebo spread FAIL →
  `REVIEW_C2_AGGREGATE_GATE_UNCLOSED`;
- všetko PASS →
  `PASS_C2_FOURIER_COVERAGE_10_OF_10_CANDIDATE_ONLY`.

Skript nevydáva autoritatívny verdikt. Ten môže po internom audite zapísať
iba hlavný orchestrátor. Ani PASS nemení K4 `60/100`; iba odblokuje C3.

## 5. Artefakty a preflight

- base:
  `scripts/baseScripts/p5_general_synchronous/c2_authoritative_atom_aggregate.py`;
- runner:
  `scripts/371_script_KMPC_127_P5_3g7_C2_authoritative_atom_aggregate.py`;
- raw:
  `scripts/results/k_mpc_005/RUN_KMPC_127_P5_3G7_C2_FOURIER_COVERAGE_AUTHORITATIVE_AGGREGATE.json`;
- interný limit: `4.8 s`; vonkajší limit najmenej `10 s`;
- povinne pred official: base/runner `py_compile`, `--help`, behaviorálny
  `--smoke`, output-absence guard a negatívny missing-input test v čerstvej
  kópii.

## 6. Nonclaims

Bez C3 `gamma0/af0`, fyzickej S-M dvojice, full hierarchy, finite opacity,
P5.4/ODE, G8/G9, CLASS/CMB/BBN/S8/H0, dátového fitu a bez zmeny teórie.

## 7. Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | C2 atómový register dosiahol scoped PASS `10/10`; EA-028 zapečatený | `AGGREGATE_AUTHORIZED` |
| 2026-07-19 | register, hashe, identity, brány, spread vzorec, prah a rozhodovací strom zmrazené pred vytvorením/spustením Pythonu | `PREREGISTERED_NOT_RUN` |
| 2026-07-19 | base SHA `69E0C35CDC871CEB5185C51D35A3F26D3B26FD4D6117DC443E6E16CB7EEE8EEC`; runner SHA `EE25391AC56D561FF7B9E1FFD38F23906772CE763C1EF045EAB56A38F223F6FC`; cieľový raw neexistuje | `FROZEN_BEFORE_PYTHON` |
| 2026-07-19 | base+runner compile exit 0; help exit 0; smoke exit 0 v 0.144 s, 4/4 checks; fresh-copy vetva bez KMPC-126 exit 2 v 0.391 s a nevytvorila output | `PREFLIGHT_PASS_OFFICIAL_AUTHORIZED` |
| 2026-07-19 | official exit 0 za 0.189 s; raw SHA `CA33E4167953F2112AFF13E186E7D8E47A135FE947B837D63CCE5F7F5B0D247F`; candidate PASS; interný audit dokument 199 | `C2_AGGREGATE_PASS_C3_UNLOCKED_SCORE_UNCHANGED` |
