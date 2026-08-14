# SHA-256 manifest — EA-008

Zdrojom pravdy je strojový `01_MANIFEST_SHA256.tsv`. Všetkých 26 položiek
musí mať zhodný `source_sha256` a `copy_sha256`; package preflight navyše
overuje existenciu, source/copy parity a úplnú runtime mapu.

| Rozsah | Rola | Počet |
|---|---|---:|
| `EVIDENCE/001–004` | proces, kontrakt, prereg a výsledkový audit | 4 |
| `EVIDENCE/005–013` | raw reference, PF-075 stopa, official zdroje a prerequisites | 9 |
| `EVIDENCE/014–026` | úplný Python import closure | 13 |

Manifest vznikol pred zapečatením balíka; po stave
`SEALED_READY_FOR_AUDIT` sa obsah nemení.
