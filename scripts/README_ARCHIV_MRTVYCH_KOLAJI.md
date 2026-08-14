# Archivácia skriptov mŕtvych koľají

Skripty, ktoré prispeli k označeniu koľaje za mŕtvu, sú súčasťou dôkazu a nesmú sa mazať.

Aktuálne dôkazové skripty vetvy `S8/H0`:

| Skript | Zachovaný dôkaz |
|---|---|
| `17_script_reproduce_claimed_drag_curvature_grids.py` | Reprodukcia dodaných gridov a ich charakter response-surface/toy výpočtu. |
| `18_script_test_proposed_curvature_drag_combo.py` | Vyvrátenie konkrétneho tvrdenia, že `Omega_K=0.002`, `gamma=0.015` trafí `H0=68`, `S8=0.82`. |
| `19_script_postdata_toy_calibration_H0_S8.py` | Dôkaz, že cieľ možno trafiť post-data riešením dvoch parametrov; výsledok má nulovú predikčnú váhu. |
| `20_script_raw_H0_residuals.py` | Surové rezíduá voči H0 kotve vrátane zostávajúceho napätia bodu `Omega_K=0.005`. |

Podrobný vedecký register je v:

- `Audit/REGISTER_MRTVYCH_KOLAJI_A_DOKAZOV_v3.18.md`.

## Pravidlo zmien

Ak sa v skripte nájde chyba:

1. pôvodný skript sa zachová;
2. vytvorí sa opravená verzia s novým číslom alebo príponou;
3. vznikne Markdown erratum;
4. znovu sa vyhodnotí iba verdikt, ktorý závisel od chyby;
5. starý a nový výstup sa uchovajú s kontrolnými súčtami.

Pri vydaní sa k skriptom uložia presné reprodukčné príkazy, verzia prostredia a SHA-256.

