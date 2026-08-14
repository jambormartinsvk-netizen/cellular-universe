# Erratum skriptu 28 a nástupca 29

**Dátum:** 2026-07-13

## Čo sa stalo

Skript 28 dokončil backgroundové aj perturbačné integrácie, ale pri zápise výsledku zlyhal na `TypeError: Object of type bool is not JSON serializable`. Príčinou bol skalár `numpy.bool_` vo výstupnom slovníku, nie fyzikálna rovnica ani integrátor.

## Zachovanie pôvodného behu

`28_script_A2_K4_full_superhorizon_relative_mode.py` zostáva nezmenený ako auditná stopa neúspešného serializačného behu.

## Nástupca

`29_script_A2_K4_full_superhorizon_relative_mode_serialized.py` importuje rovnice a funkciu `run()` zo skriptu 28. Mení iba prevod výstupných skalárov na vstavané typy `float` a `bool`. Nemení:

- fyzikálne rovnice;
- počiatočný gauge-invariantný mód;
- background;
- kroky mriežky ani `k/H0`;
- Einsteinov constraint;
- rozhodovacie prahy.

