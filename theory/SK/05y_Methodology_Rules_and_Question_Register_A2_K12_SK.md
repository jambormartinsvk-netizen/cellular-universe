# REGISTER 05 — SK dodatok A2-K12

**Dátum:** 2026-07-14  
**Status:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR pravidlá už vyžadujú zachovanie celkovej energie, oddelenie absolútneho
transferu od referenčného pomeru a uchovanie mŕtvych koľají. Žiadne doterajšie
pravidlo však výslovne nevyžaduje pri viaczložkovom popole oddeliť celkový
hustotný mód od nábojového/izokurvatúrneho módu ani rozlíšiť produkciu častíc
od sily medzi nimi. AR26 preto nie je duplicitné.

## AR26 — Viaczložkový popol musí prejsť súčtovou aj relatívnou bránou

Pri dvoch alebo viacerých druhoch popola sa musia osobitne odvodiť a testovať:

```text
sum_i Q_i,
delta_total a theta_total,
nezávislé relatívne/nábojové módy,
matica G_ij alebo mu_ij,
produkčné zdroje C_i.
```

Zrušenie síl alebo zdrojov v celkovom móde nie je dôkazom stability, pokiaľ
neprešli relatívne módy. Nelineárna fragmentácia alebo rozptyl halo nie sú
náhradou za výpočet lineárneho `sigma8`. Opačný náboj sám osebe nie je zdroj
energie: ak energiu dodáva produkcia páru, jej lokálny operátor a spätná
reakcia sa musia odvodiť samostatne.

## Q52 — Môžu dva druhy popola s opačným skalárnym nábojom zachovať tok a znížiť zhlukovanie?

**Stav:** `ČIASTOČNE; A2-K12 PREŽÍVA 25/100.`

- K12-K1, presne symetrická konformná dvojica bez produkcie, je
  `MŔTVA M-016 — 25/100`: dáva nulový čistý skalárny tok a GR-like celkový
  lineárny mód.
- K12-K2 s asymetriou zostáva otvorená, ale červená: tok sa obnovuje spolu s
  netienenou silou.
- K12-K3, symetrická produkcia párov plus opačné náboje, je aktívna hypotéza
  `20/100`. Musí odvodiť produkčný operátor a nábojový mód.

### Obmedzenie staršej slovnej formulácie

Tvrdenie „opačné náboje otočia piatu silu a súčasne zabezpečia prenos energie
popola“ je obmedzené. Opačné náboje môžu zmeniť silovú maticu, ale pri presnej
symetrii rušia skalárny čistý tok. Nenulový tok symetricky produkovaného páru
musí niesť samostatne odvodený produkčný mechanizmus.

