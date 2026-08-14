# A2-K7.1a-K3 — kovariantná brána expansion-scalar operátora

**Dátum:** 2026-07-13  
**Stav podkoľaje:** `PREŽÍVA IBA FORMULAČNÚ BRÁNU`  
**Stav A2-K7:** `PREŽÍVA 30/100; BEZ ZVÝŠENIA SKÓRE`

## 1. Kandidát

Ako lokálny replacement backgroundového `3H` sa používa expanzia
donorového paliva:

```text
Theta_phi=nabla_mu u_phi^mu,
Q1=[(1-epsilon)Gamma
    +epsilon(1-delta)Theta_phi]rho_F,
Q2=Gamma rho_F.
```

Vektorový ledger zostáva donorovo orientovaný:

```text
Q_phi^mu=-Q1 u_phi^mu,
Q_M^mu=+Q1 u_phi^mu-Q2 u_M^mu,
Q_c^mu=+Q2 u_M^mu.
```

Voľba `u_phi` nie je ľubovoľný nový energy-frame. Ide o rýchlosť donora
prvého procesu, ktorá už existuje v K7.0.

## 2. Background a porucha skalára

Na FRW backgrounde `Theta_phi=3H`, takže sa presne obnoví K7.0. Pri
konštantných `epsilon,delta,Gamma` je prvá porucha

```text
delta Q1 = [(1-epsilon)Gamma
            +epsilon(1-delta)Theta_phi]delta rho_F
           +epsilon(1-delta)rho_F delta Theta_phi.
```

V Newtonovej gauge so signatúrou `(-,+,+,+)`:

```text
a delta Theta_phi
  =theta_phi-3Phi'-3Hconf Psi.
```

Člen `delta Theta_phi` sa nesmie vymazať. Bez neho by `Q1` nebolo poruchou
deklarovaného lokálneho skalára, ale iba backgroundovým ansatzom.

## 3. Symbolické kontroly skriptu 57

| Kontrola | Výsledok |
|---|---|
| FRW redukcia na presné `Q1` | `PASS` |
| produktové pravidlo pre `delta Q1` | `PASS` |
| skalárna gauge transformácia `delta Q1 -> delta Q1-Q1' T` | `PASS` |
| súčet troch `Q_A^mu` | `PASS`, identicky nula |
| regulárny limit `epsilon->0` | `FAIL` |
| CTP/spektrálny pôvod | `NEODVODENÝ` |
| noise correlator | `NEODVODENÝ` |

Interakčná miera mediátora je

```text
R1=Q1/(epsilon rho_F)
  =Gamma/epsilon-Gamma+(1-delta)Theta_phi.
```

Preto

```text
lim_{epsilon->0} epsilon R1=Gamma
```

a `R1` diverguje. K3 nevyliečila singularitu okamžite eliminovaného
mediátora známu z K7.0.

## 4. Čo prežilo

K3 je viac než zápis `H` do lokálnej rovnice: zvolila kovariantný skalár,
fixovala jeho referenčný rámec a jednoznačne určila povinnú poruchu
`delta Theta_phi`. Preto sa zatiaľ nevyhlasuje za mŕtvu.

## 5. Čo neprežilo

Formulačná kovariancia nedokazuje, že člen vznikne z lokálnej hermitovskej
akcie alebo konzistentného coarse-grainingu. Závislosť od expanzie má
hydrodynamický/disipatívny charakter. Ak ide o otvorenú EFT, musí mať
entropickú a fluktuačnú časť. Skript 57 ich nevytvoril.

Koľaj preto neprešla K7.1a, nezískava nové body a nesmie pokračovať rovno
na `S8`.

## 6. Nasledujúca brána K3.1

1. zostaviť Schwinger-Keldysh/open-EFT operátor, ktorého stredná rovnica
   obsahuje `Theta_phi rho_F`;
2. odvodiť retardačné a noise jadrá a podmienku lokálneho limitu;
3. uviesť energiu, tlak a entropiu všetkých integrovaných módov;
4. dokázať, že koeficient nie je iba spätne zrekonštruovaný z A1;
5. pri neúspechu vyhlásiť `K7.1a-K3 MŔTVA M-014b` a zachovať skript 57;
6. iba pri úspechu vstúpiť do plnej K7.1b superhorizontovej sústavy.

