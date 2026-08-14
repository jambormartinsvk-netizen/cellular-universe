# A2-K7.1a-K3.1 — Onsagerov problém a podkoľaje

**Dátum:** 2026-07-13  
**Nadradená koľaj:** A2-K7  
**Kanonický stav nadradenej koľaje:** `PREŽÍVA K7.0 — 30/100`

## Význam stĺpca Max. hĺbka

`Max. hĺbka` označuje najhlbšiu skutočne vykonanú auditnú kontrolu danej
podkoľaje. Neznamená, že nadradená K7 túto bránu prijala. K7 sa posunie nad
`30/100` až po uzavretí rozmerových koeficientov, bath ledgeru, noise a
mikrofyzického kernelu.

## Aktuálny strom s maximálnou hĺbkou

| Podkoľaj | Fyzikálny základ | Stav | Max. hĺbka | Dôvod smrti alebo stena |
|---|---|---|---:|---|
| K7.1a-K1 | konštantné on-shell šírky | `MŔTVA M-014a` | `32/100` | produkčná šírka by sa musela meniť faktorom `106–6891` |
| K7.1a-K2 | rekonštruované `Upsilon(phi)` | `PREŽÍVA IBA REKONŠTRUKCIU` | `34/100` | chýba spektrálny kernel, noise a bath ledger |
| K7.1a-K3.0 | lokálny `Theta_phi` operátor | `PREŽILA FORMULAČNÚ BRÁNU` | `36/100` | kovariancia prešla, ale nie otvorená termodynamika |
| K7.1a-K3.1-K1 | holý cross-term expanzia → reakcia | `MŔTVA M-014b` | `38/100` | Onsagerova matica `[[0,alpha],[alpha,0]]` má zápornú vlastnú hodnotu |
| K7.1a-K3.1-K2 | pozitívne Onsagerovo doplnenie | `PREŽÍVA IBA TERMODYNAMICKÚ FORMULÁCIU` | `38/100` | chýbajú rozmerové koeficienty, teplota, bulk-pressure background a mikrofyzika |
| K7.1a-K4 | prahová/neadiabatická produkcia | `ČAKÁ` | `5/100` | pri zmene A1 patrí do K10/v4 |

## K3.1-K1 — prečo zomrela

Po normalizácii termodynamických síl je skalárna odozva

```text
(reaction flux, bulk stress)^T
  = -L (chemical affinity, expansion)^T.
```

Holá K3 chcela ponechať iba vzájomný cross-koeficient:

```text
L_bare=[[0,alpha],[alpha,0]],
alpha=epsilon(1-delta)>0.
```

Jej vlastné hodnoty sú `-alpha,+alpha`. Entropická kvadratická forma preto
nie je pozitívna pre všetky lokálne odchýlky. Toto je termodynamická smrť
konkrétnej holej realizácie, nie numerická chyba.

## K3.1-K2 — čo musí pribudnúť

Najmenšie všeobecné doplnenie je

```text
L=[[ell,alpha],[alpha,zeta]],
ell>=0,
zeta>=0,
ell*zeta-alpha^2>=0.
```

Pri lokálnom termálnom/KMS limite je noise kovariancia úmerná `2T L`.
Skript 58 ukázal, že pozitívne doplnenie matematicky existuje na celom
gride. Neurčil však fyzikálne jednotky ani hodnoty `ell,zeta,T`.

Táto koľaj je od holej K3 fyzikálne odlišná, pretože obsahuje:

- chemickú reakčnú odozvu;
- recipročný bulk-stress kanál;
- bulk-viskózny tlak na backgrounde;
- korelovaný reaction/bulk noise;
- nový entropický a bath ledger.

## Nasledujúca brána K3.1-K2.1

1. zaviesť rozmerovo správne termodynamické sily a chemickú afinitu;
2. odvodiť `ell,alpha,zeta` z konkrétneho collision alebo SK kernelu;
3. vypočítať bulk pressure `Pi` a kompenzovať ho v celkovom `p_F` bez
   porušenia kladnej entalpie;
4. určiť teplotu/stav bathu a noise maticu;
5. overiť lokálny KMS/Markovovský rozsah;
6. ak to nie je možné bez spätného fitu, vyhlásiť K3.1-K2 mŕtvu ako
   M-014c;
7. iba pri prežití zvýšiť kanonické skóre K7 a pokračovať K7.1b.

EFT dissipativnych fluidov vyžaduje noise a lokálne KMS/Onsagerove väzby
(Crossley, Glorioso a Liu, <https://arxiv.org/abs/1511.03646>). Chemické
reakcie a bulk viskozita sú fyzikálne previazané kanály, nie nezávislé
pozadie bez spätného tlaku
(Gavassino, Antonelli a Haskell, <https://arxiv.org/abs/2003.04609>).

