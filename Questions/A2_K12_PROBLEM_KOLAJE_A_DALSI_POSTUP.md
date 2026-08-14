# A2-K12 — problém, koľaje a ďalší postup

**Dátum:** 2026-07-14  
**Cieľ:** overiť, či dva druhy vznikajúceho popola s opačným skalárnym
nábojom dokážu zachovať tok energie palivo -> popol a zároveň znížiť rast
štruktúr bez nestability.

## Problém

Opačné náboje vytvárajú medzi druhmi odpudzovanie, ale pri presnej symetrii
zrušia aj skalárny backgroundový tok. Súčasne vzniká osobitný nábojový mód,
ktorý môže viesť k segregácii namiesto pokojného tlakového rozptylu.

Preto musia byť osobitne auditované:

```text
Q_total, delta_total, delta_charge, theta_total, theta_charge.
```

## Koľaje

| Koľaj | V čom je iná | Stav | Kanonická hĺbka | Historický checkpoint |
|---|---|---|---:|---:|
| K12-K1 | spolieha sa iba na dve presne symetrické konformné väzby | `MŔTVA M-016` | `10/100 = G1` | `25` |
| K12-K2 | ponecháva populačnú asymetriu, aby skalár niesol aj čistý tok | `OTVORENÁ — ČERVENÁ` | `10/100 = G1` | `25` |
| K12-K3 | energiu dodáva samostatná tvorba párov; opačné náboje upravujú iba následné sily | `AKTÍVNA HYPOTÉZA` | `10/100 = G1` | `20` |

## Prečo K12-K1 zomrela

Pri `rho_+=rho_-` platí presne

```text
Q_scalar,total = beta varphi' (rho_+ - rho_-) = 0.
```

Na rovnakej bráne má celkový lineárny mód efektívnu gravitačnú vlastnú
hodnotu `1`, takže sa nezískalo ani požadované lineárne tlmenie `S8`.
Skript, rovnice a čísla sa zachovávajú; M-016 sa nesmie oživiť tvrdením, že
odpudzovanie samo vytvára energiu.

## Akčný plán K12-K3.1

1. Navrhnúť jednu lokálnu, Lorentzovsky a kovariantne konzistentnú reakciu
   `fuel -> c+ + c-`.
2. Odvodiť produkčné sadzby, spätnú reakciu na palivo a skalárny zdroj.
3. Odvodiť kvadratickú akciu alebo ekvivalentnú kinetickú uzáveru vrátane
   produkčného šumu.
4. Oddeliť adiabatický a nábojovo-izokurvatúrny mód.
5. Predregistrovať kill testy: ghost/gradient, rast separácie, CMB
   izokurvatúra, halo segregácia a zlyhanie cieľa `S8`.
6. Nevkladať nový voľný rozptylový parameter podľa `S8`; jeho hodnota musí
   vzniknúť z rovnakého operátora alebo zo symetrie.

## Rozhodnutie

Pokračovať má K12-K3. K12-K2 zostáva rezervná koľaj, kým sa neodvodí presný
vzťah medzi požadovaným tokom, asymetriou a rastovou maticou.

Jednotná rekalibrácia: checkpointy 20/25 dokazujú vykonanú analytiku, ale G2
neprešla žiadna K12 dcéra, pretože registrovaný A1 production ledger nie je
uzavretý bez placeholdera. Fyzikálny M-016 sa nemení.

