# A2-K4/P5.3g6 RERUN1 — výsledok: synchronný photon `l=2` gauge bridge

**Verdikt:** `FORMULA_PASS_P5_3G6_RERUN1_SYNCHRONOUS_PHOTON_GAUGE_BRIDGE`  
**Čas/limit:** `0.047 s / 5 s`; bez ODE.  
**Hĺbka a skóre A2-K4:** bez zmeny, `60/100`.

## Presne uzavretý most

Lokálny CAMB symbolický zdroj uvádza v synchronnej CDM báze

```text
sigma_syn = (hdot + 6 eta_dot)/(2k).
```

Preto photon kvadrupólový drive má konzistentný tvar

```text
2 k q_gamma/5 + 8 k sigma_syn/15
= 2 k q_gamma/5 + 4 hdot/15 + 8 eta_dot/5.
```

Obe algebraické rezíduá sú presne `0`; `q_gamma=4 theta_gamma/(3k)` je
viazané na synchronný seed zo skriptu 84. Tým sa PF-053 (nezmapovaný shear
v 255) uzavrel ako provenance chyba, nie fyzikálny STOP.

## Rozsah

255/018 sa môže čítať ako photon TCA formulačný blok **iba spolu s týmto
výsledkom 021**. Žiadny z týchto dvoch artefaktov nepreukazuje plný regular
seed, Einsteinove rezíduá, recombination alebo stabilnú evolúciu.

Historický photon zápis v `A2_K4_3B...` bol obmedzený samostatným erratom:
`Audit/A2_K4_3B_PHOTON_L2_METRIC_SOURCE_ERRATUM_2026-07-16.md`.

## Ďalší krok

P5.3g7/261: zložiť všetky už auditované standardné, neutrínové, photon TCA a
tmavosektorové členy do jedného seedového vektora a priamo testovať `00`,
`0i`, trace a traceless Einsteinove rezíduá na dvoch skorých plochách.
