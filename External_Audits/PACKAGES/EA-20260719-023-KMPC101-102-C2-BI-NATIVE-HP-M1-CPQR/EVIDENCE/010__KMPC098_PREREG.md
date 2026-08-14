# KMPC-098 — HP-M1 combined-register successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `6/10`

## Izolovaná príčina PF-101

KMPC-097 corrected smoke prešiel a official v pamäti vykonal V5 matrix
provenance aj disclosed binary64 bridge. Následne pôvodný KMPC-093 handoff
nahradil celý 13-stavový combined standard register iba 11 stavmi, ktoré
vlastní M1 reassembly. Downstream atribúcia preto skončila `KeyError:
delta_f`; failure SHA je
`9B1B10318E1AC54D1CE710BAADE4B36AE29C78C3E3298E67C7963194AF2F19E5`.

## Jediná povolená oprava

V6 po M1 reassembly vytvorí combined register v autoritatívnom poradí 13
stavov, nahradí iba 11 stavov uvedených v `STATE_TO_LEGACY` a zachová
existujúce fuel-owned `delta_f,U_f`. Pred a po merge reportuje fingerprint
oboch fuel stavov a vyžaduje ich úplnú hodnotovú zhodu.

V5 matrix-provenance diagnostika, binary64 bridge, V1–V4 matematika, rovnice,
vstupy, support `[0,7]`, 80 dps, F0/fractional background/M3 generátory,
non-fit holdout a prahy ostávajú byteovo nezmenené.

## Zákaz fyzikálneho PASS a interpretácia

KMPC-098 zostáva `DIAGNOSTIC_ONLY`. Aj pri úspešnom dokončení musí mať:

- `pass_c2_atom_candidate=false`;
- `authoritative_high_precision_m1_solve_count=0`;
- kandidáta
  `REVIEW_C2_BI_K0p15_HP_M1_MATRIX_PROVENANCE_DIAGNOSTIC_COMPLETE`;
- nulový score/verdict/prediction-table/release dopad.

Úspešný výsledok sa interpretuje výhradne podľa matrix pravidiel zmrazených v
predregistrácii 160. Compile/help/smoke/official pád je iba
`TECHNICAL_ERROR / NO_PHYSICS_VERDICT` a zvýši counter.

## Zmrazená implementácia pred prvým Python behom

- V6 combined-register modul:
  `1332758076A50FC3EE8160786357E8BD04B7964307D7C3BB673F0167379D2B9A`;
- runner 342:
  `53DD70E945200037DD1A5526485F4A59BCD299A50BFA660FD16C41744465B74E`;
- V5 matrix-provenance modul ostáva
  `8C15D74DC752C07986DA95EB350CEE3C11C7917F317125F020A05047B634AC52`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `35/35` source a `12/12` prerequisite hashov sedelo;
  všetkých `50` dlhých hash výskytov malo presne 64 hex znakov.

Od tohto bodu sú V6 a runner 342 pre prvý Python beh immutable.
