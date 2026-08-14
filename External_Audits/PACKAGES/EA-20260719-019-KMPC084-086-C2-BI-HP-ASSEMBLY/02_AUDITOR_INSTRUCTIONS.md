# Pokyny externému auditorovi — EA-019

Over manifest, source/copy paritu a runtime mapu. V čerstvej kópii `REPRO`
spusti iba runner 330: compile, smoke s 4.8 s a official s 45 s. Nemeň dps,
solver, support, prahy, rovnice, upstream vstupy ani holdout rolu.

Zapíš presný príkaz, exit code, wall time a SHA-256 generated JSON pre
manifest preflight, smoke aj official audit. Ak urobíš odchýlku od
oficiálnej vetvy, označ ju `DECLARED_DEVIATION` a uveď jej dôvod a dopad.

Over najmä:

- driver fingerprint `FE5E5A7C...127240F` a presne jeden 80-dps solve;
- holdout shape `16x104`, fingerprint `2DE8C982...06E2DE` a non-fit `0`;
- `Einstein_0i[7]` residual, affine norm a metriku;
- explicitný HP driver replacement ostatných brán;
- source hashe, owner separation/restore a corrected affine fixture;
- že PF-089/PF-090/PF-091 skončili pred fyzikou.

Porovnaj generated JSON s Evidence 011 po odrátaní iba runtime a lokálnych
path polí. Package tier a fyzikálny verdict vyhodnoť osobitne.
