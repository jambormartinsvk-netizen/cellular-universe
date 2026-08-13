# HISTORY — nemenné staršie vydania

Tento adresár uchováva presný historický snapshot teórie, aby bolo možné
spätne overiť citácie, zmeny tvrdení a kontrolné súčty bez tichého
prepisovania publikovanej verzie.

## v3.17 / Zenodo verzia 2.0

```text
ZENODO_RECORD_ID: 21297228
DOI: 10.5281/zenodo.21297228
ZENODO_VERSION: 2.0
PUBLICATION_DATE: 2026-07-10
FILE_COUNT: 16
ARCHIVAL_COMMIT: e9e3579afdffc3c719f0beabb4ec33929cfb4d62
ARCHIVAL_TREE: 6e317b76e17c08febb800fcc80742c77c8801aeb
SOURCE_MAPPING: HISTORY/v3.17/<pôvodná_relativna_cesta>
PRE_EXPORT_MD5: 16/16 PASS
POST_IMPORT_MD5: 16/16 PASS
```

Zdrojom súborov je výhradne uvedený archívny commit, nie pracovná kópia
`D:/Teoria-v3.17-release`. Najmä historický skript 09 je publikovaný blob,
nie jeho neskorší pracovný variant.

| Historická cesta pod `HISTORY/v3.17/` | Zenodo MD5 |
|---|---|
| `scripts/06_script_Q14_light_cone_front_sharpening.py` | `8d3f0e1767b270184b611c3dc40f8f1d` |
| `scripts/07_script_Q12_dispersion_Lorentz_test.py` | `7579c7bcfddd051dd144f49cbf8b0a4d` |
| `scripts/08_script_Q7_sound_horizon_H0.py` | `f5b43100fec3b6c3aaf2fe0ae86e41ec` |
| `scripts/09_script_K3_cosmology_pipeline.py` | `2e2c6b32c8d39a5a6dc399018424d039` |
| `scripts/10_script_Q10_Vlinks_dowry_rule.py` | `ddd8d9f48fd4136bd333515d7f3f83d7` |
| `theory/EN/00_README_EN.md` | `7bfc3e84c1653c03e92ce752ae1b86a0` |
| `theory/EN/01b_Introduction_and_Philosophy_EN.md` | `fb97e07c7c712dc96f9ec47e1b54400c` |
| `theory/EN/02_Predictions_Table_v3.17_EN.pdf` | `6dd7d46611eaa8f6e0a9129f84812882` |
| `theory/EN/03_Predictions_Table_v3.17_EN.csv` | `754f4e9e6a40a16304c69019f0bb73a5` |
| `theory/EN/04b_Main_Document_Theory_Equations_Values_v3.17_EN.md` | `ac45868b41b4ffb9ea096677e6b78971` |
| `theory/EN/05b_Methodology_Rules_and_Question_Register_EN.md` | `9a896b77fc991d8b2e72d7335f6aeb3f` |
| `theory/SK/01_Introduction_and_Philosophy_SK.md` | `8667297005bdd0f87df36816c38cfe7f` |
| `theory/SK/02b_Predictions_Table_v3.17_SK.pdf` | `9c229bc1421850b6852b43ca5f5e0f0b` |
| `theory/SK/03b_Predictions_Table_v3.17_SK.csv` | `0c489c9aac33ecd0c6b5b6bc3ba14858` |
| `theory/SK/04_Main_Document_Theory_Equations_Values_v3.17_SK.md` | `8b942abc62b6333b789a3c6aac66309d` |
| `theory/SK/05_Methodology_Rules_and_Question_Register_SK.md` | `4f60e2e27961c64e6b87c1281b7be42d` |

## Hranica použitia

- Súbory v `HISTORY/` sú historické tvrdenia a výpočty; neprepisujú stav
  current v3.18.
- Na pochopenie v3.18 ich netreba čítať.
- História je Git provenance vrstva a nevstupuje do current Zenodo payloadu
  v3.18.
- Changelog vysvetľuje rozdiely, ale autoritou current tvrdení sú očíslované
  SK/EN súbory v `theory/` a ich release manifest.
- Historické súbory sa nesmú redakčne opravovať. Oprava alebo obmedzenie
  tvrdenia patrí do novej verzie s dôvodom v changelogu.
