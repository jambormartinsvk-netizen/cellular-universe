# A2-K4 / C7.7c-K7a-J1 — smrť double-FD kontroly T'

**Dátum:** 2026-07-14  
**Skript:** 159  
**Povrch:** NID/deep, `x=-25`  
**Rozsudok:** J1 je mŕtva numerická podkoľaj; K7a ostáva otvorená  
**Skóre:** bez zmeny, `66.5/100`

## Výsledok

| Brána | Výsledok |
|---|---:|
| `Omega_fs>0` | PASS, `0.4131098542` |
| `cond_2(T)<10^4` | PASS, `4.7954` |
| `det(T)` | `0.34132` |
| explicitný vs transformačný projected Jacobian | PASS |
| relatívna Frobeniova chyba | `1.41×10^-17` |
| maximálna absolútna chyba | `4.44×10^-16` |
| frozen-spectrum chyba | `2.46×10^-15` |
| projected safety `max|A|<10^4` | PASS, `43.535` |
| radiačný nulový limit | PASS, rezíduum `0` |
| double-FD `T'` relatívna chyba `<10^-8` | **FAIL**, najlepšie `6.28×10^-6` |

## Príčina smrti J1

Analytické `T'` má dominantnú škálu iba `ell≈5.1064×10^-8`, kým samotná transformačná matica `T` obsahuje prvky rádu `1`. Centrálna diferencia preto odčíta dve takmer rovnaké double-precision matice.

| FD krok | max. absolútna chyba | relatívna Frobeniova chyba |
|---:|---:|---:|
| `10^-4` | `4.08×10^-13` | `6.28×10^-6` |
| `10^-5` | `7.49×10^-12` | `1.31×10^-4` |
| `10^-6` | `5.36×10^-11` | `7.71×10^-4` |

Menší krok výsledok zhoršuje, čo potvrdzuje roundoff stenu. Prah sa po výsledku neuvoľňuje.

## Čo zostáva platné

- explicitné odvodenie `D',M'`;
- povinný connection člen `T'T^-1`;
- znamienka a nulový limit;
- dobrá invertibilita transformácie;
- projected Jacobian bez veľkých škálovacích artefaktov.

Tieto PASS však zatiaľ nestačia na úplný K7a verdict, pretože predregistrovaná nezávislá kontrola `T'` zlyhala svojou numerickou metódou.

## Následník

K7a-J2 overí rovnakú analytickú `T'` v 80-cifernej aritmetike bez zmeny rovníc alebo prahu. J1 ani skript 159 sa nemažú.

