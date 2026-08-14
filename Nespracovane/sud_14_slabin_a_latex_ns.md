# SÚD NAD 14 SLABINAMI + VERDIKT NAD LaTeX DERIVÁCIOU n_s
## Triedenie externého zoznamu a kritický nález v navrhovanej derivácii

**Dátum:** 11. júl 2026
**Vstupy:** (1) zoznam 14 slabín, (2) LaTeX sekcia „Fyzikálne odvodenie n_s"
**Hlavný výsledok:** zoznam slabín obsahuje 3 fakticky nesprávne námietky,
5 už registrovaných a 3 skutočne akčné body. LaTeX derivácia obsahuje
**skrytú nekonzistenciu škálovania T–H, ktorá by po prijatí zdvihla r
z 10⁻²⁰ na ~2×10⁻⁵ a prerazila náš vlastný registrovaný strop o päť
rádov.** V tejto podobe sa do dokumentov vkladať NESMIE.

---

# ČASŤ I — TRIEDENIE 14 SLABÍN

## I.A Fakticky nesprávne námietky (zamietnuté s číslom)

**#7 „Relikt je nekompatibilný s infláciou; Planck/ACT/SPT/LIGO ho nevidia."**
Námietka si protirečí: model infláciu NEMÁ — prežitie reliktu je jeho
registrovaný diskriminátor, nie chyba. „Planck ho nevidí": Planck meria
N_eff = 2.99 ± 0.17; model dáva 3.10 → **0.65σ, plne kompatibilné** —
súčasné dáta relikt nevedia rozlíšiť, preto rozhodne až CMB-S4 (to je
zmysel riadku 1 tabuľky). LIGO: relikt má vrchol 53 GHz a teplotu 0.9 K —
o ~13 rádov mimo LIGO pásma aj citlivosti (v CSV priznané: „today
undetectable, Dyson bound"). Námietka nečítala registráciu.

**#9 „H₀ = 66.4 je nekompatibilné s BAO."**
Námietka tvrdí, že zníženie H₀ vyžaduje zmenu r_s — ale pipeline presne
toto rešpektuje: kotví θ* (akustickú škálu), drží r_s ≈ 144.3 Mpc
a H₀ = 66.4 vychádza zo ZMENENEJ neskorej expanzie (w = −1+δ + para)
pri fixnej ranej fyzike. To je konštrukčne BAO-konzistentný postup.
Model netvrdí, že rieši H₀ tenziu zdvihnutím — stavia na systematiku
rebríka (kill: lokálne H₀ ≥ 72 bez systematiky = smrť). Námietka
v kategorickej podobe zamietnutá; jej KONŠTRUKTÍVNE jadro preberám
ako nový krok B (plný BAO dištančný test, časť III).

**#12 „Entanglement bez signálu je logický rozpor."**
Učebnicová chyba. No-communication theorem: previazanosť nesie
KORELÁCIE, nie signál — lokálne merania na jednej strane nedokážu
preniesť informáciu, hoci spoločná štatistika je korelovaná. Presne
túto vlastnosť QM V-vrstva kopíruje (a #12 v registri + veta VS-1 ju
vynucujú). Keby platila logika námietky, bola by rozporná samotná
kvantová mechanika. Zamietnuté bez náhrady.

## I.B Známe a registrované (námietka neprináša nič nové)

**#8 S₈:** registrované ako najslabší front (2.4–3.3σ), priznané
v README aj CSV, kill condition definovaná. Oponent tu cituje našu
vlastnú dokumentáciu späť na nás.
**#10 GR / #11 QFT:** známe steny (Z1 boost — historicky najtvrdší
problém; QFT emergencia — dlhodobé lešenie). Teória ich neignoruje,
má ich v registri stien; Newton už emergoval (R² = 0.9991). Poctivá
odpoveď oponentovi: áno, toto je program, nie hotová veta.
**#13, #14:** estetické duplikáty #1/#3 („prečo práve takto") bez
nového obsahu. Odpoveďou je práve register popravených alternatív —
teória nevyberá „takto" svojvoľne, ale súdom (n_s: nekorelovaný šum
→ n_s = 4 †, kritický bod → ~2 †, rovnodelenie → mimo okna †).

## I.C Legitímne s existujúcou čiastočnou obranou

**#1 δ = 1/(⟨k⟩ + C) „numerológia":** obrana existuje, ale treba ju
vytiahnuť na svetlo. δ nie je ľubovoľná kombinácia — je to réžia
delenia = 1/(celkový počet väzieb, ktoré bunka pri delení prestavuje):
k povrchových + n_V vnútorných. Alternatívy 1/k, 1/C, 1/(kC) nie sú
rovnocenné čítania — nezodpovedajú „prestavuješ VŠETKY svoje väzby".
A kľúčové: **VCM to meria, nie postuluje** — Q2 (δ_sim = ⟨1/k⟩ bez
V-spojov) a Q9 (n_V ≈ 5–10 dáva δ ∈ [0.04, 0.05], škáluje s k + n_V).
Akčný bod: sformulovať to v dokumentácii ako explicitné pravidlo
s odkazom na obe merania — dnes je to roztrúsené.
**#2 C = 28:** Q16 má verdikt — alternatívy (g* = 106.75, fermióny,
reprezentácie) popravené dátami 2.6–6.8σ s priznaným look-elsewhere;
fázová námietka („počet stavov závisí od fázy") je vyriešená pascou M8
(symetrická fáza aj Goldstonovo účtovníctvo dávajú 28; topológia
zamknutá pri genéze atraktorom vena). Zostávajúca poctivá diera:
DYNAMICKÝ dôvod, prečo kapacitu sýtia práve nosiče (bozóny) a nie
náklad (fermióny) — držať ako otvorené dorazenie Q16b.

## I.D Legitímne a AKČNÉ (nové kroky)

**#4 + #5 „rovnice V1 nie sú z akcie / GR nepozná réžiu" → krok A.**
Toto sa dá zabiť jednou stranou, lebo V1 je presne FRW limita
štandardnej kovariantnej triedy interagujúcej tmavej energie:

    ∇_μ T^{μν}_f = −Q u^ν,   ∇_μ T^{μν}_m = +Q u^ν,   Q = λ H₀ ρ_f
    w_f = −1 + δ

Súčet dáva ∇_μ T^{μν}_tot = 0 identicky → Bianchi splnená, nie
deklarovaná. Presne táto trieda (Q = Γρ_DE, Γ konštantné) je v
literatúre interagujúcej DE štandardne študovaná. δ a λ sú v tejto
vrstve fenomenologické parametre efektívneho popisu — ich MIKROSKOPICKÝ
pôvod (bunky, réžia) je interpretácia pod tým, tak ako je kinetická
teória pod Navierom–Stokesom. Poctivá poznámka, ktorú treba pripísať:
pipeline predpokladá výmenu energie bez prenosu hybnosti do porúch
(geodetický transfer) — rovnice rastu ostávajú štandardné; toto je
voľba, ktorú treba v dokumente vysloviť nahlas.

**#6 „palivo → hmota bez kvantových čísel" → registrovať.**
Legitímna diera: mechanizmus nukleácie nemá mikrofyziku (baryónové
číslo, stabilita protónu). Návrh: registrovať ako otvorenú stenu
(W5: mikrofyzika nukleácie) — rovnaká kategória ako Z1. Nie je to
smrteľné (aj ΛCDM baryogenézu len parametrizuje), ale nesmie sa
tváriť ako vyriešené.

**#9-konštruktívne → krok B: plný BAO dištančný test.**
Vypočítať D_M(z)/r_s a D_H(z)/r_s modelu na efektívnych červených
posuvoch DESI DR2 a spraviť χ² proti publikovaným bodom. Pipeline má
všetko potrebné (pozadie + r_s); je to popoludnie práce a zavrie
námietku #9 číslom namiesto argumentu.

---

# ČASŤ II — VERDIKT NAD LaTeX DERIVÁCIOU n_s

## II.1 Čo je správne

- Algebra w = −1+δ ⇒ φ̇²/U = δ (na vedúci rád; presne φ̇² = δU/(1−δ/2)) ✓
- ε = (3/2)(1+w) = (3/2)δ — štandardná FRW identita ✓
- Reťaz P ∝ H ⇒ n_s − 1 ≈ −ε cez k = aH ✓ (na prvý rád, pozri II.4)
- Zámer (dať pozadiu kovariantný efektívny popis poľom) je správny
  a presne odpovedá na slabinu #3.

## II.2 Čo je ozdoba, nie odvodenie

Akcia S[φ] je v texte DEKORATÍVNA: podmienka w = −1+δ sa do poľa
VKLADÁ rukou („požadujeme"), žiadny potenciál U(φ) ju negeneruje.
Oponent to uvidí za desať sekúnd. **Oprava je lacná a robí to
odvodením naozaj:** exponenciálny potenciál

    U(φ) = U₀ · exp(−√(3δ) · φ/M_P)

má presné škálovacie riešenie s konštantným w = −1 + δ a ε = (3/2)δ
(štandardný výsledok pre exponenciály: w = −1 + λ²/3 pri U ∝ e^{−λφ/M_P};
λ = √(3δ) ≈ 0.262). Jedna rovnica navyše — a veta „dôsledok stavovej
rovnice, nie definícia" začne byť pravdivá.

## II.3 KRITICKÝ NÁLEZ: škálovanie T–H protirečí A13 a rozbíja r

LaTeX používa: Φ ∝ T/T_P a T ∝ √H.
A13 (registrované) používa: amplitúda ∝ √(T/T_P) a T ∝ H (krok 3,
Hagedorn, m = ½).

Obe kombinácie dajú P ∝ H (preto si to nik nevšimne na n_s!) — ale
sú to RÔZNE fyzikálne mechanizmy a normalizácia amplitúdy A_s z nich
vytiahne rôzne teploty zamrznutia:

    A13:   A_s ⇒ T_f ~ 2–7×10⁹ GeV   (registrované)
    LaTeX: A_s ⇒ T_f = √A_s·T_P/√γ ≈ 5.6×10¹⁴ GeV  (pri γ = 1)

A teplota zamrznutia kŕmi tenzorový odhad (A14: Δ_h² ≈ 0.4·H·T):

    A13 škálovanie:   r = 8×10⁻²² … 4×10⁻²⁰   ✓ sedí s registrovaným
    LaTeX škálovanie: r ≈ 1.8×10⁻⁵            ✗ preráža registrovaný
                                                strop r < 10⁻¹⁰ o 5 rádov

Záchrana cez konštantu by vyžadovala γ ~ 10¹⁰ — to už nie je „O(1)
plošná konštanta", to je nový nevysvetlený veľký parameter. **Keby sa
LaTeX v tejto podobe vložil do dokumentov, teória by potichu
falzifikovala vlastnú registrovanú predpoveď r.** Toto je presne ten
typ chyby, ktorý sa chytá pred publikáciou alebo nikdy.

**Oprava:** sekciu 3.3 LaTeXu prepísať na A13 krok 3:
Φ ∝ √(T/T_P) (nasýtený kanál: δE ∝ √(T·E_P)·√N, N ∝ (R/l_P)²)
a T ∝ H pri výstupe módov. Výsledok P ∝ H aj n_s − 1 = −(3/2)δ
ostávajú; T_f ostáva 10⁹⁻¹⁰ GeV; r ostáva 10⁻²¹⁻¹⁹.

**Bonus — audit r týmto UZAVRETÝ:** nezávislý prepočet A14 vzorca
s registrovaným T_f reprodukuje r = 8×10⁻²²–4×10⁻²⁰, v zhode
s dokumentom („realisticky 10⁻²¹–10⁻¹⁹"). Riadok 3 CSV má krytie.

## II.4 Menší nález: druhý rád v ε

Presný vzťah je n_s − 1 = −ε/(1−ε) = −ε − ε² − …
S ε = 0.03446: n_s = 0.96432 namiesto 0.96554 — **posun −0.0012,
teda ~0.75× deklarovanej neistoty ±0.0016.** Pri presnosti, akou sa
tabuľka chváli (CMB-S4 σ ≈ 0.002), to nie je zanedbateľné zaokrúhlenie.
Možnosti: (a) zdokumentovať skrátenie na prvý rád a rozšíriť teoretickú
neistotu, (b) zaviesť druhý rád do registrovanej hodnoty pri ďalšej
verzii — ale POZOR, zmena registrovanej predpovede je vážny krok
a musí byť verzálne priznaná, nie ticho prepísaná. Odporúčam (a) teraz,
(b) len s explicitným záznamom v changelogu.

## II.5 Kladná bodka: kvantový kanál je legálne zanedbaný

Zavedenie poľa φ prináša povinnú otázku: prečo jeho kvantové vákuové
fluktuácie (P ∝ H²/(8π²εM_P²)) nedominujú? Prepočet: pri T_f ~ 5×10⁹ GeV
je P_quantum ~ 10⁻³⁸, teda **29 rádov pod A_s** — termálny kanál
dominuje legálne. Toto do LaTeXu PRIDAŤ ako jednu vetu: predbehne
otázku, ktorú by položil každý kozmológ.

## II.6 Preformulovať záver LaTeXu

„Takto je tilt odvodený z akcie a dynamiky, nie z voľnej numerologickej
konštrukcie" — PRESILENÉ. Akcia kryje pozadie (po oprave II.2); spektrum
naďalej stojí na termálno-holografickom mechanizme s meraným plošným
zákonom. A δ samotné ostáva z 1/(⟨k⟩+C) — LaTeX rieši slabinu #3,
nie #1. Poctivá formulácia: „pozadie má kovariantný efektívny popis
poľom; spektrum plynie z termálnych fluktuácií nasýtenej vrstvy,
ktorých plošná kapacita je v modeli meraná (p = 1.97)."

---

# ČASŤ III — KROKY

| # | Krok | Zavrie | Náklad |
|---|------|--------|--------|
| A | Kovariantné zobrazenie V1 (interagujúca DE, Q = λH₀ρ_f) — 1 strana do dokumentu 04 + poznámka o geodetickom transfere | slabiny #4, #5 | hodiny |
| B | BAO dištančný test: D_M/r_s, D_H/r_s na DESI DR2 bodoch, χ² | slabina #9 číslom | popoludnie |
| C | LaTeX: oprava škálovania na A13 krok 3 + exponenciálny potenciál + veta o kvantovom kanáli + preformulovaný záver + poznámka o ε² | slabina #3 poctivo | hodiny |
| D | Register: W5 (mikrofyzika nukleácie — otvorená stena), Q16b (prečo nosiče), zamietnutia #7/#9/#12 s číslami | evidencia | minúty |
| E | Rozhodnutie o ε² v registrovanej n_s (možnosť a/b z II.4) | konzistencia tabuľky | tvoje rozhodnutie |

---

## Kľúčová veta

Zoznam štrnástich slabín má tri námietky, ktoré nevedia čítať vlastnú
fyziku (relikt je diskriminátor a nie chyba, θ* kotva BAO rešpektuje,
no-communication theorem platí aj pre V-vrstvu), päť, ktoré len citujú
náš vlastný register späť na nás — ale navrhovaná LaTeX „záchrana" n_s
je nebezpečnejšia než celý zoznam: zamieňa škálovanie amplitúdy tak,
že by potichu zdvihla r o pätnásť rádov nad registrovaný strop, a preto
platí staré pravidlo tohto projektu — každý dar sa pred vložením do
dokumentov najprv súdi.
