# Python runtime pre reprodukovateľnosť K4 auditov

**Dátum overenia:** 2026-07-14

## Funkčné prostredie

- interpreter: `C:\Python311\python.exe`;
- Python: `3.11.3`;
- SciPy: `1.17.1`;
- NumPy: `2.4.4`.

Skripty 157 a 158 v tomto prostredí prešli nulovo-integračnými behmi NID/deep a NIV/deep.

## Nefunkčné voľby po reštarte

- príkaz `python` smeroval aj na WindowsApps alias a pri prvom pokuse sa nevrátil v limite;
- pribalený interpreter `C:\Users\jambor.CHASTIA\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe` bol spustiteľný ako Python `3.12.13`, ale nemal modul SciPy a skript 157 skončil pred výpočtom na `ModuleNotFoundError`.

## Pravidlo pre ďalšie výpočty

Kým sa prostredie vedome nezmení, fyzikálne skripty závislé od SciPy sa spúšťajú explicitne cez `C:\Python311\python.exe`. Každý proces musí ďalej používať vnútorný aj vonkajší časový limit.
