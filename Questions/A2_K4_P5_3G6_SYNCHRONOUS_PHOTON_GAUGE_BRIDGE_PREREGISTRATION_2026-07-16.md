# A2-K4/P5.3g6 — predregistrácia: synchronný photon `l=2` gauge bridge

**Route:** `A1-K1 / A2-K4 / P5 / P5.3g6`  
**Prvý pokus:** `257_script_KMPC_020_P5_3g6_synchronous_photon_gauge_bridge.py`
skončil fail-closed na ceste historického markera (PF-054), hoci obe
algebraické identity prešli.  
**Autoritatívny nástupca:** `260_script_KMPC_021_P5_3g6_synchronous_photon_gauge_bridge_rerun1.py`  
**Vnútorný/vonkajší limit:** 5 s / 10 s. **Bez ODE, CAMB importu a skóre.**

## Problém

P5.3g4 použila exact CAMB term `8 k sigma/15`, no bez explicitného dôkazu,
že je v synchronnej CDM báze kompatibilný so seedom zo skriptu 84. Starší
interný dokument 73 navyše uvádza photon `F_gamma2` rovnicu bez metrického
zdroja, hoci kolízny blok samotný zostáva správny.

## Čo sa má overiť

Lokálny, zamrazený zdroj `camb/symbolic.py` musí deklarovať

```text
sigma_syn = (hdot_s + (6 eta_s)dot)/(2 k),
pi_g dot = ... + 8 k sigma/15 + opacity polter.
```

Skript potom presne overí

```text
8 k sigma_syn/15 = 4 hdot_s/15 + 8 eta_s_dot/5,
2 k q_gamma/5 = 8 theta_gamma/15,
```

a uloží dôkaz, že drive P5.3g4 sa dá čítať ako jedna synchronná MB rovnica.

## PASS / STOP

- **PASS:** zdrojová proveniencia a obe algebraické identity sú presné;
  255 sa zvýši z `REVIEW_GAUGE_BINDING` na formulačný photon-TCA PASS.
- **STOP:** chýba mapovanie alebo vyjde nenulové znamienkové/faktorové
  rezíduum; g4 ostáva review a plný seed sa neskladá.

Ani PASS neznamená plný seed, dynamický residual, P5.4 ani G8.

RERUN1 mení výlučne cestu kontrolného markera: photon lower equation sa
overuje v `Audit/A2_K4_3B_HIERARCHY_MODE_TAXONOMY_RECOMBINATION_AUDIT.md`,
nie v Python skripte 73. Fyzika, vstupy, limity a PASS kritériá sa nemenia.
