# 01_AUDITOR_AUDIT_ADDENDUM — veľký obraz (registrácia v3.17 ↔ K_MPC lineage)

**Auditor:** externý (Claude), po sprístupnení projektovej dokumentácie
(registračné vydanie v3.17: dokumenty 00–05, skripty 06–10, register otázok,
metodika, tabuľky predikcií)  
**Dátum:** 2026-07-17  
**Vzťah k 00_AUDITOR_AUDIT.md:** addendum; pôvodný audit sa neprepisuje.
Verdikty z §1 pôvodného auditu (COMPUTED_STOP_SCOPE; mapovanie nutné;
žiadny nový fit na úrovni bookkeepingu) zostávajú v platnosti a nižšie sa
**posilňujú**.

---

## A. Karanténa potvrdená: K7 únik sa NEDOTÝKA registrovaných predikcií

Overil som registrovaný skript `09_script_K3_cosmology_pipeline.py` riadok
po riadku voči otázke balíka:

1. **Neobsahuje `K_MPC` ani žiadny Fourierov mód.** Je to čisto
   backgroundová pipeline: V1 ODE (`dΩ_f/dx = −3δΩ_f − λΩ_f/E`,
   `dΩ_m/dx = −3Ω_m + λΩ_f/E`, `dΩ_r/dx = −4Ω_r`), θ*-kotva s dvojitou
   slučkou, CPL fit vážený ρ_DE,eff a škálovo nezávislá rastová rovnica V3.
2. **Registrované čísla (H₀ = 66.4, w₀/wₐ, S₈ = 0.874, n_s, ΔN_eff, r)
   nemajú žiadnu závislosť od K7 perturbačného adaptéra.** n_s pochádza
   z plošného zákona + kvázi-de Sitter (A13), ΔN_eff z entropie (A12) —
   obe cesty sú od 213 úplne oddelené.
3. Registrácia navyše **sama poctivo deklaruje** „plný Boltzmann —
   DORIEŠIŤ" v tabuľke K3. Zenodo záznam teda nikdy netvrdil to, čo K7
   STOP zabil.

**Dôsledok:** k^p únik je plne karanténovaný v perturbačnej vetve.
Registrované predikcie v3.17 nie sú kontaminované a nevyžadujú žiadnu
korekciu ani scope poznámku z tohto titulu.

## B. Silnejší záver: „korektný background" z auditu = registrovaný V1

Presné `D_A1(a) = a⁴E²/Ωr0` z P4a je algebraicky **identické** so
zaregistrovaným V1 systémom (A7 hlavného dokumentu; rovnaké rovnice bežia
v skripte 09). Historický K7 `denominator` bol teda neautorizovaná raná
aproximácia **už zaregistrovaného** backgroundu, ktorá bola omylom
extrapolovaná do `a=1` (a pri `a≈0.709` prechádza nulou). Oprava K_MPC
problému preto nie je nová fyzika ani nová vetva — je to **návrat
k registrovanému stavu**. Toto je najsilnejšia možná forma odpovede na
otázku balíka a odporúčam ju takto explicitne zapísať do K-N2 uzáveru.

## C. Nový nález rovnakej triedy: N-7 — dátová verzia S₈ v registrovanom skripte

Pri krížovej kontrole som našiel nezrovnalosť **priamo v registrovanom
zázname v3.17**, štruktúrne totožnú s K_MPC problémom (číslo vložené v kóde,
ktorého verzia/význam nesedí s deklaráciou):

- Hlavný dokument v3.17 (stráž dát, 7.7.2026) uvádza headline skóre
  **„model χ² ≈ 19.6–19.9 vs ΛCDM ≈ 30.0"** počítané s KiDS-Legacy
  **S₈ = 0.815 ± 0.018**.
- Priložený registrovaný skript 09 však počíta
  `chi2 = ... + ((S8−0.759)/0.024)²` — teda so **starým KiDS-1000 bodom
  0.759 ± 0.024**.

Registrovaná pipeline v dodanej podobe **nereprodukuje headline χ²
registrovaného dokumentu** bez ručnej úpravy dátového bodu. Nie je to chyba
fyziky (w₀, wₐ, S₈ samotné skript počíta správne a dokument rozdiel dátových
stavov popisuje v texte), ale je to reprodukovateľnostný šev v zázname,
ktorý má ako hlavnú hodnotu práve reprodukovateľnosť. Zhodou okolností je
to presne lekcia AR66.2: „úspešný runtime" nie je dôkaz parity vzorca
a vstupu s deklaráciou.

**Odporúčanie:** vo v3.18 changelogu jedna veta + oprava skriptu 09 (alebo
parametrizácia dátového bodu s defaultom = stav pri registrácii a komentárom
oboch hodnôt). Registrovaný v3.17 skript sa podľa vlastných pravidiel
neprepisuje — patrí to do novej verzie.

## D. Sprísnenie proveniencie `A_f`

S kontextom pipeline možno P2a výrok spresniť: „zmrazený A1-K1 closure" je
flat closure `Ω_f0 = 1 − Ω_m0 − Ω_r0` s `h, Ω_m0` z θ*-kotvy pri danom
`(λ, δ, ΔN_eff)`. Preto

```text
A_f = A_f(λ, δ, ΔN_eff, θ*-kotva).
```

`A_f` teda **nie je nový fit** (P2a verdikt drží), ale je to odvodená
funkcia jediného existujúceho fitu λ. Dve praktické povinnosti:

1. Registrácia uvádza λ ako **rozsah 0.10–0.15**. Hodnota
   `A_f = 7809.270…` implicitne fixuje jeden bod tohto rozsahu
   (pravdepodobne λ = 0.15, pracovný bod v4). Provenance tag z pôvodného
   auditu (bod 5.3) treba rozšíriť o **explicitné λ**: bez neho je
   šestnásťciferné číslo nedourčené v rámci vlastnej registrácie.
2. Testy k-nezávislosti backgroundu s `A_f` sú podmienené voľbou λ —
   k-nezávislosť ako taká platí pre každé λ (algebra zrušenia je od λ
   nezávislá), ale numerické hodnoty raného radu nie.

## E. Rád veľkosti proti čítaniu „k_* = škála siete" (K-N1)

Vlastné pravidlo projektu K4 („najprv odhad rádu, potom roky práce")
aplikované na otvorenú koľaj K-N1: prirodzená škála bunkovej siete je
Planckova, `k_cell ~ 1/l_P ~ 10⁵⁷ Mpc⁻¹`. Čítanie `0.05 Mpc⁻¹` ako
fyzikálnej škály siete teda vyžaduje vysvetliť hierarchiu **~58 rádov**
medzi bunkou a údajnou korelačnou dĺžkou — čo je bremeno rovnakého typu ako
priznaná záhada ε ~ 10⁻⁶² (P7). Nie je to dôkaz smrti K-N1, ale je to
kvantitatívny dôvod, prečo je pivotové čítanie a priori silne favorizované
a prečo K-N1 nesmie byť uzavretá bez samostatného mechanizmu tejto
hierarchie. Odporúčam tento odhad zapísať do K-N1 ako vstupnú latku.

## F. Vzťah blokovaného G9 k registrovanej S₈ predikcii — riziko na horizonte

Registrované S₈ = 0.874 (λ=0.15) pochádza zo škálovo nezávislého rastového
proxy (V3, σ₈ = 0.811·D/D_ΛCDM). Celý zmysel P5 → G8 → G9 je nahradiť toto
proxy plnou perturbačnou výbavou. Ak G9 raz dá materiálne odlišné S₈:

- registrovaná predikcia sa podľa zero-reversals **nemení**;
- nová hodnota musí vzniknúť ako verziovaný nástupca s changelogom
  (presne mechanizmus PT2 z execution plánu), s explicitným výrokom, ktorá
  vrstva výpočtu sa zmenila;
- kill condition `S₈ ≤ 0.78 ∧ wₐ ≤ −0.6` sa vyhodnocuje voči registrovanému
  protokolu, nie voči neskoršej pipeline.

Toto riziko dnes nevyžaduje akciu — vyžaduje len, aby bolo pomenované skôr,
než G9 pobeží, aby výsledok G9 nebolo možné spätne interpretovať ani ako
tichú záchranu, ani ako tichú popravu.

## G. Aktualizovaný celkový záver

Veľký obraz odpoveď na balík **zjednodušuje a spevňuje**: (1) únik `k^p`
je reálny, výpočtovo doložený a plne karanténovaný v perturbačnej vetve —
registrácia v3.17 je čistá; (2) „oprava" je návrat k backgroundu, ktorý bol
celý čas registrovaný ako V1, takže K-N2 nemá otvorenú fyzikálnu otázku
o `H(a)`, iba implementačnú (P5); (3) `A_f` je odvodená funkcia jediného
fitu λ a musí niesť λ vo svojom provenance tagu; (4) rovnaká trieda chyby
ako K_MPC — nedeklarovaná verzia čísla v kóde — existuje na jednom mieste aj
v registrovanom zázname (N-7, S₈ dátový bod v skripte 09) a patrí do v3.18
changelogu; (5) čítanie „0.05 = škála siete" nesie hierarchické bremeno
~58 rádov a K-N1 by mala dostať túto latku ako vstupnú podmienku.

Metodicky: projekt obstál v najtvrdšom teste, aký lineage audit pozná —
chyba bola nájdená vlastným protokolom, správne ohraničená, nezomrel pri
nej mechanizmus a jej oprava konverguje k už zaregistrovanému stavu. N-7
ukazuje, že rovnaký reflex treba raz prehnať aj samotným registračným
balíkom, nie len pracovným stromom.
