# Pokyny externému auditorovi — EA-020

Over manifest, source/copy paritu, rovnicový prepis a runtime mapu. V čerstvej
kópii `REPRO` spusti iba runner 331: compile, smoke s 4.8 s a official s
45 s. Nemeň dps, solver, support, prahy, rovnice, upstream vstupy ani
holdout rolu.

Zapíš presný príkaz, exit code, wall time a SHA-256 generated JSON. Ak
urobíš odchýlku od oficiálnej vetvy, označ ju `DECLARED_DEVIATION` a uveď
dôvod a dopad.

Over najmä:

- paritu 13 stavov a 13 driver rovníc s `full_ra_m3_seed.py` a
  `full_ra_contract.py`;
- baseline driver SHA `FE5E5A7C...127240F` a exact-driver SHA
  `CEBB46C4...43EF2`;
- exact-driver residual `8.720279045e-82`, shape 104x104 a jeden nový solve;
- holdout shape 16x104, fingerprint `2DE8C982...06E2DE`, non-fit `0` a
  `Einstein_0i[7] = 3.019756577618421e-9`;
- presne dva high-precision solve celkom a explicitný binary64 upstream
  scope limit;
- source hashes, owner restore, affine fixture a immutable output;
- reportingovú poznámku interného auditu o zdedenom top-level contract
  payload; rozhodujúce polia kontroluj priamo v driver boundary.

Porovnaj generated JSON s Evidence 021 po odrátaní iba runtime a lokálnych
path polí. Package tier a fyzikálny verdict vyhodnoť osobitne.
