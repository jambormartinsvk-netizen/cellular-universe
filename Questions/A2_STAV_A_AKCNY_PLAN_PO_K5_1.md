# A2/Q20 — stav a akčný plán po K5.1

**Dátum:** 2026-07-13

## Aktuálny stav

| Koľaj | Stav |
|---|---|
| A2-K1 | `MŔTVA M-009` |
| A2-K2 | `MŔTVA M-008` |
| A2-K3 | `MŔTVA M-010` |
| A2-K4 | `MŔTVA M-011` |
| A2-K5/K1 | `PREŽÍVA A2-K5.1 — 60/100; A3 RASTOVÁ BRÁNA ČERVENÁ` |

K5/K1 prešla rovnicami, nulovým limitom, constraintmi, relatívnym aj
adiabatickým superhorizontovým módom. Nezomrela. Jej kvázistatická sila však
zvyšuje rast, takže nemá observačný verdikt.

## Najbližšie kroky

### A3-K5/K1 — povinné dokončenie živej koľaje

1. implementovať `delta_n`, `theta_c`, `chi` a `chi'` do CLASS alebo CAMB;
2. zachovať štandardnú fotónovú, neutrínovú a baryónovú hierarchiu;
3. reprodukovať `lambda=0` spektrá;
4. overiť superhorizontové počiatočné série hlboko v radiačnej ére;
5. vypočítať CMB TT/TE/EE, lensing, `P(k)`, `f sigma8` a `S8`;
6. bez nového parametra rozhodnúť `PREŽÍVA N/100` alebo `MŔTVA M-012`.

### Nový smer s najvyššou šancou

Založiť A2-K5/K3a: derivatívnu `f(n_c,phi,X,Z)` akciu s energy aj momentum
transferom a predregistrovanou podmienkou `G_eff,c<=G`. Najprv iba akcia,
kinetická matica, nulový limit a background; až potom perturbácie.

## Čo sa nesmie urobiť

- označiť `S8 približne 0.920` za plnú predikciu;
- zabiť K5/K1 iba kvázistatickou projekciou;
- ponechať z K5/K1 trenie a vymazať piatu silu;
- oživiť K1–K4 novou gauge alebo nulovou počiatočnou amplitúdou;
- pridať nezávislý „screening parameter“ až po výsledku;
- tváriť sa, že prahový `Gamma_eff(a)` je stále ten istý A1-K1 background.

## Verzia

K5/K1 môže zostať kandidátnym efektívnym dokončením v3.18, kým sa nemení
fundament a kým je jasne označená za nedokončenú v A3. K5/K3a môže zostať vo
v3 iba ako alternatívna efektívna akčná koľaj. Explicitný nový mediátor,
produkčný fundament alebo zmena časového profilu `Gamma` pravdepodobne patria
do verzie 4.
