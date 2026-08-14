# A2-K7.1a-K3.1-K2.2-K1b1 — audit zosilnenej vedúcej soft spin-2 väzby

**Dátum:** 2026-07-13  
**Skript:** `scripts/61_script_A2_K7_K3_1_K2_2_K1b_spin2_coupling_scale_gate.py`  
**Verdikt:** `MŔTVA M-014d2a`  
**Max. hĺbka:** `41/100`  
**Akceptované skóre K7:** `30/100`

## 1. Presný rozsah

K1b1 skúma iba možnosť zosilniť alebo urobiť druhovo závislou vedúcu
mäkkú väzbu hmotnostne nulového helicity-2 poľa

```text
h_mn T^mn / M_eff.
```

Audit **nevylučuje** všetky vyššie-derivačné difeomorfne invariantné
curvature operátory. Tie sú samostatná K1b2. Toto obmedzenie je zapísané aj
v errate skriptu 61.

## 2. Rate požiadavka

Ak sa vedúca univerzálna spin-2 väzba opíše efektívnou škálou `M_eff`,
optimistický rate odhad škáluje ako

```text
Gamma ~ T^5/M_eff^4.
```

Skript vyriešil najväčšie `M_eff`, ktoré by ešte dokázalo splniť presný K7
zdroj. Dnes vychádza iba

```text
M_eff <= 1.77 až 1.92 keV,
```

kým pozorovaná znížená Planckova škála je
`Mbar_Pl=2.435e27 eV`. Vedúci coupling by musel byť silnejší o
`1.27e24` až `1.38e24`; jeho univerzálna gravitačná sila by bola
`1.61e48` až `1.89e48` krát `G_N`.

To nie je malá korekcia ani neistota prefaktora. Univerzálne použitie takej
väzby je priamo nezlučiteľné s registrovanou gravitačnou škálou.

## 3. Wardova/soft stena

Alternatíva „silná iba pre dark sektor“ neprechádza vedúcou soft spin-2
bránou. Pri štandardných predpokladoch lokálnej Lorentzovsky invariantnej
unitárnej S-matice vyžaduje decoupling nefyziologických polarizácií
univerzálnu vedúcu väzbu massless spin-2 kvanta. Svojvoľné druhovo závislé
zosilnenie `h_mn T_dark^mn` preto nie je konzistentný spôsob, ako zachovať
tie isté gravitonové kvantá pary.

## 4. Dôvod smrti

K1b1 je `MŔTVA M-014d2a`:

- univerzálne zosilnenie vyžaduje efektívne `G` približne `10^48 G_N`;
- neuniverzálne zosilnenie vedúcej massless-spin-2 väzby porušuje soft
  Wardovu konzistenciu za uvedených predpokladov.

Max. hĺbka `41/100` zostáva pri mŕtvej podkoľaji. Nadradená K1b ani K7
neumierajú týmto rozsudkom: K1b2 je stále otvorená a K7 má prijatých
`30/100`.

## 5. Čo čísla hovoria o novej podkoľaji K1c

Skript diagnosticky ukázal, že nový nespin-2 relativistický nosič s
generickou škálou `Gamma~g^4 T` by potreboval iba
`g~2.3e-8` až `7.0e-8` na skúmanom backgrounde. Toto nie je dôkaz K1c;
iba ukazuje, že rate no-go je špecifický pre Planckovsky potlačený graviton.
Nový nosič však prináša vlastnú akciu, tlak, `Delta N_eff`, šum a coupling.

## 6. Erratum a zákaz príliš širokého záveru

Prvý pracovný výstup skriptu 61 príliš široko pomenoval celú K1b ako
nekonzistentnú. Pôvodný skript je zachovaný s príponou
`PRE_ERRATUM_OVERBROAD`; logická oprava je v
`Audit/A2_K7_K3_1_K2_2_K1b1_SCOPE_ERRATUM_SCRIPT61.md`.

Zakázaná formulácia: „soft theorem vylúčil všetky neštandardné interakcie
gravitónov“. Dovolená formulácia: „soft theorem a rate test vylúčili
zosilnenie vedúcej `hT` väzby K1b1“.

## 7. Primárne zdroje

- Weinberg, *Photons and Gravitons in S-Matrix Theory*,
  <https://doi.org/10.1103/PhysRev.135.B1049>.
- Weinberg, *Photons and Gravitons in Perturbation Theory*,
  <https://doi.org/10.1103/PhysRev.138.B988>.
- Boulanger et al., *Inconsistency of interacting, multi-graviton theories*,
  <https://arxiv.org/abs/hep-th/0007220>.

