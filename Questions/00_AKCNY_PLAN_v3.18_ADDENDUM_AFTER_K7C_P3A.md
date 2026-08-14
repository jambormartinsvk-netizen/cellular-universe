# Akčný plán po K7c P3a-A

Dátum: 2026-07-15

## Aktuálny rozsudok

P3a-A je PASS iba pre presnú nulovosť dvoch koeficientov. A2-K4 ostáva
`66.5/100` a G5 ostáva REVIEW, kým sa nezopakuje evolúcia.

## P3a-B — povinné poradie

1. zmraziť skript 197, P1 raw, skript 201 a P3a-A raw hashmi;
2. vytvoriť nový číslovaný skript, ktorého jediná fyzikálna zmena je
   `c_U=0` a `c_delta=0` na auditovanom backgrounde;
3. staticky dokázať, že ostatných sedem členov `M'`, seed, background,
   stavová báza, closure, kroky, normy a prahy sa nezmenili;
4. vykonať py_compile, help/smoke a nový versioned corpus checker;
5. s interným aj externým timeoutom zopakovať mriežky 100/200/400;
6. vyhodnotiť bez zmeny prahov:
   pomer `(100/200)/(200/400) in [8,32]` a
   `diff200/400 < 1e-6`;
7. zapísať raw JSON, hashe, konečný audit, route HISTORY a stav.

PASS oboch brán otvorí širší G4/G6 audit. FAIL ktorejkoľvek fyzikálnej brány
uzavrie P3a-B ako mŕtvu s dôkazmi a presunie prioritu na lokálnu
tuhosť/eigenmódy. Timeout alebo provenance chyba je REVIEW, nie fyzikálna
smrť.
