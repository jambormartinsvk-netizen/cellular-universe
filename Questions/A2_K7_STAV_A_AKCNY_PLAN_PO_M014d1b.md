# A2-K7 — stav a akčný plán po M-014d1b

**Dátum:** 2026-07-13  
**Kanonický stav K7:** `PREŽÍVA K7.0 — 30/100`  
**Najhlbšia nová podkoľaj:** mŕtva K1a2a — `42/100`  
**Aktívna podkoľaj:** K3.1-K2.2-K1a2b-K1

| Podkoľaj | Stav | Max. hĺbka | Dôvod/stena |
|---|---|---:|---|
| K1a1 | `MŔTVA M-014d1` | `40/100` | iba thermal `2->2` rate no-go |
| K1a2a | `MŔTVA M-014d1b` | `42/100` | nekoherentná KMS emisia/absorpcia príliš slabá |
| **K1a2b-K1** | **`AKTÍVNA`** | **`5/100`** | kauzálne konečná koherentná doména |
| K1a2b-K2 | `ČAKÁ` | `5/100` | ideálny superradiant horný limit |
| K1a2b-K3 | `ČAKÁ` | `5/100` | globálna sieťová koherencia |
| K1a2c/K2 | `PRESUNUTÁ` | `42/100` | high-frequency non-KMS farebný kernel |
| K1b1 | `MŔTVA M-014d2a` | `41/100` | vedúce zosilnenie soft coupling |
| K1b2 | `ČAKÁ` | `5/100` | curvature operator basis; nezabitá |

## Akčný plán K1a2b-K1

1. definovať mikroskopickú emisnú jednotku a jej energiu/quadrupole moment;
2. odvodiť maximálnu kauzálnu koherentnú doménu, nie ju vložiť ako fit;
3. zapísať form factor `F(kR)` a efektívny počet `N_eff(k)`;
4. rozlíšiť škálovanie rate `N`, `N^2` a saturáciu optickej hrúbky;
5. porovnať dosiahnuteľné zosilnenie s požadovaným
   `2.2e26–3.7e33` na celom backgrounde;
6. overiť dobu dekoherencie voči `H^-1` a bath korelačnému času;
7. uzavrieť energy/backreaction ledger a šum;
8. uložiť výpočet ako skript 63; pri neúspechu zachovať dôvod a pokračovať
   K1a2b-K2.

K7.1b lineárne perturbácie zostávajú zablokované. Max. hĺbka listu
nepromuje K7 nad `30/100`.

