# Externý audit — EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO

**Auditor:** externý (Claude, nezávislý beh, iba zapečatený balík; žiadny prístup k pracovnému stromu projektu)
**Dátum:** 2026-07-18
**Overenie manifestu:** 26/26 SHA-256 zhôd — všetkých 17 evidence kópií, 5 REPRO súborov a 4 package-control súbory sa zhodujú s `01_MANIFEST_SHA256.md`. Navyše overená deklarovaná identita REPRO kópií so zdrojovými hashmi (224≡005, 234≡011, 235≡015, base moduly ≡ 006/012). Balík je autentický voči zapečatenému stavu.
**Prostredie reprodukcie:** Linux x86_64 (glibc 2.39), Python 3.12.3, SymPy 1.14.0, NumPy 2.4.4, SciPy 1.17.1 (SciPy iba pre nezávislé kontrolné výpočty auditora, nie pre R1–R3). Pôvodné behy: Python 3.11, verzie nezmrazené — deklarovaná medzera prostredia trvá, ale je teraz ohraničená z dvoch strán (pozri Odchýlky).
**Dosiahnutá dôkazová úroveň:** `T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP` — dosiahnutá. Pôvodný audit EA-001 sa týmto posilňuje z `PASS_MAPY` na reprodukovateľný formula/calculation audit.

---

## Odpoveď na presnú otázku

Balík kladie štyri otázky (00_SCOPE). Odpovede po primárnej kontrole riadkov, troch reprodukciách a nezávislých prepočtoch auditora:

**1. Preniklo fixed `K_MPC=0.05` do starého K7 denominatoru cez `z^p`? ÁNO — `INDEPENDENTLY_RECOMPUTED`.**
Primárny runner 213 obsahuje na riadkoch 65–68 a 112–114 presne: `K_MPC = 0.05`, `z = K_MPC*exp(x)/(HUBBLE0_MPC*sqrt(OMEGA_R0))`, `fuel_piece = z**P_EXPONENT`, `denominator = 1 + MU*z + fuel_piece*(1 + TRANSFER_SHAPE*z**2)`. Reprodukcia R1 potvrdila bit-identicky (na `runtime_seconds` presne), že `mu*z` a `g2*z²` sú k-nezávislé, ale palivový faktor je homogénny stupňa `p` v `k`, takže `D(a,k) = 1 + Ωm·a/Ωr + k^p·A(a)`. Auditor navyše vykonal vlastný multi-k numerický test (požiadavka 002 §6.7), ktorý balík doteraz neobsahoval: pri `a=10⁻⁴` dáva stará formulácia `D = 1.4157` (k=0.01), `D = 28.2115` (k=0.05), `D = 15017.5` (k=0.25) — tri rádovo odlišné „backgroundy" pre tri módy. Prenos je preukázaný výpočtom aj nezávislou rekonštrukciou.

**2. Nie je preto tento denominator univerzálny FLRW background? ÁNO, nie je — `INDEPENDENTLY_RECOMPUTED`.**
Priamy dôsledok bodu 1: `H²(a)` nesmie závisieť od Fourierovho módu evolvovanej poruchy. STOP `STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED` je vecne správny a správne ohraničený na implementáciu, nie na mechanizmus ani exponent `p`. Auditor navyše overil opravené mapovanie: s `Φ(k)=A_f(H0√Ωr0/k)^p` je `D` identické na 12 platných číslic pre k=0.01, 0.05, 0.25 (`D=1.367688715066`), a negatívna kontrola (Φ=A_f bez kompenzačnej mocniny) bránu okamžite zhodí (`D=376` vs `D=209632`). Tri deklarované podmienky z 002 §6.7–6.8 (rozdielne staré D, zhodné opravené D, funkčná negatívna kontrola) sú týmto splnené.

**3. Je `A_f` odvodené z konkrétneho zmrazeného A1 closure pri `λ=0.15`, nie nový nezávislý fit? ÁNO — `INDEPENDENTLY_RECOMPUTED`, s provenance výhradou.**
R2 reprodukovala `A_f = 7809.270101963506` bit-identicky na všetkých troch RK4 rozlíšeniach vrátane `relative_medium_fine = 5.343344047845171e-13`. Auditor nezávisle overil: (a) pomer chýb (coarse−medium)/(medium−fine) = 16.90, konzistentný so 4. rádom RK4; (b) Richardsonova extrapolácia dáva 7809.2701019632; (c) úplne nezávislá reimplementácia pozadia iným integrátorom (adaptívny DOP853, rtol=1e-13) dáva 7809.270101971514 — relatívny rozdiel 1.0e-12 voči projektovej hodnote. Skript nemá žiaden vstup `K_MPC` ani `k`; hodnota je jednoznačne určená zmrazenými A1 vstupmi (λ=0.15, δ=0.02297, Ωm0=0.3517, h=0.6637, plochá uzávierka). Je to parameter-bookkeeping výsledok podmienený A1 closure (P2b ostáva otvorené), nie konštanta prírody — v súlade so zmrazenou hranicou balíka.

**4. Je normalizovaný skrátený K7 rad iba skorá aproximácia, ktorá pri `a≈0.70896` stráca fyzikálnu prípustnosť? ÁNO — `INDEPENDENTLY_RECOMPUTED`, s dôležitým spresnením.**
R3 reprodukovala všetkých 10 checkpointov aj nulový prechod bit-identicky (`a_linear_crossing = 0.7089578778205975`, `D_K7,trunc(1) = −24131.55780453146`, `D_A1(1) = 10470.78753381634 = 1/Ωr0` presne). Auditor nezávisle: (a) analyticky prepočítal `D_K7(1) = 1 + Ωm0/Ωr0 + A_f(1 + Cλ/√Ωr0)` s `C = 1/(p+1) − 1/2 = −0.2972050804183254` — zhoda na posledný bit; (b) bisekciou určil skutočný koreň skráteného polynómu `a* = 0.708957922`, čo potvrdzuje, že projektová hodnota 0.70895788 je korektná lineárna gridová lokalizácia (odchýlka 4.4e-8, v rámci mriežky). **Spresnenie (nový výsledok auditora, odpoveď na 002 §7.5):** nulový prechod je iba neskorá smrť; kvantitatívna použiteľnosť radu končí oveľa skôr. Relatívna chyba voči presnému A1 backgroundu prekročí 0.1 % pri `a ≈ 3.6e-6` (x≈−12.5), 1 % pri `a ≈ 4.0e-5` (x≈−10.1), a v hmotnej ére sa ustáli na plateau ~8.2 % ešte pred kolapsom znamienka. Expanzný parameter korekcie `g = λa²/√Ωr0` dosiahne 1 už pri `a ≈ 0.255` — rad je tam formálne mimo polomeru použiteľnosti. Skrátený K7 rad je teda legitímna aproximácia iba hlboko v radiačnej ére; nikdy nebol kandidátom na neskorý background.

---

## Formula ledger s cestami, hashmi a riadkami

Hash skratky = prvých 8 znakov SHA-256 z manifestu (plné hodnoty overené 26/26).

| # | Krok | Súbor (hash) | Riadky | Presný obsah | Nosič `k` | Tag |
|---|---|---|---|---|---|---|
| L1 | Zdroj exponentu | `010__FUEL_TERM_PROVENANCE.md` (213DF36C) §1 | — | `y_f,x = [4−3δ−λH0/H]·y_f ⇒ p = 4−3δ` | žiadny | `INFERRED_FROM_PROJECT_DOCS`; aritmetika `4 − 3·0.02297 = 3.93109` overená exaktne (Decimal) → `INDEPENDENTLY_RECOMPUTED` |
| L2 | Párované fuel/ash koeficienty | `004__PRIMARY_PREDECESSOR_128.py` (998A7D42) | 44–50 | `f2 = −G/2`, `a2 = G/(p+1)`; identity `(p+2)f2 = pf2−G`, `(p+2)a2 = a2+G` | jeden vybraný mód — legálne | `INDEPENDENTLY_RECOMPUTED` — obe identity overené vlastným SymPy, residuál 0 |
| L3 | Fixná konštanta | `003__PRIMARY_HISTORICAL_RUNNER_213.py` (8726BAE5) | 63–68 | `OMEGA_R0 = 2.47282e-5·(1+0.2271·NEFF)/H0²`; `HUBBLE0_MPC = 100h/299792.458`; `K_MPC = 0.05`; `MU`; `G2 = 0.15(H0/K)²√Ωr`; `TRANSFER_SHAPE = G2·(1/(p+1)−0.5)` | `k` fixovaný ako backgroundová konštanta | `OBSERVED_IN_PRIMARY` |
| L4 | Kontaminovaný background | `003__…213.py` | 112–114, 119 | `z = K_MPC·e^x/(H0M√Ωr)`; `fuel_piece = z^p`; `denominator = 1+MU·z+fuel·(1+TS·z²)`; `s2 = z²/denominator` | `k^p` únik do `D`; `s2` je legitímny poruchový vstup | `OBSERVED_IN_PRIMARY` |
| L5 | Symbolický dôkaz úniku | `006__BASE…py` (EB3B1F3A) | 10–20 | `μz−Ωm a/Ωr = 0`; `g2z²−(3/20)a²/√Ωr = 0`; `k·∂F/∂k−pF = 0`; `∂F/∂k ≠ 0` pri `p=3.93109` | `k` symbolický | `INDEPENDENTLY_RECOMPUTED` — R1 bit-identická + vlastná nezávislá SymPy konštrukcia auditora dala rovnaké 4 výsledky |
| L6 | Strojový STOP | `008__RUN_FULL_002_RAW.json` (1564DDE5) | — | `D(a,k) = Ωm a/Ωr + 1 + (ak/(H0√Ωr))^p·(…)`; verdikt STOP | `k^p` explicitne v reťazci denominatora | `INDEPENDENTLY_RECOMPUTED` (R1) |
| L7 | Povinné mapovanie | `010` §4, `001` §1b | — | `Φ(k) = A_f[H0√Ωr0/k]^p` | ruší `k^p` v rannom rade | `INDEPENDENTLY_RECOMPUTED` — multi-k test: opravené `D` zhodné na 12 číslic naprieč k∈{0.01,0.05,0.25}; negatívna kontrola funguje |
| L8 | `A_f` z A1 closure | `011__RUNNER_234_AF.py` (232FB2BA) + `012__BASE…py` (72B750EE) | 012: 27–37 (RHS), 63–101 (integrate_af) | RK4 spätne, `A_f = (X_f/X_r)/e^{p·x}` pri x=−18 | žiadny — check `no_K_MPC_or_fourier_k_input` je pravdivý (overené čítaním kódu) | `INDEPENDENTLY_RECOMPUTED` (R2 bit-identická + nezávislý DOP853 na 1e-12) |
| L9 | Skrátený K7 test | `015__RUNNER_235_P3.py` (C603B845) | 31–34 | `D_K7 = 1 + (Ωm0/Ωr0)a + A_f a^p(1 + Cλa²/√Ωr0)`, `C = 1/(p+1)−1/2` | žiadny — po cancelácii | `INDEPENDENTLY_RECOMPUTED` (R3 bit-identická + analytický prepočet `D_K7(1)` a bisekcia koreňa) |
| L10 | Interpretačné dokumenty | `009`, `014`, `017` | — | scope STOP-ov a PASS-ov | — | `CONTEXT_ONLY` — konzistentné s primárnymi výsledkami, žiadne zlievanie implementačnej a mechanizmovej smrti nenájdené |

Poznámka k L4: rovnica `Of = fuel_piece·(1 − G2z²/2)/denominator` (riadok 122) je konzistentná s L2 (`f2=−G/2`) a `Oc` obsahuje ash člen `G2z^{p+2}/(p+1)` konzistentný s `a2=G/(p+1)` — párovanie koeficientov je v implementácii 213 skutočne prítomné, nie iba deklarované.

---

## Reprodukcia R1 — symbolická univerzálnosť

| Položka | Hodnota |
|---|---|
| Smoke | `{"scope":"exact_symbolic_no_ode","smoke":"PASS"}`, exit 0 |
| Plný beh | exit **1 zámerne** (runner mapuje STOP→1), wall 0.81 s, interný runtime 0.409 s (limit 10 s) |
| Výstupný JSON | vytvorený, immutable; **bit-identický s `008__RUN_FULL_002_RAW.json` vo všetkých poliach okrem `runtime_seconds`** (0.485 s pôvodne vs 0.409 s teraz) |
| Verdikt | `STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED`; všetky 4 checks true; residuály `0,0,0` a nenulová derivácia — reťazce identické so zapečateným raw vrátane presného tvaru `denominator` |

Splnená podmienka z 03: exit 1 so správnym JSON = technicky uzavreté. Hash skriptu aj base modulu vo výstupe sa zhodujú s manifestom.

## Reprodukcia R2 — `A_f` zo zmrazeného A1

| Položka | Hodnota |
|---|---|
| Beh | exit 0, wall 1.32 s (limit 10 s externý, 5 s/rozlíšenie interný) |
| `A_f` (dx=1.25e-4) | `7809.270101963506` — **bit-identické** so zapečateným `013` |
| `A_f` (dx=2.5e-4 / 5e-4) | `7809.270101967679` / `7809.270102038179` — bit-identické |
| medium/fine rel. rozdiel | `5.343344047845171e-13` — identický do posledného bitu |
| Nezávislá kontrola auditora | iný integrátor (DOP853, rtol 1e-13): `7809.270101971514`, rel. odchýlka 1.0e-12; konvergenčný pomer RK4 = 16.90 ≈ 16 (4. rád); Richardson `7809.2701019632` |

Deterministickosť IEEE-754 dvojitej presnosti naprieč Python 3.11→3.12 a odlišným OS je pre tento reťazec operácií potvrdená empiricky. Výsledok znamená výlučne „bez nového nezávislého fitu pri zmrazenom A1 closure" — mikropôvod vstupov (P2b) tým nie je dotknutý.

## Reprodukcia R3 — exact-A1 verzus skrátený K7

| Položka | Hodnota |
|---|---|
| Beh | exit 0, wall 0.82 s |
| Verdikt | `STOP_K7_TRUNCATED_SERIES_IS_NOT_FULL_BACKGROUND` |
| Nulový prechod | `a = 0.7089578778205975`, `x_interval_end = −0.3435` — bit-identické |
| `a=1` | `D_A1 = 10470.78753381634`, `D_K7,trunc = −24131.55780453146` — bit-identické; všetkých 10 checkpointov bit-identických so `016` |
| Nezávislé kontroly | `D_A1(1)=1/Ωr0` exaktne; analytický `D_K7(1)` zhoda na posledný bit; skutočný koreň polynómu bisekciou `a*=0.708957922` (gridová hodnota je korektná lineárna lokalizácia); `C=−0.2972050804183254` prepočítané nezávisle |

---

## Odchýlky, riziká a nonclaims

### Odchýlky reprodukcie
Žiadne fyzikálne ani numerické. R1–R3 sú bit-identické so zapečatenými raw výsledkami vo všetkých fyzikálnych poliach; jediný rozdiel je `runtime_seconds` (očakávané). Platí prvý riadok vyhodnocovacej tabuľky z 03: **pôvodný audit sa posilňuje na T2.** Medzera prostredia sa zužuje: pôvodné behy (Python 3.11, Windows — cesty so spätnými lomkami v `016`) a táto reprodukcia (Python 3.12.3/Linux/SymPy 1.14.0) dávajú identické bity, takže výsledok nie je artefakt jednej platformy.

### Nové nálezy auditora (nemenia žiaden verdikt)

| ID | Nález | Závažnosť | Detail |
|---|---|---|---|
| A-1 | **Ωr0 šev medzi runnerom 213 a FrozenA1** | stredná | 213 riadok 63 používa fotónovú konštantu `2.47282e-5`; `FrozenA1` (012) používa `omega_gamma = 2.469e-5`. Výsledné `Ωr0`: 9.5652e-5 vs 9.5504e-5, rel. rozdiel **1.55e-3**. Pre STOP verdikty (štrukturálne) je to irelevantné, ale „zmrazený A1 pracovný bod" nie je numericky totožný s radiačnou hustotou historického runnera. Keďže `A_f` sa cituje na 16 číslic, pri budúcom porovnávaní so starými K7 behmi vznikne rozdiel na 3. platnej číslici z čisto konvenčného dôvodu. Analóg S8 švu — treba changelog/deklaráciu, ktorá konštanta je záväzná (T_CMB konvencia). |
| A-2 | Gridová vs skutočná nula | nízka | `0.70895788` je lineárna lokalizácia na mriežke 36 000 bodov; skutočný koreň skráteného polynómu je `0.708957922`. Odchýlka 4.4e-8 — bez dopadu, ale ledger by mal hodnotu označovať ako „grid-localized", čo `016` robí a `017` preberá korektne. |
| A-3 | **Interval platnosti skráteného radu je oveľa užší než nulový prechod** | stredná (fyzikálna interpretácia) | Rel. chyba voči presnému A1: >0.1 % od `a≈3.6e-6`, >1 % od `a≈4.0e-5`, plateau ~8.2 % počas hmotnej éry, kolaps znamienka až pri 0.709. Expanzný parameter `g=λa²/√Ωr0` prekročí 1 už pri `a≈0.255`. Akékoľvek budúce kvantitatívne použitie radu (napr. seedy porúch) musí byť obmedzené na `a ≲ 4e-5` pri 1 % tolerancii, nie „do a≈0.7". Toto uzatvára požiadavku 002 §7.5. |
| A-4 | Chýbajúce hash-viazanie `--af-json` v 235 | nízka | Runner 235 overuje iba reťazec verdiktu vstupného JSON, nie jeho SHA-256 (na rozdiel od disciplíny runnera 213, ktorý viaže input pack hashom). Substitúcia iného PASS JSON s inou `A_f` by prešla. Riziko R-2 z EA-001 (referencovať `A_f` cez hash zdrojového runu) tak nie je vynútené strojovo. |
| A-5 | λ natvrdo ako 3/20 v symbolickom audite | nízka | `006` používa `sp.Rational(3,20)` namiesto symbolu λ; audit je preto viazaný na pracovný bod λ=0.15. K-nezávislosť je pritom štrukturálna (nezávislá od λ) — pre budúci multi-λ test (002 §7.4) treba λ symbolizovať. |
| A-6 | `--x-min` v 235 je voľný, ale checkpointy sú fixné | nízka | Pri `--x-min ≠ −18` by `trajectory["samples"]` nemusel obsahovať kľúč `x=-18.0` a skript by padol KeyError; reprodukčný príkaz to maskuje. Defenzívna kontrola chýba. Nie je to chyba pre zapečatený beh. |

### Potvrdené staršie nálezy
N-3 (jednotková konvencia): overené priamo — `HUBBLE0_MPC = 100h/299792.458` je `H0/c` v Mpc⁻¹, takže `z` je bezrozmerné a `z^p` s necelým `p` je definované; konvencia však stále nie je nikde deklarovaná dokumentom. N-4 (provenance tag `A_f`): stále otvorené, teraz zosilnené nálezmi A-1 a A-4. N-1 (terminológia 0.05): tento balík zámer čísla neaudituje (nonclaim) — zostáva otvorený review.

### Riziká
1. **R-A1 (konvenčný drift):** Ωr0 šev (A-1) je presne typ chyby, ktorá prežije, lebo je „iba" 0.15 % — kým sa neprenesie do CLASS/CAMB, kde sa stretnú obe konvencie naraz.
2. **R-A4 (provenance bypass):** bez hash-viazania `af-json` môže budúci beh 235 potichu konzumovať inú `A_f`.
3. **R-A3 (rehabilitačné pokušenie, zosilnené):** plateau 8 % ukazuje, že skrátený rad nie je „dobrý do a≈0.7 a potom zomrie" — je kvantitatívne nepoužiteľný od konca radiačnej éry. Komunikovať nulový prechod ako jedinú hranicu by bolo zavádzajúce.

### Nonclaims (potvrdzujem dodržané)
Balík neaudituje CLASS/CAMB, CMB/S8, úplné perturbácie, zámer autora pri `0.05`, ani celý v3.17. Tento audit neudeľuje projektový PASS/REVIEW/STOP; autorita je odporúčacia. Nezávislé kontrolné výpočty auditora (multi-k test, DOP853, bisekcia, interval platnosti) sú vlastné artefakty auditu, nie projektové výsledky — projekt ich smie prevziať iba cez vlastný registrovaný beh.

---

## Odporúčanie hlavnému orchestrátorovi

1. **Prijať T2.** Všetky tri reprodukcie sú bit-identické na nezávislej platforme; dôkazová úroveň EA-001 sa oprávnene zvyšuje z `PASS_MAPY` na `T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP`. Medzera prostredia je odteraz dvojbodovo ohraničená (Windows/Py3.11 ↔ Linux/Py3.12.3+SymPy1.14.0); odporúčam zmraziť aspoň túto dvojicu do package history.
2. **Uzavrieť A-1 erratou, nie prepisom:** jednoveté vyhlásenie záväznej fotónovej konštanty (2.469e-5 vs 2.47282e-5, t. j. T_CMB konvencia) a poznámka, že historický 213 používal inú; zaradiť do jednotkového dodatku požadovaného už v EA-001 bode 5.2.
3. **Doplniť hash-viazanie do 235** (A-4): `--af-json-sha256` povinný argument alebo kontrola voči registrovanému hashu — malý patch, veľká provenance hodnota; realizovať ako nový skript, nie mutáciu zapečateného.
4. **Registrovať interval platnosti radu** (A-3) ako záväzný scope výrok: „skrátený K7 rad je kvantitatívne použiteľný len pre a ≲ 4×10⁻⁵ (1 % voči D_A1); nulový prechod pri 0.709 je len neskorý symptóm." Tým sa definitívne zatvára 002 §7.5 a odzbrojuje R-3/R-A3.
5. **Pokračovať v K-N2/P4 (exact-background rederivation) podľa 017** — tri brány (H(a) a dτ/da z D_A1; rederivácia koeficientov bez skráteného radu; až potom nulový limit a CLASS rozhranie) sú správne navrhnuté; tento audit nenašiel nič, čo by ich menilo. Multi-λ štrukturálny test (002 §7.4) vyžaduje najprv symbolizáciu λ v base module (A-5).
6. **Žiadna zmena projektového verdiktu ani skóre** — STOP-y zostávajú v pôvodnom, správne ohraničenom rozsahu; exact-A1 background zostáva jediným prípustným kandidátom.

**Celkové zhodnotenie:** balík 004 splnil presne to, čo sľúbil — uzavrel medzeru E-1. Primárne riadky sedia s mapou, tri behy sú reprodukovateľné bit-po-bite, mapovanie Φ(k) je nezávisle potvrdené aj negatívnou kontrolou, a `A_f` je potvrdené druhou, metodicky odlišnou integráciou na 1e-12. Nájdené nedostatky (A-1 až A-6) sú konvenčné a provenienčné, nie matematické; žiaden nemení verdikt, ale A-1 a A-4 treba uzavrieť pred prenosom do CLASS/CAMB, kde by inak vyrobili presne ten typ tichej chyby, ktorý tento projekt inak disciplinovane loví.
