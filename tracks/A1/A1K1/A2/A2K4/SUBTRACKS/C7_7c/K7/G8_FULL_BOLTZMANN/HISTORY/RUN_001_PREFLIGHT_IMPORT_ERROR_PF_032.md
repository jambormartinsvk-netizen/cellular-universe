# RUN-001 — technická stopa PF-032: import CAMB

**Stav:** `DO_NOT_RUN / TECHNICAL`  
**Fyzika vykonaná:** nie  
**Dotknuté súbory:** prvá verzia runnera 221 a
`scripts/baseScripts/a2_k4_g8/structural.py`

`py_compile` prešiel, ale samostatný `--help` skončil ešte počas importu:

```text
ModuleNotFoundError: No module named 'camb'
```

Príčina: v `structural.py` bola koreňová cesta odvodená cez `parents[4]`,
čo ukazuje nad `D:\Teoria`; lokálna závislosť je však
`D:\Teoria\.deps\python`. Správna úroveň je `parents[3]`.

Toto nie je výsledok SCREEN-S0/S1, neexistuje JSON a nezmenilo sa skóre.
Následná technická oprava mení iba výpočet cesty, potom povinne opakuje
`py_compile`, `--help` a `--smoke` pred prvým autoritatívnym behom.
