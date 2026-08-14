# Pokyny externému auditorovi

1. Auditujte iba presnú otázku a dvojitú tier hranicu v dokumente 00.
2. Spustite package preflight a zaznamenajte presný príkaz, exit code a wall
   time.
3. Overte source/copy hashe všetkých 29 manifestových položiek, runtime mapu
   `3/3`, absenciu fyzických hash duplicit a package pred/po nemennosť.
4. Forenzne overte finálne rawy: `.005` `014`, `.05` `016`, `.15` `017`;
   prechodové príčiny overte v `015` a dvoch rawoch v `REPRO`.
5. Overte, že PF-127 je exact identity-schema adaptér a PF-128 iba
   parity-scope false-negative; žiadny z nich nesmie dostať fyzikálny
   verdikt.
6. V primary zdrojoch overte target role same-matrix refinementu, tri
   korekcie, nezmenené matrix/RHS/support/thresholdy a zákaz fitu na
   independent holdout.
7. V novej dočasnej kópii `REPRO/` spustite compile, help, smoke a official
   KMPC-145. Uveďte exit code, wall time a generated JSON SHA-256.
8. Generated JSON porovnajte s `EVIDENCE/017`; povolená normalizácia je iba
   top-level `runtime_seconds`. Každý ďalší rozdiel je nález.
9. V dvoch ďalších čistých kópiách osobitne odstráňte KMPC-131 a KMPC-144
   prerequisite a overte fail-closed missing/hash-mismatch guard. Pôvodný
   package nemeňte.
10. Nezávisle overte protected snapshot pred/po, presne dve opravené parity
    polia a nulové worker/solver/CPQR counts.
11. Skontrolujte účtovanie: tri nominal atómy už boli v stave `33/45`, takže
    NID pridáva šesť, nie deväť: `33+6=39`.
12. Pri každom závere použite evidence tag a oddeľte integritu, tier,
    numeriku, fyziku, formálnu logiku, účtovanie a dokumentáciu.
13. Každú odchýlku označte `DECLARED_DEVIATION`; explicitne uveďte, že
    KMPC-131/142/143/144 numerika nebola v tomto balíku T2 reprodukovaná.
14. Externý posudok nemení projektový verdict, C3 register ani K4 score.

Termíny `generated JSON`, `exit code`, `wall time` a `odchýlka` sú povinné
v auditnom ledgeri.
