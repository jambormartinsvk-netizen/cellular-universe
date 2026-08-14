# KMPC-102 — natívny HP-M1 CPQR routing successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `1/10`

## Dôvod

KMPC-101 compile/help aj oba CPQR smoke fixtures prešli. Prvé official CLI
volanie však uviedlo v `--output` iba basename. Stabilný harness ho preto
vyriešil ako `D:/Teoria/<name>`, nie ako canonical
`D:/Teoria/scripts/results/k_mpc_005/<name>`, a skončil v `guarded_import`
pred volaním `run_atom`. Immutable failure má SHA
`378A4FC7180E01FD89AF58CA803D3FBDD058DED6AA57AF38E1D1EB0B53A119CA`.

Nevykonala sa M1 assembly ani production CPQR. Nejde o výsledok fyziky ani
numeriky.

## Jediná dovolená zmena

KMPC-102 je routing-only successor:

- V9 výpočtový modul a jeho SHA ostávajú byteovo nezmenené;
- CPQR metóda, dva reortogonalizačné priechody, `1e-60` rank prah,
  `1e-60/1e-60/1e-55` numerické brány, 80 dps, rovnice, support, anchor a
  scope ostávajú nezmenené;
- V10 smie zmeniť iba run identity na `KMPC-102` a zdokumentovať PF-104;
- official príkaz musí použiť presnú relative canonical cestu
  `scripts/results/k_mpc_005/RUN_KMPC_102_P5_3G7_C2_BI_K0p15_NATIVE_HP_M1_CPQR_ROUTING_SUCCESSOR.json`;
- rozhodovací strom a zákaz fyzikálneho PASS sú presne podľa KMPC-101.

## Zmrazená implementácia pred prvým Python behom

- V9 calculation modul:
  `8EBDA7232BEADF0640A2C8361B444A9A896EB215E159E552AC494EAE2C0CCD0A`;
- V10 routing wrapper:
  `0E70793D89F32D70A0B1CDB021DE4D8C5785D06DB7245BE83ED2F2F720920801`;
- runner 346:
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `39/39` source a `15/15` prerequisite hashov sedí.

Pred vytvorením tejto predregistrácie nebol V10 ani runner 346 spustený cez
Python. Od tohto bodu sú V10, runner 346 a canonical execution command
immutable.
