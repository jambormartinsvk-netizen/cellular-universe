# A2-K4 / C7.7c / K7b.3a — preregistrácia vysokopresného štandardného solvera

**Dátum:** 2026-07-15, pred prvým behom  
**Cieľ:** odstrániť NID/deep koeficientový floor bez zmeny Jacobiánu alebo fyziky

## Povolená zmena

- Zostaví sa tá istá float64 matica a pravá strana štandardného Puiseuxovho systému ako v registrovanom skripte 119/127.
- Least-squares minimum sa prepočíta pri 80 dps riešením normálnych rovníc `A^T A x = A^T b`; vzhľadom na registrovanú podmienenosť približne 513 je 80 dps dostatočná rezerva.
- Pôvodné `numpy.linalg.lstsq` riešenie, rank a singulárne hodnoty zostanú zachované na porovnanie.
- Vysokopresné koeficienty sa exportujú ako desatinné reťazce; následný double reťazec zostáva len kompatibilným zdrojom pre staré kontroly.

## Zakázané zmeny

- žiadna zmena rovníc, riadkov, počiatočných podmienok, mocnín, backgroundu, K7a Jacobiánu alebo tolerancií K7b.1;
- žiadna projekcia výsledku podľa jeho veľkosti;
- žiadna ODE evolúcia ani zvýšenie skóre;
- žiadne odstránenie pôvodného double výsledku.

## Brány

1. všetky pôvodné zdrojové kontroly ostanú `true`;
2. high-precision riešenie je konečné, plného ranku a jeho least-squares rezíduum nie je väčšie než pri double riešení;
3. NID normalizačné kotvy a staré pomerové kontroly ostanú v pôvodných limitoch;
4. po dosadení vysokopresných štandardných koeficientov prejde celý K7b.1 audit;
5. activity-relative chyba `D'`, definovaná ako `abs(rhs-series_derivative)/abs(series_derivative)`, je `<0.1` na NID/deep aj NID/shallow;
6. každý beh má vnútorný aj vonkajší časový limit.

## Rozhodovanie

- Prvý neúspech zastaví 3a a zdokumentuje sa pred 3b.
- Menšie maticové rezíduum bez splnenia brány `D' < 0.1` nie je úspech.
- PASS 3a môže uzavrieť koeficientový floor K7b, ale stále nie evolučnú C7.7c bránu.

