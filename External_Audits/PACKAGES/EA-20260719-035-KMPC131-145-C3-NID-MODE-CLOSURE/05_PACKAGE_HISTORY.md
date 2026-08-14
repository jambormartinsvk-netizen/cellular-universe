# História balíka EA-035

## 2026-07-19 — DRAFT_NOT_DELIVERED

R5 single-copy kapsula obsahuje `26` evidence a `3` REPRO kópie, `7`
controls a jednu oddelenú response šablónu. Celkom `37 < 40`; budget
exception nie je potrebná.

Target je T2 pre self-contained read-only KMPC-145 a T1 pre forenzný audit
KMPC-131/142/143/144 numeriky. Pred seal musí prejsť source/copy parity,
runtime mapa, response-template kontrola, nulová duplicita a fresh-copy
behavior: compile/help/smoke/official, field parity okrem runtime a oba
missing-prerequisite guardy.

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

- štrukturálny preflight pred sealom: `171/171 PASS`;
- manifest source/copy parity: `29/29 PASS`;
- runtime dependency map: `3/3 PASS`;
- fresh-copy compile/help/smoke/official exit: `0/0/0/0`;
- fresh-copy wall time: `0.140/0.160/0.240/0.150 s`;
- generated raw SHA-256:
  `488C7EC1E9125690FDC61C2CF368797CDB66FD92495592C7FF2F46F67A43A752`;
- field parity voči reference `017`: PASS po odstránení iba top-level
  `runtime_seconds`;
- correction checks `14/14`, pair PASS, workers/solvers/CPQR `0/0/0`;
- protected snapshot pred/po:
  `EBD4021F5BC285551D2EE8DC521E0A9DE23BA6D61CDE5D6DEBAE473BAA2FD97D`;
- samostatný missing-KMPC-131 guard: exit `2`, fail-closed, bez success rawu;
- samostatný missing-KMPC-144 guard: exit `2`, fail-closed, bez success rawu;
- package files `36` + response `1` = `37 < 40`;
- duplicate physical hash groups: `0`;
- tier: KMPC-145 T2 read-only; KMPC-131/142/143/144 numerika T1;
- po tomto zápise je package immutable.
