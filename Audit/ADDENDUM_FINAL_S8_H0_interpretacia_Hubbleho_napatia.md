# Dodatok ku konečnému auditu: interpretácia Hubbleho napätia

**Dátum:** 2026-07-13  
**Nadväzuje na:** `AUDIT_FINAL_S8_H0_drag_curvature_v3.18_2026-07-13.md`

## Overovaná hypotéza

Tvrdenie: otvorená koľaj `ΩK≈0,005` s `H0≈68,71` „dramaticky uvoľní Hubbleho napätie“.

## Aritmetický audit

Skript `scripts/20_script_H0_raw_residual_audit.py` porovnáva body s kotvami:

- SH0ES: `73,04 ± 1,04 km s^-1 Mpc^-1`;
- DESI DR2+CMB v plochom ΛCDM: `68,17 ± 0,28`;
- DESI DR2+CMB v `ΛCDM+ΩK`: `68,50 ± 0,33`.

Pre `ΩK=0,005`, `H0=68,7060`:

- voči SH0ES zostáva surové rezíduum približne `−4,17σ`;
- voči DESI DR2+CMB neplochému ΛCDM je surové rezíduum približne `+0,62σ`.

Pre základ `H0=66,3658` je surové rezíduum voči SH0ES približne `−6,42σ`.

Všetky tieto počty ignorujú neistotu bunkového modelu a nie sú spoločnou likelihood.

## Verdikt

- Hypotéza „krivostný bod priblíži model ku kozmologickej CMB+BAO hodnote okolo 68,5“: **PREŽÍVA ARITMETICKY**.
- Hypotéza „bod vyrieši alebo takmer vyrieši napätie so SH0ES“: **MŔTVA**.
- Formulácia „dramaticky uvoľní“ je prípustná iba s vysvetlením, že surový rozdiel sa zmenší z približne 6,4σ na 4,2σ; napätie zostáva veľké.

Primárne zdroje: [SH0ES](https://arxiv.org/abs/2112.04510) a [DESI DR2 Results II](https://arxiv.org/abs/2503.14738).

