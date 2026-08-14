# SHA-256 manifest — EA-20260718-006-KMPC047-NID-C1

Strojový zdroj pravdy je `01_MANIFEST_SHA256.tsv`. Všetkých 18 evidence
položiek je byte-identická kópia uvedeného projektového zdroja; source aj
copy SHA-256 sú v TSV. Runtime kópie a oba runtime-opened JSON vstupy sú
osobitne uzavreté v `04_RUNTIME_DEPENDENCY_MAP.tsv`.

| Rozsah | Počet | Úloha |
|---|---:|---|
| process/contract/prereg/audit | 4 | autorita, scope a predregistrácia |
| raw result + runner + direct NID base | 3 | hlavný T2 výpočet |
| Python error ledger | 1 | preventívna stopa |
| transitive Python import closure | 10 | úplný reprodukčný kapsul |
| runtime prerequisites v `REPRO/` | 2 | S-C0 a predchádzajúci BI closure |

Balík neobsahuje generated KMPC-047 output v `REPRO/`; ten musí vzniknúť až
official auditom v čerstvej pracovnej kópii a dostať vlastný hash v odpovedi
auditora.

