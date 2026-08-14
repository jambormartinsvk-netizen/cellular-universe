# KROK B — BAO DIŠTANČNÝ TEST PROTI DESI DR2
## Verdikt nad námietkou #9 („H₀ = 66.4 je nekompatibilné s BAO")

**Dátum:** 11. júl 2026
**Metóda:** priamy test vzdialeností — žiadny fit, žiadne voľné parametre.
Model aj ΛCDM z tej istej pipeline, obidva kotvené identicky na θ*
(Planckova akustická škála), r_d počítané na drag epoche z_d = 1059.94
(nie r_s na rekombinácii — rozdiel ~2 %, ktorý by test potichu pokrivil).
**Dáta:** DESI DR2 (2025), 13 nezávislých meraní zo 7 trasovačov:
BGS D_V/r_d; LRG1/LRG2/LRG3+ELG1/ELG2/QSO/Lyα po dvojici D_M/r_d
a D_H/r_d; blokové 2×2 kovariancie s publikovanými koreláciami
ρ(D_M,D_H) = −0.459/−0.404/−0.416/−0.431 (LRG1/LRG2/LRG3+ELG1/Lyα);
pre ELG2 a QSO korelácia nepublikovaná v dostupnom zdroji → dosadené
−0.43 s citlivostným skenom.

---

## 1. Výsledok

| konfigurácia | h | Ω_m | r_d [Mpc] | χ² (13 bodov) |
|---|---|---|---|---|
| ΛCDM (pipeline, Planck kotva) | 0.6730 | 0.3157 | 146.97 | **36.8** |
| model s parou, λ = 0.15 | 0.6637 | 0.3517 | 146.71 | **36.7** |
| model s parou, λ = 0.10 | — | — | — | **34.4** |

    Δχ²(model − ΛCDM) = −0.1 (λ = 0.15)  až  −2.4 (λ = 0.10)

Citlivosť na neznámu koreláciu ELG2/QSO: Δχ² sa hýbe medzi +0.03
a −0.30 pri ρ ∈ [−0.30, −0.55] — na verdikt nemá vplyv.

## 2. Verdikt nad námietkou #9

**ZAMIETNUTÁ ČÍSLOM.** Model s H₀ = 66.4 sedí na DESI DR2 vzdialenostiach
presne tak dobre ako Planckom kotvená ΛCDM (Δχ² ≈ 0), pri λ = 0.10
mierne lepšie. Mechanika je presne tá, ktorú námietka tvrdila, že chýba:
r_d ostáva 146.7 Mpc (raná fyzika nedotknutá, para posúva r_d len
o 0.26 Mpc) a zmenená neskorá expanzia kompenzuje v D_M aj D_H tak,
že θ* kotva drží. Nižšie H₀ model za BAO nič nestojí.

## 3. Poctivé čítanie — dve dôležité pravdy nahlas

**Pravda 1: ani jeden model nesedí na DESI DR2 dobre.** χ² ≈ 35–37 na
13 bodov je vysoké pre oba. To NIE JE vlastnosť nášho modelu — je to
známa tenzia DESI × Planck (ťahy +2 až +3σ v D_M pri z = 0.7–0.9,
viditeľné v oboch stĺpcoch rovnako). Test je zámerne predikčný
(bez refitu); ΛCDM fitovaná priamo na BAO by mala χ² podstatne nižšie,
ale to by porovnávalo jablká s hruškami. Relatívny výrok je jediný,
ktorý tento test robí: model vs ΛCDM pri identickom kotvení = remíza.

**Pravda 2: priame vzdialenosti a fitované (w₀, wₐ) merajú rôzne veci.**
V metrike „3 fronty" (kde sa porovnávajú fitované w₀/wₐ tieňové hodnoty)
model ΛCDM výrazne poráža (18.8 vs 30.0 s KiDS-Legacy kotvou).
V priamych vzdialenostiach je remíza. Nie je to rozpor: DESI preferencia
dynamickej tmavej energie žije prevažne v KOMBINÁCII BAO × SN × CMB,
nie v samotných BAO vzdialenostiach. Model si teda nesmie pripisovať
„vysvetľuje DESI BAO lepšie" — správny výrok je „prechádza BAO testom
bez pokuty za nízke H₀ a jeho tieňové w(z) sedí na kombinovanú DESI
preferenciu". Tento rozdiel bude prvá vec, ktorú skúsený kozmológ
preverí; teraz ho máme zapísaný skôr, než sa spýta.

## 4. Čo test pridáva do dokumentácie

- Nová interná validácia pipeline: D_M(z), D_H(z), D_V(z) a r_d(z_drag)
  — rozšírenie skriptu 09 o BAO modul (kód testu archivovať k skriptom).
- Odporúčam pridať do dokumentu 04 jednu tabuľku (sekcia B alebo nová
  A17): 13 DESI bodov, predikcie modelu, ťahy — a vetu z Pravdy 2.
- Do registra stávok: S1 sa spresňuje — finálna DESI analýza (DR3+)
  rozhodne, či kombinovaná preferencia w₀ > −1, wₐ < 0 prežije;
  model na nej stojí cez tieň, nie cez samotné vzdialenosti.

---

## Kľúčová veta

Námietka „nekompatibilné s BAO" zomrela na Δχ² = −0.1: model platí za
nízke H₀ presne nula, lebo drží drag horizont aj θ* a rozdiel schová
do neskorej expanzie — ale test zároveň prikazuje pokore: na samotných
DESI vzdialenostiach model ΛCDM neporáža, iba jej nič nestráca, a jeho
skutočný súboj o tmavú energiu sa odohráva v kombinovaných dátach,
kde žije tieň w(z).
