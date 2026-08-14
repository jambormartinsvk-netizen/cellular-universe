# A2-K7.1a-K3.1 — audit Onsagerovej a noise pozitivity

**Dátum:** 2026-07-13  
**Skript:** `scripts/58_script_A2_K7_K3_1_onsager_noise_positivity_gate.py`

## Rozsudky

```text
K7.1a-K3.1-K1 bare cross-only = MŔTVA M-014b
K7.1a-K3.1-K2 completed Onsager = PREŽÍVA IBA TERMODYNAMICKÚ FORMULÁCIU
A2-K7 parent = PREŽÍVA 30/100
```

## 1. Predpoklady a rozsah

Audit platí pre lokálnu near-equilibrium otvorenú EFT s Onsagerovou
reciprocitou a lokálnym KMS limitom. Ak by systém bol ďaleko od rovnováhy a
bez lokálnej entropickej expanzie, išlo by o inú podkoľaj s vlastným
kernelom; nemožno ňou spätne oživiť K3.1-K1.

Termodynamické sily boli bezrozmerne normalizované. Preto sú auditované
znamienka, determinant a existencia pozitívneho doplnenia, nie fyzikálne
jednotky alebo veľkosť viskozity.

## 2. Holý cross-term

Po zoskupení reakčného fluxu a bulk stressu:

```text
J=-L X,
L_bare=[[0,alpha],[alpha,0]],
alpha=epsilon(1-delta).
```

Pre každé `epsilon>0`:

```text
eig(L_bare)={-alpha,+alpha}.
```

Kvadratická produkcia entropie `X^T L X` preto môže byť záporná. Holý
expanzný zdroj bez diagonálnej reakcie, recipročného stressu a noise nie je
prípustnou near-equilibrium dissipativnou EFT.

Na gride sa `alpha` menilo od `2.24424e-4` po `2.01981e-2`; záporná vlastná
hodnota vznikla vo všetkých šiestich bodoch.

## 3. Pozitívne doplnenie

Všeobecná symetrická matica

```text
L=[[ell,alpha],[alpha,zeta]]
```

je pozitívne semidefinitná práve pri

```text
ell>=0,
zeta>=0,
ell*zeta>=alpha^2.
```

Skript použil iba demonštračnú normalizáciu

```text
ell=1,
zeta=1.01 alpha^2,
T=1.
```

Všetky vlastné hodnoty `L` aj normalizovanej noise matice `2TL` boli
kladné. Matematická termodynamická kompletizácia teda existuje.

## 4. Prečo to ešte nie je fyzikálny prechod K7.1

Voľba `ell=1` je normalizácia, nie odvodený reaction coefficient. Kladné
`zeta` vytvára bulk pressure, ktorý K7.0 nemala. Local-KMS noise vyžaduje
teplotu alebo všeobecnejší stav bathu. Ani jedna z týchto veličín ešte nemá
miesto v backgroundovom ledgeri.

Pozitívna matica preto dokazuje iba, že K3 nemá všeobecný termodynamický
no-go po doplnení nových fyzikálnych členov. Nedokazuje, že pôvodný
`phi,chi,psi_c` scaffold tieto členy vytvorí alebo že zachová A1.

## 5. Max. hĺbka

| Podkoľaj | Stav | Max. hĺbka |
|---|---|---:|
| K7.1a-K3.1-K1 | `MŔTVA M-014b` | `38/100` |
| K7.1a-K3.1-K2 | `PREŽÍVA IBA TERMODYNAMICKÚ FORMULÁCIU` | `38/100` |
| nadradená A2-K7 | `PREŽÍVA K7.0` | akceptovaných `30/100` |

Hĺbka `38/100` neznamená, že K7 prešla K7.1. Ide o najhlbšie vykonaný test
podkoľaje. Akceptačná hranica mikrofyzickej K7.1a je predregistrovaná na
`40/100`.

## 6. Ďalší krok

K3.1-K2.1 musí rozmerovo uzavrieť affinity/reaction/bulk/noise systém a
znovu prepočítať entalpický budget. Bez toho sa nesmie odvodiť úplná
superhorizontová matica.

