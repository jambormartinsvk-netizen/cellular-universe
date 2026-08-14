# Pokyny externému auditorovi EA-037

1. Auditujte iba presnú T2 closure otázku z dokumentu 00; vedecký REVIEW
   sa nemení.
2. Spustite aktuálny R6 package preflight z koreňa projektu a zaznamenajte
   príkaz, exit code a wall time. Očakávanie je `passed=true`.
3. Overte manifest `30/30`, runtime mapu `25/25`, exact REPRO coverage,
   hardcoded dependency checks `3/3`, package `37` + response `1` a nulové
   duplicate hash groups.
4. Originál package nechajte read-only. V novej dočasnej kópii `REPRO/`
   zaznamenajte OS, Python, NumPy, SciPy, SymPy a BLAS/LAPACK.
5. Spustite oddelene compile, help, smoke a official audit. Vonkajší limit
   official procesu nastavte na `20 s`; frozen worker `4.8 s` a parent `9 s`
   guardy sa nesmú meniť.
6. Pri každom procese zapíšte presný príkaz, exit code, wall time,
   stdout/stderr a pri official generated JSON cestu a SHA-256.
7. Porovnajte generated JSON s `EVIDENCE/005` presne podľa corrected parity
   pravidla v dokumente 03. Každý ďalší rozdiel je nález.
8. V dvoch ďalších fresh kópiách odstráňte osobitne script 88 a source-map
   26 a spustite official. Očakávajte nonzero exit, presnú missing/hash
   príčinu, žiadny success raw a žiadny fyzikálny verdict.
9. Overte, že reference aj generated raw majú rovnaké štyri primárne M3
   driver failures a všetky ostatné frozen brány uvedené v audite 237.
10. Každú odchýlku označte `DECLARED_DEVIATION`; official s odchýlkou
    nemôže dostať T2.
11. Pri záveroch používajte evidence tags a oddeľte integritu, numeriku,
    fyziku, formálnu logiku, účtovanie a dokumentáciu.
12. Externý audit nemení projektový REVIEW, NIV/C3 register ani K4 score.

Povinné ledger termíny: `generated JSON`, `exit code`, `wall time`,
`odchýlka`.
