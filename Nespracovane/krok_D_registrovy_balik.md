# KROK D — REGISTROVÝ BALÍK (sedenia 10.–11. júl 2026)
## Súhrn všetkých položiek na zápis do registrov pred zastávkou v3.18

**Účel:** jeden dokument, z ktorého sa aktualizujú registre v dokumente 05
(otázky, mŕtve cesty, steny, stávky) a changelog. Každá položka má dôvod
a odkaz na verdiktový dokument.

---

## D1. Zamietnuté externé tvrdenia (nová sekcia registra — navrhujem
označenie E#, aby sa neplietli s vlastnými mŕtvymi cestami #)

| E# | tvrdenie (zdroj) | dôvod zamietnutia | dokument |
|---|---|---|---|
| E1 | chyba znamienka v rovniciach rastu (Gemini) | algebra = učebnicový tvar; Heath exakt 0.014 %; kontrafaktuál σ₈ ≈ 24 | verdikt_O1 |
| E2 | gravitónový relikt „nekompatibilný, Planck ho nevidí" (Gemini/Copilot #7) | model infláciu nemá — relikt je diskriminátor; Planck N_eff 2.99 ± 0.17 vs 3.10 = 0.65σ; LIGO mimo pásma o ~13 rádov | sud_14_slabin |
| E3 | „H₀ = 66.4 nekompatibilné s BAO" (#9) | priamy test 13 bodov DESI DR2: Δχ²(model − ΛCDM) = −0.1 pri identickom θ* kotvení; r_d = 146.71 Mpc | verdikt_B |
| E4 | „entanglement bez signálu = logický rozpor" (#12) | no-communication theorem; korelácie ≠ signál; inak by bola rozporná QM sama | sud_14_slabin |

Poznámka: slabiny #8, #10, #11, #13, #14 sa nezamietajú ani neregistrujú
nanovo — sú to citácie nášho vlastného registra (S₈ front, steny Z1/QFT,
estetika). Odpoveď na ne = odkaz na register.

## D2. Mŕtve cesty (pokračovanie číslovania #)

| # | čítanie | zabité čím | dokument |
|---|---|---|---|
| #21 | škálovanie fluktuácií Φ ∝ T & T ∝ √H (návrh LaTeX v1) | vlastným r: normalizácia A_s vynúti T_f ≈ 5.6×10¹⁴ GeV → r ≈ 2×10⁻⁵, preráža registrovaný strop r < 10⁻¹⁰ o 5 rádov; záchrana by chcela γ ~ 10¹⁰ | sud_14_slabin II.3; derivacia_ns_opravena_C §6.6 |

## D3. Nové a aktualizované otázky

| Q | znenie | stav | poznámka |
|---|---|---|---|
| Q11e | Odvodiť T ∝ H pri výstupe módov z mikrodynamiky V-vrstvy | OTVORENÁ, váha 3 | jediný neodvodený krok derivácie n_s; JEDNOBODOVÁ PORUCHA: nesie n_s, T_f aj r súčasne — priorita po zastávke |
| Q16b | Dynamický dôvod, prečo kapacitu sýtia nosiče (bozóny), nie náklad (fermióny) | OTVORENÁ, váha 2 | Q16 verdikt (poprava alternatív 2.6–6.8σ) platí; toto je dorazenie „prečo", nie „či" |
| Q17 | Trojbodová štatistika (f_NL) z V-termalizácie | PRVÝ PRECHOD ✓ | S₃ = 2/√C_V ⇒ f_NL^intr ~ 10⁻¹⁵; podlaha jedných hodín ⇒ f_NL^local ≈ +0.01–0.05; kritérium (≲5 prežíva / ≥10 smrť) splnené s rezervou ~10²; ČAKÁ: druhý rád (tvar, znamienko) |

## D4. Nové steny

| W | znenie | poznámka |
|---|---|---|
| W5 | Mikrofyzika nukleácie: kvantové čísla vytvorenej hmoty (baryónové/leptónové číslo, stabilita) | legitímna diera zo slabiny #6; rovnaká kategória ako Z1 — program, nie okamžitá úloha; nesmie sa tváriť ako vyriešené |

## D5. Nové povrchové stopy / mini-predpovede (kandidáti do tabuľky
pri ďalšej verzii — až po dorazení, nie teraz)

| stopa | hodnota | pôvod | rozhodne |
|---|---|---|---|
| beh spektra α_s | 0 (presne, na ráde derivácie) | exponenciálny atraktor: ε konštantné | CMB-S4 (Planck dnes: −0.0045 ± 0.0067 ✓) |
| RSD deformácia z prenosu hybnosti | žiadna nad rámec pozadia | geodetický prenos Q^ν = Q u^ν (A16.4) | RSD analýzy DESI/Euclid |
| f_NL^local | +0.01…0.05 | Q17 (po druhom ráde) | SPHEREx / budúce LSS |

## D6. Fronta dokumentačných opráv (tvoje commity)

1. skript 09: δ 0.03 → 0.02297 (+ komentár „derived: 1/(15.54+28)");
   S₈ kotva v χ² 0.759 ± 0.024 → 0.815 ± 0.019 (KiDS-Legacy) alebo
   tlačiť obe s poznámkou o dátovom stave
2. GitHub README: BibTeX na konceptový DOI („Cite all versions"),
   opraviť rozbitú zátvorku v url
3. Zenodo popis záznamu: „no B-modes, ever" → „no primordial B-modes"
   (metadáta, bez novej verzie)
4. dokument 04/04b: vložiť A16 (SK+EN) a opravenú LaTeX sekciu n_s
   (po tvojom prečítaní); pri vkladaní zmazať značku konca fragmentu

## D7. Rozhodnutie E (otvorené — tvoje)

Presný sklon je n_s − 1 = −ε/(1−ε) ⇒ n_s = 0.9643 (posun −0.0012
vs registrovaných 0.9656 ± 0.0016).
(a) ponechať prvý rád, zdokumentovať skrátenie ako súčasť teoretickej
    neistoty (odporúčam teraz — nulový zásah do registrácie), alebo
(b) verzálne zaviesť druhý rád pri ďalšej verzii s explicitným
    changelogom (zmena registrovanej predpovede = vážny krok).
Poznámka pre rozhodovanie: kill condition „n_s mimo 0.9656 ± 0.004"
pokrýva obe hodnoty — smrť modelu sa voľbou (a)/(b) nemení.

## D8. Stav programu pred zastávkou

    [x] A  kovariantné zobrazenie (A16 SK+EN)
    [x] B  BAO test (verdikt: E3)
    [x] C  oprava LaTeX derivácie n_s
    [x] D  tento balík
    [ ] E  tvoje rozhodnutie (D7)
    [ ] opravy D6 (tvoje commity)
    [ ] mapa závislostí (ja)
    [ ] ZASTÁVKA: tvoje hĺbkové štúdium + obrátená obhajoba

---

## Kľúčová veta

Za dve sedenia pribudli do cintorína štyri cudzie tvrdenia a jedno
vlastné čítanie, do otázok tri nové položky a do stien jedna — a to je
presne pomer, aký má zdravý výskum mať: viac hrobov cudzích omylov než
vlastných, ale žiadny týždeň bez aspoň jedného vlastného.
