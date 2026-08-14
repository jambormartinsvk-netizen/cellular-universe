# P3a-B skript 206 — source-delta predbehové očakávania

Dátum: 2026-07-15  
Typ: AST/source audit bez importu a bez evolúcie  
Score effect: `NONE`

## Zmrazené zdroje

- základ 197:
  `088B4CD58F57A30BD061D30042BA3E2CB5021DF9BF320003ED8291D86FB6C022`;
- kandidát 205:
  `B7EC8BAD3BFB0D48EC91D6F1BB0A602FA1834A021BB94C92D6D1B398D5F3CDC2`.

## Očakávaný PASS

Skript 206 nesmie zdroje importovať ani spúšťať. AST audit musí potvrdiť:

1. rovnaké `SOURCE`, `NAMES`, backgroundové konštanty a seed/scale
   výrazy;
2. funkcie `background`, `scaled_rhs` a `integrate_fixed_rk4` sú AST
   zhodné;
3. telo `physical_rhs` pred returnom je AST zhodné;
4. return obsahuje rovnakých 13 komponentov;
5. komponenty 0–6 a 8–12 sú AST zhodné;
6. aditívny rozklad komponentu 7, `M'`, nemá žiadny nový člen a chýbajú
   presne dva predregistrované nulové členy;
7. tri volania RK4 mriežok a ich kroky sú AST zhodné;
8. oba zdrojové hashe sú presné.

Rozdiely v docstringu, parseri, provenance, názve checkpointu, verdict
logike a fail-closed JSON exporte sú auditná vrstva a nepovažujú sa za
fyzikálnu zmenu.

PASS povoľuje až ďalší corpus checker a formálny preflight 205. FAIL
znamená REVIEW a zákaz evolúcie; timeout alebo chyba je tiež REVIEW.
Interný limit je 5 s, externý 10 s.
