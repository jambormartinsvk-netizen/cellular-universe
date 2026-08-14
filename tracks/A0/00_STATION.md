# A0 — kontrolná stanica: pripúšťa substrát Lorentzovsky invariantný limit?

**ID stanice:** `A0`
**Zavedená:** 2026-08-14
**Dôvod zavedenia:** externý fyzikálny audit 2 (13. 8. 2026), sekcia V.9 —
mapa verifikačných staníc `A1 → A2 → A3 → A4` nemá stanicu pre otázku,
ktorá je upstream od všetkých ostatných.
**Autoritatívny stav:** `LIVE / BLOCKING_UPSTREAM`
**Rozhodnutie autora (14. 8. 2026):** `A0` sa rozhodne **pred** akoukoľvek
ďalšou kozmologickou prácou. `A2` a `A3` sú do jej rozhodnutia zmrazené.

---

## 1. Otázka stanice

> **Pripúšťa substrát teórie kontinuálny limit, ktorý je Lorentzovsky
> invariantný a stabilný voči radiačným korekciám?**

Nie tree-level. Nie disperzia. **Voči smyčkám.**

`FS-C9` z `A2/00_CONSTRAINT_FEASIBILITY_LEDGER.md` sa tejto otázky dotýka
(*„`k → ∞` nemá ghost, záporné `c_s²`, acausalitu ani runaway"*), ale je to
podmienka na **tree-level poruchový operátor**. Podľa auditu je tree-level
bezpečný o 8.7 rádov a celý problém sedí v smyčkách, kde v ledgeri nie je
žiadny mantinel.

## 2. Prečo je A0 upstream od všetkého

```text
A0   substrat pripusta stabilny LI limit?
 |
 +-- NIE  -> A1, A2, A3 su bezpredmetne v predlozenej podobe.
 |          Kozmologicky sektor je fluidna parametrizacia, ktoru
 |          dostanete aj bez siete; siet do nej nevstupuje.
 |
 '-- ANO  -> A1 (background) -> A2 (poruchy) -> A3 (CMB/S8/H0) -> A4
```

Ak `A0` padne, zomiera `A2-K4` aj všetkých päť backupov `K7/K8/K9/K11/K12`
naraz — nie preto, že by ich fyzika bola zlá, ale preto, že hľadaný objekt
žije na substráte, ktorý neexistuje.

## 3. Vstupný nález

Externý audit 2, Časť III.5. Jednosmyčková vlastná energia v dvojskalárnom
modeli s vrcholom `(g/2)φχ²`, kde `χ` nesie disperziu Poisson–Delaunay siete:

```text
16 pi^2 (B - A)  =  0.1026 ln(Lambda/m)  +  0.294        (Lambda = 1/l_cell)

pri l_cell = l_Planck a g ~ Lambda:      dc^2/c^2 ~ 3.5e-02

experimentalne limity na dim-4 LV:
   elektron (Crab, vakuovy Cerenkov)      1e-16     medzera 14.5 radov
   foton (opticke rezonatory, SME kappa)  1e-19     medzera 17.5 radov
   UHECR / hadronovy sektor               1e-23     medzera 21.5 radov
```

**Stav reprodukcie (14. 8. 2026):** obe povinné null-kontroly formuly som
spustil nezávisle a prechádzajú (`W = k²`, cutoff → ∞ dá 10⁻¹⁵…10⁻²²;
`W = k²` s priestorovým cutoffom dá `16π²(B−A) = −0.01097` proti analytickému
`−1/(96π²k²_max)`). Výpočet je korektne vykonaný. Viď
`Audit/EA_EXT2_2026-08-14/01_VERIFICATION_LOG.md`.

**Uplatnená výhrada:** dôsledok III.5(1) auditu („akákoľvek teória s konečným
počtom dof na objem") je v rozpore s jeho vlastným III.6(b) (kauzálne množiny
majú konečnú hustotu dof a sú exaktne LI). Rozhoduje III.6(b). Číslo −0.011
meria nekovarianciu **regulátora**, nie fyziku. Pre QCTS však preferovaný rám
nie je artefakt schémy — je to ontológia teórie (globálne „teraz"), takže
sieťová časť zostáva fyzikálna. Podrobne v
`Audit/EA_EXT2_2026-08-14/00_RESPONSE_TO_EXTERNAL_AUDIT_2_SK.md`, §2.1.

## 4. Register koľají A0

| Koľaj | Podmienka / mechanizmus | Stav | Hĺbka | Prečo |
|---|---|---|---|---|
| `A0-K1` | ochrana supersymetriou (Groot Nibbelink–Pospelov, PRL 94, 081601, 2005) | `STOP_SCOPE / CONDITIONAL` | `10/100` | vyžaduje bozón = fermión. `C = 56 → n_s` na 3.36σ, `C = 118` na 5.68σ (overené). Únik existuje iba pri **škálovo závislej kapacite** — nie je odvodená; bez odvodenia je to ad-hoc záchrana zakázaná `FS-C11` |
| `A0-K2` | diskrétnosť na úrovni **priestoročasu** (Bombelli–Henson–Sorkin; Rideout–Sorkin CSG) | `SEPARATE_ROUTE` | `20/100` | funguje exaktne (boosty zachovávajú štvorobjem), ale rozpúšťa globálne „teraz", teda `δ` ako overhead delenia, teda `w_f = −1+δ`. Zachrániteľné iba cez rekonštrukciu z IV.B3 |
| `A0-K3` | silne viazaný RG fixný bod, `Δ ≳ 0.8` | `LIVE / OPEN` | `10/100` | perturbatívne `Δ ~ 10⁻³` (nestačí), **ale** Bednik–Pujolàs–Sibiryakov, JHEP 11 (2013) 064 dosahujú mocninové potlačenie zo silnej dynamiky bez SUSY cez gauge/gravity. Audit tento mechanizmus vynechal. Otvorené |
| `A0-K4` | ladenie `g/Λ < 1.7×10⁻⁹` | `NOT_ADMISSIBLE` | `0/100` | deväť rádov, pre každé pole a každú väzbu, bez vysvetlenia. Nie je to mechanizmus |
| `A0-K5` | **separácia škál EFT/LV** (Belenchia–Gambassi–Liberati, JHEP 06 (2016) 049) | `LIVE / OPEN / PRIORITA` | `10/100` | ak SM ako EFT končí pri `M ≪ Λ`, smyčka nikdy nevidí oblasť s O(1) narušením; potlačenie `(M/Λ)²`. **Jedno číslo, raz, pre všetky polia** — nie ladenie po poliach. Cena je kvantifikovaná v §5 |

`A0-K5` je nová koľaj, ktorú audit nemá. Je to najlacnejšia živá možnosť a má
najostrejšiu cenu.

## 5. Cena koľají A0-K3 a A0-K5 — vyčíslená

Pri `Λ = M_Pl`, `g = Λ`, `ln(Λ/m_e) = 51.5` (overené výpočtom):

| cieľový limit | potrebné potlačenie | `M/Λ` (K5) | `M` [GeV] (K5) | `Δ` (K3) |
|---|---|---|---|---|
| `10⁻¹⁶` elektrón | `2.83×10⁻¹⁵` | `5.3×10⁻⁸` | `6.5×10¹¹` | `0.650` |
| `10⁻¹⁹` fotón | `2.83×10⁻¹⁸` | `1.7×10⁻⁹` | `2.0×10¹⁰` | `0.785` |
| `10⁻²³` UHECR | `2.83×10⁻²²` | `1.7×10⁻¹¹` | `2.0×10⁸` | `0.963` |

**Toto je predikcia, nie výhovorka.** Ak `A0-K5` prejde, teória tvrdí, že
existuje Lorentzovsky invariantná UV kompletizácia SM pod `~10¹⁰ GeV`. To je
falzifikovateľné a je to prvé tvrdenie tejto teórie, ktoré nie je
kozmologické.

## 6. DONE_WHEN — kedy je A0 rozhodnutá

`A0` sa uzavrie práve jedným z troch výsledkov:

```text
A0_PASS      aspon jedna kolaj A0-K1..K5 doda mechanizmus, ktory vynuti
             B = A alebo potlaci dim-4 koeficient pod 1e-19, bez ladenia
             po poliach a bez post-data fitu.
             -> odblokuje A2 a A3; z A0 sa stane nova hard constraint
                pre kazdy A2 operator.

A0_NO_GO     vsetkych pat kolaji je certifikovane prazdnych alebo
             neprijatelnych.
             -> A2-K4 a vsetkych pat backupov su bezpredmetne;
                trat IV.A (cista falzifikacia) sa stava jedinou.

A0_UNDECIDED_BY_EXHAUSTION
             vycerpany rozpocet 30 chyb na fyzikalnu otazku (viz AGENTS.md
             §4) bez rozhodnutia.
             -> vydaj NO_GO_BY_EXHAUSTION s presnym zoznamom skusaneho.
                To je publikovatelny vysledok, nie zlyhanie.
```

## 7. Poradie prác vnútri A0

1. **`A0-K5` prvá** (2–3 týždne). Je najlacnejšia, jej cena je už vyčíslená
   a rozhoduje o použiteľnosti celého auditného výpočtu III.5. Konkrétne:
   zopakovať smyčku s cutoffom `M < k_max` a overiť, či koeficient škáluje
   ako `(M/Λ)²`. Ak áno, `A0` je otvorená a otázka sa presúva na *existuje
   taká `M`?*
2. **`A0-K3` druhá** (1 mesiac). Toto je zároveň krok `B1` z Časti IV auditu.
   Napísať najjednoduchší interagujúci model na sieti s **bezrozmernou**
   väzbou a pozrieť sa, či sa LV časť vykráti. Povinná kontrola: formula musí
   dať nulu pre `W = k²`.
3. **`A0-K1` iba ak K5 aj K3 padnú.** Vyžaduje odvodenie škálovo závislej
   kapacity, čo je zásah do §4.3, teda `TRACK_IDENTITY_GATE`.
4. **`A0-K2` je paralelná a špekulatívna.** Rideout–Sorkin CSG rekonštrukcia
   (IV.B3). Nespúšťať pred rozhodnutím K5/K3.

## 8. Povinné mantinely pre každú koľaj A0

| ID | Mantinel |
|---|---|
| `A0-C1` | povinná null-kontrola: `W = k²`, cutoff → ∞ musí dať nulu na 10⁻¹⁵ alebo lepšie |
| `A0-C2` | povinná kontrola nekovariancie regulátora: `W = k²` s použitým cutoffom sa vykáže samostatne a odčíta sa od výsledku siete |
| `A0-C3` | výsledok sa vykazuje pre **bezrozmernú** väzbu; dimenzionálne `g` dáva únikovú cestu `(g/Λ)²`, ktorá v SM neexistuje |
| `A0-C4` | žiadne ladenie po poliach ani po väzbách; mechanizmus musí byť jeden pre všetky |
| `A0-C5` | `FS-C11` platí aj tu: žiadna sadzba ani škála z trafenia dát |

## 9. Väzba na existujúce stanice

- `A1` (background) — nezmenená, ale jej výsledky sú od 14. 8. 2026
  `CLAIM_QUARANTINE / PRE_A0_CONDITIONAL` pre všetko, čo tvrdí, že sieť je
  fyzikálny substrát. Čisto fluidná parametrizácia `A1` prežije `A0_NO_GO`;
  jej väzba na sieť nie.
- `A2` — zmrazená. `A2-K4` aj `K7/K8/K9/K11/K12` zostávajú `LIVE`, ale
  `contract not open` a **žiadny nový task sa neotvára**, kým `A0` nerozhodne.
- `A3` — nezmenená, blokovaná dvakrát (`A2` neuzavretá, `A0` nerozhodnutá).

## 10. Pravidlo aktualizácie

Táto stanica sa mení iba po autoritatívnom výsledku koľaje `A0-K1..K5` alebo
po rozhodnutí autora. Zjemnenie špecifikácie blockeru **nie je** zmena stavu a
nesmie vytvoriť nový artefakt (viď `AGENTS.md` §4.1, pravidlo
`HRUBÝ_KANDIDÁT_FIRST`).
