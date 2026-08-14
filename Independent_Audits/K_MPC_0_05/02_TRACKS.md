# Koľaje auditu významu `K_MPC=0.05`

| Koľaj | Predpoklad | Stav | Čo musí prejsť |
|---|---|---|---|
| K-N1 | `k_*` je fundamentálny globálny inverse correlation scale siete, nie Fourierov mód | REVIEW | odvodiť `k_*` z prvých princípov alebo z už existujúcich konštánt bez nového fitu; ukázať jediné `H(a)` |
| K-N1a | energeticky náročné delenia vytvárajú spoločný stochastický zdroj porúch a prípadne odvodený scale `k_*` | ŽIVÁ HYPOTÉZA / bez skóre | odvodiť `S -> P_S(k) -> zeta`, korelácie palivo–popol–para a každý `k_*` bez CMB fitu; `k` nesmie vstúpiť do `H(a)` |
| K-N2 | v poruchovom fuel term-e `rho_f/rho_r=Phi z^p` musí `Phi(k)=A_f(H0 sqrt(Omega_r)/k)^p`, aby globálny člen bol `A_f a^p` | P1 PREŠLA; P2a PREŠLA; P3 dal STOP pre **skrátený K7 rad ako plný background**; P2b a exact-background rederivation OTVORENÉ | `A_f=7809.27010196` je bez nového fitu; `D_K7,trunc` prejde nulou pri `a≈0.70896`, kým presný A1 je kladný. Výsledok `08`; potrebná je nová odvodená vetva z `D_A1`, nie dosadenie do K7 |
| K-N3 | `K_MPC` je Fourierov mód poruchy aj scale backgroundu | MŔTVA pre globálny background | RUN-FULL-002: `D(a,k)` obsahuje `k^p`; porušuje univerzálnosť FLRW backgroundu |
| K-N4 | `0.05 Mpc^-1` je iba konvenčný/publikačný pivot bez fyzikálneho významu | MŔTVA pre background | ľubovoľná zmena pivotu by zmenila expanziu; konvencia nemôže určovať fyziku |
| K-N5 | nastaviť `p=0`, aby k-závislosť zmizla | MŔTVA | mení už zmrazený exponent `p=3.93109`, teda nie je oprava významu `K`, ale nová teória |

## Priorita

Začíname K-N2, pretože je matematicky najbližšie k existujúcej formule a
nevyžaduje, aby sa `0.05` vydávalo za nový fyzikálny fit. K-N1 je možná
fundamentálna interpretácia iba vtedy, ak používateľ dodá mechanizmus siete,
z ktorého sa scale dá odvodiť.

## Mobilné zjednotenie

Úplný mobilný súhrn bol prečítaný a zosúladený s P1–P4 v
`17_MOBILE_CHAT_FULL_RECONCILIATION_AUDIT_SK.md`. Ten je autoritatívny pre
stav `A_f`, rozsah radiačného limitu a zákaz extrapolácie skráteného K7 radu.
K-N1a je detailný návrh spoločného zdrojového spektra delenia v
`18_K_N1A_DIVISION_SOURCE_SPECTRUM_HYPOTHESIS_SK.md`; patrí pod Q22, nie pod
backgroundový adapter.

## Pravidlo rozsudku

K-N2 neprejde len preto, že algebra odstráni `k`. Musí súčasne zachovať
energetickú normalizáciu, nevložiť nový voľný parameter a prežiť nové
porovnanie s už publikovanými hodnotami. P2a dokázala iba to, že `A_f` nie
je ďalší fit nad zmrazeným A1 closure; P2b a P3 ostávajú podmienkou koľaje.
Ak zmena ovplyvní predpovede, ide o dôvod pre novú Zenodo verziu s
changelogom, nie o tichú opravu.
