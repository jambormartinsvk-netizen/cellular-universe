# KMPC-097 — HP-M1 matrix provenance: diagnostická predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `4/10`

## Dôvod a jediný cieľ

KMPC-094 aj KMPC-096 skončili ešte pred vznikom fyzikálneho výsledku na
`mpmath.qr_solve: matrix is numerically singular`. KMPC-095 sa k official
behu nedostal pre chybu syntetického fixture. Stĺpcová ekvilibrácia v
KMPC-096 pád neodstránila. Ďalšia slepá výmena solvera preto nie je povolená.

KMPC-097 je iba diagnostika pôvodu M1 matice. Porovná:

1. natívne zostavenú 80-dps redukovanú M1 maticu a pravú stranu po projekcii
   do binary64;
2. nezávisle znovu zostavenú zmrazenú binary64 M1 maticu a pravú stranu z
   live `mode_resolved_puiseux_v2_m1_anchored` kontraktu.

Report musí uviesť hashe, rank, spektrum singulárnych hodnôt, condition,
nulové riadky/stĺpce, počet odlišných prvkov, maximálny a normový rozdiel aj
identitu najhoršieho riadka a stĺpca.

## Diagnostický bridge a zákaz fyzikálneho PASS

Aby mohla nezmenená downstream atribučná cesta dobehnúť, KMPC-097 smie raz
použiť `numpy.linalg.lstsq` nad binary64 projekciou **natívnej** matice. Tento
výpočet je výslovne `DIAGNOSTIC_BRIDGE_NOT_HP_M1_SOLVE`:

- nepočíta sa ako autoritatívny high-precision M1 solve;
- nesmie vydať `pass_c2_atom_candidate=true`;
- nesmie meniť skóre, prahy, support ani verdikty;
- výsledný kandidát je vždy
  `REVIEW_C2_BI_K0p15_HP_M1_MATRIX_PROVENANCE_DIAGNOSTIC_COMPLETE`;
- `physics_verdict_role` musí byť `DIAGNOSTIC_ONLY`.

F0, fractional background, M3, holdout non-fit kontrakt, rovnice, vstupy,
support `[0,7]`, `80 dps` a všetky prahy ostávajú nezmenené.

## Predregistrovaná interpretácia

- Ak obe projekcie majú rank `98/98` a iba malé rozdiely zodpovedajúce
  binary64 verzus natívnym racionálnym koeficientom, blokér sa lokalizuje na
  numerické správanie `mpmath.qr_solve`; až potom možno navrhnúť samostatne
  predregistrovaný rank-revealing HP solver.
- Ak natívna projekcia stratí rank alebo sa matice materiálne rozchádzajú,
  ďalší krok musí auditovať konkrétny riadok/koeficient zostavenia pred
  akoukoľvek zmenou solvera.
- Compile/help/smoke/official pád je iba
  `TECHNICAL_ERROR / NO_PHYSICS_VERDICT` a zvýši counter.
- Úspešný vecný diagnostický výsledok môže po internom audite resetovať
  technický counter, ale nemení C2 skóre ani autoritatívny stav A2-K4.

## Zmrazená implementácia pred prvým Python behom

- V5 matrix-provenance modul:
  `8C15D74DC752C07986DA95EB350CEE3C11C7917F317125F020A05047B634AC52`;
- runner 341:
  `5A3A1B86172D17D45965D85E1B9475F7CE9C3D398E6F234A78961E61A5044874`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `34/34` source a `12/12` prerequisite hashov sedelo;
  všetkých `49` dlhých hash výskytov malo presne 64 hex znakov.

Od tohto bodu sú modul a runner pre prvý Python beh zmrazené. Zmena po
prvom behu vyžaduje nový successor, nové ID a nový zápis v error ledgeri.
