# Q99 / C7-G8 — predregistrácia plnej Boltzmannovej hierarchie

**Dátum zmrazenia:** 2026-07-15  
**Rodič:** `A1-K1 → A2-K4 → C7.7c-K7`  
**Vstupný stav:** `K7d G0–G7 PASS; support/WBS 90/100`  
**Stav pri zmrazení:** `PREREGISTERED / NOT RUN`  
**Opravný rozpočet:** prvá implementácia + najviac dve technické opravy

**Vykonávacia aktualizácia 2026-07-15:** `SCREEN-S0+S1 PASS` cez
RUN-002/skript 233 po technickom RUN-001 PF-034 a `SCREEN-S2 PASS` cez
RUN-003/skript 222 a `SCREEN-S3 PASS` cez RUN-004/skript 223. Skóre zostáva
`0`; FULL nebežal. Autoritatívny aktuálny stav je v `00_MANIFEST.md`.

## 1. Otázka a hranica tvrdenia

G8 má rozhodnúť, či K7 zostáva konzistentná po nahradení dnešnej
perfect-fluid/tight-coupling redukcie plnou fotónovou teplotnou,
polarizačnou a kolektívnou free-streaming hierarchiou so samostatnou
baryónovou rýchlosťou, Thomsonovým rozptylom a štandardnou rekombináciou.

Skorý `SCREEN` môže povoliť pokračovanie, ale **nemôže udeliť G8 PASS ani
zvýšiť support nad 90/100**. G8 PASS vyžaduje aj `FULL` backend na presnom
K4 backgrounde najmenej cez posledný rozptyl.

## 2. Zmrazená architektúra

1. Autoritatívnym zdrojom štandardných koeficientov je lokálny CAMB 1.6.6
   (`camb.symbolic`) a už auditované skripty 73, 74 a 76.
2. Skompilovaná lokálna `cambdll.dll` nie je modifikovateľný zdroj K4.
   Route-local Python operátor preto slúži ako auditovateľná referenčná
   implementácia rovnakých rovníc. Plný produkčný backend musí používať
   zdrojovo zostaviteľný CAMB/CLASS alebo ekvivalentný backend s tým istým
   registrovaným operátorom; nejde o novú fyzikálnu koľaj.
3. Zachová sa projektovaná báza `D,M`. Free-streaming hustota a rýchlosť sa
   rekonštruujú algebraicky, aby sa nevrátila katastrofická cancellation
   K1–K6.
4. Pribudnú samostatné `U_b`, fotónové teplotné multipóly `J_2..J_lmax`,
   skalárne polarizačné multipóly `E_2..E_lmax` a kolektívne
   free-streaming multipóly `G_2..G_lmax`. Presné aliasy `J_2=pi_g` a
   `G_2=pi_r` sa nesmú zameniť.
5. Pre vyššie multipóly sa použije škálovanie kompatibilné s K7:
   `L_l=(k/Hconf)^(l-2) F_l`. Všeobecná bezkolízna rekurencia musí pre
   `l=3,4` presne vrátiť dnešné K7 rovnice.
6. Nepridáva sa nový fyzikálny parameter. Atómové konštanty, Thomsonov
   prierez a ionizačná kinetika zostávajú štandardné; mení sa iba vstupný
   K4 background.

Pri spoločnom `lmax=L` má projektovaný CAMB `J/E/G` screen
`3L+8` stavov: 32 pre `L=8`, 44 pre `L=12` a 56 pre `L=16`.

## 3. Pevné úrovne jedného G8 balíka

| Úroveň | Obsah | Bodový účinok |
|---|---|---:|
| `SCREEN-S0` | provenance, exact CAMB koeficienty, register stavov, aliasy | 0 |
| `SCREEN-S1` | presný K7 redukčný limit, collision momentum ledger, nulový limit | 0 |
| `SCREEN-S2` | ohraničená skorá evolúcia a TCA/direct overlap | 0 |
| `SCREEN-S3` | zmrazený sweep `lmax=8,12,16` a closure konvergencia | 0 |
| `FULL` | presný K4 background, rekombinácia, úplná hierarchia a constrainty | +5 iba pri PASS |

Nevznikne nový `K7e`, `K7f` ani ďalší fyzikálny suffix. Parameter cases sú
konfigurácie/JSON jedného runnera.

## 4. Pred prvým Python behom — očakávanie

Prvý beh zopakuje iba exact coefficient audit skriptu 76.

- očakávanie: 22/22 symbolických rezíduí je presne `0`;
- prijateľný výsledok: iba úplný PASS;
- PASS: potvrdí dostupnosť zmrazeného CAMB 1.6.6 a dovolí vytvoriť skript
  221; nezmení skóre ani fyzikálny stav;
- mismatch: `STOP_G8_IMPLEMENTATION_MAPPING`, nie smrť K7;
- import/timeout: technický `REVIEW`, výber zdrojového backendu alebo oprava
  prostredia v rámci opravného rozpočtu.

Interný limit je 10 s, externý procesný limit 15 s. Nesmie sa spúšťať bez
oboch limitov.

## 5. SCREEN PASS/STOP kritériá

Všetky nasledujúce podmienky musia byť pred behom implementované v exporte:

1. exact CAMB rezíduá a aliasy sú nulové;
2. zoznam, poradie a počet stavov sú presné pre každý `lmax`;
3. pri `U_b=U_gamma`, nulovom fotónovom šmyku/polarizácii a registrovanom
   `L5=0` limite sa spodné rovnice algebraicky redukujú na K7;
4. Thomsonove členy presne zachovávajú celkovú fotónovo-baryónovú hybnosť;
5. interakčný nulový limit nepridá mód ani zdroj;
6. všetky stavy/RHS sú konečné a ostanú pod safety cap;
7. TCA a priama hierarchia v spoločnom overlap bode súhlasia v
   projektovaných nízkych momentoch do `1e-4`;
8. `lmax=12` proti `16`: normalizovaný endpoint rozdiel nízkych momentov
   `<=1e-5`; `lmax=8` proti `12` musí byť `<=5e-4` alebo sa musí zlepšiť
   aspoň faktorom 4 voči `12→16`;
9. tail/low-moment pomer na poslednom priamom checkpoint-e je `<=1e-6`;
10. Einsteinove ledgery použijú zmiešanú hranicu
    `1e-12 + 1e-8*term_norm` a všetky checkpointy prejdú.

Nulový truncation na `lmax` nie je autoritatívny closure. Použije sa
štandardný asymptotický/backend closure; nulový closure smie byť iba
diagnostická citlivostná varianta pri `lmax=16`.

## 6. FULL PASS/STOP kritériá

G8 PASS vyžaduje súčasne:

1. štandardnú atómovú kinetiku vyhodnotenú na presnom K4 backgrounde;
2. konečnú a nezápornú ionizáciu/opacitu/visibility a normalizáciu
   visibility v intervale `0.95–1.05`;
3. zdokumentovaný TCA switch a stabilný overlap;
4. konvergenciu backend accuracy a multipólového chvosta;
5. nulový referenčný beh konzistentný so zmrazeným CAMB referenčným
   rozhraním v deklarovaných výstupoch;
6. plné Einsteinove constrainty bez fail-open kontrol;
7. žiadny potvrdený nový rastúci gauge-invariantný mód.

Fyzikálny STOP K7/A2-K4 sa smie vydať iba pri reprodukovateľnej
nestabilite, nekonvergentnej hierarchii alebo porušení constraintov po
platnej numerike a nezávislom potvrdení. Timeout, import, kompilácia,
parser, škálovanie alebo chybný marker sú iba technické REVIEW.

## 7. Očakávaný fyzikálny obraz

Na skorom intervale K7 je `k/Hconf << 1` a Thomsonova opacity veľká.
Očakávame preto potlačený fotónový šmyk/polarizáciu, klesajúci vyšší
free-streaming chvost a zmenu projektovaných nízkych momentov voči K7 menšiu
než `1e-3` ich predregistrovanej obálky pri `x=-18`. Toto je očakávanie,
nie PASS podmienka ani výsledok. Ak sa zmení, audit musí uviesť konkrétny
dominantný člen a obhájiť, prečo je nové očakávanie fyzikálne správne.

Pre FULL časť sa kladný výsledok nepredpokladá: rekombinácia a neskorší
prechod môžu odhaliť nový konflikt. Dáta S8/CMB sa neotvoria pred G8 PASS.

## 8. Runtime, bezpečnosť a artefakty

- každý Python proces: interný deadline a externý timeout;
- exact/structural screen: `10 s` interne, `15 s` externe;
- jedna evolučná case: najviac `45 s` interne, `55 s` externe;
- jedna case na proces, žiadne neobmedzené agregované behy;
- povinný RHS-call cap, safety cap, immutable JSON a SHA-256 provenance;
- pred každým behom samostatný Markdown očakávaní; zmena očakávania sa
  zdôvodní pred novým behom;
- nefunkčné verzie sa nemažú, idú do `HISTORY` s dôvodom obmedzenia.

## 9. Skriptový rozpočet

| Skript | Úloha |
|---:|---|
| 221 | S0+S1: provenance, exact coefficient a K7 reduction audit |
| 222 | S2: bounded TCA/direct operator screen |
| 223 | S3: single-case `lmax` runner |
| 224 | S3/FULL konfigurácie a konvergenčný agregát |
| 225 | G8 finálny gate/audit export |

Opravy patria do rezervy 233–240 a musia explicitne uviesť, ktorý starší
výsledok obmedzujú. Skript 226 sa nezačne pred autoritatívnym G8 PASS.
