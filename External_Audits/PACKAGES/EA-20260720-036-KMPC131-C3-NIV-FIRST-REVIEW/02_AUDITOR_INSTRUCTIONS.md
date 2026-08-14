# Pokyny externému auditorovi

1. Auditujte iba presnú otázku a tier hranicu v dokumente 00.
2. Z koreňa projektu spustite package preflight a zapíšte presný príkaz,
   exit code a wall time:

   `powershell -NoProfile -ExecutionPolicy Bypass -File External_Audits\TOOLS\Test-ExternalAuditPackage.ps1 -PackagePath External_Audits\PACKAGES\EA-20260720-036-KMPC131-C3-NIV-FIRST-REVIEW`
3. Overte `31/31` source/copy hashe, runtime mapu `23/23`, package count
   `38` plus jednu response šablónu a nulové fyzické hash duplicity.
4. Originál package nechajte read-only. V novej dočasnej kópii adresára
   `REPRO/` zaznamenajte OS/architektúru, Python, NumPy, SciPy, SymPy a
   BLAS/LAPACK a spustite oddelene compile, help, smoke a official audit.
5. Pri každom procese uveďte príkaz, exit code, wall time, stdout/stderr a
   pri official aj generated JSON cestu a SHA-256.
6. Generated JSON porovnajte s `EVIDENCE/008`; normalizovať sa smú iba
   explicitné runtime polia v dokumente 03. Každý ďalší rozdiel je nález.
7. Nezávisle zrekonštruujte primárnu false množinu. Oddeľte neprejdené M3
   driver brány od odvodených core/logical/bridge polí, neaplikovateľných
   booleanov a zámerných `physics_evolution_executed=false` receiptov.
8. Overte všetky číselné tvrdenia z auditu 237 priamo z reference a
   generated rawu, vrátane rankov, holdoutov, common, tail a background.
9. V dvoch ďalších fresh kópiách samostatne odstráňte nominal KMPC-126 a C2
   aggregate KMPC-127. Spustite smoke a overte fail-closed bez fyziky a bez
   success outputu. Package originál nemeňte.
10. Staticky overte, že import closure je úplný a že official vetva číta iba
    dva deklarované runtime vstupy pre NIV/k=.15.
11. Posúďte navrhovaný successor iba metodicky: nijaký refinement nespúšťajte
    a nepriznávajte PASS. Uveďte, či musí pokryť oba varianty a oba ranky.
12. Pri každom závere použite evidence tag a oddeľte integritu, tier,
    numeriku, fyziku, formálnu logiku, účtovanie a dokumentáciu.
13. Každú odchýlku označte `DECLARED_DEVIATION` a vysvetlite jej dopad.
14. Externý posudok nemení projektový REVIEW, NIV/C3 register ani K4 score.

Termíny `generated JSON`, `exit code`, `wall time` a `odchýlka` sú povinné
v auditnom ledgeri.
