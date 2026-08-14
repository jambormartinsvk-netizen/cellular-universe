# Akčný plán po K7d / C7-G4+G6+G7

**Dátum:** 2026-07-15  
**Vstup:** integrované G4+G6+G7 PASS  
**Aktívny krok:** C7-G8

## Aktuálny stav

Numerické jadro K7d prešlo NID/NIV × deep/shallow, 13-zložkovou aktivitou,
Einsteinovými consistency ledgermi a deep/shallow zhodou. C7-W1 support a
WBS-1 sú `90/100`; otvorené ostáva `10/100`.

## Najbližší balík — G8

Pred prvým behom treba rozhodnúť jednu architektúru plnej hierarchie:

1. určiť maximálne multipóly a closure/convergence sweep;
2. zahrnúť plnú fotónovú a neutrínovú hierarchiu, anizotropný stres a
   baryón-fotónové väzby;
3. rozhodnúť, či sa použije existujúci CLASS/CAMB backend alebo vlastný
   spoločný operator; nové fyzikálne parametre sa nesmú pridať potichu;
4. zmraziť analytické nulové limity, hierarchy convergence, runtime a
   najviac dve technické opravy;
5. vykonať najprv lacný high-weight screen, až potom plný výpočet.

Architektúra, očakávania, PASS/STOP hranice, timeouty a skriptový rozpočet
sú od 2026-07-15 zmrazené v:
`tracks/A1/A1K1/A2/A2K4/SUBTRACKS/C7_7c/K7/G8_FULL_BOLTZMANN/00_PREREGISTRATION.md`.

G8 má iba dve pevné úrovne `SCREEN` a `FULL`. SCREEN nepridáva body. Nové
K7 suffixy ani nové Q sa pre technické varianty nevytvárajú.

PASS G8 zvýši support na `95/100` a otvorí G9. Reprodukovateľná nestabilita,
porušenie Einstein–Boltzmann konzistencie alebo nekonvergentná hierarchia s
platnou numerikou môže zastaviť K7/A2-K4. Timeout zostáva technický REVIEW.

## Potom — G9

Zmrazená fyzika G0–G8 sa pripojí na CMB/S8 likelihood. Po otvorení dát sa
nesmie meniť mechanizmus alebo parameter iba na trafenie pozorovania.

