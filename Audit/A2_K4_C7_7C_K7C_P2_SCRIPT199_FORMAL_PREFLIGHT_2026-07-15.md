# K7c P2 / skript 199 — formálny preflight pred vedeckým behom

Dátum: 2026-07-15  
Vedecká fyzika skriptu 199 pri tomto audite: **nespustená**  
Verdikt: **PASS_FORMAL_PREFLIGHT_SCRIPT199**

## Predregistrácia

Pred vytvorením skriptu vznikol
`Questions/A2_K4_C7_7C_K7C_P2_SCRIPT199_PRERUN_2026-07-15.md`. Zachováva
stabilné ID `SCI-A2K4-C7G5-K7C-P2-MLEDGER`, deväť termov, prah 10×,
child 185, P1 paritu, nulový score effect a povinné timeouty.

## Statické kontroly

- presne jeden zdrojový skript s prefixom 199;
- marker `__K7C3D_CONTINUE__`: 0;
- entry point `if __name__ == "__main__"`: 1;
- cieľový raw JSON pred behom neexistoval;
- priamy interpreter `C:\Python311\python.exe` existuje;
- SHA-256 skriptu 199:
  `911F7DDBDC6B41C019CD041FC024A2B8FAF9CF2A27A1F35686ECB6649BAD8DF9`.

## Python formálne brány

Každý príkaz mal samostatný externý limit:

| Kontrola | Limit | Výsledok |
|---|---:|---|
| `py_compile` skriptu 199 | 10 s | exit 0 |
| CLI `--help` skriptu 199 | 10 s | exit 0 |
| JSON `--smoke-test` | interný 5 s, externý 10 s | `PASS_SCRIPT199_SMOKE_NO_PHYSICS`, deväť termov, `physics_executed=false` |
| `py_compile` checkeru 200 | 10 s | exit 0 |
| CLI `--help` checkeru 200 | 10 s | exit 0 |

## Checker 200

Skript 200 je nový nemenný snapshot po pridaní 199. Staticky číta a
kompiluje AST; nič neimportuje ani nespúšťa.

| Pole | Výsledok |
|---|---|
| verdict | `PASS_SCRIPT_CORPUS_INVENTORY` |
| korpus bez auditora | 204 |
| karanténa | 70 |
| syntaxové chyby | iba historické 118/119 |
| neúplný 186 | detegovaný |
| cieľ 199 | `NOT_IN_QUARANTINE` |
| cieľ vykonaný | nie |

- SHA-256 checkeru 200:
  `77829D7737334289A0E4A984956714D200F1DAE303C0C248C817395F2A595412`;
- uložený checker JSON:
  `Audit/A2_K4_K7C_P2_CORPUS_CHECKER_200_2026-07-15.json`;
- SHA-256 checker JSON:
  `C261E23CEB06338C4BB142A9EFD332D5DFF852A7BE720A1629E0C14198B6BDCE`.

## Formálne chyby počas preflightu

- PF-023: prvý generátor checkeru 200 bezpečne zastal na krehkom exact
  markeri; súbor nevznikol a Python sa nespustil.
- PF-024: prvý zápis PF-023 sa zastavil v JavaScript obale pred shellom pre
  vnorené Markdown backticky.

Obe chyby sú zapísané v `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md`. Opravený
generátor použil ukotvený významový regex s presne jednou zhodou. Žiadna
chyba nevykonala fyziku ani nezmenila prah P2.

## Povolenie ďalšieho kroku

Skript 199 je formálne pripravený na jediný predregistrovaný beh:

- interný limit 30 s;
- child subprocess 22 s;
- child 185 interný 20 s, seed source 15 s, seed child 6 s;
- externý limit 40 s;
- nový nemenný output
  `Audit/A2_K4_K7C_P2_MLEDGER_RAW_2026-07-15.json`.

