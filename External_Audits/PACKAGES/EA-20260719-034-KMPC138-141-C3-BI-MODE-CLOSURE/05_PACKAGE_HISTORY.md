# História balíka EA-034

## 2026-07-19 — DRAFT_NOT_DELIVERED

R5 single-copy kapsul obsahuje `19` evidence a `2` REPRO kópie, `7`
controls a jednu oddelenú response šablónu. Celkom `29 < 40`; žiadna
budget exception nie je potrebná.

Target je T2 pre self-contained read-only KMPC-141 a T1 pre forenzný audit
45-s exact KMPC-139. Pred seal musí prejsť source/copy parity, runtime map,
response-template kontrola, nulová duplicita a fresh-copy behavior:
compile/help/smoke/official, field parity okrem runtime a missing-prerequisite
guard.

Prvý behaviorálny orchestration príkaz nepoužil Python runner: PowerShell
`Copy-Item -LiteralPath '...\\*'` zámerne nerozbalil wildcard, takže fresh
copy ostala prázdna. Package sa nezmenil. Opravený príkaz kopíroval explicitný
adresár `REPRO/scripts` a až potom spustil behavior vetvy.

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

- štrukturálny preflight: `129/129 PASS`;
- manifest source/copy parity: `21/21 PASS`;
- runtime dependency map: `2/2 PASS`;
- fresh-copy compile/help/smoke/official exit: `0/0/0/0`;
- fresh-copy wall time: `0.127/0.144/0.191/0.215 s`;
- generated raw SHA-256:
  `EA94A317EE8B25C774A788CE782A5E54C65EF08107166FAD773E480ED2A177B1`;
- field parity voči reference `013`: PASS po odstránení iba top-level
  `runtime_seconds`;
- missing-prerequisite guard: exit `2`, `frozen source missing`, success raw
  nevznikol;
- package files `28` + response `1` = `29 < 40`;
- duplicate physical hash groups: `0`;
- tier: KMPC-141 T2 read-only; KMPC-139 exact T1;
- po tomto zápise je package immutable.
