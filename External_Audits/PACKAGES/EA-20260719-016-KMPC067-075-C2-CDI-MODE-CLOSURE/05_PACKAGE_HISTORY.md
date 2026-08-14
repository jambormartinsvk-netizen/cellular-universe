# História balíka EA-016

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

Theory author Martin Jambor; script creator Codex (OpenAI). Podľa R4 ide o
jeden balík pre celý uzavretý CDI mód, nie samostatné balíky pre support a
technické medzikroky. Auditný kapsul obsahuje 36 plochých evidence kópií a
34 REPRO súborov.

Fresh-copy behavior prešiel:

- compile `EXIT=0`;
- KMPC-073 smoke `EXIT=0`, official `EXIT=0`, všetky brány PASS;
- KMPC-075 smoke `EXIT=0`, official `EXIT=0`, všetky brány PASS;
- chýbajúci checkpoint: očakávaný `EXIT=2`, žiadny kanonický raw;
- zmenený KMPC-074 base: očakávaný `EXIT=2`, žiadny kanonický raw.

Generated fresh-copy SHA boli
`46F746EDFC608B530DBA186C04CB398F2DEC06BB4B43DC4DE958D553E6291512`
pre KMPC-073 a
`C5D5C769CCCC2B6350E38A5580CCC061141EA7E5DB2291541DE29AEF6ED068D5`
pre KMPC-075. Diff voči referencii je iba meraný runtime; pri KMPC-075 navyše
lokálna absolútna cesta `frozen_algebra_source`. Fyzikálne, numerické,
prahové, kandidátske a ostatné provenance polia sú zhodné. Preflight pred
behavior testom aj finálny preflight po seale: `438/438 PASS`.
