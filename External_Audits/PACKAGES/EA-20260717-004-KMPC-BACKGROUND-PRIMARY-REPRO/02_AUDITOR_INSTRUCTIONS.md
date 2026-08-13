# Pokyny auditorovi

Najprv over manifest. Potom skontroluj priamo riadky runnera 213, vzťahy
`K_MPC`, `z`, `G2`, `fuel_piece`, `denominator` a `s2`. Rozlišuj fakt, čo
kód robí, od neznámeho historického zámeru čísla `0.05`.

Spusť tri reprodukcie podľa `03_REPRODUCTION_AND_EXPECTATIONS.md` v čerstvej
kópii `REPRO/` s externým timeoutom 10 s na proces. Zapíš Python, SymPy,
OS/architektúru, exit code a wall time. Pôvodné runy presné verzie prostredia
nezmrazili; ide o deklarovanú medzeru.

Neudeľuj projektový PASS/REVIEW/STOP. Ak reprodukcia zlyhá technicky,
neprepisuj tým fyzikálny scope a nepouži `INDEPENDENTLY_RECOMPUTED`.
