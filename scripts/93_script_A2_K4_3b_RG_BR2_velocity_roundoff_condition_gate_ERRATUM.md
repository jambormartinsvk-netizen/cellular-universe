# Erratum skriptu 93 — JSON typ

Prvý beh dokončil podriadený solver aj výpočet IEEE-754 hraníc, ale výstup
nebolo možné serializovať pre typ `numpy.bool_`. Alias 94 pridáva iba prevod
na natívny `bool` a vykonáva nezmenený skript 93. Nejde o fyzikálny `FAIL`.
