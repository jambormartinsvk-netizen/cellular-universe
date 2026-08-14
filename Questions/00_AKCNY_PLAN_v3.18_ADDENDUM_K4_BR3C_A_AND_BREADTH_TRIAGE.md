# Akčný plán v3.18 — po K4 BR3C-a a bod breadth triage

**Dátum:** 2026-07-14  
**K4:** `ŽIVÁ; 66.2/100; G6 PASS; G7 OTVORENÁ`

| Poradie | Úloha | Bod po PASS | Možná hĺbka | Stav |
|---:|---|---:|---:|---|
| 1 | BR3C-b: obe skoré evolúcie dobehnú v limite | `+0.3` | `66.5` | **NEXT** |
| 2 | úplný evolučný species/mode ledger | `+0.2` | `66.7` | PENDING |
| 3 | zhoda oboch štartov na spoločnom neskoršom bode | `+0.3` | `67.0` | PENDING |
| 4 | `00`, `0i`, trace a traceless rezíduá | `4 x +0.1` | `67.4` | PENDING |
| 5 | kroková, tolerančná a `lmax` konvergencia | `3 x +0.2` | `68.0` | PENDING |
| 6 | breadth triage K8/K9 a re-entry K7/K11/K12 | nemení K4 | podľa vlastných G1–G3 ledgerov | PENDING PRED BR4 |
| 7 | BR4 plný backend | `+1.0` | `69.0` | PENDING PO TRIAGE |
| 8 | coupled transfery a integrovaný G7 rozsudok | `+1.0` | `70.0` | PENDING |

## Trigger skoršieho breadth triage

Triage sa presunie pred aktuálny ďalší krok iba ak:

- K4 dostane robustný fyzikálny dôvod smrti; alebo
- rovnaká technická stena zostane po troch po sebe idúcich časovo
  ohraničených opravných revíziách a ďalší zásah by už nebol lacný.

Timeout jedného behu nie je trigger ani fyzikálna smrť.

## Povinné limity BR3C-b

- vnútorný limit jedného behu najviac `50 s`;
- vonkajší limit najviac `60 s`;
- checkpoint pred každým predĺžením integračného intervalu;
- bez tichých nulových species alebo multipólov;
- pôvodné 130/131/133 zostávajú zachované ako REVIEW/ERROR dôkazy.

