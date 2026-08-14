# Python formal error ledger — K7d V2 dodatok

**Dátum:** 2026-07-15  
**Dotknuté diagnostiky:** 213/215  
**Stav:** čaká na skript 216

## FE-K7D-03 — float64 product rule nie je HP parita kompenzovaného D

Aj po injekcii autoritatívneho `D,M` sa derivácia `D_x` skladá z veľkých
členov. Absolútny roundoff `~3.9e-21` sa pri mierke `1.77e-14` javí ako
relatívna chyba `2.22e-7`. Prevencia: parity audit kompenzovaných zdrojov sa
vykoná vo vyššej presnosti; evolved float64 trajektória sa tým nemení.

## FE-K7D-04 — zamenená konvencia F2 a sigma

Starší ledger používal `F2`, pre ktorý platí `F2=2 sigma`. K7 stav ukladá
priamo `sigma_fs`. Prenos starého faktora dal `S=(2/3)Omega_fs sigma`
namiesto správneho `S=(4/3)Omega_fs sigma` a vytvoril falošný traceless
FAIL. Prevencia: každý shear/anizotropic-stress ledger musí exportovať názov
premennej aj mapovanie `F2 ↔ sigma`.

