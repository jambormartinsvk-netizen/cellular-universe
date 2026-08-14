# A2-K7.1a — problém mikrofyzických sadzieb a koľaje

**Dátum:** 2026-07-13  
**Nadradená koľaj:** A2-K7, konečno-entalpický mediátor  
**Stav nadradenej koľaje:** `PREŽÍVA K7.0 — 30/100`

## Problém

Presný background K7.0 pri konštantnom `epsilon` vyžaduje

```text
Q2 = Gamma rho_F,
Q1 = [(1-epsilon)Gamma + 3H epsilon(1-delta)]rho_F.
```

K7.1a musí určiť, či tieto zdroje vzniknú z lokálnej fyziky. Samotné
dosadenie funkcie, ktorá presne reprodukuje požadovaný background, nie je
mikrofyzické odvodenie.

## Koľaje

| Koľaj | Základ | V čom je iná | Stav |
|---|---|---|---|
| K7.1a-K1 | on-shell reťaz s konštantnými šírkami `phi -> chi -> c` | oba zdroje majú byť obyčajné konštantné proper-time rozpady | `MŔTVA M-014a` |
| K7.1a-K2 | otvorený systém `Q1=Upsilon(phi,state) dot(phi)^2` | koeficient sa môže meniť s lokálnym stavom, ale musí vzniknúť spolu s pamäťou a šumom | `PREŽÍVA IBA REKONŠTRUKCIU; BEZ ZVÝŠENIA SKÓRE` |
| K7.1a-K3 | expanzne riadený kovariantný operátor s `Theta=nabla_mu u^mu` | člen úmerný `H` sa berie ako lokálny expansion-scalar efekt a určuje vlastné `delta Theta` | `ČAKÁ; NASLEDUJE` |
| K7.1a-K4 | neadiabatická/instant-preheating produkcia pri prahu `phi_*` | produkcia je udalosť alebo séria prahov, nie spojitá Markovovská sadzba | `ČAKÁ; PRI ZMENE Q2/H(z) PRECHÁDZA DO A1-K2/A2-K10` |

## K7.1a-K1 — dôvod smrti

Ak

```text
Q2=Gamma_chi rho_M,
Q1=Gamma_phi rho_phi
```

a šírky sú konštantné, potom presný ledger vynúti

```text
Gamma_chi/H0=lambda/epsilon,
Gamma_phi_required/H0
  =lambda+3E(a)epsilon(1-delta)/(1-epsilon).
```

Prvá šírka je konštantná, druhá nie. Na predregistrovanom gride sa musí
meniť faktorom `106.45–6890.98` od rekombinácie po dnešok. To nie je
konštantný lokálny rozpad. K1 je preto mŕtva ako M-014a. Jej skript a
výstup sa zachovávajú.

## K7.1a-K2 — čo prežilo a čo nie

Pre kanonické palivo platí

```text
dot(phi)^2=(delta-epsilon)rho_F,
Upsilon/H0=[(1-epsilon)lambda
             +3E epsilon(1-delta)]/(delta-epsilon).
```

Na celom gride je `Upsilon>0`, pole je monotónne a funkcia sa dá zapísať
ako jednoznačné `Upsilon(phi)` pozdĺž backgroundu. Presný ledger má
rezíduum najviac `5.551e-17`.

Tým sa dokazuje iba matematická rekonštruovateľnosť. Zostáva nepreukázané:

- spektrálne/retardované jadro, z ktorého `Upsilon` vzniká;
- korelačný čas a Markovovský limit;
- šumový kernel viazaný na disipáciu;
- energia a tlak prípadného ďalšieho bathu;
- či jednoduchá akcia s jediným `g^2(phi-phi_*)^2 chi^2` prechodom vie
  vytvárať spojitý kladný zdroj od rekombinácie po dnešok.

Monotónne pole prejde jednou hodnotou `phi_*` najviac raz. Známy mechanizmus
instant preheating s touto väzbou opisuje rýchlu neadiabatickú udalosť, nie
automaticky trvalý zdroj
(Felder, Kofman a Linde, <https://arxiv.org/abs/hep-ph/9812289>).
Všeobecný kvantový otvorený systém má ne-lokálne pamäťové aj šumové jadro a
lokálny Markovovský opis vyžaduje osobitné podmienky
(Gautier a Serreau, <https://arxiv.org/abs/1209.1827>).

## K7.1a-K3 — nasledujúca koľaj

Najpriamejší kovariantný kandidát zachovávajúci presný v3 background je

```text
Q1 = [(1-epsilon)Gamma
      +epsilon(1-delta)Theta]rho_F,
Theta=nabla_mu u^mu.
```

Na FRW backgrounde `Theta=3H`. K3 však nesmie prebrať iba background:
musí odvodiť referenčné `u^mu`, `delta Theta`, momentum transfer, entropiu
a noise/viscosity partnera. Ak ide iba o premenovanie požadovaného `H`
člena bez lokálnej akcie alebo konzistentnej otvorenej EFT, K3 zomrie.

## Pravidlo pokračovania

- smrť K1 sa nesmie obísť tým, že sa konštantná šírka premenuje na
  `effective constant`;
- rekonštruované `Upsilon(phi)` sa nesmie citovať ako odvodená mikrofyzika;
- K2 a K3 sú odlišné: ich poruchy závisia od `delta phi/state` oproti
  `delta Theta`;
- ak K2 aj K3 zomrú a K4 zmení backgroundový tok, K7 vetva v3 zomrie a K4
  pokračuje iba ako A1-K2/A2-K10.

