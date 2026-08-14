# REGISTER 05 — SK dodatok k A2-K7.0

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; existujúce pravidlá sa nemenia

## Kontrola duplicity

Staršie pravidlá vyžadovali explicitný mediátor a uzavretý ledger. Neurčili
však, že kladná hustota mediátora sa musí započítať do už registrovaného
backgroundu a jeho entalpického rozpočtu. AR12 preto nie je duplicitné.
Q41 aktualizuje stav predtým čakajúcej K7.

## AR12 — Dynamický mediátor sa nesmie backgroundovo skryť

Každý explicitný mediátor s vlastným `T_M^{mu nu}` musí mať v backgrounde
uvedené `rho_M`, `p_M`, entalpiu a miesto v Friedmannovej rovnici. Ak má
zostať pôvodný celkový sektor `rho_F,p_F`, musí platiť

```text
rho_F=sum_i rho_i,
p_F=sum_i p_i,
rho_F+p_F=sum_i(rho_i+p_i).
```

Kladná `rho_M` sa nesmie pridať nad pôvodný `H(z)` ani zahodiť ako
„virtuálna“, ak na lineárnom ráde nesie energiu alebo hybnosť. Ak je
efektívny tok výsledkom coarse-grainingu lokálnej akcie, audit musí zachovať
aj pamäťový/šumový člen alebo zdôvodniť Markovovský limit.

## Q41 — Prežila A2-K7 prvú akčnú a ledgerovú bránu?

**Stav:** `ÁNO — PREŽÍVA K7.0, 30/100.`

Pre prachový masívny mediátor a presný A1 background bolo odvodené

```text
0<epsilon<delta=0.02297,
Q2=Gamma rho_F,
Q1=(1-epsilon)Gamma rho_F+3H epsilon(1-delta)rho_F.
```

Maximálne ledgerové rezíduum bolo `2.220e-16`. Donorovo orientovaná
collision matica mala iba eigenhodnoty `-R1,-R2<0`; lokálny anti-damping sa
neobjavil. Priamy collision-only mód popola sa však od rekombinácie utlmí
iba faktorom `0.9100` a mikrofyzický pôvod `Q1,Q2` ešte chýba.

Rozhodujúci dokument:
`Audit/A2_K7_0_akcna_ledgerova_a_collision_brana.md`.

## Obmedzenie staršieho stavu

Katalógový stav K7 `ČAKÁ` je historický stav pred prvou bránou. Od tohto
dodatku je kanonický stav `PREŽÍVA K7.0 — 30/100`; nesmie sa skracovať na
„stabilná“ alebo „rieši S8“.

