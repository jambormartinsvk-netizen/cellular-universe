# B6b-2.7 — mapa fyzických realizácií H_RDIV a author gate pre RW1

**Task:** `A2K4-B6B2-7-H-RDIV-SUBBRANCH-MAP-20260727-129`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.7`  
**Autor teórie:** Martin Jambor  
**Formalizácia mapy:** Codex, hlavný orchestrátor  
**Stav:** `AUTHOR_INPUT_MAP / C01_RECOMMENDED_NOT_APPROVED / NO_RUN / NO_PYTHON`  
**Nadradený výsledok:**
`PASS_H_RDIV_MF1_V1_FORMAL_FIRST_PASSAGE_MANTLE_BEHAVIORAL_OPEN`

## 1. Čo tieto označenia znamenajú

`RDIV-C01` až `RDIV-C10` sú **kandidátne podvetvy jedného fyzického
blockera H_RDIV**. Nie sú to nové A2 koľaje, K-identifikátory, body skóre
ani desať povolených pokusov. Mapa ich zachováva, aby sa po výbere prvej
realizácie nestratili ostatné hlavné možnosti.

Žiadna podvetva nie je týmto dokumentom fyzicky schválená. Autor teórie
musí osobitne schváliť prvú testovaciu realizáciu. Kým sa tak nestane,
platí:

```text
R_DIV_PHYSICAL_CLOSURE = OPEN
P4_PHYSICAL_WITNESS = no
P4_PHYSICAL_WITNESS_ATTEMPTS_CONSUMED = 0
D03 = PARTIAL_CANDIDATE_BRIDGE_BEHAVIORAL_OPEN
K4 = 60/100
P5 = 3.5/6
RUN_AUTHORIZED = false
```

## 2. Spoločný zmrazený mantle

Každá podvetva musí zostať v mantineli dokumentu 254:

- `chi_div` je lokálny reálny skalár odlišný od digestion `chi_D`, PH1 a
  expanziou kontaminovaného energy clocku;
- event je prvý jednoduchý vzostupný crossing `chi_div=chi_c`;
- realized count a jeho dual predictable projection zostávajú odlíšené;
- parent sa vyradí, dcéry dostanú nové ID a reset striktne pod prahom;
- žiadny globálny čas, `a`, `ln(a)`, `H0`, realizovaný Fourierov mód `k`,
  `S8` ani post-event produkt nesmie konštruovať trigger;
- kandidát musí mať lokálnosť, kovarianciu, jednotky, pozitivitu, source-off
  limit a netautologický nonzero witness.

## 3. Desať hlavných podvetiev

| ID | Kandidátny fyzický stav | Ľudský mechanizmus | Hlavný prínos | Prvý blocker / riziko | Priorita |
|---|---|---|---|---|---|
| `RDIV-C01-RW1` | kumulatívna lokálna práca prestavby nového rozhrania | bunka postupne vykonáva prácu potrebnú na prípravu deliaceho rozhrania; po dokončení sa rozdelí | priamo nadväzuje na A2 „nové rozhranie nie je zadarmo“, je lokálny a monotónny | odvodiť pre-event výkon `P_rec` a kladnú completion prácu `W_*`; `delta` ani `C=28` nie sú energetická škála | **odporúčaná prvá author gate** |
| `RDIV-C02-LC1` | dokončenosť link/bond prestavieb | delenie nastane po pripravení potrebného podielu lokálnych väzieb | progress je prirodzene bezrozmerný a auditovateľný | regular `v1` vyžaduje spojitú pre-event súradnicu prípravy s konečnou kladnou ľavou deriváciou; doslovný integer jump count je `OUTSIDE_H_RDIV_MF1_V1_REGULAR_SCOPE`, nie fyzikálne vylúčený; nesmie sa zameniť s už nasýteným `C` | vysoká záloha |
| `RDIV-C03-SI1` | lokálny invariant napätia/deformácie | bunka sa delí, keď jej pravidelné tkanivo dosiahne kritickú deformáciu | môže dať priamy geometrický trigger | samotný stress môže klesať; treba monotónny loading path alebo presný crossing a stabilitný zákon | stredná |
| `RDIV-C04-TI1` | lokálna topologická nestabilita Voronoi/Delaunay bunky | zmena susedstva sa aktivuje, keď lokálna geometria stratí stabilitu | najbližšie k diskrétnej sieti a vzniku novej steny | flip môže byť skokový alebo násobný a ležať mimo regular `v1`; treba invariantný pre-event indikátor | stredná |
| `RDIV-C05-DL1` | kumulatívne lokálne defekty/jazvy | nezvratné mikrozmeny sa hromadia, kým bunka musí rekonfigurovať svoje väzby | používa filozofiu konečnej pamäti a nezvratnosti | odlíšiť príčinu delenia od následnej jazvy a dokázať kladnú lokálnu produkciu | stredná |
| `RDIV-C06-FD1` | integrovaná lokálna dávka prichádzajúceho toku | bunka spracúva prichádzajúci tok; po dosiahnutí lokálnej kapacity prípravy sa delí | prirodzený most k „bunka spracúva energiu“ | nesmie to byť pomer hustôt riedený expanziou ani event/product energy; treba causal boundary current | stredná |
| `RDIV-C07-EP1` | kumulatívna lokálna produkcia entropie | delenie je relaxácia po nahromadení určitého množstva nezvratnej prestavby | source-off a šípka času sú prirodzené | coarse-graining, jednotky a lokálna entropia musia byť fyzicky definované, nie iba metafora | nižšia |
| `RDIV-C08-CH1` | kumulatívny lokálny hazard | lokálny stav určuje okamžitú šancu prípravy delenia; `Lambda(tau)=integral lambda(Y)d tau` prekročí kladný pre-event mark `m` | pri `chi_div=Lambda/m`, absolútne spojitej `Lambda` a `lambda>0` pri prvom crossingu ide pathwise o simple upward root aj pri stochastickom marku | hazard law a mark potrebujú mikrofyziku; skokový hazard je mimo regular `v1`, nie fyzikálne vylúčený | stredná záloha |
| `RDIV-C09-CP1` | vnútorný division checkpoint/cyklus | bunka prechádza lokálnymi stavmi prípravy a delí sa pri dokončení cyklu | podobá sa reálnym viacstupňovým bunkovým checkpointom | vysoké riziko prezlečeného timeru alebo zámene s PH1/`chi_D`; musí mať division-specific state law | nižšia |
| `RDIV-C10-HG1` | hybrid: akumulátor práce plus geometrický gate | práca sa musí dokončiť a zároveň musí byť lokálna geometria pripravená na stabilné nové rozhranie | môže oddeliť energetickú prípravu od topologickej realizácie | dve otvorené fyziky naraz; použiť až keď C01 a geometrický gate majú samostatné mantinely | fallback, nie prvý test |

Táto desiatka je uzavretý organizačný zoznam pre aktuálny B6b-2.7 mapovací
scope. Nová položka sa nepridáva len pre premenovanie, inú jednotku alebo
parameter. Ak sa neskôr objaví fyzikálne odlišný primárny zdroj, najprv sa
urobí differential audit voči C01–C10.

### 3.1 Quotient pravidlo proti falošným podvetvám

Podvetvy sú samostatné iba vtedy, ak môžu pri rovnakom stave jednej
súradnice predpovedať rozdielny crossing. Inak sa quotientujú:

- C02 sa zleje s C01, ak je počet pripravených väzieb iba monotónnou
  reparametrizáciou práce pri pevnej práci na väzbu;
- C06 sa zleje s C01, ak sa vstupná dávka mení na interface work pevnou
  účinnosťou bez ďalšieho stavového rozdielu;
- C05 a C07 sa zlejú, ak defect load a entropy production sú navzájom
  jednoznačné stavové funkcie;
- C10 sa zleje s C01 alebo s geometrickou vetvou, ak druhý gate nikdy
  nezmení event prediction.

Počet desať je horný organizačný rozpočet, nie tvrdenie desiatich fyzikálne
nezávislých mechanizmov.

## 4. Zachované, ale neaktívne komparátory

Nasledujúce možnosti sa nestrácajú; nie sú však samostatnými živými
podvetvami tejto desiatky:

| Komparátor | Dôvod, prečo teraz nie je aktívny kandidát |
|---|---|
| čistý proper-time timer | vlastný čas je kovariantný parameter, ale voľná perióda nie je fyzický stavový trigger a nereaguje na source-off |
| objemový sizer/adder | bunky teórie nerastú; expanzia vzniká pribúdaním buniek, nie zväčšením jednej bunky |
| obsadenosť `C=28` | `C` je dimenzia nasýtenej vnútornej kapacity; už je na atraktore a sama nemôže monotónne rásť k deleniu |
| `integral Theta_cell d tau` | `Theta_cell` kinematicky sumarizuje expanziu/delenie; použiť výsledok delenia ako jeho príčinu by bolo kruhové |

## 5. Odporúčaná prvá fyzická realizácia — ľudsky

### 5.1 Obraz mechanizmu

Predstavme si bunku priestoru ako uzol tkaniva, ktorý má vzniknúť na dve
dcéry. Nová deliaca stena nevznikne naraz a zadarmo. Bunku treba lokálne
preusporiadať: pripraviť časť väzieb, presmerovať lokálnu kapacitu a vykonať
prácu potrebnú na vytvorenie nového rozhrania.

`W_rec` je účtovníctvo tejto **už vykonanej alebo nevratne zaviazanej
pre-event práce**. Nie je to zásoba paliva, energia budúcich produktov ani
čas. Kým bunka nič nepripravuje, `W_rec` stojí. Keď lokálny proces vykonáva
reconfiguračnú prácu, `W_rec` rastie. `W_*` je celková práca potrebná na
dokončenie jedného konkrétneho budúceho rozhrania.

```text
chi_div = W_rec / W_*,
D_u W_rec = P_rec(Y_div) >= 0,
W_* > 0 a počas jedného parent cyklu je zmrazené,
chi_c = 1.
```

Keď `chi_div` prvýkrát dosiahne `1`, príprava rozhrania je dokončená a bunka
sa rozdelí. Parent identita končí. Dcéry sú nové bunky a v najjednoduchšom
testovacom variante začnú s `W_rec=0`; rodičovský kredit sa nekopíruje.

### 5.2 Čo to znamená pre „trávenie“

Živá bunka používa spracovanú energiu a materiál na tvorbu deliaceho
aparátu; experimentálne sa pri baktériách pozoruje architektúra, v ktorej sa
division iniciátory akumulujú do prahu. Stochastické modely ju zapisujú ako
first-passage problém. V Bunkovom vesmíre je to iba analógia typu procesu:

```text
lokálne spracovanie -> práca na prestavbe -> dokončené rozhranie -> delenie.
```

Biológia neurčuje Planckovský `P_rec` ani `W_*`. Primárne biologické zdroje
sa preto klasifikujú iba ako `E2_MECHANISM_ANALOGY`, nie ako dôkaz teórie:

- Si et al., *Mechanistic origin of cell-size control and homeostasis in
  bacteria*: https://pmc.ncbi.nlm.nih.gov/articles/PMC6548602/
- Ghusinga et al., *A mechanistic stochastic framework for regulating
  bacterial cell division*: https://pmc.ncbi.nlm.nih.gov/articles/PMC4960620/

### 5.3 Prečo nejde o kruh s expanziou

`P_rec` sa nesmie definovať z `R_div`, z už realizovaného eventu, z
produktového `Q_D`, z makroskopického A2 expansion-pressure člena ani zo
samotného `Theta_cell`. Musí byť predikovateľný z lokálneho **pre-event**
stavu. Potom delenie vzniká z prípravy rozhrania; nie je definované vetou
„bunka sa delí, lebo už pozorujeme delením vytvorenú expanziu“.

### 5.4 Čo dávajú `delta` a `C=28`

- `delta=1/(<k>+C)` hovorí, že prestavba má nenulovú relatívnu réžiu;
- `C=28` určuje nasýtenú dimenziu/kapacitu vnútornej V-vrstvy;
- ani jedno číslo nemá jednotku energie, preto samo neurčuje `W_*`;
- na odvodenie `W_*` treba lokálnu prácu na väzbu alebo interface tension,
  geometriu nového rozhrania a účtovnú konvenciu bez dvojitého započítania.

## 6. Prvý test po autorovom schválení C01

Bez voľby čísel sa má najprv odvodiť množina prípustných dvojíc
`(P_rec,W_*)`:

1. `P_rec` je lokálny pre-event skalár s jednotkou `E/T` a `P_rec>=0`;
2. `W_*` je lokálny kladný skalár s jednotkou `E`, zmrazený pre parent cyklus;
3. source-off dá `P_rec=0` a zastaví ďalší rast `chi_div`;
4. `P_rec` nepoužíva `R_div`, `Q_D`, produkty ani makroskopický expansion
   output;
5. kandidát uvedie lokálny energy/current alebo stress-work pôvod;
6. celková vykonaná práca neporuší lokálnu conservation identity;
7. dcérsky reset nevytvorí ani neduplikuje rodičovský kredit;
8. existuje aspoň jeden explicitný lokálny nonzero witness;
9. nulový limit nevyrobí delenie bez práce;
10. až potom sa rozhodne, či C01 obsahuje fyzický P4 witness.

Výsledok môže byť `PHYSICAL_WITNESS_FOUND`, presný scoped no-go alebo
`REVIEW_PHYSICAL_PROVENANCE_OPEN`. Nenájdenie jedného ansatzu nezabije C01
ani ostatné podvetvy.

## 7. Minimálny author gate

Odporúčané rozhodnutie autora je:

```text
Schvaľujem H_RDIV-MF1-RW1-v1 ako E3_PROVISIONAL prvú testovaciu fyzickú
podvetvu, nie ako fyzické R_div/P4 closure. chi_div=W_rec/W_* znamená
kumulatívnu lokálnu pre-event prácu prestavby nového rozhrania,
D_u W_rec=P_rec(Y_div)>=0 a chi_c=1. W_*>0 sa určí predvídateľne z
lokálneho pre-event stavu najneskôr na začiatku parent cyklu a počas cyklu
zostane zmrazené. Source-off znamená P_rec=0. Parent sa po evente vyradí;
dcéry s novými ID začínajú s W_rec=0. P_rec a W_* sa majú najprv odvodiť
ako množina lokálne konzervatívnych možností. delta a C=28 sú iba
štrukturálne obmedzenia, nie energetická škála.
```

Bez tohto alebo iného explicitného autorovho výberu z C01–C10 sa nevytvorí
fyzikálna preregistrácia nástupcu.

## 8. Auditný handoff

```text
TASK_ID: A2K4-B6B2-7-H-RDIV-SUBBRANCH-MAP-AUDIT-20260727-130
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/rdiv_prereg_audit_v2
ARTIFACT_AUTHOR_TASK_ID: /root task129
STATIC_AUDITOR_TASK_ID: N/A_NO_PYTHON
INTERNAL_AUDITOR_TASK_ID: /root/rdiv_prereg_audit_v2 task130
PACKAGE_CURATOR_TASK_ID: N/A_THIS_PHASE
EXTERNAL_AUDITOR_TASK_ID: N/A_THIS_PHASE
SEPARATION_OF_DUTIES_CHECK: PASS; /root task129 != /root/rdiv_prereg_audit_v2 task130
ROUTE: A1_K1_A2_K4_P5.3_B6b-2.7_H_RDIV_AUTHOR_INPUT_GATE
CURRENT_PHASE: PHYSICAL_REALIZATION_SUBBRANCH_MAP_INDEPENDENT_AUDIT
ALLOWED_NEXT_ACTION: read-only audit C01-C10 completeness, naming, scope, RW1 explanation and author gate
ALLOWED_READS: mandatory bootstrap; documents245,254-256; exact theory sources; event-ledger handoff; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: select a branch for the author; edit; Python; physical verdict/score/depth/run change; C_x/Pi_J/steam/completion; external package
IMMUTABLE_INPUT_PATHS_AND_SHA256: document245=AF289165385801F019454F2CAFF41EFEB25D0A3E2444FA73EAF6B6EBF4E901CB; document254=9AF71F8289D6D5D1072439BF322F261480C76A3AACC8F3A55FCDE10BE9C02B99; theory_intro=678FA9C1AC3C24916FE2E75BEAB6E164ED95933CBE4A1F530C47978AB23AC8A1; theory_main=01B8DD903C3BB97B30E29E2C1E2E2B280D3968EDD0679C610E84A78CC55CBF43
PREREG_SHA256: N/A_MAP_NOT_PREREGISTRATION
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit recommendation
LIVE_FILE_BUDGET: 1 new scientific map + 1 append-only ledger = 2
DONE_WHEN: map preserves at most ten distinct candidate subbranches; rejected comparators remain visible; C01 is recommendation not author approval; human explanation is noncircular and consistent with frozen mantle; exact next author decision is unambiguous
NEXT_ROLE: main_orchestrator
```
