# Scope — KMPC-101/102 native 80-dps HP-M1 CPQR

- Package ID: `EA-20260719-023-KMPC101-102-C2-BI-NATIVE-HP-M1-CPQR`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Potvrdzuje KMPC-102 na natívne zostavenej 80-dps reduced M1 matici
`121×98`, že rank-revealing dvojpriechodový MGS-CPQR má plný stĺpcový rank
`98/98`, zachováva pôvodný nevážený least-squares cieľ a spĺňa vopred
zmrazené brány ortogonality, faktorizácie a normálového reziduálu? Uzatvára
tým starú `mpmath.qr_solve: numerically singular` výnimku ako algoritmický
problém nepivotovaného solvera? Je PF-104 iba canonical-output routing chyba
pred výpočtom?

## Poradie čítania

1. Evidence 001–004: R4 protokol, C2 kontrakt a upstream atribučné východisko.
2. Evidence 040–042: KMPC-101/102 predregistrácie a interný audit výsledku.
3. Evidence 043–044: PF-104 failure raw a vecný KMPC-102 raw.
4. Evidence 045–048: oba runnery, V9 calculation a V10 routing wrapper.
5. Evidence 013–017: aktualizované technické registre, stav a predošlý audit.
6. Dokument 03 a dve izolované fresh-copy reprodukcie.

## Nonclaims

- Nie je to finálny BI/k=.15 C2 PASS ani fyzikálny STOP.
- M1-local non-fit holdout nie je finálny C2 holdout po F0/M3 handoffe.
- CPQR diagonály nie sú singular values a ich ratio nie je condition number.
- V9 nemení rovnice, support, anchor ani fyzikálne prahy; row scaling je nulový.
- C2 zostáva `5/10`, P5 `3.5/6` a K4 `LIVE / 60/100`.

## Predregistrované hodnotenie balíka

`PASS_PACKAGE_CLAIM` vyžaduje:

- source/copy a runtime paritu;
- reprodukciu PF-104 s exitom 2 v `guarded_import`, presným failure SHA a bez
  volania M1/CPQR;
- KMPC-102 compile/help/smoke/official exit 0 v samostatnej čerstvej kópii;
- field-level paritu generated KMPC-102 voči Evidence 044 okrem jediného
  poľa `runtime_seconds`;
- shape `121×98`, rank `98/98`, jeden native HP solve, bez row scalingu;
- `orthogonality <=1e-60`, `factorization relative <=1e-60` a
  `normal residual relative <=1e-55`;
- physics PASS polia false a `pass_c2_atom_candidate=false`.

Iný výsledok je `REVIEW_REPRODUCTION_MISMATCH`, nie fyzikálny verdikt.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
