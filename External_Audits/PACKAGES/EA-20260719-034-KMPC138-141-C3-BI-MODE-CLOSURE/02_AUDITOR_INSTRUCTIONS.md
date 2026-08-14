# Pokyny externému auditorovi

1. Auditujte iba otázku a dvojitú tier hranicu v dokumente 00.
2. Spustite package preflight a zaznamenajte presný príkaz, exit code a wall
   time.
3. Overte source/copy hashe všetkých 21 položiek a absenciu duplicitných
   fyzických kópií; balík nemeňte.
4. Forenzne overte v raw `012`, že všetky štyri coefficient a oba exact
   workery majú `returncode=0`, exact `technical_pass=true`, lokálny owner
   aktívny/obnovený a runtime pod `45 s`.
5. Overte v `015` až `019`, že výnimka nemení rovnice, thresholdy ani
   coefficient limit a že parent chyby boli alias a supersession equality.
6. V novej dočasnej kópii `REPRO/` spustite compile, help, smoke a official
   KMPC-141. Uveďte exit code, wall time a generated JSON SHA-256.
7. Generated JSON porovnajte s `EVIDENCE/013`; povolená normalizácia je iba
   top-level `runtime_seconds`. Každý ďalší rozdiel je nález.
8. V ďalšej čistej kópii odstráňte jediný raw KMPC-140 prerequisite a
   overte fail-closed missing-input guard. Tento negatívny beh nesmie meniť
   pôvodný package.
9. Skontrolujte množinovú logiku: pôvodná false množina musí byť neprázdna
   podmnožina scope, false mimo scope zakázaný, driver exact uzavretý a už
   prechádzajúci holdout exact potvrdený.
10. Pri každom závere použite evidence tag. Oddeľte package-integrity, tier,
    numerical, physics, formal/logical a documentation dopad.
11. Každú odchýlku od príkazov označte `DECLARED_DEVIATION`; explicitne
    uveďte, že exact KMPC-139 nebol v tomto balíku T2 reprodukovaný.
12. Externý posudok nemení projektový verdict, C3 register ani K4 score.

Termíny `generated JSON`, `exit code`, `wall time` a `odchýlka` sú povinné
v auditnom ledgeri.
