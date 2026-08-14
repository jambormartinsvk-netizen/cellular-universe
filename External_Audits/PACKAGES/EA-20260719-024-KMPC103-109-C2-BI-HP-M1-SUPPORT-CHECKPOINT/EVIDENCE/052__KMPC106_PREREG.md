# KMPC-106 — HP-M1 support checkpoint: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `3/10`

## Dôvod a jediná dovolená zmena

KMPC-105 opravil identitu predchodcu a prešiel compile/help/smoke, ale
monolitické spojenie natívneho 80-dps CPQR, dvoch F0/M3 support solve a
exact 104×104 driver/holdout prekročilo vnútorný limit `45 s` (`PF-107`).
Limit, rovnice ani prahy sa nezvyšujú. Výpočet sa delí na dva immutable,
hashovo previazané runtime segmenty.

KMPC-106 je prvý segment a smie vykonať iba:

1. nezmenený natívny 80-dps M1 CPQR z V9;
2. accepted support `[0,5]` a audit support `[0,7]` cez zmrazené F0/M3;
3. nezmenené common, tail, S-C0, R-fs a background brány;
4. vytvorenie verdict-free checkpointu pre samostatný KMPC-107 resume.

Exact driver, independent non-fit holdout a C2 fyzikálny PASS sú v tomto
atóme zakázané.

## Checkpointový kontrakt

- jedenásť HP-M1 stavov sa ukladá v autoritatívnom poradí ako 90-digit
  desatinné reťazce a pri 80 dps sa musí obnoviť presná `mpf` hodnota;
- `delta_f,U_f` z audit F0 sa ukladajú ako `float.hex()` a musia sa obnoviť
  bitovo identicky;
- kombinovaný 13-stavový register musí zachovať autoritatívne poradie;
- serializovaný M1+F0 register dostane samostatný SHA-256 odtlačok;
- KMPC-107 smie pokračovať iba z presného SHA celého raw KMPC-106 a musí
  znovu overiť schema, poradie, round-trip a odtlačok registrov;
- `pass_c2_atom_candidate=false`, `physics_verdict_role` je iba checkpoint.

## Rozhodovací kontrakt

- technický výsledok je publikovateľný iba ak CPQR, M1, accepted/audit
  support, merge, serialization round-trip, common/tail/S-C0/background a
  restore checks prejdú;
- interpretácia úspechu je iba
  `REVIEW_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_COMPLETE`;
- timeout/import/hash/schema/serialization chyba je technická, zvýši counter
  a nevydá fyzikálny verdikt;
- úspešný checkpoint je vecný reprodukovateľný medzivýsledok a resetuje
  aktívny counter, ale nemení C2 `5/10`, P5 `3.5/6` ani K4 `60/100`.

## Zmrazená implementácia pred prvým Python behom

- V13 checkpoint:
  `301E3121DA9E260308FB46E6011A9694BA79676EE57F653DCCD3D472C4C44A78`;
- runner 350:
  `978D5D4CBDC814B393AD5D1098BEF54123C9AAB80741BBEB145EEBCB29442E1F`;
- prior runner 349:
  `1AA37C77A9992424EB7878C9056DD6AF4A48609149148F4F9663CEAE9C8D146E`;
- PF-107 failure raw:
  `DAF1A456678310A12E3D5A3E46EECF23A4421F502384775A5099577915239EC3`;
- výsledný literal contract: `42` source a `17` prerequisite položiek;
- harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- interný aj CLI official limit: presne `45.0 s`.

Pred vytvorením tejto predregistrácie nebol V13 ani runner 350 spustený cez
Python. Od tohto bodu sú V13 a runner 350 immutable.
