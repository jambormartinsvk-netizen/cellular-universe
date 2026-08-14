# Pokyny externému auditorovi EA-038

1. Auditujte iba presné otázky z dokumentu 00 a zachovajte mixed-tier
   hranicu: KMPC-146 T1, KMPC-147 T2.
2. Spustite R6 package preflight cez PowerShell 7+ z koreňa projektu.
   Zaznamenajte príkaz, exit code a wall time; očakávanie je PASS.
3. Overte manifest `15/15`, runtime mapu `3/3`, exact REPRO coverage `3/3`,
   package `22`, response `1`, nulové duplicate hash groups a nulové
   placeholdery/temp súbory.
4. T1: skontrolujte všetkých päť súborov `SOURCE_REVIEW/` voči prereg 238,
   EA-037 autorite a KMPC-146 rawu v `REPRO/`. Overte frozen source hashe,
   tri corrections, ranky 104/130, same matrix/RHS, selection rule,
   obnovenie ownera a nulové zmeny support/depth/prahov/holdoutu.
5. T1: nezávisle vyčítajte zo source rawu presnú false množinu, štyri
   baseline/refined residualy, všetky inherited fyzikálne brány a exact F0
   JSON-semantic parity s KMPC-131 predecessorom.
6. T2: originál package nechajte read-only. V novej dočasnej kópii
   `REPRO/` zaznamenajte OS a Python, potom spustite oddelene compile, help,
   smoke a official KMPC-147. Vonkajší limit každého procesu je `10 s`.
7. Pri každom procese zapíšte presný príkaz, exit code, wall time,
   stdout/stderr a pri official generated JSON cestu a SHA-256.
8. Porovnajte generated JSON s `EVIDENCE/007` podľa jedinej povolenej
   normalizácie v dokumente 03. Každý ďalší rozdiel je nález.
9. Nezávisle zostavte protected projekciu podľa prereg 240 a overte exact
   current/source zhodu, štyri F0 parity a operation counts nula.
10. V dvoch fresh kópiách odstráňte osobitne KMPC-146 source raw a
    KMPC-131 predecessor raw. Official musí skončiť nonzero bez success
    rawu a bez fyzikálneho verdiktu.
11. Každú odchýlku označte `DECLARED_DEVIATION`; official s odchýlkou
    nemôže dostať T2.
12. Pri záveroch používajte evidence tags a oddeľte integritu, numeriku,
    fyziku, formálnu logiku, účtovanie a dokumentáciu.
13. Explicitne posúďte, či interné účtovanie NIV `9/9`, C3 `45/45 logical
    PASS` a K4 `60/100` je podporené v deklarovanom mixed-tier scope.

Povinné ledger termíny: `generated JSON`, `exit code`, `wall time`,
`odchýlka`.
