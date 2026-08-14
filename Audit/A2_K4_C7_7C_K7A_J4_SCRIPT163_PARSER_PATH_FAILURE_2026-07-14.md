# A2-K4 / C7.7c / K7a-J4 — zlyhanie parserovej cesty skriptu 163

**Dátum:** 2026-07-14  
**Hlavná koľaj:** A2-K4 živá, **66.5/100**  
**Podkoľaj skriptu 163:** **mŕtva ako agregátor**, fyzikálny/Jacobiánový verdikt z nej nebol vydaný

## Čo zlyhalo

Prvý zložený beh NID/deep načítal oba JSON výstupy a správne overil:

- všetky nehistorické kontroly projektovaného auditu boli `true`;
- jediná neúspešná kontrola bola zachovaná stará `NID_deep_K7a_Tprime_fd`;
- vysokopresný J3 audit prešiel so všetkými bránami;
- bezpečná relatívna chyba \(T'\) bola \(1.8845\times10^{-16}\).

Skript 163 však hľadal blok `K7a_projected_jacobian_audit` priamo pod `results/NID/deep`. Skutočná registrovaná cesta je:

```text
results / NID / deep / zero_integration_jacobian_diagnostic /
K7a_projected_jacobian_audit
```

Preto polia `ell_method`, podmienenosť a rezíduá vyšli ako `null` a zložená brána správne skončila `REVIEW`.

## Overenie, že nešlo o fyzikálny neúspech

Priamy výstup skriptu 162 na NID/deep obsahoval:

- `ell_method = denominator_x/denominator`;
- relatívna Frobeniova chyba explicitného a transformovaného Jacobiánu \(9.9437\times10^{-18}\);
- maximálna absolútna chyba \(2.7707\times10^{-16}\);
- \(\kappa_2(T)=4.7954\);
- rezíduum nulového limitu 0;
- plný projektovaný spektrálny polomer \(3.444151542625027\).

## Rozsudok

- Skript 163 sa zachováva ako dôkaz chyby v agregácii.
- Tolerancie, rovnice ani fyzikálne koeficienty sa nemenia.
- Nástupca 164 smie opraviť iba chýbajúcu úroveň `zero_integration_jacobian_diagnostic` a označenie testu.
- Ďalší povrch sa nesmie spustiť, kým opravený agregátor neprejde znovu na NID/deep.

