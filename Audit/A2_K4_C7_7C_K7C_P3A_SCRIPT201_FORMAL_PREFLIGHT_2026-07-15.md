# P3a-A skript 201 — formálny preflight

Dátum: 2026-07-15  
Fyzika v tomto audite vykonaná: **nie**

## Zmrazené artefakty

| Artefakt | SHA-256 |
|---|---|
| `scripts/201_script_A2_K4_C7_7c_K7c_P3a_exact_zero_identity_audit.py` | `03AA42272D05B8031EC54A39209275EE6B15D448FFE7204AA20EE25967FCAF38` |
| `scripts/202_script_python_corpus_status_audit_after_K7c_P3a_script201.py` | `31E04B16F4DEDF1AA05A7750DCFF67753F85FCF98CD9BBB0AD8BE34771592B8C` |
| `Audit/A2_K4_K7C_P3A_CORPUS_CHECKER_202_2026-07-15.json` | `A9DA15341EF99C4019DD0B7871E291546BDF8F945FBEC0F7A019BE75C111FF4B` |
| `Questions/A2_K4_C7_7C_K7C_P3A_SCRIPT201_PRERUN_2026-07-15.md` | `FB1E05B2270366B9D787006367FA85A21C79D5FA8D0E8C9BE0C5C8BE0063D053` |

## Kontroly

- presne jeden `__main__` entry point: PASS;
- neúplný marker/TODO/FIXME: neprítomný;
- import/volanie `solve_ivp`, DOP853, Radau, subprocess, importlib alebo
  `exec`: neprítomné;
- autoritatívny P3a raw výstup pred behom: neprítomný;
- priamy Python `3.11.3`: PASS;
- `py_compile`: PASS;
- `--help`: PASS;
- `--smoke`: PASS, `physics_executed=false`,
  `new_ODE_executed=false`, štyri očakávané plochy;
- checker 202: `PASS_SCRIPT_CORPUS_INVENTORY`, 206 ostatných skriptov,
  71 karanténnych, iba historické syntax chyby 118/119;
- cieľ 201: `NOT_IN_QUARANTINE`, checker ho neimportoval ani nespustil.

Prvý široký statický marker a prvý združený PowerShell Python preflight sú
technicky neplatné a sú zapísané ako PF-028/PF-029. Nemajú fyzikálny
výsledok. Samostatné opravené preflighty prešli.

## Rozhodnutie

Skript 201 je formálne povolený na jeden predregistrovaný P3a-A beh s
interným limitom 5 s, externým limitom 10 s a novým výstupom
`Audit/A2_K4_K7C_P3A_ZERO_IDENTITY_RAW_2026-07-15.json`.
Preflight nepridáva body a nepovoľuje P3a-B bez fyzikálneho PASS.
