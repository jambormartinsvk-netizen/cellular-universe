# A2-K4.3a — manifest a SHA-256

**Dátum zapečatenia:** 2026-07-14  
**Rozsah:** predregistrácia, audit, reprodukčný skript, výstup, stav a SK/EN register

## Verifikačný stav

- `python -m py_compile scripts/72_script_A2_K4_3a_species_ledger_and_anisotropic_stress_audit.py`: **PASS**;
- skript 72: exit code `0`, `PASS_K4_3A_LEDGER`, 9/9 kontrol `true`;
- všetky symbolické rezíduá: presne `0`;
- kontrola placeholderov `TODO`, `TBD`, `file:///`, interných citačných tokenov: bez nálezu;
- kanonické skóre po audite: K4 `60/100 = G6`; G7 otvorená.

## Súbory

| Súbor | Bajty | SHA-256 |
|---|---:|---|
| `Questions/A2_K4_3_G7_PROBLEM_PODBRANY_A_KILL_KRITERIA.md` | 4658 | `38eda7ab439a72b917d4bb6862d7795cbed3de35caa024f23eef9c937999e4f6` |
| `Audit/A2_K4_3A_SPECIES_LEDGER_ANISOTROPIC_STRESS_AND_NULL_AUDIT.md` | 8043 | `87c47334f1a7cca20a44cd6d5294ac0d0d8513ac488f295f5595669fdbafa632` |
| `scripts/72_script_A2_K4_3a_species_ledger_and_anisotropic_stress_audit.py` | 4492 | `41c05b563dc4e036b76cc89d79d7923f26e3dcff00af4a5af171c067ffb96562` |
| `scripts/OUTPUT_A2_K4_3A_72.md` | 1939 | `229dd7dc7b01bc0864adcc94ef4e034b54004adaf2071354eb6baf4926ffa46a` |
| `theory/SK/05zzzz_Methodology_Rules_and_Question_Register_A2_K4_3a_SK.md` | 1954 | `5cee61b2b3afddbfee4a7347f8d32c9c39911fda6322663b77ad331af9bedadd` |
| `theory/EN/05zzzz_Methodology_Rules_and_Question_Register_A2_K4_3a_EN.md` | 1998 | `684b4d30c0877b005fcb587e54ce45eb638c7feab77b3ad6875270c4edcba7f6` |
| `Questions/00_READ_FIRST_A2_Q20_AFTER_K4_3A.md` | 2150 | `166315ac46630ec71179a683ffd9cdf61ca18fc1728e988af778dbca7e5e1596` |
| `Questions/A2_K4_3A_STAV_A_AKCNY_PLAN.md` | 2492 | `d16ca341d0c6f3b984b3462dee8166fef88608f38a697582f29d59beee3562f0` |
| `Audit/A2_K4_3A_SCORE_AND_CATALOG_ADDENDUM.md` | 1760 | `a8bb35b7483da35d73cfad6d636fbfd8bb2f263aa5ee1279c6b9dad6096ad699` |
| `Audit/A2_K4_3A_GLOBAL_STATE_ADDENDUM.md` | 855 | `553d198a1c0967f3a8dcc02319986a2dba4d61ff096a9ede2c528a90203ed08d` |

## Poznámka k nemennosti

Ak sa ktorýkoľvek z uvedených súborov zmení pri K4.3b, musí sa vytvoriť
nový manifest alebo changelog. Tento manifest sa nesmie potichu prepísať tak,
aby predstieral pôvodný K4.3a snapshot.

