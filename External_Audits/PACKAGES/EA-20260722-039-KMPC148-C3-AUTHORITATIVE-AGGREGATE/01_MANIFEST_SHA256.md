# SHA-256 manifest — EA-039

Strojovým zdrojom pravdy je `01_MANIFEST_SHA256.tsv` s `25` exact
source/copy riadkami. SHA-256 pri seal:

`724489858A4D1DEB1C285F782CA0C054BB74D97D8BA0D76D518B402B1F37F99D`.

| skupina | počet | umiestnenie |
|---|---:|---|
| predregistrácia, interný audit a PASS reference | 3 | `EVIDENCE/` |
| runner a read-only base | 2 | `REPRO/scripts/` |
| frozen pair rawy | 15 | `REPRO/scripts/results/k_mpc_005/` |
| frozen mode-closure autority | 5 | `REPRO/tracks/.../P5_3_SEEDS/` |
| spolu | 25 | single-copy |

Runtime mapa má `22` riadkov a SHA-256
`53633A7E7A47CA5F8E5B7321D3ECC05295FE4F08FD7D8039B975FB831E8E26E5`.

Balík má `32` fyzických súborov, response šablóna je jeden ďalší súbor;
spolu `33 < 40`. Rovnaký hash sa v balíku nekopíruje na dve cesty.
