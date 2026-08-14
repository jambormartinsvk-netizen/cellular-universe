# Pokyny externému auditorovi — EA-006

**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)

Najprv over `01_MANIFEST_SHA256.tsv` a `04_RUNTIME_DEPENDENCY_MAP.tsv`.
Pracuj v čerstvej kópii adresára `REPRO/`; zapečatený balík nemeň.

Spusť iba official príkazy z `03_REPRODUCTION_AND_EXPECTATIONS.md`.
Runner, prahy, runtime limit, output path ani prerequisite JSON sa nesmú
meniť. Nevolaj interný solver priamo. Každý Python proces má vonkajší limit
najviac 10 s a vnútorný limit presne 4.8 s.

Pre manifest preflight, compile, help, smoke, official audit a prípadnú
odchýlku zapíš presný príkaz, exit code a wall time. Pre generated JSON
zapíš SHA-256. Uveď Python, NumPy, SymPy, BLAS/LAPACK, OS a architektúru;
neznáme položky označ `NOT_AVAILABLE`.

Over najmä:

- source a prerequisite hash guards;
- exact identity NID/`.05`/nominal;
- support/count a powers;
- combined-`R_fs` density a velocity kompenzáciu;
- core, actual S-C0, common a tail brány osobitne;
- absolute envelope tail, nie signed cancellation;
- nulový počet temp súborov po úspechu aj failure fixture.

Ak official vetva zlyhá a urobíš odchýlku, označ ju `DECLARED_DEVIATION`,
uveď obídený guard a nevydávaj ju za T2 reprodukciu official runnera.
Každé hlavné tvrdenie označ `OBSERVED_IN_PRIMARY`,
`INDEPENDENTLY_RECOMPUTED`, `INFERRED_FROM_PROJECT_DOCS` alebo
`CONTEXT_ONLY`.

Externý posudok nemení projektový verdict, skóre, prediction table, release
ani Zenodo stav.

