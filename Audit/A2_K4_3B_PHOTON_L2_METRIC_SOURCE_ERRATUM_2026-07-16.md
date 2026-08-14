# Erratum A2-K4.3b — metrický zdroj v synchronnej photon `l=2` rovnici

**Dotknutý historický dokument:**
`Audit/A2_K4_3B_HIERARCHY_MODE_TAXONOMY_RECOMBINATION_AUDIT.md`, riadky 65–68.

## Obmedzenie staršieho zápisu

Starší zápis uviedol photon `F_gamma2` rovnicu len s rýchlostným a kolíznym
členom. Pre synchronnú Ma–Bertschinger/CAMB bázu je spodná rovnica neúplná:
musí obsahovať aj metrický zdroj

```text
8 k sigma_syn/15 = 4 hdot/15 + 8 eta_dot/5,
sigma_syn = (hdot + 6 eta_dot)/(2k).
```

Kolízny blok na riadkoch 124–142 historického dokumentu ostáva správny:
erratum nemení determinant `-3/10`, TCA nulový limit ani Thomsonovu
konzerváciu hybnosti. Obmedzuje iba použitie jeho skrátenej spodnej rovnice
ako úplného synchronného seedového operátora.

Primárna konvencia je Ma–Bertschinger, *Cosmological Perturbation Theory in
the Synchronous and Conformal Newtonian Gauges* (1995),
https://arxiv.org/abs/astro-ph/9506072. Lokálna CAMB symbolická implementácia
je v tomto audite použitá ako reprodukovateľný kontrolný zdroj, nie ako
náhrada fyzikálneho odvodenia.

## Dôkaz a dôsledok

`RUN_KMPC_021_P5_3G6_RERUN1_SYNCHRONOUS_PHOTON_GAUGE_BRIDGE.json` overil
na zamrazenom lokálnom `camb/symbolic.py` exact mapu aj oba koeficienty s
rezíduami `0`. P5.3g4 photon TCA algebra sa preto obnovuje ako formulačný
PASS, ale iba spolu s týmto mostom. Plný seed, dynamické residualy, P5.4 a
G8 tým stále neprešli.
