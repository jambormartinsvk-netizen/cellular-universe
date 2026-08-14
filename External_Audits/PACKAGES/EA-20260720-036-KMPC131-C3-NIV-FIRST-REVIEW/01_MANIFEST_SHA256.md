# SHA-256 manifest — EA-036

Strojovým zdrojom pravdy je `01_MANIFEST_SHA256.tsv` so všetkými `31`
source/copy položkami a úplnými cestami. Jeho SHA-256 pri seal je:

`371ADB50818F4D7152FB6D910E5FDF5480E0F6DDD071704EE41564985717AD16`.

| skupina | počet | single-copy umiestnenie |
|---|---:|---|
| interné audity, plán, ledgery a reference raw | 8 | `EVIDENCE/` |
| official runner | 1 | `REPRO/scripts/` |
| runtime JSON prerequisites | 2 | `REPRO/scripts/results/k_mpc_005/` |
| úplný lokálny import closure | 20 | `REPRO/scripts/baseScripts/p5_general_synchronous/` |
| spolu manifest | 31 | bez fyzických source duplicít |

Runtime mapa má `23` položiek a SHA-256
`49BE750EE2B41BD791030F9E247F9B70F3005FE707B2735A48C506076DD48F11`.
Každý manifestový copy hash sa musí rovnať uvedenému live source hashu.
