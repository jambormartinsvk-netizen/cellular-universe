# KMPC-099 — standalone M1 matrix provenance: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `7/10`

## Dôvod samostatného rezu

KMPC-098 potvrdil opravu combined registra, ale zdedená KMPC-088 atribučná
brána vyžadovala reprodukciu starého KMPC-087 residualu. Ten po
diagnostickej zmene M1 nie je invariant. Brána ani jej tolerancie sa nesmú
uvoľniť; matrix otázka sa preto oddelí od celej downstream pipeline.

## Presný rozsah KMPC-099

Atóm vykoná iba:

1. jeden zmrazený binary64 hard-anchored M1 reference solve pre 11-stavový
   referenčný vektor;
2. natívne 80-dps zostavenie M1 affine systému bez autoritatívneho HP solve;
3. V5 porovnanie natívnej matice po binary64 projekcii s nezávislým frozen
   binary64 rebuildom;
4. jeden disclosed `numpy.linalg.lstsq` bridge nad natívnou projekciou iba na
   výpočet diagnostických residualov.

Atóm sa zastaví pred F0, M3, holdout atribúciou a všetkými C2 fyzikálnymi
bránami. Nesmie volať KMPC-088 reconstruction gate.

## Povinný výstup a interpretácia

Raw musí obsahovať shape, hashe matrix+rhs, ranky, condition, najmenšie
singulárne hodnoty, nulové riadky/stĺpce, počty a maximá rozdielov, najhorší
riadok/stĺpec a úplné solve-count priznanie.

- `rank(native)=rank(frozen)=98` lokalizuje predošlé `mpmath.qr_solve`
  výnimky na HP solver/algoritmickú hranicu, nie na binary64-projected rank.
- Rozdiel rankov lokalizuje ďalší krok na assembly riadok/koeficient.
- Spoločný rank pod 98 znamená spoločnú rank deficiency a zakazuje návrh
  plnorankového HP solve bez novej algebraickej analýzy.

Hodnota rozdielu matíc sa reportuje bez dodatočne vymysleného PASS prahu.
Žiadna z vetiev nie je fyzikálny verdict.

## Zákazy

- `authoritative_high_precision_m1_solve_count=0`;
- `pass_c2_atom_candidate=false`;
- kandidát iba
  `REVIEW_C2_BI_K0p15_HP_M1_MATRIX_PROVENANCE_DIAGNOSTIC_COMPLETE`;
- žiadna zmena skóre, supportu `[0,7]`, rovníc, vstupov, prahov,
  prediction table, release ani Zenodo;
- technický pád je `TECHNICAL_ERROR / NO_PHYSICS_VERDICT`.

## Zmrazená implementácia pred prvým Python behom

- V7 standalone modul:
  `B2CF9C98734303122F82CE85D4BE2D560EA853126EFC447E82C05EAAB77CE9E0`;
- runner 343:
  `B391FB0FB497922BB63C0F528CA3A5699B47E645B610A4D13084BE1357E1A5BD`;
- V5 matrix-provenance modul ostáva
  `8C15D74DC752C07986DA95EB350CEE3C11C7917F317125F020A05047B634AC52`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `36/36` source a `12/12` prerequisite hashov sedelo;
  všetkých `51` dlhých hash výskytov malo presne 64 hex znakov.

Od tohto bodu sú V7 a runner 343 pre prvý Python beh immutable.
