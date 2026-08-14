# A2-K4 / C7.7c / K7c.2 — predregistrácia high-precision seed handoffu

Dátum: 2026-07-15  
Vstup: K7c.1 algebraická reprezentácia PASS  
Rozsah: ODE-ready počiatočný stav bez evolúcie a bez bodov

## Dôvod

Transformácia K7c.1 je algebraicky invertibilná, ale dopredný float64 súčet druhových NID stavov znova stráca kompenzovaný zdroj `D`: namiesto autoritatívneho signálu rádovo `1e-23` vytvorí roundoff rádovo `1e-16`. To nevyvracia projektovanú bázu; zakazuje to iba zostaviť jej počiatočný `D,M` z už zaokrúhlených species.

## Autoritatívny handoff

ODE-ready projektovaný stav sa zostaví takto:

- nekompenzované zložky sa vezmú z 80-dps Puiseuxovho vyhodnotenia K7b;
- `D` sa vezme priamo z `D_metric=(h_x-2s^2 eta)/3` v K7b;
- `M` sa vezme priamo z `M_metric=eta_x` v K7b;
- až potom sa 13 hodnôt jednotlivo skonvertuje do float64;
- `D,M` sa nesmú spätne prepočítať zo súčtu float64 species.

## Povinné plochy a zdroje

- NID/deep a NID/shallow: skript 175;
- NIV/deep a NIV/shallow: skript 166;
- rovnaké parametre a background ako v konečnom skripte 176.

## Brány

1. každý zdrojový child skončí PASS a všetky jeho checky sú `true`;
2. projektovaný seed má presne registrovaných 13 mien a všetky hodnoty sú konečné;
3. `D,M` v seedu sa bitovo rovnajú float64 konverzii HP `D_metric,M_metric` z príslušného child výstupu;
4. spätná rekonštrukcia `delta_fs,U_fs` z projektovaného seedu súhlasí s HP druhovým stavom do `5e-14` v škále `max(1,abs(value))`;
5. `h_x=3D+2s^2 eta` a `eta_x=M` prejdú s absolútnou toleranciou `5e-14` plus relatívnou časťou `5e-10`;
6. report musí ukázať aj neautoritatívny `naive_D_from_double_species` a jeho odchýlku, ale táto diagnostika nesmie prepísať seed;
7. každý podproces a celý agregátor majú časový limit.

## Rozhodovanie

- PASS všetkých štyroch plôch povoľuje prvý K7c.3 ODE segment.
- Ak HP seed neumožní stabilnú inverziu species alebo poruší constraint, K7c.2 zomiera.
- Veľký rozdiel voči `naive_D_from_double_species` je očakávaná diagnóza roundoffu, nie FAIL.
- Tento krok nemení `66.5/100`.
