# A2-K7 — stav a akčný plán po K7.1a-K3.0

**Dátum:** 2026-07-13  
**Kanonický stav:** `PREŽÍVA 30/100`  
**Aktívny krok:** K7.1a-K3.1 — stochastic/open-EFT pôvod

## Aktuálny strom

| Podkoľaj | Stav | Najbližšia alebo posledná stena |
|---|---|---|
| K7.1a-K1 | `MŔTVA M-014a` | konštantná produkčná šírka nevie sledovať povinný `H` člen |
| K7.1a-K2 | `PREŽÍVA IBA REKONŠTRUKCIU` | chýba nezávislá spektrálna hustota, pamäť a noise |
| K7.1a-K3 | `PREŽÍVA IBA FORMULAČNÚ BRÁNU` | kovariantné `Theta_phi` a `delta Theta_phi` existujú; chýba open-EFT pôvod a regulárny nulový limit |
| K7.1a-K4 | `ČAKÁ` | prahová produkcia môže zmeniť A1 a prejsť do K10/v4 |

## K3.1 — povinné úlohy

1. zapísať najvšeobecnejšiu kvadratickú Schwinger-Keldysh akciu pre
   disipativny skalárny kanál kompatibilný s difeomorfizmami;
2. identifikovať retardačný kernel, z ktorého v lokálnom limite vznikne
   člen úmerný `Theta_phi rho_F`;
3. zapísať zodpovedajúci symetrický/noise kernel a jeho pozitivitu;
4. určiť korelačný čas a overiť
   `tau_corr*max(H,Upsilon,|dot Upsilon/Upsilon|)<<1`;
5. zahrnúť backgroundovú energiu, tlak a entropiu bathu podľa AR12;
6. preveriť, či single-crossing akcia
   `g^2(phi-phi_*)^2 chi^2` vôbec dáva spojitý zdroj; ak nie, nesmie sa
   používať ako dôkaz K3;
7. pri zlyhaní zapísať M-014b, pri prežití pokračovať K7.1b.

## Čo sa zatiaľ nesmie robiť

- nespúšťať `S8` grid;
- nenazývať `delta Q1` úplnými perturbáciami;
- nevynechať stochastic/noise sektor;
- nepočítať formulačný prechod ako zvýšenie skóre;
- neoživovať K1 stavovo závislým názvom pre konštantnú šírku.

