# A2-K4 / C7.7c / K7b.1 — číselné brány koeficientového auditu

**Dátum registrácie:** 2026-07-14, pred prvým behom skriptu 166  
**Nadväzuje na:** všeobecnú preregistráciu K7b  
**Rozsah:** bez ODE a bez bodov

## Autoritatívne projektované seedy

Pri NID sa druhové hustoty a momenty rušia až pod presnosť float64 koeficientového solvera. Preto sa projektované seedy neurčia druhovým double súčtom, ale z nezávislých metrických radov:

\[
D_{metric}=\frac{h_x-2s^2\eta}{3},\qquad M_{metric}=\eta_x.
\]

Druhové súčty

\[
D_{species}=\sum_A\Omega_A\delta_A,
\]

\[
M_{species}=(2\Omega_\gamma+1.5\Omega_b)U_\gamma
 +2\Omega_{fs}U_{fs}+1.5\delta\Omega_fU_f
\]

zostávajú nezávislou constraintovou kontrolou. Koeficienty exportované skriptom 165 sú pôvodné registrované float64 výsledky po exact-zero projekcii. Mpmath nemení presnosť ich pôvodu; iba zabráni ďalšej strate cifier pri mocninách a súčtoch.

## Fixné nastavenia

- `mpmath` presne 80 desatinných miest;
- `standard_order=6`, `k=0.05 Mpc^-1`, koeficient paliva 1;
- NID/deep, NID/shallow, NIV/deep, NIV/shallow v tomto poradí;
- priamy `ell=denominator_x/denominator`;
- každý zdrojový, auditný aj vonkajší beh má časový limit.

## Číselné brány na každom povrchu

1. zdrojový export prejde a mená `standard`, `fractional`, `fuel` sú presné;
2. relatívny rozdiel vysokopresného a exportovaného `z` je `<5e-14`;
3. rekonštruované exportované stavové hodnoty a ich `h_x,eta_x` spĺňajú zmiešanú toleranciu `5e-14 + 5e-12*scale`;
4. druhové constraintové rezíduá normalizované súčtom absolútnych členov sú `<5e-12`;
5. rekonštrukcia `delta_fs,U_fs` z `D_metric,M_metric` má normalizovanú chybu `<5e-12`;
6. metrické identity po dosadení `D_metric,M_metric` majú absolútne rezíduum `<1e-60` v 80-cifernej aritmetike;
7. každá z 13 derivácií projektovaného RHS spĺňa

```text
abs(residual) < 5e-12 + 5e-8*max(abs(rhs), abs(series_derivative))
```

8. všetky hodnoty sú konečné.

## Rozhodovanie

- Prvý nový neúspech zastaví ďalšie povrchy a najprv sa zdokumentuje.
- Rezíduum pod koeficientovou/roundoff hranicou nezabíja fyzikálnu koľaj, ale musí zostať reportované.
- Prahy sa po výsledku nemenia.
- PASS všetkých štyroch povrchov uzavrie K7b, stále však neoprávňuje zvýšiť hĺbku bez evolučnej brány.

