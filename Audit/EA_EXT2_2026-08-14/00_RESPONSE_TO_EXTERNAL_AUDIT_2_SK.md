# Odpoveď na externý fyzikálny audit QCTS v3.18 (audit č. 2, 13. 8. 2026)

**Autorita dokumentu:** návrh odpovede pre Martina Jámbora; nie autoritatívna zmena stavu
**Dátum:** 14. 8. 2026
**Rozsah:** nezávislá rekonštrukcia sporných čísel auditu; klasifikácia každého
materiálneho nálezu na `PRIJATÉ / PRIJATÉ S VÝHRADOU / ODMIETNUTÉ`
**Nonclaim:** tento dokument nemení žiadnu hĺbku, žiadne skóre ani stav koľaje.
Autoritatívne zmeny sú v samostatných deltách uvedených v §6.

---

## 0. Zhrnutie v šiestich vetách

1. **Aritmetika auditu je správna.** Nezávisle som prepočítal II.1, II.3, II.4,
   II.6, II.7, III.1, III.2 a obe povinné null-kontroly z III.5. Všetko sedí
   v rámci deklarovanej presnosti; podrobnosti v §1.
2. **Dva numerické preklepy** v samotnom audite: `Ω_cell = c/(2.117 ℓ₀)` má byť
   `c/(2.169 ℓ₀)`, a Dodatok A1 má obrátené znamienko exponentu
   (`*1091**3` namiesto `/1091**3`). Ani jeden nemení záver (§1.6).
3. **Kategoriálne nálezy auditu prijímam** — chýbajúca stanica A0, algebraická
   trivialita §6.4, FIRAS dichotómia pri steam, `IDENTITY` status P10,
   nefinitnosť `X_K`, chybový rozpočet obnovovaný delením, rozpor
   „Neprijaté" vs. publikované survival targets, a mŕtvy git tag v3.18.
4. **Jeden vecný logický rozpor v audite:** dôsledok III.5(1) („akákoľvek
   teória s konečným počtom dof na objem dostane dim-4 narušenie Lorentza")
   je v priamom rozpore s vlastným III.6(b) (kauzálne množiny majú konečnú
   hustotu dof a sú exaktne Lorentzovsky invariantné). Správne tvrdenie je
   užšie: **priestorový cutoff v preferovanom ráme** to spôsobí. Číslo −0.011
   z III.5 nie je fyzika, je to miera nekovariancie regulátora (§2.1).
5. **Audit vynechal dva publikované mechanizmy**, ktoré patria do jeho
   vlastného zoznamu III.6: Belenchia–Gambassi–Liberati (2016) — separácia
   škál EFT a LV, a Bednik–Pujolàs–Sibiryakov (2013) — emergentná Lorentzova
   invariancia zo silnej dynamiky bez SUSY. Tvrdenie „nič také nie je známe"
   je preto nesprávne. Nie je to však záchrana zadarmo: obe majú cenu a tá
   cena je merateľná (§2.2, §2.3).
6. **Hlavný záver auditu napriek tomu stojí.** Program je blokovaný upstream
   na stanici, ktorá v mape neexistuje. Odporúčanie zaviesť A0 a rozhodnúť ju
   pred akoukoľvek ďalšou kozmologickou prácou prijímam bez výhrad.

---

## 1. Nezávislá rekonštrukcia — čo som prepočítal a čo vyšlo

Prostredie: Python 3.12, numpy 2.4.4, scipy 1.17.1. Kód a raw výstup sú v
`01_VERIFICATION_LOG.md` a `verify_*.py` v tomto adresári.

### 1.1 Pozadie, popol z prenosu, vynútené Ω_m0 (audit II.1)

```
delta                 = 0.022969782752802058     zhoda na vsetky cifry
popol z prenosu       = 0.0270787837             audit 0.027080     OK
omega_m(rekombinacia) = 0.14299                  audit 0.14299      OK
vynutene Om0          = 0.14299/0.6637^2 + 0.02708 = 0.35170        OK
```

**Prijaté ako výpočet.** Ale s jednou vecnou výhradou k interpretácii:

> II.1 nie je predikcia, je to **reparametrizácia**. Zobrazenie
> `Ω_m0 → ω_m(rek)` je monotónne a invertovateľné; audit ho iba obrátil a
> nazval vstup výstupom. Model nepredpovedá `Ω_m0 = 0.3517` — model hovorí,
> že **`Ω_m0` a `ω_m(rek)` nie sú nezávisle nastaviteľné**. To je slabšie
> tvrdenie než „model niečo predpovedá", ale je to presne to tvrdenie, ktoré
> II.3 potrebuje, a to je dôležitejšie.

Odporúčanie auditu preformulovať §5.2 tak prijímam, ale s touto formuláciou,
nie s formuláciou „model niečo predpovedá, nie iba prijíma".

### 1.2 S₈ ∝ 1/h a nemožnosť doladenia (audit II.3)

Prepočítal som λ-sken pri sebe-konzistentnom `Ω_m0` (`ω_m(rek)` fixované):

| λ | Ω_m0 (moja) | Ω_m0 (audit) |
|---|---|---|
| 0.00 | 0.3246 | 0.3248 |
| 0.05 | 0.3337 | 0.3339 |
| 0.10 | 0.3427 | 0.3429 |
| 0.15 | 0.3517 | 0.3518 |
| 0.20 | 0.3606 | 0.3607 |

Zhoda na 4. desatinu. **Štrukturálny bod prijímam bez výhrady:** pri kotvení
`ω_m` na CMB platí `S₈ = σ₈√(ω_m/0.3)/h` exaktne, teda tlačenie `H₀` dole a
zdvíhanie `S₈` sú tá istá algebraická operácia. Obe napätia sa nezhoršujú
„zhodou okolností"; zhoršujú sa mechanicky.

Overil som aj dátový kontext: KiDS-Legacy skutočne udáva
`S₈ = 0.815⁺⁰·⁰¹⁶₋₀.₀₂₁` a **0.73σ zhodu s Planckom**. Priestor, do ktorého by
`S₈ ≈ 0.87` mohlo zapadnúť, naozaj zmizol.

### 1.3 Tabuľka §6.4 (audit II.4)

```
S8 * H0 = [58.266, 58.155, 58.044]     rozptyl 0.381 %
```

**Prijaté.** Tabuľka §6.4 kóduje `S₈ ∝ 1/H₀`, čo je algebraický dôsledok
definície `S₈` pri fixnom `ω_m`. Skutočná rastová fyzika je 0.4 % z nej.
Reprodukovateľnosť RK4 na 10⁻¹² pre algebraickú identitu nie je vedecká
validácia a §6.4 aj EA-047 to musia priznať.

### 1.4 Okno pre C a degenerácia s α (audit II.6)

Z relácie `n_s = 1 − (3/2)δ` a `δ = 1/(⟨k⟩+C)`:

```
n_s(C=28)  = 0.965545
najlepsi fit                 C = 27.20
1 sigma  [0.9607, 0.9691] -> C = [22.63, 33.01]     13 celych cisel
2 sigma                   -> C = [18.95, 40.64]     24
3 sigma                   -> C = [15.91, 51.13]     36
C = 56  (SUSY-zdvojene)   -> n_s = 0.9790 = 3.36 sigma
C = 118 (bozony+fermiony) -> n_s = 0.9888 = 5.68 sigma
```

Všetko bit-identické s auditom. **Prijaté.** `C = 28` leží 0.15σ nad optimom,
okno je široké 13 celých čísel na 1σ a `C` nemá druhý observačný úchyt.
Zhoda `n_s` je dvojparametrická koincidencia. §4.3 to má povedať takto
explicitne, nie v slabšej forme.

### 1.5 Steam pri 0.905 K (audit II.7)

| 30 GHz | 53.21 GHz | 100 GHz | 217 GHz |
|---|---|---|---|
| 17.81 % | 9.82 % | 2.41 % | 0.04 % |

`ρ_steam/ρ_CMB = 1.216 %`; Wienov frekvenčný vrchol 53.21 GHz. Zhoda
s auditom (audit uvádza 9.9 % pri 53 GHz — to je 53.00 GHz, nie 53.21 GHz;
nepodstatné).

**Prijaté vrátane dichotómie.** COBE/FIRAS obmedzuje odchýlky od čierneho
telesa na 10⁻⁴–10⁻⁵. Ak steam interaguje elektromagneticky, 17.8 % pri 30 GHz
je vylúčené o 3–4 rády. Ak sú to gravitóny, je nedetegovateľný. P11 v
súčasnej podobe pôsobí ako merateľná predikcia, ktorou nie je, a musí túto
dichotómiu obsahovať explicitne.

### 1.6 Sieť: Ω_cell a koeficient q⁴ (audit III.1, III.2)

Vlastná triangulácia (scipy Delaunay, len vnútorné hrany, dva seedy):

| M | seed | ⟨Δ²⟩/ℓ₀² | ⟨Δ⁴⟩/ℓ₀⁴ | ξ | Ω_cell |
|---|---|---|---|---|---|
| 60 000 | 1 | 1.7982 | 4.4756 | 0.124446 | c/(2.158 ℓ₀) |
| 200 000 | 1 | 1.8088 | 4.5128 | 0.124745 | c/(2.164 ℓ₀) |
| 200 000 | 7 | 1.8075 | 4.5165 | 0.124937 | c/(2.163 ℓ₀) |

`ξ ≈ 0.1247` proti auditovým `0.12522` — zhoda na 0.4 %, v rámci konvergencie
s M. **Prijaté**, vrátane oboch štrukturálnych pozorovaní: `⟨k⟩` sa v
disperzii vykráti (centrálny most teórie do jej vlastnej disperzie nevstupuje)
a znamienko je subluminálne.

**Numerická chyba auditu č. 1.** Audit píše
`Ω_cell = c·√(6/(⟨k⟩⟨D²⟩)) = c/(2.117 ℓ₀)`. Dosadením jeho vlastných čísel
(`⟨k⟩ = 15.5355`, `⟨D²⟩ = 1.8175`) vychádza `√(6/28.234) = 0.46102`, teda
**`c/(2.169 ℓ₀)`**. Hodnota 2.117 by vyžadovala `⟨k⟩ = 14.79`. Odvodenie samo
je správne a cenné; opravte prosím číslo.

**Numerická chyba auditu č. 2.** V Dodatku A1 je riadok
`om_rec = (Y[1]+Y[2])[i]*1091**3*h**2`. Pri deklarovanej normalizácii ODE
(`ρ_i/ρ_crit,0`, `dB/dx = −3B`) je `Y[1]+Y[2]` pri `a = 1/1091` už zväčšené
o `1091³`, takže sa má **deliť**, nie násobiť. Ako je publikované, snippet dá
`2.4×10¹⁷`, nie `0.14299`. Po oprave znamienka exponentu vychádza presne
`0.14299`. Dodatok A tak v predloženej podobe nie je reprodukovateľný a je to
presne ten typ nálezu, ktorý audit sám radí priznať.

**Tretia, menšia:** audit uvádza `ω_m(rek) = 0.14299` ako „0.5σ" od Planckovho
`0.1431 ± 0.0012`. Mne vychádza **0.09σ**. Bod I.4 je teda ešte silnejší,
než ho audit predáva.

### 1.7 Povinné null-kontroly smyčkovej formuly (audit III.5)

Implementoval som formulu z Dodatku A3 od nuly a spustil obe kontroly, ktoré
audit sám označuje ako povinné:

```
W = k^2, cutoff -> nekonecno  (plna Lorentzova invariancia):
   m=0.01  ->  B-A =  2.2e-15
   m=0.20  ->  B-A =  3.0e-18
   m=1.00  ->  B-A = -1.8e-18
   m=5.00  ->  B-A =  6.9e-22          => PRESNA NULA, kontrola prechadza

W = k^2, priestorovy cutoff k_max = (6 pi^2)^(1/3) = 3.8978:
   m=0.20  ->  B-A = -6.9014e-05
   m->0    ->  B-A = -6.9470e-05 = -1/(96 pi^2 k_max^2)     analyticky presne
   16 pi^2 (B-A) = -0.01097                                 audit: -0.011
```

**Obe kontroly prechádzajú a reprodukujú auditové čísla.** Výpočet III.5 je
korektne vykonaný. To, čo z neho vyplýva, je iná otázka a je predmetom §2.

---

## 2. Kde sa audit mýli

Tri body. Prvý je logický rozpor vnútri auditu, druhý a tretí sú vynechaná
literatúra. Žiadny z nich program nezachraňuje; všetky tri menia to, čo treba
urobiť ďalej.

### 2.1 Dôsledok III.5(1) je v rozpore s III.6(b) — a rozhoduje III.6(b)

Audit v III.5, dôsledok (1), píše:

> „Akákoľvek teória s konečným počtom stupňov voľnosti na objem priestoru
> dostane dim-4 narušenie Lorentza zo smyčiek."

O tri strany nižšie, v III.6(b), píše:

> „Poissonov sprinkling do Minkowskiho priestoročasu je presne boostovo
> invariantný… Diskrétnosť teda nikdy nevygeneruje preferovanú sústavu a
> perkolácia nemá čím sa nakŕmiť."

Kauzálna množina **má** konečnú hustotu stupňov voľnosti a **je** exaktne
Lorentzovsky invariantná. Obe tvrdenia naraz platiť nemôžu. Rozhoduje druhé,
pretože je to dokázaná veta (Bombelli–Henson–Sorkin), zatiaľ čo prvé je
zovšeobecnenie jedného numerického výsledku.

Diagnóza je jednoduchá a audit ju má vo vlastných dátach. Číslo
`16π²(B−A) = −0.011` bolo získané pre **exaktne Lorentzovsky invariantnú**
disperziu `W = k²`. Jediná vec, ktorá tam narúša Lorentza, je **priestorový**
cutoff `|k| < k_max` — a ten je definovaný v jednom vybranom ráme. Nie je to
vlastnosť konečného počtu módov; je to vlastnosť **frame-závislého
regulátora**. Číslo −0.011 nie je fyzika. Je to miera nekovariancie schémy.

Dôsledky, ktoré z toho beriem vážne:

1. **Formulácia dôsledku (1) sa musí stiahnuť.** Správne znenie: *teória,
   ktorej regularizácia definuje priestorový cutoff v preferovanom ráme,
   dostane dim-4 narušenie Lorentza zo smyčiek.* To je oveľa užšie tvrdenie a
   nie je to no-go pre diskrétnosť ako takú.
2. **Hlavný výsledok pre QCTS napriek tomu stojí.** QCTS má globálne „teraz",
   takže preferovaný rám v nej nie je artefakt schémy — je to jej ontológia.
   Sieťová časť `0.1026 ln(Λ/m) + 0.294` je preto pre QCTS fyzikálna.
3. **Ale magnitúda je kontaminovaná.** Tá istá schéma, ktorá dala −0.011 tam,
   kde je pravda nula, dala 0.294 v konštantnom člene siete. Rovnaký rád.
   Logaritmický člen (0.1026) je od schémy oddeliteľný, konštanta nie.
   Pri `ln(Λ/m_e) = 51.5` je logaritmický príspevok 5.28 proti konštante
   0.294, teda kontaminácia je ~5 %. **Numericky to záver nemení** —
   14 rádov nezachráni 5 %. Ale znamená to, že publikovať 0.294 ako fyzikálne
   číslo (odporúčanie IV.A2) nie je možné bez kovariantnej separácie
   regulátora. To je práca navyše, ktorú A2 v tej podobe nemá.

### 2.2 „Známe sú tri mechanizmy" — sú aspoň päť

Audit v III.6 uvádza SUSY, Lorentzovsky invariantnú diskrétnosť a silne
viazaný RG fixný bod, a uzatvára: *„Nič také nie je známe, a nie preto, že
by sa nehľadalo."* To je nesprávne. Chýbajú minimálne dva publikované návrhy,
oba priamo v triede, ktorú audit definuje ako potrebnú.

**(e) Separácia škál EFT a LV — Belenchia, Gambassi, Liberati, JHEP 06 (2016)
049, arXiv:1601.06700.** Ukazujú, že oddelenie škály platnosti efektívnej
teórie `M` od škály narušenia Lorentza `Λ` **bráni** nízkoenergetickej
perkolácii. Toto je priama námietka proti III.5, pretože audit svoj integrál
vedie až po `k_max = 1/ℓ_cell` — teda predpokladá, že tá istá EFT platí až po
škálu siete. Ak SM ako EFT končí pri `M ≪ Λ`, smyčka nikdy nevidí oblasť, kde
je narušenie O(1), a indukovaný dim-4 koeficient je potlačený `(M/Λ)²`.

Kvantifikoval som, čo by to stálo (Λ = M_Pl, `g = Λ`):

```
limit 1e-16 (elektron)  ->  potrebne M/Lambda = 5.3e-08  ->  M = 6.5e11 GeV
limit 1e-19 (foton)     ->  potrebne M/Lambda = 1.7e-09  ->  M = 2.0e10 GeV
limit 1e-23 (UHECR)     ->  potrebne M/Lambda = 1.7e-11  ->  M = 2.0e08 GeV
```

**Toto je materiálne iná situácia než audit predkladá.** Audit v III.6(d)
píše: *„g/Λ < 1.7×10⁻⁹ — deväť rádov, pre každé pole a každú väzbu, bez
vysvetlenia."* Pri separácii škál je to **jedno číslo, raz, pre všetky polia a
všetky väzby**. Nová škála pri 10⁸–10¹⁰ GeV nie je exotická požiadavka;
seesaw aj PQ škála tam ležia. Nie je to zadarmo — je to netriviálny nový
predpoklad a jeho aplikovateľnosť na QCTS nie je preukázaná — ale je to
kvalitatívne iná cena než ladenie o deväť rádov po jednotlivých poliach.

**(f) Emergentná Lorentzova invariancia zo silnej dynamiky bez SUSY —
Bednik, Pujolàs, Sibiryakov, JHEP 11 (2013) 064, arXiv:1305.0011.** Cez
gauge/gravity korešpondenciu konštruujú silne viazané teórie, v ktorých sú
odchýlky od relativistického tvaru pri nízkych energiách **mocninovo
potlačené** pomerom IR/UV škál — bez supersymetrie.

To je presne trieda, ktorú audit v III.6(c) definuje ako potrebnú
(`Δ ~ O(1)`) a o ktorej píše, že nie je známa. Overil som auditovu
aritmetiku Δ a sedí (`Δ = 0.65 / 0.785 / 0.963` pre limity 10⁻¹⁶ / 10⁻¹⁹ /
10⁻²³). Auditova námietka *„sektor SM silne viazaný nie je"* je správna, ale
mieri vedľa: v tejto konštrukcii nemusí byť silne viazaný SM, stačí skrytý
sektor, na ktorý sa SM naviaže.

### 2.3 „C = 28 je presne anti-supersymetrický predpoklad" — prijaté, ale s únikom

Audit má pravdu, že `C = 56` dá `n_s` na 3.36σ a `C = 118` na 5.68σ (overené,
§1.4), takže SUSY vo forme, kde kapacita počíta všetky dof, je pre QCTS
zatvorená.

Únik existuje a treba ho priznať aj s cenou: kapacita by musela byť
**škálovo závislá** — počítať dof, ktoré sú v hre na tej škále, kde mechanizmus
delenia beží. Ak je SUSY exaktná pri škále bunky a zlomená pri TeV, potom
kapacita relevantná pre `δ` a kapacita relevantná pre `n_s` nie sú to isté
číslo. To by SUSY ochranu (Groot Nibbelink–Pospelov) sprístupnilo bez
zabitia `n_s`.

**Túto možnosť neponúkam ako obranu.** Ponúkam ju ako presne formulovaný dlh:
vyžaduje odvodiť, na ktorej škále sa kapacita číta, a §4.3 sama pripúšťa, že
*„prečo výlučne bozóny"* nie je vysvetlené. Bez toho odvodenia je to ad-hoc
záchrana číslom, čo `FS-C11` zakazuje. Ak sa nedá odvodiť, auditov záver
stojí v plnej sile.

---

## 3. Čo prijímam bez výhrad

| Nález | Sekcia auditu | Akcia |
|---|---|---|
| Chýba prvá stanica — LI stabilná voči smyčkám | V.9 | zavedená stanica `A0`, viď §6 |
| `X_K` nie je finitne parameterizovaný, §8 nemôže skončiť | V.7 | prijaté; `A0` má prednosť, potom SOS/CAD rez |
| Chybový rozpočet sa obnovuje delením problému | V.5 | prijaté; rozpočet presunutý na fyzikálnu otázku |
| Špecifikácia nahradila konštrukciu (9 úrovní blockeru) | V.4 | prijaté; `HRUBÝ_KANDIDÁT_FIRST` pravidlo |
| Päť záložných koľají je jeden chýbajúci objekt | V.8 | prijaté; stĺpec „spoločný objekt" v registri |
| Rozpor „Neprijaté" vs. publikované survival targets | V.10 | prijaté; P01/P04/P05/P06/P11 → `PRE_A3_DIAGNOSTIC` |
| `FS-C1` porušuje `FS-C11` toho istého ledgeru | V.6 | prijaté; `FS-C1` z tvrdého obalu do mäkkých cieľov |
| P10 je algebraická identita, nie predikcia | II.8 | prijaté; → `IDENTITY / NOT_A_PREDICTION` |
| P11 potrebuje FIRAS/gravitón dichotómiu | II.7 | prijaté |
| P02 potrebuje degeneráciu s α | II.6 | prijaté |
| §6.4 kóduje algebraickú identitu | II.4 | prijaté; §6.4 aj EA-047 preformulovať |
| Git tag `v3.18` neexistuje, všetky evidence odkazy sú 404 | VI.1 | prijaté; oprava je 5 minút |
| README tvrdí, čo v3.18 popiera | VI.2 | prijaté |
| „Externý audit" = LLM agent; konotácia klame | VI.3 | prijaté; premenovať na `independent LLM agent audit` |
| Falošné 16-miestne cifry | C2 | prijaté; zaokrúhliť na 4 platné číslice |
| Zmraziť verziovanie | C1 | prijaté |
| Trieda operácií bez contractu pre rešerš | V.11 | prijaté |
| Agentová vrstva nezachytí kategoriálnu chybu | VI.5–VI.7 | prijaté; viď §5 |

Osobitne prijímam **VI.7**. Je to najdôležitejšia veta celého auditu a platí
aj na tento dokument: aj tento je písaný jazykovým modelom, v rámci, ktorý mu
zadal autor. Že v ňom sedia tri chyby auditu (§1.6, §2.1), neznamená, že v ňom
nesedí štvrtá, ktorú ani jeden z nás nevidí, pretože ju obaja nevidíme z toho
istého dôvodu.

---

## 4. Kde audit podhodnotil vlastný nález

Dva body vo váš neprospech, ktoré audit uvádza slabšie, než si zaslúžia.

**4.1 Kontrast tree-level vs. smyčka je ešte ostrejší.** Audit ho pomenúva
v III.5(3): 8.7 rádov bezpečne v disperzii, 14–22 rádov nad limitmi v smyčke.
Nedopovedá dôsledok: **celý observačný program QCTS v Lorentzovom sektore je
postavený na veličine, ktorá nemôže rozhodnúť.** GRB testy, anizotropia,
birefringencia — všetko sú tree-level veličiny. Ak sa niekedy v budúcnosti
zlepšia o desať rádov, stále nepovedia nič o tom, čo teóriu zabíja. To patrí
do P10/P11 sekcie ako explicitná veta, nie ako implikácia.

**4.2 `ω_m(rek)` na 0.09σ je nevyužitý argument.** Audit ho v I.4 správne
označuje za elegantný a nevyužitý, ale sám ho zoslabuje na „0.5σ". Skutočná
hodnota je 0.09σ. Je to najlepšia jednotlivá zhoda modelu s dátami a je
netriviálna, pretože ju vyrába mechanizmus (popol vzniká neskoro), nie voľba.

---

## 5. K metodologickému záveru (VI.5–VI.9)

Prijímam diagnózu aj jej mechanizmus. Doplním jedno testovateľné kritérium,
ktoré z nej vyplýva a v audite nie je:

> **Kategoriálny nález nikdy nepríde ako odpoveď na otázku z balíka.**
> Príde iba ako odmietnutie tej otázky.

Z toho vyplýva prevádzkové pravidlo, ktoré zaraďujem do workflow (§6): každý
audítorský balík musí obsahovať povinnú položku
`FRAME_CHALLENGE: je táto otázka správne položená? Ak nie, ktorý upstream
výpočet ju robí bezpredmetnou?` — a odpoveď „otázka je správne položená" musí
byť zdôvodnená, nie predvolená. To korelované slepé miesto neodstráni. Ale
aspoň otvorí kanál, ktorým kategoriálny nález môže prísť; dnes taký kanál
v procese neexistuje.

**Odporúčanie VI.9 (jeden e-mail jednému kozmológovi) prijímam ako najvyššiu
prioritu po A0.** S jednou zmenou: navrhované otázky sú dve a rozhodujú
rôzne veci. Odporúčam poslať ich **dvom rôznym ľuďom**, pretože sú z rôznych
odborov:

- *„Je `S₈ ∝ 1/h` v tejto triede IDE modelov vynútené, alebo mi niečo uniká?"*
  → kozmológ (CEICO Praha, ako navrhuje C4).
- *„Generuje priestorová diskrétnosť dim-4 narušenie Lorentza cez smyčky, alebo
  to niečo chráni — a je Belenchia et al. 2016 aplikovateľné, ak je preferovaný
  rám ontologický, nie regulátorový?"*
  → fenomenológ kvantovej gravitácie (SISSA, Liberatiho skupina — je to jeho
  vlastný výsledok).

Druhá otázka je pre program dôležitejšia a je odpovedateľná za dvadsať minút
človekom, ktorý to robí.

---

## 6. Autoritatívne delty, ktoré z tejto odpovede vyplývajú

Zámerne minimálny počet artefaktov. Audit správne diagnostikuje, že choroba
tohto projektu je množenie dokumentov; odpovedať naň pätnástimi novými by bolo
sebavyvrátenie.

| # | Delta | Súbor | Trieda |
|---|---|---|---|
| 1 | Zavedená stanica `A0` s koľajami `A0-K1..K5` | `tracks/A0/00_STATION.md` (nový) | proces + fyzika |
| 2 | `A0` routy v registri ciest | `tracks/00_ROUTE_REGISTER.md` | proces |
| 3 | Stĺpec „spoločný objekt s K4"; upstream blok od `A0` | `tracks/A1/A1K1/A2/00_TRACK_REGISTER.md` | proces |
| 4 | `FS-C1` z tvrdého obalu do mäkkých cieľov; `FS-C13` finitný rez | `tracks/A1/A1K1/A2/00_CONSTRAINT_FEASIBILITY_LEDGER.md` | fyzika |
| 5 | Chybový rozpočet na fyzikálnu otázku; `NO_GO_BY_EXHAUSTION`; trieda operácií bez contractu; `FRAME_CHALLENGE`; `HRUBÝ_KANDIDÁT_FIRST`; premenovanie „external audit" | `AGENTS.md`, `tracks/00_PROJECT_OPERATING_SYSTEM.md` | proces |
| 6 | P01/P04/P05/P06/P11 → `PRE_A3_DIAGNOSTIC`; P10 → `IDENTITY` | `A2K4/00_A2K4_EXECUTION_MAP_SK.md` + release tabuľka | fyzika |
| 7 | Revidovaný plán a poradie prác | `tracks/00_POST_AUDIT_PLAN_2026-08-14_SK.md` (nový) | proces |

Klasifikácia nálezu podľa §6 `AGENTS.md`: **`S4_PARENT_THEORY_IMPACT`**.
Nález III.5 je dosiahnuteľný na úroveň rodičovských axióm (priestorová
diskrétnosť s globálnym časom), nie iba na A2-K4. Preto:

```
CLAIM_QUARANTINE:  vsetky A3-typove observably (P01, P04, P05, P06, P11)
EARLIEST_INVALID_CHECKPOINT: ziadny existujuci - chyba upstream stanica
TRACK_IDENTITY_GATE: UNRESOLVED_AUTHOR_DECISION
ROZHODNUTIE MARTINA: A0 sa rozhodne pred akoukolvek dalsou kozmologickou pracou
```

---

## 7. Poďakovanie a jedna žiadosť

Audit je najlepší vstup, aký tento projekt dostal. Časť III je práca, ktorú
sme si nevedeli zadať, pretože sme nevedeli, že ju treba zadať — a to je presne
definícia kategoriálneho nálezu. Časť V.1 (tri priznané vlastné chyby na
začiatku) je dôvod, prečo je zvyšok čitateľný.

Žiadosť: prosím o revíziu troch bodov z §1.6 a §2.1–2.2 pred tým, než sa
akýkoľvek výsledok z Časti III použije v samostatnej publikácii (IV.A2).
Konkrétne:

1. `Ω_cell = c/(2.169 ℓ₀)`, nie `2.117`.
2. Dodatok A1: `/1091**3`, nie `*1091**3`.
3. Dôsledok III.5(1) preformulovať na „preferovaný priestorový cutoff", nie
   „konečný počet dof na objem" — inak je v rozpore s III.6(b).
4. Do III.6 doplniť Belenchia et al. 2016 a Bednik et al. 2013 a povedať,
   prečo pre QCTS nestačia (alebo že stačia).

Bod 3 a 4 sú podmienkou publikovateľnosti perkolačného výsledku. Recenzent,
ktorý si všimne rozpor medzi III.5(1) a III.6(b) sám, stratí dôveru k celej
Časti III — čo je presne argument, ktorý audit používa v IV.A3.

---

## Dodatok — reprodukovateľnosť tejto odpovede

Prostredie: Python 3.12, numpy 2.4.4, scipy 1.17.1.
Skripty: `verify_background.py`, `verify_spectra_and_windows.py`,
`verify_network_moments.py`, `verify_loop_nullchecks.py`,
`verify_escape_scales.py`.
Raw výstupy: `01_VERIFICATION_LOG.md`.
Externé zdroje overené 14. 8. 2026: arXiv:2503.19441 (KiDS-Legacy),
arXiv:1601.06700 (Belenchia–Gambassi–Liberati), arXiv:1305.0011
(Bednik–Pujolàs–Sibiryakov).

*Tento dokument je návrh odpovede. Nemení žiadny autoritatívny stav, hĺbku ani
skóre. Autoritatívne zmeny sú v deltách §6 a podliehajú rozhodnutiu autora.*
