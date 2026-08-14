# A2-K7.1a — audit prvých dvoch mikrofyzických koľají

**Dátum:** 2026-07-13  
**Rozsah:** K7.1a-K1 a K7.1a-K2  
**Nadradený stav:** `A2-K7 PREŽÍVA 30/100`

## Rozsudok

```text
K7.1a-K1 fixed-width cascade = MŔTVA M-014a
K7.1a-K2 open-system Upsilon = PREŽÍVA IBA REKONŠTRUKCIU
A2-K7 ako celok              = PREŽÍVA 30/100, bez zvýšenia skóre
```

## 1. Algebra presného K7.0 backgroundu

Pri

```text
rho_M=epsilon rho_F,
rho_phi=(1-epsilon)rho_F,
Q2=Gamma rho_F
```

je presne potrebné

```text
Q1=[(1-epsilon)Gamma+3H epsilon(1-delta)]rho_F.
```

Člen s `H` nie je voľná numerická oprava. Kompenzuje rozdiel medzi
prachovým riedením mediátora a near-vacuum vývojom celého sektora pri
konštantnom `epsilon`.

## 2. K7.1a-K1 — konštantné šírky

Najjednoduchší lokálny rozpad dáva

```text
Q2=Gamma_chi rho_M,
Q1=Gamma_phi rho_phi.
```

Z `Q2` sa dá odvodiť zdravá konštanta

```text
Gamma_chi/H0=lambda/epsilon.
```

Z `Q1` však vychádza

```text
Gamma_phi/H0=lambda
  +3E(a)epsilon(1-delta)/(1-epsilon).
```

Pre `epsilon>0`, `delta!=1` a meniace sa `E(a)` nejde o konštantu. Na
predregistrovanom gride výsledok skriptu 55 je:

| `epsilon/delta` | `Gamma_phi/H0` pri rekombinácii | dnes | pomer max/min |
|---:|---:|---:|---:|
| 0.01 | 16.0391 | 0.150673 | 106.449 |
| 0.05 | 79.6683 | 0.153370 | 519.451 |
| 0.10 | 159.370 | 0.156748 | 1016.72 |
| 0.25 | 399.579 | 0.166929 | 2393.70 |
| 0.50 | 803.648 | 0.184055 | 4366.36 |
| 0.90 | 1460.02 | 0.211874 | 6890.98 |

Tento no-go je algebraický. Nezávisí od integračnej tolerancie ani od
počiatočnej amplitúdy perturbácií. M-014a zabíja iba konštantnú produkčnú
šírku, nie časovo/stavovo závislý otvorený systém.

## 3. K7.1a-K2 — rekonštruované otvorené trenie

Pre kanonický skalár

```text
rho_phi+p_phi=dot(phi)^2=(delta-epsilon)rho_F
```

a stredný disipativny zákon `Q1=Upsilon dot(phi)^2` vyžaduje

```text
Upsilon/H0=[(1-epsilon)lambda
            +3E epsilon(1-delta)]/(delta-epsilon).
```

Skript 56 preukázal:

- `delta-epsilon>0` na celom gride;
- `phi(x)` je monotónne a prejde `0.0665–0.2093 M_Pl`;
- `Upsilon(phi)>0` a je konečné;
- backgroundový zdroj sa reprodukuje na `2.776e-17–5.551e-17`;
- `Upsilon/H0` sa mení faktorom `106.45–6890.98`;
- dnes je `Upsilon/H=6.62–90.33`, pri rekombinácii
  `0.0299–26.38`.

Existencia jednej monotónnej trajektórie znamená, že požadovanú časovú
funkciu možno vždy premenovať na funkciu poľa. Preto to nie je odvodenie
couplingu. K2 prejde až vtedy, keď konkrétna spektrálna hustota alebo CTP/2PI
výpočet vytvorí tento tvar vopred a súčasne určí šum.

Výpočty nonequilibrium kvantových polí ukazujú, že presný Langevinov opis
obsahuje pamäť aj noise a lokálny Markovovský limit nie je automatický
(Gautier a Serreau, <https://arxiv.org/abs/1209.1827>). Disipácia
kozmologického skalára je viazaná na produkciu fluktuácií
(Bartrum, Berera a Rosa, <https://arxiv.org/abs/1412.5489>).

## 4. Prečo sa skóre nezvyšuje

K7.0 už mala presný ledger a kontraktívnu collision maticu. K7.1a-K2 zatiaľ
iba rekonštruovala koeficient z toho istého ledgeru. Neodvodila nový
mikroskopický parameter, kernel ani perturbáciu. Preto zostáva `30/100`.

## 5. Nasledujúca brána

Aktívna je K7.1a-K3:

1. definovať kovariantný expansion scalar `Theta` a jeho referenčný rámec;
2. odvodiť `delta Q1`, najmä povinný člen `epsilon(1-delta)rho_F deltaTheta`;
3. uzavrieť celkový momentum ledger;
4. zistiť, či operátor vznikne z lokálnej otvorenej EFT s entropiou a
   šumom, alebo je iba backgroundovou tautológiou;
5. až po prejdení zostaviť úplné superhorizontové módy.

Ak K3 zlyhá, pokračuje sa K2 s explicitne zvolenou spektrálnou hustotou;
nesmie sa použiť už zrekonštruovaný výsledok ako vstup bez nezávislej
mikrofyziky.

