# Auditné skripty 25–30 — A2-K3 a A2-K4

**Dátum:** 2026-07-13  
**Verdikty:** `MRTVA_A2_K3`, `MRTVA_A2_K4`

## K3

### Skript 25

`25_script_A2_K3_superhorizon_velocity_instability.py`

- rovnaký background ako K1;
- miera `Gamma/delta`;
- exponent `6.1065536987`;
- zosilnenie `448.7893835`;
- konvergencia `9.1895e-9 < 1e-8`;
- návratový kód 0, `MRTVA_A2_K3`.

### Skript 26

`26_script_A2_K3_equation_sign_and_null_limit_audit.py`

- presné mapovanie `Gamma_ref=-Gamma_cell`;
- kontinuita CDM/paliva;
- Euler CDM/paliva;
- veľkoškálové znamienko;
- štyri nulové limity a backgroundová bilancia;
- `10/10 PASS`, návratový kód 0.

## K4

### Skript 27

`27_script_A2_K4_equation_sign_null_and_eigenvalue_audit.py`

- entalpická definícia `theta_d`;
- mapovanie kontinuít a Eulerových zdrojov;
- nulové limity;
- `det M=-r^2/(1+delta r)<0`;
- `12/12 PASS`, návratový kód 0.

### Skript 28 — zachovaný neúspech

`28_script_A2_K4_full_superhorizon_relative_mode.py`

Integrácie sa dokončili, ale JSON výstup zlyhal na `numpy.bool_`. Skript sa nemení ani nemaže.

### Skript 29 — zachovaný neuzavretý beh

`29_script_A2_K4_full_superhorizon_relative_mode_serialized.py`

- opravil iba serializáciu;
- našiel gain približne `1.08028e5`;
- neprešiel krokovou bránou a bodová norma constraintu bola zle podmienená;
- návratový kód 1, `REQUIRES_FULL_REVIEW`.

### Skript 30 — finálny beh

`30_script_A2_K4_full_superhorizon_relative_mode_converged.py`

- kroky `1.25e-4/6.25e-5`;
- `k/H0=1e-5` a `5e-6`;
- kroková konvergencia `8.68094e-8`;
- k-konvergencia `6.28286e-11`;
- globálne `00` rezíduum `3.01385e-10`;
- interakčný gain `108028.1391`, log gain `11.5901470`;
- všetkých šesť brán `true`;
- návratový kód 0, `MRTVA_A2_K4`.

## Reprodukčné príkazy

```powershell
python scripts/25_script_A2_K3_superhorizon_velocity_instability.py
python scripts/26_script_A2_K3_equation_sign_and_null_limit_audit.py
python scripts/27_script_A2_K4_equation_sign_null_and_eigenvalue_audit.py
python scripts/28_script_A2_K4_full_superhorizon_relative_mode.py
python scripts/29_script_A2_K4_full_superhorizon_relative_mode_serialized.py
python scripts/30_script_A2_K4_full_superhorizon_relative_mode_converged.py
```

Skripty 28 a 29 majú zámerne neúspešné návratové kódy a sú súčasťou auditnej stopy.

