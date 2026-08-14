# A2-K11-CS2 — immutable result manifest

**Aktuálny autoritatívny technický výsledok:** attempt 5 source-AST PASS  
**Fyzikálny účinok:** žiadny; K11 zostáva `10/100 = G1`

| Výsledok | Stav | Dôvod |
|---|---|---|
| `RUN_A2_K11_CS2_S0_001.json` | diagnostický, external timeout | PF-061 |
| `RUN_A2_K11_CS2_S0_002.json` | formula regression / STOP state register | PF-062 extra `E_0,E_1` |
| `RUN_A2_K11_CS2_FULL_V002_ATTEMPT1_SMOKE.json` | smoke PASS, neautoritatívny full scope | iba L4 |
| `RUN_A2_K11_CS2_FULL_V002_ATTEMPT1.json` | diagnostický PASS payload / external timeout 124 | PF-065, internal 3.25 s |
| `RUN_A2_K11_CS2_FULL_V002_ATTEMPT2_L4.json` | diagnostický PASS / stale attempt ID | PF-066; L6/L8 zámerne nebežali |
| `RUN_A2_K11_CS2_FULL_V002_ATTEMPT3_L4.json` | diagnostický PASS payload / external timeout 124 | PF-065; L6/L8 zámerne nebežali |
| `RUN_A2_K11_CS2_FULL_V002_ATTEMPT4_SOURCE_AST.json` | diagnostický 55/55 / external timeout 124 | PF-067 eager package init |
| `RUN_A2_K11_CS2_FULL_V002_ATTEMPT5_SOURCE_AST.json` | **AUTORITATÍVNY STRUCTURAL PASS** | 55/55, counts 25/33/41, exit 0, hash `2180093D79D0D449CAA056507819FB7EB349013958CD808192F572728892EE58` |

Attempt 5 neobsahuje ODE, thermal/TCA/HyRec, constraint propagáciu ani
evolučnú `lmax` konvergenciu. Nesmie sa citovať ako fyzikálny PASS K11.
