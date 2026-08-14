# Akčný plán v3.18 — po K4 BR3C-b

**Dátum:** 2026-07-14  
**K4:** `ŽIVÁ; 66.5/100; G6 PASS; G7 OTVORENÁ`

| Poradie | Úloha | Bod po PASS | Možná hĺbka | Stav |
|---:|---|---:|---:|---|
| 1 | C7.7c: evolučný species/mode ledger | `+0.2` | `66.7` | **NEXT** |
| 2 | C7.7d: deep/shallow endpoint agreement | `+0.3` | `67.0` | PENDING |
| 3 | štyri nezávislé Einsteinove rezíduá | `4 x +0.1` | `67.4` | PENDING |
| 4 | kroková, tolerančná a `lmax` konvergencia | `3 x +0.2` | `68.0` | PENDING |
| 5 | breadth triage K8/K9 a re-entry K7/K11/K12 | nemení K4 | vlastné G1–G3 | PENDING PRED BR4 |
| 6 | BR4 plný backend | `+1.0` | `69.0` | PENDING |

## Povinný audit C7.7c

- všetkých 13 komponentov musí byť prítomných v každom móde a povrchu;
- každý dynamický komponent musí mať nenulový RHS alebo zdokumentovanú
  symetriu/rád, ktorý jeho nulu vynucuje;
- `U_c=0` a `L5=0` sa vedú ako explicitné scope limity, nie ako skryté PASS;
- porovnať component maxima a checkpointové zmeny, nie iba konečný JSON key;
- NIV vysoký `nfev` sa zachová ako otvorené konvergenčné riziko.

