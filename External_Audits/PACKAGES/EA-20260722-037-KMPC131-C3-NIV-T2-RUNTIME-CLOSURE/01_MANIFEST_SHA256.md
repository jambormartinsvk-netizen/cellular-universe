# SHA-256 manifest — EA-037

Strojovým zdrojom pravdy je `01_MANIFEST_SHA256.tsv` s `30` exact
source/copy riadkami. SHA-256 pri seal:

`138D38E804900E3FCEA99446BC7A29C3BF114C25E526F7C5EF1B2E653E560330`.

| skupina | počet | umiestnenie |
|---|---:|---|
| EA-036 audit/assessment, prereg, internal audit, reference raw | 5 | `EVIDENCE/` |
| runner + transitive imports | 21 | `REPRO/scripts/` |
| JSON runtime prerequisites | 2 | `REPRO/scripts/results/k_mpc_005/` |
| hardcoded exact-hash prerequisites | 2 | `REPRO/scripts/` a `REPRO/tracks/` |
| spolu | 30 | single-copy |

Runtime mapa má `25` riadkov a SHA-256
`CD74A29FC07F09EED3B02730F2C456B598B6976D15C1EA8B858B2815BC5F2A23`.
