# Pokyny externému auditorovi — EA-021

Over manifest, source/copy paritu, rovnicový term ledger a runtime mapu. V
čerstvej kópii `REPRO` spusti iba runner 336: compile V1–V5 a runnera,
behaviorálny smoke s `4.8 s` a official s `45 s`. Nemeň dps, solver,
support, prahy, rovnice, upstream hodnoty ani holdout rolu.

Over najmä:

- cieľ `Einstein_0i[7]`, presne 73 členov a power-sum 7 každého člena;
- term SHA `9BB2F029...5B5EA`, driver SHA `CEBB46C4...43EF2` a holdout SHA
  `2DE8C982...06E2DE`;
- reconstructed residual `-5.4970171428314830743e-17`, error `< 2e-66`;
- physical absolute term sum `4.8965432763492801743e-8` a cancellation
  factor `890763690.40157`;
- owner subtotaly: fractional background × M1 `-7.04818880487719e-9`,
  F0 `-1.8002335213599055e-11`, standard background × exact M3
  `+6.074780307594782e-10` a exact M3 `+6.458713054361139e-9`;
- V4 binary64 product-before-bridge opravu: osem fuel členov zmenených,
  všetky non-fuel členy nezmenené;
- V5 mení iba owner expectation a všetci vnorení owneri sa obnovia;
- presne dva HP solve a `holdout_rows_added_to_solve = 0`.

PF-092 až PF-095 posúď osobitne ako technickú audit trail. Porovnaj
generated JSON s Evidence 017 po odrátaní iba runtime a lokálnych path polí.
Zapíš príkazy, exit codes, wall time, SHA generated JSON a každú odchýlku.
