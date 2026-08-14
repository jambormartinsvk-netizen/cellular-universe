# Pokyny externému auditorovi — EA-005

Najprv over `01_MANIFEST_SHA256.tsv` a `04_RUNTIME_DEPENDENCY_MAP.tsv`.
Over, že KMPC-034 prerequisite je prítomný v presnej runtime ceste a má hash
`37FB4453CBFF38710CF5694C21104689F1B070742FB02324011AA389508DCE20`.

Spusť iba príkazy z `03_REPRODUCTION_AND_EXPECTATIONS.md` v čerstvej kópii
`REPRO/`. Official smoke a official audit nesmú obísť guard, priamo volať
interný solver ani meniť output path, limit alebo prah. Každý proces má
externý limit 10 s a zachovaný interný limit presne 4.8 s.

Pre každú fázu zapíš presný príkaz, exit code, wall time a SHA-256 generated
JSON. Zapíš Python, NumPy, SciPy, SymPy, BLAS/LAPACK, OS a architektúru.
Ak prostredie alebo tool nevie niektorú položku zistiť, označ ju
`NOT_AVAILABLE`; nevymýšľaj ju.

Official regresný výsledok s prahom `1e-12` a nový cross-platform
diagnostický výsledok s prahom `1e-9` vyhodnoť osobitne. Diagnostika má
`verdict_effect=NONE`; nesmie spätne zmeniť frozen candidate interpretation.

Ak vykonáš odchýlku, vytvor osobitný riadok procesného ledgeru a uveď:

- prečo bola potrebná;
- ktoré guardy alebo vrstvy obchádza;
- či jej generated JSON a kód majú vlastný hash;
- prečo jej výsledok smie alebo nesmie niesť tag `INDEPENDENTLY_RECOMPUTED`.

Skontroluj aj collision fixture, absolute-branch would-be relative
diagnostiku a z-scan. Z-scan nie je bound nekonečného radu a nesmie dostať
fyzikálny PASS/STOP.

Použi response template bez vynechania metadát. Neudeľuj projektový
PASS/REVIEW/STOP a nemen score, prediction table, release ani Zenodo stav.
