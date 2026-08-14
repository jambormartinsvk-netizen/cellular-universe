# A2-K4.3b-RG BR3B-2e — výstup skriptov 104 až 109

Dátum: 2026-07-14  
Kanonický stav: **ŽIVÁ, 60/100 = G6**  
G7: **neuzavretá**

## Behy

| Skript | Výsledok | Význam |
|---|---|---|
| 104 | `PASS_EARLIEST_RELATIVE_RADIATION_SECTORS` | Najskoršie NID/NIV relatívne rýchlostné sektory sú konečné, presne kompenzované a metrické/Bianchiho rezíduá sú nula. |
| 105 | `ERROR_UNCLOSED` | Symbolický CAMB výstup vyžadoval chýbajúci Fortran kompilátor. Bez fyzikálneho rozsudku. |
| 106 | `PASS_CAMB_SELF_CONSISTENT_NIV_SHEAR_MAPPING` | Predkompilovaný CAMB 1.6.6 cez Eulerovu rovnicu potvrdil NIV šmyk `1/(4Rnu+5)`, nie izolovaný CLASS koeficient `1/(4Rnu+15)`. |
| 107 | `EXTERNAL_TIMEOUT_TERMINATED_UNCLOSED` | Exaktný `linsolve` prekročil vonkajší limit 15 s. Bez fyzikálneho rozsudku; skript zachovaný. |
| 108 | `PASS_NID_NIV_FIRST_SHEAR_SECTORS_BOUNDED` | Exaktné zdrojové identity + numerická SVD odozva uzavreli prvé šmykové NID/NIV sektory. |
| 109 | `PASS_MANIFEST_CREATED` | SHA-256 manifest 104–108. |

## Skript 104

NID pri mocnine `p=3.93109` a NIV pri `p-1=2.93109` majú:

- presne nulovú váženú základnú rýchlosť;
- presne nulové vážené Eulerovo nútenie;
- presne nulovú váženú indukovanú rýchlosť;
- dve Bianchiho rezíduá `0,0`;
- kladné regulárne exponenty.

Obmedzenie: hodnota NIV šmyku uvedená v pomocnom poradovom ledgeri 104 pochádzala z izolovaného CLASS riadku. Nevstupovala do riešenia najskoršieho rýchlostného sektora. Pre všetky neskoršie výpočty ju nahrádza audit 106.

## Skript 106 — oprava NIV šmyku

Predkompilované CAMB výstupy poskytli `delta_nu`, `q_nu=4 theta_nu/(3k)`, `eta_s` a `delta_c`. Použitá identita bola

`sigma_nu = delta_nu/4 - (3/4) d q_nu / d(k tau)`.

| Veličina | CAMB meranie | Konzistentná hodnota | Izolovaný CLASS riadok |
|---|---:|---:|---:|
| `eta/(k tau)` | -0.0620949 | -0.0620990 | -0.0620990 |
| `sigma/(k tau)` | 0.1503262 | 0.1503208 = `1/(4Rnu+5)` | 0.0600513 = `1/(4Rnu+15)` |
| `h_x/(k tau)` | -5.47e-6 | 0 | 0 |
| relatívne traceless rezíduum | 8.73e-5 | `<2e-2` | izolovaný koeficient neprejde |

Starší skript 84 porovnal skrátený seed vektor bez šmyku. Jeho PASS preto nepotvrdzoval NIV šmykový koeficient.

## Skript 108 — prvé šmykové sektory

| Mód | Sektor | `rank` | condition | škálované rezíduum | Bianchi |
|---|---:|---:|---:|---:|---|
| NID | 5.93109 | 7 | 49.73 | 2.48e-15 | `0,0` |
| NIV | 4.93109 | 7 | 43.91 | 5.56e-15 | `0,0` |

Oba systémy majú konečné jedinečné odozvy. Vedúci indukovaný `h_x` je numericky kompatibilný s nulou; odozva ostáva prevažne relatívnym radiačným módom s nenulovým `eta`, hustotami, rýchlosťami a šmykom.

Prvý spätný vstup `l=3` nastáva:

- NID pri 7.93109, teda po spoločnom fuel sektore 6.93109;
- NIV pri 6.93109, teda po spoločnom fuel sektore 5.93109.

Ďalšie správne poradie je preto BR3B-2f spoločný fuel sektor a potom neskoršia `l>=3` rekurzia.

## Primárne zdroje konvencií

- CLASS `perturbations.c`: https://raw.githubusercontent.com/lesgourg/class_public/master/source/perturbations.c
- CAMB 1.6.6 lokálna binárna implementácia a Eulerove premenné: https://github.com/cmbant/CAMB

