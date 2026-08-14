# A2-K7 — dôkazový dodatok skriptu 62 a M-014d1b

**Dátum:** 2026-07-13  
**Algoritmus:** SHA-256  
**Nadväzuje na:**
`Audit/A2_K7_K3_1_K2_1_TO_M014d2a_EVIDENCE_MANIFEST_SHA256.md`  
**Dôvod dodatku:** pôvodný manifest je zapečatený a nesmie sa ticho meniť

## Reprodukčný príkaz

```text
python scripts/62_script_A2_K7_K3_1_K2_2_K1a2a_incoherent_KMS_graviton_transition.py
expected exit: 1
verdict: DEAD_M014d1b_INCOHERENT_KMS_GRAVITON_TRANSITION
```

Nenulový exit je predregistrovaný kill výstup listovej koľaje, nie runtime
chyba.

## Hashy

```text
791e08995f50de8518281069aad07edd430f31afee3c8bfda4a119930fc39628  scripts/62_script_A2_K7_K3_1_K2_2_K1a2a_incoherent_KMS_graviton_transition.py
53b39b30a6837e00b0db21aac5d9f743cbe1d59286d04786960a069611fc97dc  Audit/A2_K7_K3_1_K2_2_K1a_SCOPE_ERRATUM_AFTER_SCRIPT62.md
4eba6854c6d74e8a18b57aa06ac4a57c007e803d1a0f20db7ea39856162f878f  Audit/A2_K7_K3_1_K2_2_K1a2a_incoherent_KMS_graviton_transition_audit.md
c84d5d6673363b72524a437411e065167bad996f38b5439f431d957bbb2873f7  Audit/A2_K7_K3_1_K2_2_K1a2a_NUMERICAL_OUTPUT_62.md
ac682c629a3c8f09f2293e7f20020aaab9024fb7c6f73913abdb2171fbccd8cd  Audit/A2_K7_PODKOLAJE_KANONICKY_STAV_A_MAX_HLBKA.md
add95f390da5861ffaac71c5eb85d7a121323dfc69ecb8a0d575aa0b707af8f5  Questions/A2_K7_K3_1_K2_2_K1a_gravitational_transition_subtracks.md
7c6f0d85e216f5ff43385e13972f3e464875a44f08d807ba24775fe0cc23cbc4  Questions/A2_K7_STAV_A_AKCNY_PLAN_PO_M014d1b.md
c17b4a92adfda27e60ba4858784d3045b319602977ab9b63b09b45b6fc4a6884  Questions/A3_STAV_A_AKCNY_PLAN_PO_K7_M014d1b.md
7cc985bb86ac649686b793d858b404487a3c95d45290306dd0f55b3b72d5de89  Questions/00_READ_FIRST_A2_Q20_AFTER_K7_M014d1b.md
f911127df8697c686d5ec973a24e9b30abd91bbf85129a0f4857182dd4b7bd61  Questions/00_READ_FIRST_A2_Q20_CURRENT_STATE.md
b74fdb1d6002610e7301c47f785018d1f4111f425070e19425c8e3974a9fd5ff  theory/SK/05w_Methodology_Rules_and_Question_Register_A2_K7_M014d1b_SK.md
ff746ff9e5edf22dfa8a04fd573c924670c6fc1ac559095be68235581cb1eaa5  theory/EN/05w_Methodology_Rules_and_Question_Register_A2_K7_M014d1b_EN.md
```

## Kanonická zmena voči starému manifestu

- M-014d1 sa obmedzuje na K1a1 thermal-scattering realizáciu;
- K1a rodič sa znovu označuje ako otvorený cez K1a2b;
- K1a2a zomiera samostatne ako M-014d1b na hĺbke `42/100`;
- K1a2c sa nemaže, ale presúva do vákuovej/farebnej K2;
- K1b2 zostáva živá a čaká;
- akceptované skóre K7 zostáva `30/100`.

