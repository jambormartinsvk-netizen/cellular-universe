# READ FIRST — A2 po zavedení očakávaní pred behom

Dátum: 2026-07-15

Aktuálne: **A2-K4 ŽIVÁ, 66.5/100; K7b numerický PASS s fail-closed hardeningom; K7c REVIEW.**

Pred každým ďalším vedeckým Python behom musí existovať vyplnený MD podľa `Questions/00_SCRIPT_PRE_RUN_EXPECTATION_TEMPLATE.md`. Musí obsahovať očakávanú hodnotu/trend, prípustnú odchýlku, rozhodovacie kritériá a timeout. Ak je hodnota neznáma, označí sa `EXPLORATORY` a predregistrujú sa aspoň invarianty a kill kritériá.

Priorita zostáva K4. Najbližšie poradie:

1. fail-closed regresný nástupca 175/176;
2. čistá samostatná reprodukcia RK4 REVIEW 184/185;
3. nový `M'` term ledger namiesto nedokončeného 186;
4. až podľa ledgeru fsum, algebraické preusporiadanie alebo vyššia presnosť.

Súhrn všetkých koľají je v `Audit/A2_CURRENT_TRACK_STATUS_AND_RECOMMENDATION_2026-07-15.md`. Konkrétne očakávania najbližších behov sú v `Questions/A2_K4_C7_7C_NEXT_RUN_PREREGISTERED_EXPECTATIONS.md`.
