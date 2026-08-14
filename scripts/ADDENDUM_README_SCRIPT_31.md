# Dodatok k skriptom 25–30 — skript 31

**Dátum:** 2026-07-13

`31_script_A2_K4_frame_endpoint_crosscheck.py` je záverečná symbolická krížová kontrola smeru prenosu.

Overuje:

1. `beta=0` reprodukuje K1 v Eulerovej rovnici CDM;
2. `beta=0` reprodukuje K1 v Eulerovej rovnici paliva;
3. `beta=1` reprodukuje K3 v Eulerovej rovnici CDM;
4. `beta=1` reprodukuje K3 v Eulerovej rovnici paliva;
5. rozklad relatívnej rýchlosti cez ľubovoľný prenosový frame zachováva `V_f-V_c`.

Výsledok: `5/5 PASS`, návratový kód 0. Skript nemení verdikt; nezávisle kontroluje, že K4 znamienka správne interpolujú už odvodené endpointy K1 a K3.

Reprodukcia:

```powershell
python scripts/31_script_A2_K4_frame_endpoint_crosscheck.py
```

