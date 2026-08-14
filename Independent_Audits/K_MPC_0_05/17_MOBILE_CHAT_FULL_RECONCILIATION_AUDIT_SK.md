# K_MPC = 0.05 — audit úplného mobilného súhrnu

**Dátum:** 2026-07-15  
**Vstup:** úplný mobilný súhrn dodaný autorom teórie.  
**Účel:** zjednotiť mobilné vysvetlenie s immutable auditmi P1–P4 bez tichého
zvyšovania stavu K-N2.

## Potvrdené body

| Bod zo súhrnu | Verdikt | Presný rozsah |
|---|---|---|
| `p=4-3 delta` pochádza z pomeru `rho_f/rho_r`, nie z Fourierovho módu. | **PASS** | Presná ranej-éra continuity identita je v `03_FUEL_TERM_PROVENANCE_AND_K_ROLE_SK.md`. |
| `z=k a/(H0 sqrt(Omega_r0))` je perturbatívna/horizontová súradnica. | **PASS** | V existujúcej proveniencii je `k` komový Fourierov mód; nie odvodená škála siete. |
| `Phi(k)=A_f(H0 sqrt(Omega_r0)/k)^p` dáva `Phi z^p=A_f a^p`. | **PASS, algebraický** | Zrušenie holého `k^p` je presné. |
| Aj `g2 z^2=lambda a^2/sqrt(Omega_r0)` je bez `k`. | **PASS iba v radiačnom limite** | Mimo neho je `Gamma/H=lambda/E(a)` a plná exponenciála sa musí odvodiť z presného A1 backgroundu. |
| K-N3, K-N4 a K-N5 nie sú prípustná oprava univerzálneho backgroundu. | **MŔTVE pre background** | Ich dôvody ostávajú v `02_TRACKS.md`. |

## Dôležité opravy oproti mobilnému textu

### `A_f` už nie je neznámy nový fit

Mobilný text správne uvádza, že úplné uzavretie záviselo od `A_f`, ale tento
krok už odvtedy prešiel ako **P2a**. Zo zmrazeného A1-K1 closure, bez vstupu
`K_MPC` alebo Fourierovho `k`, vyšiel

```text
A_f = 7809.270101963506.
```

To je parameter-bookkeeping PASS, nie mikrofyzikálne odvodenie A1 z buniek.
P2b — pôvod samotného zmrazeného A1 closure — zostáva otvorený.

### `D_univ` z K7 radu nie je dovolené povýšiť na plný `H(a)`

Po normalizácii je skorý fuel/ash rad k-nezávislý, ale P3 ukázal, že jeho
neskrátená extrapolácia nie je globálny background: `D_K7,trunc` prejde
nulou pri `a≈0.70896`. Preto univerzálny background, ktorý sa smie použiť
ďalej, je presný

```text
D_A1(a)=a^4 E_A1(a)^2/Omega_r0,
H(a)=H0 sqrt(Omega_r0 D_A1)/a^2,
```

nie formálne pokračovanie skorého K7 radu až do súčasnosti. P4a tento
k-nezávislý exact-A1 mapping už overila.

## Aktuálny rozsudok koľají

| Koľaj | Stav | Čo ešte rozhoduje |
|---|---|---|
| K-N1 | `REVIEW` | samostatný mechanizmus korelačnej škály siete bez nového fitu |
| K-N2 | `ŽIVÁ, čiastočne uzavretá` | P2a prešla; P2b a plný perturbatívny successor na exact-A1 backgrounde zostávajú otvorené |
| K-N3 | `MŔTVA` | módovo závislý FLRW background |
| K-N4 | `MŔTVA pre background` | pivot s implicitným `Phi=1` mení fyziku |
| K-N5 | `MŔTVA` | menila by odvodený exponent namiesto normalizácie |

## Záväzná formulácia pre ďalšiu prácu

`K_MPC=0.05` sa v starej K7 línii **nesmie** opisovať ako fundamentálna
škála siete. Je to pevne vložená hodnota perturbatívneho `k`; jej spojenie s
Planck pivotom je plausibilná konvencia, nie doložený úmysel zdrojového kódu.
Staré K7 backgroundové runnery ostávajú `DO_NOT_USE_PHYSICS`.

Otvorená práca sa už nevolá „nájsť význam 0.05“, ale: preniesť plný A2-K4
species-first perturbatívny systém na `D_A1(a)` s regular seedmi, constraintmi
a plnou hierarchiou. To je súčasná vetva P5 v `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/`.

## Oddelená otázka produkčných ciest

Otázka, či delenie tvorí hmotu, popol a paru paralelne alebo reťazcovo, nie
je dôsledok K_MPC opravy. Zostáva samostatná hypotéza: treba vytvoriť
paralelnú aj reťazcovú koľaj s vlastným ledgerom, BBN/CMB/rast/lensing
bránami a bez prenášania verdiktu K-N2.
