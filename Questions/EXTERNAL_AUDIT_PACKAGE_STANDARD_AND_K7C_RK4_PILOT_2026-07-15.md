# Štandard externého auditu a pilot K7c P1 RK4

Dátum: 2026-07-15  
Stav: pripravený rozsah balíka; export balíka ešte nebol vytvorený

## Prečo samostatný balík

Externý auditor nemá hádať, prečo sa používa `K7c`, ktorý skript je
autoritatívny ani ktoré čísla boli očakávané pred výpočtom. Balík musí byť
malý, nemenný, hashovaný a musí obsahovať aj otázky, ktoré môžu spochybniť
našu interpretáciu, nie iba potvrdiť výsledok.

## Adresár auditu

```text
External_Audits/
└── A1/A1K1/A2/A2K4/C7_7c/K7/K7c/P1_RK4/
    └── T001_EXTERNAL_RK4_CONVERGENCE/
        ├── 00_README_SCOPE.md
        ├── 01_CLAIMS_TO_AUDIT.md
        ├── 02_EQUATIONS_UNITS_AND_CONVENTIONS.md
        ├── 03_FROZEN_EXPECTATIONS.md
        ├── 04_INPUT_PARAMETER_MANIFEST.md
        ├── 05_CODE_DEPENDENCY_AND_HASH_MANIFEST.md
        ├── 06_RAW_EVIDENCE_MANIFEST.md
        ├── 07_KNOWN_LIMITATIONS.md
        ├── 08_QUESTIONS_FOR_AUDITOR.md
        ├── 09_REPRODUCTION_INSTRUCTIONS.md
        └── AUDIT_THREADS/
            └── T001/
                ├── 00_CURRENT_THREAD_STATUS.md
                ├── ROUND_01/
                │   ├── 01_EXTERNAL_AUDIT.md
                │   ├── 02_PROJECT_RESPONSE.md
                │   ├── 03_EVIDENCE_MANIFEST.md
                │   └── 04_OPEN_POINTS.md
                └── 99_THREAD_DECISION.md
```

## Pilotné dôkazy

- `scripts/197_script_A2_K4_C7_7c_K7c_P1_clean_standalone_RK4.py`;
- checkpointy mriežok 100, 200 a 400;
- `Audit/A2_K4_K7C_P1_CLEAN_RK4_RAW_2026-07-15.json`;
- predbehový dokument K7c P1;
- konečný interný audit;
- zdrojový hash skriptu 179 a mechanický lineage 179 → 197;
- error-ledger relevantný pre vznik skriptu;
- tento lineage/gate-weight audit.

Export musí obsahovať kópie zmrazených dôkazov alebo content-addressed archív,
nie odkazy na mutable pracovné súbory. Každá položka dostane SHA-256.

## Presné otázky pre externého auditora

1. Je pomer definovaný správnou orientáciou pre klasický RK4 a je rozsah
   `8–32` primeraný pre použitú normu a tri mriežky?
2. Je systém pri 100/200/400 krokoch už v asymptotickom režime, alebo je
   očakávanie pomeru približne 16 predčasné?
3. Je `max` normalizovaný endpoint rozdiel vhodná a škálovo férová norma?
4. Uzatvára sa pevná mriežka presne na rovnakých checkpointoch a používa
   identickú RHS bez skrytého time dependence alebo stavu?
5. Je dominancia `M` dôsledok fyzikálneho módu, cancellation/summation chyby,
   algebraickej kondície, stuhnutosti alebo nesprávnej transformácie?
6. Ktoré monitory sú tautologické a ktoré nezávisle overujú constraint?
7. Reprodukuje výsledok nezávislá implementácia alebo solver s vyššou
   pracovnou presnosťou bez zmeny rovníc?
8. Aký minimálny ďalší výpočet odlíši stavovú diskretizačnú chybu od chyby
   sčítania členov `M'`?
9. Je interný verdikt `REVIEW, nie fyzikálna smrť` primerane prísny?

## Čo auditor nesmie dostať ako hotový záver

Tvrdenie „RK4 nefunguje“ ani „rovnice sú nestabilné“ nie je preukázané.
Preukázané je iba to, že v konkrétnom čistom behu sa normalizovaný rozdiel
200/400 zväčšil a predregistrovaná konvergenčná brána neprešla. Externý audit
má mať voľnosť označiť chybu v norme, režime, implementácii, rovnicách alebo
v našom očakávaní.

## Váha auditu

Audit sa týka `C7-G5` s váhou `20/100`, najväčšou jednotlivou váhou v
scorecarde C7-W1. Reprodukcia uložených čísel sama neopraví G5; kladný
verdikt vyžaduje zdôvodnenú konvergenciu alebo auditované vysvetlenie, prečo
je predregistrovaný gate nesprávny. Každá zmena gate po výsledku musí zostať
v `HISTORY/SCORE_CHANGES` s pôvodnou aj novou formuláciou.

