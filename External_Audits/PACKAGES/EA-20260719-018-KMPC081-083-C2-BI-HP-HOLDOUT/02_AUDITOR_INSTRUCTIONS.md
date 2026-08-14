# Pokyny externému auditorovi — EA-018

Over manifest a runtime mapu. V čerstvej kópii `REPRO` spusti iba runner 327:
compile, smoke s 4.8 s a official s 45 s. Nemeň dps, solver, support, prahy,
matice ani holdout rolu. Zapíš príkazy, exit, wall time a generated SHA.

Over presne jeden HP solve, exact float bridge, oba matrix/constant SHA,
`rows_added_to_driver_solve=0`, driver/holdout decimal metrics a owner restore.
PF-086/087 nemajú fyzikálny payload. PF-088 je agregačné obmedzenie, ktoré
nesmie zakryť priamo vypočítaný holdout REVIEW.
