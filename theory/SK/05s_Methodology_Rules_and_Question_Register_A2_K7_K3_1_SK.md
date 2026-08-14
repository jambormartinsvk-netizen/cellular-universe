# REGISTER 05 — SK dodatok k A2-K7.1a-K3.1

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; existujúce pravidlá sa nemenia

## Kontrola duplicity

AR15 rozlišuje rekonštrukciu od mikrofyziky a AR16 vyžaduje lokálne
`Theta`. Neurčili však pozitivitu celej Onsagerovej/noise matice ani rozdiel
medzi maximálnou hĺbkou podkoľaje a akceptovanou hĺbkou nadradenej vetvy.
AR17 a AR18 preto nie sú duplicitné.

## AR17 — Cross-disipácia vyžaduje pozitívnu úplnú maticu a noise

Skalárny cross-koeficient medzi expanziou a reakciou sa nesmie auditovať
izolovane. V near-equilibrium otvorenej EFT musí byť súčasťou celej
Onsagerovej matice s nezápornou entropickou kvadratickou formou. Nenulový
off-diagonálny člen vyžaduje dostatočné diagonálne koeficienty; pri lokálnom
KMS limite aj pozitívnu noise covariance. Recipročný stress, bulk pressure a
noise sa nesmú vyhodiť, ak sú potrebné pre pozitivitu.

## AR18 — Max. hĺbka podkoľaje nepromuje automaticky nadradenú koľaj

Každá podkoľaj musí mať stĺpec `Max. hĺbka`. Ide o najhlbší vykonaný test,
nie automaticky prijatú bránu nadradenej koľaje. Nadradené skóre sa zvýši až
po splnení všetkých acceptance kritérií danej úrovne. Mŕtva podkoľaj si
maximálnu hĺbku ponecháva spolu s dôvodom smrti.

## Q46 — Prežila K7.1a-K3.1 Onsagerovu/noise bránu?

**Stav:** `HOLÁ K3 NIE; DOPLNENÁ PODKOĽAJ IBA FORMULAČNE.`

K3.1-K1 zomrela ako M-014b, pretože `[[0,alpha],[alpha,0]]` má vlastné
hodnoty `±alpha`. K3.1-K2 má pozitívne doplnenie
`ell*zeta>alpha^2` a pozitívny normalizovaný noise na celom gride, ale
`ell,zeta,T`, bulk pressure a bath neboli mikrofyzicky odvodené.

Max. hĺbka oboch podkoľají je `38/100`; akceptované skóre K7 zostáva
`30/100`. Nasleduje rozmerový bath/background closure K3.1-K2.1.

