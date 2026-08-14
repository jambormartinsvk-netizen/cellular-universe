# KMPC-109 — checkpoint read-only receipt: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `6/10` do overenia už publikovaného raw

## Dôvod a scope

KMPC-108 publikoval raw SHA
`683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995`
a vytlačil summary, ale host shell skončil external timeoutom 124 po publish
(`PF-110`). Výpočet sa pre immutable target nesmie opakovať.

KMPC-109 je iba read-only receipt. Nesmie spustiť CPQR, F0, M3, exact driver
ani žiadnu rovnicu. Overí:

- presný SHA raw a source-hash ledger;
- checkpoint schema a autoritatívne poradie 11 M1 + 2 fuel stavov;
- nový výpočet serialized-state fingerprintu vo frozen poradí;
- decimal90 a float-hex round-trip flags;
- presných šesť `mpf` publish konverzií a ich cesty;
- presnú raw false množinu
  `{audit_support_complete, pre_exact_core_complete}`;
- presnú audit false množinu `{M3_driver}`;
- PASS M1, accepted, audit F0, M3 rank/production contract/independent
  holdout, common, tail, S-C0 a background;
- zachovaný zákaz C2 PASS.

Ak a iba ak všetky receipt checks prejdú, výsledok smie byť
`REVIEW_C2_BI_K0p15_HP_M1_CHECKPOINT_RECEIPT_EXACT_RESUME_ALLOWED`.
To nie je fyzikálny PASS: povoľuje iba samostatne predregistrovaný exact
driver/holdout resume, ktorý rozhodne, či float64 `M3_driver` bol numerický
artefakt alebo zostáva vecným blockerom.

## Zmrazené hashe pred prvým Python behom

- V16 receipt:
  `96B95FF8E43F782494ED4B50C2A03A0856810C03297ED760991F4AF393CB7484`;
- runner 353:
  `A390718F258FE47408888EFD6A825A5387D5C6573E8B66FF1AF5E81B2D3CAE57`;
- published runner 352:
  `1308134805BC339551177C7FA78C3379F4A2AB0D2BE90E68B26732ECBA7E4A48`;
- raw KMPC-108:
  `683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995`;
- serialized-state fingerprint:
  `402B42E11C3582B4E3E46D047EA917A4C256E552F65C9DB070589150675EBF40`;
- výsledný contract: `45` source a `19` prerequisite položiek;
- stable harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- smoke aj official limit presne `4.8 s`.

Pred vytvorením tejto predregistrácie nebol V16 ani runner 353 spustený cez
Python. Od tohto bodu sú V16 a runner 353 immutable.
