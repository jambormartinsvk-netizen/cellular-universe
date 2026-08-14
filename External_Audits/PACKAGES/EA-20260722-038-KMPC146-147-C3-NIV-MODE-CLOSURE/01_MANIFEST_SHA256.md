# SHA-256 manifest — EA-038

Strojovým zdrojom pravdy je `01_MANIFEST_SHA256.tsv` s `15` exact
source/copy riadkami. SHA-256 pri seal:

`2B7066A1B5D6E48910575D329F3A50E8F16672BA0AF8BC43A5869149C057EEA9`.

| skupina | počet | umiestnenie |
|---|---:|---|
| EA-037 autorita, preregistrácie, interné audity, PASS reference | 7 | `EVIDENCE/` |
| KMPC-146 source delta | 5 | `SOURCE_REVIEW/` |
| KMPC-147 runner + dva exact JSON vstupy | 3 | `REPRO/` |
| spolu | 15 | single-copy |

Runtime mapa má `3` riadky a SHA-256
`288B561BB354711CCB93D91D80D5A8908088C86583D0476B98FFEFC79C6159FF`.

Balík má `22` fyzických súborov, response šablóna je jeden ďalší súbor;
spolu `23 < 40`. Rovnaký hash sa v balíku nekopíruje na dve cesty.
