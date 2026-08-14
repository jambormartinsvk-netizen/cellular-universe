# Revidovaný plán po externom audite 2

**Dátum:** 2026-08-14
**Nahrádza:** poradie prác v `00_CURRENT_EXECUTION_PLAN.md` v časti „ďalší krok"
**Rozhodnutie autora:** `A0` sa rozhodne prvá; voľba medzi traťou IV.A
(falzifikácia) a IV.B (pokračovanie) sa **odkladá do rozhodnutia `A0`** a
nerobí sa driftom.
**Nemení:** žiadnu existujúcu hĺbku, žiadny prijatý výsledok, žiadny artefakt.
Nič sa nemaže.

---

## 0. Prečo sa poradie obracia

Doteraz išlo ~90 % úsilia do kozmologického sektora. Ten je z hľadiska
pravdivosti teórie **najmenej dôležitý** — je to fluidná parametrizácia, ktorú
dostanete aj bez siete. Sieť do disperzie nevstupuje vôbec: v koeficiente `q⁴`
sa `⟨k⟩ = 15.535` aj `C = 28` vykrátia (audit III.2, overené). Nula úsilia
išlo tam, kde sa o existencii rozhoduje.

```text
STARE PORADIE                          NOVE PORADIE
  A1 background                          A0  existuje LI limit stabilny
  A2 poruchy                                 voci smyckam?
  A3 CMB/S8/H0                           |
  (Lorentz nikde)                        +-- ANO -> A2 s konecnym rezom
                                         '-- NIE -> trat IV.A, publikuj
```

## 1. Okamžite — dva dni, nulové fyzikálne riziko

Zoradené podľa pomeru prínos/náklad. Toto sa dá urobiť dnes a zvýši to
dôveryhodnosť projektu viac než čokoľvek iné za tie peniaze.

| # | Akcia | Náklad | Zdroj |
|---|---|---|---|
| 1 | `git tag v3.18 <commit> && git push --tags` — oživiť všetky mŕtve `blob/v3.18/External_Audits/PACKAGES/EA-*` odkazy v release-i | 5 min | VI.1 |
| 2 | Prepísať README na v3.18 a **odstrániť** slová `derives`, `predicts`, `without unconstrained free parameters`, `fully falsifiable`, `graviton` | 1 h | VI.2 |
| 3 | Zosúladiť kill window `n_s`: README `± 0.004` vs. P02 `± 0.0016` (faktor 2.5) | 5 min | VI.2 |
| 4 | Zrušiť kill condition o WIMPoch (odporuje vlastnému P07) a doplniť, prečo `H₀ ≥ 72` nefunguje ako test | 15 min | VI.2 |
| 5 | Nahradiť `external audit` za `independent LLM agent audit (model, revízia, mode)` v release-i, README aj §13; doplniť vetu *„Žiadny audit v tomto korpuse nebol vykonaný človekom mimo projektu."* | 1 h | VI.3 |
| 6 | Premenovať sekciu audit trailu na `Computational reproducibility` a explicitne uviesť, že nejde o vedeckú validáciu | 15 min | C5 |
| 7 | Preklasifikovať `P01/P04/P05/P06/P11 → PRE_A3_DIAGNOSTIC`, `P10 → IDENTITY / NOT_A_PREDICTION`, `P02 +` degenerácia s `α` | 1 h | V.10, II.6–II.8 |
| 8 | Zaokrúhliť **všade** na 4 platné číslice. `A_f = 7809.270101963506` a `H₀ = 65.79213819466531` pri vstupoch s 3–4 ciframi nie je precíznosť, je to falošná precíznosť | 1 h | C2 |
| 9 | Doplniť do §6.4 priznanie, že tabuľka kóduje `S₈ ∝ 1/H₀` a skutočná rastová fyzika je 0.4 % z nej; opraviť rovnako formuláciu EA-047 | 30 min | II.4 |
| 10 | Doplniť explicitne bod I.4: `ω_m(rek) = 0.14299` je **0.09σ** od Planckovho `0.1431 ± 0.0012`. Je to najlepšia zhoda modelu s dátami a nevyužíva sa | 15 min | I.4 |
| 11 | Zmraziť verziovanie. Žiadna v3.19 | — | C1 |
| 12 | **Zastaviť generovanie ďalších taskov v `A2`** | — | VI.8 |

Akcia 12 je najdôležitejšia a nič nekostuje. Marginálna hodnota tasku 634 je
približne nulová a je to predvídateľné, nie náhoda: 222 taskov, 17 úrovní
vnorenia, 44 runnerov, pohyb fyzikálnej hĺbky **nula**.

## 2. Týždeň 1 — dva e-maily dvom ľuďom

Toto je jediný dostupný zdroj **iného rámca**, a rámec je presne to, čo celej
agentovej vrstve chýba. Nedá sa vyrobiť pridaním piateho agenta.

**Jedna otázka, nie dokument.** 470 kB s audit trailom nedostane odpoveď;
jedna ostrá otázka od kompetentného človeka odpoveď dostane.

| Adresát | Otázka | Prečo tento človek |
|---|---|---|
| kozmológ — CEICO, Praha | *„Je `S₈ ∝ 1/h` v tejto triede interagujúcich modelov temnej energie vynútené, alebo mi niečo uniká?"* | robia presne temnú energiu a modifikovanú gravitáciu |
| fenomenológ QG — SISSA, skupina S. Liberatiho | *„Generuje priestorová diskrétnosť dim-4 narušenie Lorentza cez smyčky, alebo to niečo chráni? Je separácia škál z Belenchia–Gambassi–Liberati 2016 aplikovateľná, ak je preferovaný rám ontologický, nie regulátorový?"* | je to jeho vlastný výsledok; odpovie za dvadsať minút |

Druhá otázka je pre program dôležitejšia. Rozhoduje o `A0`.

## 3. Týždeň 1–3 — `A0-K5`: separácia škál (PRIORITA 1)

**Otázka:** je auditov výsledok III.5 artefakt toho, že integrál beží až po
`k_max = 1/ℓ_cell`?

**Konkrétny výpočet.** Zopakovať smyčkovú formulu z Dodatku A3 auditu, ale
s cutoffom `M < k_max`, a overiť, či indukovaný dim-4 koeficient škáluje ako
`(M/Λ)²`.

**Povinné kontroly** (`A0-C1`, `A0-C2`):

```text
1. W = k^2, cutoff -> nekonecno  =>  B-A = 0 na 1e-15 alebo lepsie
2. W = k^2, cutoff = k_max       =>  vykaz samostatne; toto je miera
                                     NEKOVARIANCIE REGULATORA, nie fyzika
                                     (overene: 16 pi^2 (B-A) = -0.01097)
3. siet - (2) = fyzikalny prispevok siete
```

**Prečo je krok 2 povinný.** Číslo `−0.011` bolo získané pre **exaktne
Lorentzovsky invariantnú** disperziu. Jediná vec, ktorá tam narúša Lorentza,
je priestorový cutoff definovaný v jednom ráme. Audit z toho vyvodil, že
*„akákoľvek teória s konečným počtom dof na objem"* dostane dim-4 LV — čo je
v priamom rozpore s jeho vlastným III.6(b) (kauzálne množiny majú konečnú
hustotu dof a sú exaktne LI). Rozhoduje III.6(b). Bez odčítania kroku 2 nie
je konštantný člen `0.294` fyzikálne číslo.

**Cena, ak `A0-K5` prejde** (vyčíslené):

| cieľový limit | `M/Λ` | `M` [GeV] |
|---|---|---|
| `10⁻¹⁶` elektrón | `5.3×10⁻⁸` | `6.5×10¹¹` |
| `10⁻¹⁹` fotón | `1.7×10⁻⁹` | `2.0×10¹⁰` |
| `10⁻²³` UHECR | `1.7×10⁻¹¹` | `2.0×10⁸` |

**Kľúčový rozdiel proti auditovej diagnóze.** Audit v III.6(d) hovorí:
*„`g/Λ < 1.7×10⁻⁹` — deväť rádov, pre každé pole a každú väzbu, bez
vysvetlenia."* Pri separácii škál je to **jedno číslo, raz, pre všetky polia a
väzby**. To je materiálne iná situácia. Nová škála pri `10⁸–10¹⁰ GeV` nie je
exotická — seesaw aj PQ škála tam ležia.

**Ak `A0-K5` prejde, teória získa prvú nekozmologickú predikciu:** existuje
Lorentzovsky invariantná UV kompletizácia SM pod `~10¹⁰ GeV`.

Zdroj: Belenchia, Gambassi, Liberati, *Lorentz violation naturalness
revisited*, JHEP 06 (2016) 049, arXiv:1601.06700.

## 4. Týždeň 4–7 — `A0-K3`: perkolačné krátenie (PRIORITA 2)

Toto je zároveň krok `B1` z Časti IV auditu.

**Otázka:** existuje v dynamike siete štruktúra, ktorá vynúti `B = A`?

**Konkrétne:** napísať najjednoduchší interagujúci model na sieti
s **bezrozmernou** väzbou (`λφ⁴`, dvojsmyčkový sunset, alebo jednosmyčkový
s kalibračným vrcholom), spočítať korekciu ku koeficientu kinetického člena a
pozrieť sa, či sa Lorentz-narušujúca časť vykráti. Auditova formula z III.5
slúži ako kontrola: musí dať nulu pre `W = k²`.

**Bezrozmerná väzba je povinná** (`A0-C3`). Audit použil dimenzionálne `g`,
čo dáva formálnu únikovú cestu faktorom `(g/Λ)²`. Reálne SM interakcie —
kalibračné, Yukawa, `λφ⁴` v dvoch smyčkách — taký faktor nemajú.

**Nový vstup, ktorý audit vynechal:** Bednik, Pujolàs, Sibiryakov, *Emergent
Lorentz invariance from strong dynamics: holographic examples*,
JHEP 11 (2013) 064, arXiv:1305.0011. Cez gauge/gravity korešpondenciu
dosahujú mocninové potlačenie LV pri nízkych energiách **bez SUSY** — teda
presne triedu `Δ ~ O(1)`, o ktorej audit píše, že nie je známa. Auditova
námietka *„sektor SM silne viazaný nie je"* mieri vedľa: nemusí byť silne
viazaný SM, stačí skrytý sektor, na ktorý sa SM naviaže.

**Ak sa vykráti → veľký výsledok, publikovať samostatne, a celý QCTS z neho
vyplynie ako dôsledok. Ak nie → viete to za mesiac a môžete to čestne
napísať.**

Kým `A0-K5` a `A0-K3` nie sú hotové, **nepracovať na ničom kozmologickom.**

## 5. Rozhodovací bod — po `A0`

```text
A0_PASS
  -> odblokuj A2. Ale NIE tam, kde bola.
     Prvy krok v A2 je FS-C13: jeden konecny rez X_K (AGENTS.md §11).
     Semialgebraicka podmienka, SOS/CAD certifikat.
     3-6 tyzdnov, ukonci P5.3 v OBOCH smeroch.
     Hlada sa RAZ; vysledok plati pre K4, K7, K8, K9, K11 aj K12.
  -> A0 sa stane novym hard constraintom pre kazdy A2 operator.

A0_NO_GO
  -> trat IV.A sa stava jedinou a je to legitimna veda.
     Tri nezavisle publikovatelne vystupy, viz §6.

A0_UNDECIDED_BY_EXHAUSTION  (30 chyb na otazku)
  -> vydaj NO_GO_BY_EXHAUSTION s presnym zoznamom skusaneho.
     Publikovatelne.
```

## 6. Tri publikovateľné výstupy, ktoré existujú bez ohľadu na osud QCTS

Toto je najdôležitejšia vec, ktorú audit hovorí a ktorá sa ľahko prehliadne
v jeho negatívnom tóne: **z programu už vyšli tri veci, ktoré sa dajú
publikovať, aj keď teória padne.**

| # | Výstup | Stav obsahu | Odhad |
|---|---|---|---|
| 1 | **Perkolačný výsledok** — *pre Poisson–Delaunay sieť s mriežkovou konštantou `ℓ` generuje jednosmyčková korekcia dim-4 narušenie Lorentza s koeficientom `16π²(B−A) = 0.1026 ln(Λ/m) + 0.294`.* Konkrétne číslo pre konkrétnu geometriu, s overenou kontrolou na LI limite | obsah hotový, **ale** nutná kovariantná separácia regulátora (§3, krok 2) a oprava dôsledku III.5(1) pred submisiou | 3–4 týždne. Cieľ: Phys. Rev. D alebo Class. Quantum Grav. **Bez jedinej zmienky o fuel/ash/steam** |
| 2 | **Päť certifikátov prázdnosti** z feasibility ledgeru — `K8-Fkin-WARM-A1-SOURCE-ONLY`, `K11-R-PASSIVE-INTERACTION-BLOCK-HURWITZ-CURE`, `K12-K3.1-SYMMETRIC-INTERNAL-FORCE-COM-CURE`, `K9-1TO2-EXACT-THRESHOLD-FINITE-RATE`, `K11-R-UNIFORM-REGULAR-EXACT-POLE-CANCELLATION` | **obsah je hotový už dnes.** Auditovo hodnotenie: *„Päť certifikátov prázdnosti so skutočnými argumentmi je viac fyziky než celá kozmologická časť release-u."* | 3 týždne. Jediná položka, ktorá už dnes nič nepotrebuje |
| 3 | **Dôkaz nemožnosti `S₈`** — 2D sken v `(λ, h)`, plná mriežka, so súčasným overením `θ* = 1.04109 ± 0.00030` (s korektným `r_s` vrátane `ΔN_eff`, nie fixným), `ω_m(rek) = 0.1431 ± 0.0012`, `(w₀, wₐ)` v spoločnom DESI DR2 kontúre, `S₈ ≤ 0.83` | očakávaná prázdna množina, pretože `S₈ ∝ 1/h` je vynútené | 2–3 týždne. Ak vyjde prázdno: falzifikácia s dôkazom. Ak nájdete oblasť, ktorá prejde, je to ešte cennejšie |

Položka 2 je najlacnejšia a mala by ísť prvá, paralelne s `A0-K5`.
Nekonkuruje si s ňou o pozornosť — je to písanie, nie počítanie.

## 7. Čo sa v tomto pláne **nerobí**

Explicitne, aby to bolo kontrolovateľné:

- žiadny task 634 a vôbec žiadny nový task v `A2`;
- žiadne zjemnenie `P5.3` blockeru (`N1 → N1_COMPLETE_QUOTIENT_RANGE_… → …`);
- žiadne nové CMB-normalizované číslo;
- žiadny nový KMPC runner;
- žiadna verzia v3.19;
- žiadny nový zapečatený balík pre LLM auditora nad existujúcimi tvrdeniami;
- žiadny GRB / anizotropný test ako diskriminátor — audit III.3 dokazuje, že
  kvadratické limity by potrebovali zlepšenie o `10⁹` v `E_QG,2`; sú
  bezpredmetné a boli odporúčané chybne (aj auditorom v predchádzajúcej
  komunikácii).

## 8. Jedna veta, ktorá tento plán zhŕňa

> Čo chýba, nie je disciplína ani schopnosť. Je to **konečnosť priestoru,
> v ktorom hľadáme**, a **stanica, ktorá v mape nebola**. Tento plán zavádza
> oboje a nič nemaže.

---

## Dodatok — väzba na akcie auditu

| Akcia auditu | Kde je v tomto pláne |
|---|---|
| V.12 #1 finitne parameterizovať `X_K` | §5, po `A0_PASS`; mantinel `FS-C13` |
| V.12 #2 najhrubší explicitný kandidát | `AGENTS.md` §4.1 `HRUBÝ_KANDIDÁT_FIRST` |
| V.12 #3 `FS-C1` do mäkkých cieľov | feasibility ledger R2, hotové |
| V.12 #4 rozpočet na otázku | `AGENTS.md` §4, hotové |
| V.12 #5 stanica `A0` | `tracks/A0/00_STATION.md`, hotové — rozšírená o `A0-K5` |
| V.12 #6 preklasifikovať predikcie | §1 akcia 7 |
| V.12 #7 stĺpec „spoločný objekt s K4" | `A2/00_TRACK_REGISTER.md`, hotové |
| V.12 #8 trieda operácií bez contractu | `AGENTS.md` §10, hotové |
| V.12 #9 publikovať päť certifikátov | §6 položka 2 |
| V.12 #10 zrovnať namespace G7/G8/C7-G8 | odložené — nie je blokujúce |
| VI.8 #1–#6 release a README | §1 akcie 1–6 |
| VI.8 #7 zastaviť generovanie taskov | §1 akcia 12 |
| IV.A1 dôkaz nemožnosti `S₈` | §6 položka 3 |
| IV.A2 publikovať perkolačný výsledok | §6 položka 1, s výhradou §3 |
| IV.A3 preklasifikovať tri predikcie | §1 akcia 7 |
| IV.B1 perkolačné krátenie | §4 = koľaj `A0-K3` |
| IV.B2 fotónový sektor | až po `A0_PASS`; neplánované |
| IV.B3 Rideout–Sorkin CSG | koľaj `A0-K2`, špekulatívna, nespúšťať |
| C1 zmraziť verziovanie | §1 akcia 11 |
| C2 zrušiť 16-miestnu precíznosť | §1 akcia 8 |
| C3 jeden skutočný záväzok | odložené do `A0`; nemá zmysel dávať na kocku číslo zo sektora, ktorý možno nie je fyzikálny |
| C4 skrátiť na 15 strán, jeden e-mail | §2, rozdelené na dvoch adresátov |
| C5 oddeliť audit procesu od auditu fyziky | §1 akcia 6 |
