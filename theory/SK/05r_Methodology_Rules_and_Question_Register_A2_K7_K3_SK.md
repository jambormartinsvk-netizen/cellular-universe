# REGISTER 05 — SK dodatok k A2-K7.1a-K3

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; existujúce pravidlá sa nemenia

## Kontrola duplicity

Staršie pravidlá vyžadovali lokálnu kovarianciu a perturbovanie skalára
prenosu. Neurčili explicitne, že backgroundové `H` v disipativnom zákone sa
musí nahradiť konkrétnym lokálnym expansion scalarom a že sa potom povinne
perturbuje aj jeho referenčný rámec. AR16 túto medzeru dopĺňa.

## AR16 — Každé interakčné H musí dostať lokálny rámec a delta Theta

Ak efektívny zákon obsahuje `H`, musí audit určiť, či ide o
`Theta_A/3=nabla_mu u_A^mu/3` konkrétnej zložky alebo o inú lokálnu
geometrickú veličinu. Nesmie sa používať ne-lokálne dnešné alebo
backgroundové `H` bez kovariantnej definície.

Po voľbe `Theta_A` musí porucha transferu obsahovať jeho úplné
`delta Theta_A`, vrátane rýchlostnej a metrickej časti. V Newtonovej gauge
pre perfektný donor platí

```text
a delta Theta_A=theta_A-3Phi'-3Hconf Psi.
```

Samotný formulačný prechod nezaručuje mikrofyzický pôvod ani neprítomnosť
noise.

## Q45 — Prešla expansion-scalar koľaj K7.1a-K3?

**Stav:** `IBA FORMULAČNÚ BRÁNU; BEZ ZVÝŠENIA SKÓRE.`

Skript 57 dokázal FRW redukciu, gauge transformáciu `delta Q1` a presné
zrušenie vektorového ledgeru. Súčasne ukázal `R1~Gamma/epsilon`, takže
`epsilon->0` zostáva singulárne. CTP kernel a noise correlator neboli
odvodené.

K7 zostáva `PREŽÍVA 30/100`. Nasleduje K3.1; pri neúspechu dostane K3
rozsudok M-014b.

## Obmedzenie staršej formulácie

Člen `3H epsilon(1-delta)rho_F` v K7.0 sa odteraz nesmie perturbovať ako
pevné backgroundové číslo. V K3 znamená
`epsilon(1-delta)Theta_phi rho_F` a nesie povinné `delta Theta_phi`.

