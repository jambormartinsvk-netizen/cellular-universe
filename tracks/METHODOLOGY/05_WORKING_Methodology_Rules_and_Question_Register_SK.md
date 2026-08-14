# Pracovný register metodických pravidiel a otázok — SK

**Vrstva:** 'tracks/' — pracovná, nie release korpus  
**Aktualizované:** 2026-08-12  
**Stav:** autoritatívny pracovný smerovník

## AR70 — hranica pracovného registra a release korpusu

1. Nová pracovná otázka, zmena fyzikálneho stavu, contract a vedecká
   interpretácia patria do najnižšieho uzla 'tracks/<route>/'.
2. Bežný stav koľaje sa vedie v work plane a route history; nevytvára nový
   tematický dodatok v 'theory/'.
3. Lokálny register delty AR/Q/L obsahuje iba nové delty, nie kópiu celého
   registra, a je 'WORKING / NOT_RELEASED'.
4. 'theory/SK' a 'theory/EN' sú release alebo release-ready vrstva.
5. Povýšenie do 'theory/' vykoná iba hlavný orchestrátor pri otvorenom
   release candidate po kontrole duplicity, dôkazov, SK/EN parity, changelogu
   a SHA manifestu.
6. Historické 'theory/*/05*' sa nemažú ani nepresúvajú bez Git baseline,
   mapy 'OLD_PATH -> NEW_PATH', link auditu a hashov.

## FS-GATE-01 — funkcia sa najprv obmedzuje správaním

Pred voľbou konkrétnej funkcie, akcie alebo kernelu sa vytvorí behaviorálny
a fyzikálny mantinelový pas podľa
'tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_SK.md'.

1. Najprv vstupy, výstupy, znamienka, trendy, prahy, nulové body, saturácie
   a energetické hranice.
2. Ak sú nutné správania nezlučiteľné, presná podtrieda dostane
   'BEHAVIORAL_EMPTY_SCOPE'.
3. Neprázdny behaviorálny obal je iba 'BEHAVIORAL_OPEN'; ďalej sa hľadá
   explicitný lokálny svedok.
4. Neúspešný grid alebo nenájdený ansatz nie je dôkaz prázdnosti.
5. Smrť sa zapisuje ako certifikovaná neexistencia v presnom scope, nie ako
   „funkciu sme nenašli“.

### FS-GATE-01a — dôkazová váha

1. Každý mantinel má triedu 'E0_EXACT', 'E1_DIRECT_MEASUREMENT',
   'E2_REFERENCE_MODEL' alebo 'E3_PROVISIONAL'.
2. Iba E0 a úplne zmapovaný E1 môžu vylúčiť podtriedu pred výpočtom.
3. E2 je comparator/nulový limit; samostatná nezhoda je
   'REFERENCE_MISMATCH_ONLY'. E3 je vodidlo.
4. 'PRECHECK_EXCLUDED_SCOPE' nie je 'COMPUTED_STOP_SCOPE'.
5. Computed STOP vyžaduje úplný predregistrovaný fyzikálny výpočet;
   observational STOP úplnú model-observabla-likelihood reťaz.

## FS-GATE-02 — neznáma funkcia sa vedie ako prípustná množina

**Rozhodnutie autora:** Martin Jambor, 2026-08-01

Ak konkrétna funkcia, kernel alebo lokálny transportný zákon ešte nie je
známy, workflow najprv nehľadá svojvoľne jeden reprezentant. Zostaví jej
prípustnú množinu

```text
A_f={f in F_adm:
     všetky exact fyzikálne identity platia,
     všetky inequality/regularity/causality/stability guardy platia,
     všetky otvorené merané observables ležia v predregistrovanej
     tolerančnej oblasti}.
```

1. `F_adm` musí uviesť doménu, kodoménu, regularitu, lokálnosť, covariance,
   units, povolený jet, nulové limity a zakázané nové polia/škály.
2. Exact zákony (`E0`) sa uplatnia bez tolerancie. Meraná kompatibilita sa
   testuje iba cez zmrazenú observable mapu, dataset provenance, neistoty,
   covariance/systematics a explicitnú confidence alebo coverage oblasť;
   neurčité „plus-mínus odchýlka“ nie je rozhodovací prah.
3. Platný vedecký výsledok môže byť celá neprázdna množina alebo interval;
   unique funkcia sa nevyžaduje a null smer sa nevyberá bez ďalšieho
   fyzikálneho princípu.
4. `RANGE_EXISTENCE_PASS` vyžaduje explicitného svedka alebo vetu o
   existencii. Samotný zoznam podmienok je `RANGE_CONDITIONAL_OPEN`.
5. Ak existencia ešte nie je rozhodnutá, funkcia dostane trvalé
   `UNRESOLVED_FUNCTION_ID`, exact constraints, závislé brány a reaktivačný
   vstup. Koľaj zostáva `LIVE / WAITING` a hlbší audit sa môže vrátiť na
   tento identifikátor.
6. `EMPTY_SCOPE_CERTIFIED` je dovolené iba po dôkaze, že prípustná množina
   je prázdna v presnom scope. Nájdenie nulového počtu ansatzov, gridových
   bodov alebo explicitných formúl prázdnosť nedokazuje.
7. Pre celú teóriu sa vedie spoločná feasibility množina na spoločnom
   stavovom priestore

   ```text
   A_theory = A_exact
              intersect A_observational
              intersect intersection_i pullback_i(A_i).
   ```

   Teória má v kontrolovanom scope aspoň jeden prípustný celok iba ak je
   táto spoločná množina neprázdna. Kým niektorá povinná funkcia alebo
   observable mapa chýba, stav je `GLOBAL_FEASIBILITY_INCOMPLETE`, nie PASS
   ani STOP.
8. Každý prijatý interval sa prenáša ako set-valued constraint do potomkov;
   nesmie sa potichu nahradiť stredom, minimum-norm bodom ani fitovaným
   reprezentantom.

### FS-GATE-02a — návrat k nenájdenej funkcii a logika smrti

1. Každá nenájdená povinná funkcia má v najnižšom route-local
   `00_STATUS.md` alebo work plane trvalý záznam: `UNRESOLVED_FUNCTION_ID`,
   doménu/kodoménu, prípustnú triedu, všetky E0/E1/E2/E3 mantinely, aktuálne
   povolené rozsahy výstupov, stav svedka alebo certifikátu, závislé brány a
   presný reaktivačný vstup. Nadradené plány nesú iba súhrn a odkaz.
2. Stav `RANGE_CONDITIONAL_OPEN` znamená, že zatiaľ nebol dokázaný rozpor;
   nie je to dôkaz existencie. `RANGE_EXISTENCE_PASS` znamená, že aspoň jeden
   spoločný rozsah alebo funkčný svedok prešiel všetkými dovtedy otvorenými
   E0 a úplne zmapovanými E1 mantinelmi. Ani tento stav sám nie je PASS
   neskorších G brán.
3. Pri uzle `AND` sú všetky deti povinné a rozhoduje prienik ich pullbackov.
   Uzol zomiera iba po certifikáte, že tento spoločný prienik je prázdny.
   Pri uzle `OR` sú deti alternatívne koľaje; uzol zomiera až vtedy, keď je
   zoznam alternatív preukázane úplný a každá alternatíva má
   `EMPTY_SCOPE_CERTIFIED` v spoločnom scope.
4. Koľaj zostáva `LIVE / CONDITIONED` alebo `LIVE / WAITING`, ak aspoň jedna
   jej alternatíva má neprázdny svedok alebo ešte otvorenú necertifikovanú
   prípustnú množinu. Neschopnosť nájsť vzorec, konečný prázdny grid alebo
   neúplné mapovanie mantinelov ju nezabíja.
5. Teória je `GLOBAL_FEASIBILITY_INCOMPLETE`, kým chýba povinná funkcia,
   model-to-observable mapa alebo nebola uzavretá aspoň jedna deklarovaná
   alternatíva. `THEORY_PHYSICALLY_DEAD_IN_SCOPE` je dovolené až po dôkaze,
   že globálna spoločná prípustná množina je prázdna a všetky top-level
   alternatívne koľaje v preukázane úplnom rozdelení zomreli. Dôvod a
   certifikáty sa nikdy nemažú.
6. Chyby merania nie sú voľná tolerancia. E1 rozsah musí obsahovať dataset,
   confidence/coverage, štatistické a systematické neistoty, covariance a
   exact mapu z modelu na observablu. Dokázaný E0 zákon nemá meraciu
   toleranciu, pokiaľ samotná veta výslovne neobsahuje aproximáciu.

### FS-GATE-02b — output-range relaxácia nenájdenej funkcie

**Rozhodnutie autora:** Martin Jambor, 2026-08-01

1. Autor môže pre bounded feasibility fázu nahradiť hľadanie jednej
   nenájdenej funkcie množinou jej povolených výstupov. Musia sa oddeliť:
   `R_exact(Z)`, obraz jedného globálne prípustného funkcionálu, a
   `R_out(Z)`, state-local vonkajšia output relaxácia. Platí iba
   `R_exact(Z) subseteq R_out(Z)`; opačná inklúzia sa nesmie predpokladať.
2. `R_out` musí zachovať typ, units, linearitu alebo príslušnú set-valued
   graph štruktúru, covariance, locality vstupov, quotient/relabel guard,
   conservation, causality, regularitu, source-off limity a všetky frozen
   face/bulk/owner podmienky pôvodnej funkcie. Nepridáva pole, škálu,
   topológiu, causal rule, memory ani fitovaný reprezentant.
3. Neprázdnosť `R_out(Z)` dokazuje iba existenciu povoleného výstupu v danom
   state-local scope. Nedokazuje, že existuje jedna hladká local-natural
   funkcia cez všetky stavy, ani že existuje measurable/smooth selection.
   Vonkajší rozsah môže byť neprázdny aj keď `R_exact` ostáva nerozhodnutý.
4. Ak nie je odvodená fyzikálna horná alebo dolná hranica, `R_out` sa nesmie
   svojvoľne nahradiť konečným intervalom. Potom zostáva všeobecnou
   množinou/korešpondenciou s explicitnými guardmi.
5. Potomkovia preberajú celú korešpondenciu cez zjednotenie alebo pullback;
   nesmú použiť midpoint, minimum norm, nulový smer ani jeden vybraný
   `K_bridge`. Takýto krok je feasibility screen, nie unique dynamický zákon,
   well-posed evolúcia, observable predikcia ani globálny PASS teórie.
6. Pôvodný `UNRESOLVED_FUNCTION_ID` zostáva otvorený a output relaxácia má
   vlastný trvalý identifikátor a spätný odkaz. Fyzikálne uzavretie vyžaduje
   buď realizovateľnosť relevantného výstupu jednou prípustnou funkciou,
   alebo osobitné autorovo rozhodnutie o identite koľaje.

### FS-GATE-02c — fyzikálny prior a konečný kandidátny ensemble

**Rozhodnutie autora:** Martin Jambor, 2026-08-02

1. Ak úplná funkcia ešte nie je známa, možno pred výpočtom zostaviť bounded
   register najviac desiatich fyzikálne motivovaných tried pre každý chýbajúci
   komponent a z nich najviac desať vzájomne kompatibilných balíkov.
2. Poradie je `PHYSICS_PRIOR_RANK`: ordinal podľa minimálneho počtu nových
   predpokladov, exact covariance/conservation, lokálnosti, kauzálnej
   well-posedness, stability/passivity a proveniencie. Nie je to numerická
   pravdepodobnosť, posterior, fit ani náhrada E1 observable testu.
3. E0 a prijaté route guardy sú hard filtre. Známe fyzikálne frameworky sú
   E2 reference rodiny, pokiaľ nie je osobitne uvedená exact identita; samy
   nepreukazujú, že daný zákon platí v teórii.
4. Chýbajúci vstup znamená `WAITING_MISSING_FROZEN_LINEAGE`, nie vylúčenie.
   Kandidáta možno vylúčiť iba exact rozporom v predregistrovanom scope.
5. Konečný top-ten zoznam nie je dôkaz úplnosti všetkých same-track zákonov.
   Vylúčenie všetkých jeho členov preto samo nezatvára rodičovskú koľaj.
6. Výsledky sa používajú na výber ďalšej diskriminačnej rovnice alebo vstupu;
   nesmú spätne meniť poradie, ownere, kanálový split, škálu ani toleranciu.

### Register nenájdených funkcií

| ID | Route / funkcia | Prípustná trieda a aktuálny výsledok | Čo chýba | Reaktivácia / závislé brány |
|---|---|---|---|---|
| `UF-C01-RW1-KBRIDGE-001` | `A2-K4/P5/B6b-2.12`, `K_bridge^CT` | corrected task506 je prijatý ako `RANGE_CONDITIONAL_OPEN / LIVE-WAITING`; corrected output-range task519 prešiel task520/task521 dual auditom a je prijatý iba ako bounded state-local conditional range, nie existencia funkcie; task504 ostáva quarantined | pointwise geometric obstruction a type-correct global operator allowed set sú charakterizované, ale existencia jedného globálneho local-natural operatora, combined kernel compatibility a exact cap/current–side/traction data nie sú preukázané; observational intersection ešte nie je otvorený | explicitný same-track global operator witness alebo valid local-natural relative-horizontal existence theorem nad complete frozen face/bulk dátami a všetkými guardmi; unique physical law, D2I/D3–D6 a P5.4 zostávajú otvorené |
| `UF-C01-RW1-XI-002` | `A2-K4/P5/B6b-2.12/D2SW11-D2SW12`, existujúca material-generator mapa `Xi_Z` na úplnom fyzickom quotient tangente | task596 štrukturálne uzavrel R0–R4, ale nenašiel ani Z0_cert, ani explicitný constrained nonvertical NZ_cert | exact result `N1_QUOTIENT_ZERO_CLASSIFICATION_WAITING`; Xi/N2/N3 sa ešte nedosiahli | dodať pre ten istý regular Z buď dôkaz všetkých tangentov ako vertical, alebo jeden explicitný dovolený nonvertical tangent so všetkými constraintmi |

### Register output korešpondencií

| ID | Pôvodná funkcia | Rozsah | Aktuálny stav | Čo tvrdenie neznamená |
|---|---|---|---|---|
| `OR-C01-RW1-KOUT-001` | `UF-C01-RW1-KBRIDGE-001` | geometrický state-local linear output fiber je afinný; fyzicky guardovaný output range je iba jeho guard-cut podmnožina; boundary-power obraz je fixed-state empty-or-singleton a reservoir feasibility sa aplikuje až na `x in A_res` | task512 aj dotknutá affine-closure časť task517 sú quarantined; corrected task519 je prijatý ako `OUTPUT_RANGE_CONDITIONAL_OPEN / RESERVOIR_INTERSECTION_CONDITIONAL_OPEN`; D2SW7 task528 prešiel task529/task530 dual auditom a je prijatý ako `INPUT_SCOPE_INCOMPLETE_LIVE_WAITING`, čaká na jeden complete existing `Z0 in D_7` evaluation packet | nepreukazuje globálny `K_bridge`, smooth selection, neprázdnosť ani prázdnosť fyzického rozsahu, afinnosť po nonlinear guardoch, unique dynamický zákon ani observational/global PASS; algebraický reservoir prefilter nie je guarded witness |
| `OR-C01-RW1-Q1R6-Z0-002` | Q1R6 reference scalar–plasma total EMT a interface geometry `->` najviac jeden midpoint `Z0` source packet | task532 povoľuje iba source-exact total stress-energy a geometriu rozhrania; `u_cell` sa musí odvodiť ako unique future Landau smer celého tensoru a každý chýbajúci current, owner, `P_rec` split alebo guard zostáva explicitne nevyhodnotený | task535 prešiel task536/task537 dual auditom a je prijatý ako `Q1R6_Z0_LANDAU_RANGE_ONLY_PACKET_INCOMPLETE / LIVE_WAITING`; exact planar range `q=0: E+P_n!=0`, `q!=0: |E+P_n|>2|q|`, vždy s full Type-I/nondegeneracy/smoothness guardmi | Q1R6 nie je nové pole ani theory model; `u_plasma` nie je `u_cell`; scalar/plasma split nie je reservoir split; chýbajúci source current nie je nula; neúspech nezatvára C01-RW1, P5 ani A2-K4 |
| `OR-C01-RW1-JOINT-003` | existujúce `T_loc`, `Pi_CT`, Landau `u_cell`, `B_rec`, `Sigma_prep`, parent worldtube a reservoir ledger | task539 zmrazuje spoločný aktívny set `A_joint^*` a explicitný Noether–Cartan candidate `K_N=i_(T_CT.xi)epsilon_g`; task542 ho po task540/task541 dual contract PASS redukuje na exact full-tangent factorization test `Y_Z=D_Z compose N_T,Z compose Xi_Z`, residualy `R_g,R_F` a passive reservoir product `Delta_2(P_rec) x [0,p-P_rec]` | `TASK543_MATH_AND_TASK544_PHYSICS_IDENTITY_RESULT_AUDITS_PASS_ACCEPTED / TASK545_BOUNDARY_OR_BLOCKER_PROGRESS_ACCEPTED / JOINT_RANGE_CONDITIONAL_OPEN / LIVE_WAITING`; čaká na one-existing-Z complete paired tangent/target/owner/provenance/guard packet alebo equivalent scoped theorem plus guarded reservoir witness | active ani source-off nonemptiness/emptiness nie je dokázaná; no global `K_bridge`, dynamics, observations ani closure; nepridáva univerzálnu energy condition, pole, škálu alebo fit |
| `OR-C01-RW1-PRIOR-ENSEMBLE-004` | päť chýbajúcich RW1 komponentov nad accepted task542 | task547 body `71EFF4795B74E789604D8353FE50A1C63B16C52C114928C7F1CFD7D2B57D8542` zmrazuje 8 intrinsic, 8 constitutive, 9 evolution, 8 provenance a 8 owner rodín a top-10 kompatibilných ordinal balíkov | task550 je decision-reach quarantined; accepted corrected task552 body `706B1BFBF9FBFF2222251D223127AD1998B57FEEB799F9CAAE0E3802C40E68AF` prešiel task553/task554 dual auditom a task555 `BOUNDARY_OR_BLOCKER_PROGRESS`; stabilne `10_WAITING / 0_EXCLUDED / LIVE_WAITING / BATCH1_CLOSED_4_OF_10` | reaktivácia: one-existing-complete-Q_Z packet s paired `X_Z,Y_Z,L_N,Z`, O1/R1 worldtube/provenance a všetkými guardmi alebo exact ekvivalentná scoped veta; zero survives nie je emptiness |
| `OR-C01-RW1-PK1-CAPACITY-KERNEL-005` | PK1/I0 exact-equivalent scoped theorem route nad `B_rec=[G_loc,capacity_loc,geometry_loc]_rel` | task557 body `F7BCD8AFD474B89BC5E57FB8DD930FCEA49E0F08A7714BF0642C977861836BB0` a corrected task560+task563 effective contract prešli task564/task565 dual auditom; whole-map I0 vyžaduje complete `Q_Z` a assembled `X_Z`, sektorový ekvivalent navyše W1-W4 vrátane image independence | task566 body `4F7CFD6ECC104B85753799E8FEDE0E7DB828F674F2EF7190B0544944681B1D87` je po task567/task568 dual audite a task569 progress acceptance prijatý ako `PK1_QZ_COMPLETENESS_OR_WHOLE_MAP_INJECTIVITY_WAITING / BOUNDARY_OR_BLOCKER_PROGRESS`, 10 waiting / 0 excluded, bez evaluation `E_N`; `BATCH1_CLOSED_4_OF_10` | najmenší vstup N1–N3: one-existing regular `Z`, complete overlap-resolved quotient, assembled whole `X_Z`, potom whole-map kernel witness/injectivity alebo complete W1-W4; missing input nie je exclusion ani closure |
| `OR-C01-RW1-QX-KERNEL-006` | `UF-C01-RW1-XI-002`, bounded N1–N3 constructive allowed-set successor | task570 definuje `A_Q/A_X/A_K`; task573 opravuje existential/universal kvantifikátor a task576 dopĺňa exhaustívnu kernel-classification WAITING vetvu | `TASK579_DUAL_RESULT_AUDIT_AND_TASK582_BOUNDARY_OR_BLOCKER_PROGRESS_ACCEPTED / N1_COMPLETE_QUOTIENT_RANGE_CONDITIONAL_OPEN / LIVE_WAITING / BATCH1_CLOSED_3_OF_10`; `A_Q` nemá explicitný member/existence theorem, `A_X/A_K` sa neinštancujú a PK1 ostáva waiting | Martinom určený alebo autorizovaný exact one-state primitive capacity/contact/interface chart, overlap/gluing a gauge-vertical completeness certificate; potom sourced whole `Xi_Z` action. Žiadny Python, `E_N`, owner/power/reservoir gate ani null selection |
| `OR-C01-RW1-Q-R1R5-007` | `OR-C01-RW1-QX-KERNEL-006`, Martinom autorizovaný one-regular-`Z` R1–R5 packet | accepted task596 SHA256 `BD9A159AF4270D19EF6C86D0D40EDB80C4650D70ABFDE3D128AC626E109EED47` + task597/task598 dual PASS + task599 boundary review | `N1_QUOTIENT_ZERO_CLASSIFICATION_WAITING / SAME_TRACK_CONFIRMED / BOUNDARY_OR_BLOCKER_PROGRESS / D2SW12_BATCH1_CLOSED_8_OF_10`; upstream bez invalidácie | Martin otvoril jeden same-Z D2SW13 certificate-only atóm; contract task601 čaká na dvojitý audit |
| `OR-C01-RW1-NZ-CERT-008` | `OR-C01-RW1-Q-R1R5-007`, existujúca scalar contact capacity a spoločný contact/interface primitív | effective task601 SHA256 `7CE0369E26133D78DF90CFFDAD2EEC98A7AC5DEC92A829850CC3A9BECC5D242C` + task604 SHA256 `78664EC362BE65491E3D0B77654C908434A245C561089D1DADE1884D2128B9C2`; accepted task607 SHA256 `C4CB6944298F2EA59C4C6124ED936E6AE4CF32F5EF070B8F8AD10A603D6E96D1` vykonal C1-C3 search | `TASK607_DUAL_RESULT_AND_TASK610_BOUNDARY_PROGRESS_ACCEPTED / N1_CERTIFICATE_DATA_WAITING / BATCH1_CLOSED_1_OF_10 / LIVE_WAITING`; Martin následne autorizoval exact capacity-response same-Z curve successor | successor je `OR-C01-RW1-CAPACITY-CURVE-009`; žiadna Xi/kernel/E_N inferencia |
| `OR-C01-RW1-CAPACITY-CURVE-009` | `OR-C01-RW1-NZ-CERT-008`, state-local pasívny diferenciálny koeficient existujúcej causal traction/current odozvy voči `s=ln(A_e/A_e(0))` na jedinom shared contact/`Sigma_prep` primitíve | effective task611+task611B; historical task614 SHA256 `E34F3A02FA8FF05C80ECDCB5434DB5705008805FDBBD512FD783F69CBBEE7D2E`; corrected task618 SHA256 `DDB130415C953974E63A430E7E021329A4583E800A752DDDD0DE4F92CF9F75C1`; task617 SAME_TRACK; task619 PASS; task620 `BOUNDARY_OR_BLOCKER_PROGRESS` accepted | `N1_CAPACITY_RESPONSE_CURVE_WAITING / NZ_PROVED=false / Z0_PROVED=false / D2SW14_BATCH1_CLOSED_8_OF_10 / LIVE_WAITING`; task535 je `NOT_CERTIFIED_INSIDE_AND_NOT_CERTIFIED_OUTSIDE` | jediná reaktivácia je exact existing-evidence CR1 same-Z contact capacity/full-jet packet; až potom možno zvážiť successor contract; no run |
| `OR-C01-RW1-CR1A-PROVENANCE-010` | `OR-C01-RW1-CAPACITY-CURVE-009`, Martinom autorizovaný one-regular-`Z/e` contact-geometry/provenance screen s theory-side `B_rec` owner/orientation a Q1R6 stress-energy candidate | task621A read-only overil exact local arXiv-v1 source archive SHA256 `5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416`, receipt SHA256 `E26C8CCEC518E0358D8B8368EF1AEC9261315571F31C2D3AD374D1DA31953D02`, official arXiv/SCOAP3 surfaces a coauthored WallGo release family; bez Pythonu, digitizácie, fitu alebo runu | `CONTACT_GEOMETRY_PROVENANCE_RANGE_CONDITIONAL_OPEN / LIVE_WAITING`: arXiv source má article source/figures, nie machine profile table/code/data; WallGo v1.0.0 (2024-11-07) je neskorší E2 comparison implementation, nie preukázaný exact source článku z 2022; conditional `F_e -> Gamma_e -> C_W` a binary-owner rule sa zachovávajú | na pokračovanie treba actual `e in B_rec` s fixed incidence, unique incoming owner/orientation a embedding/lift receipt plus explicitný provenance bridge, ak sa má exact frozen WallGo verzia použiť iba ako E2 comparator; bez toho nevzniká `c_e`, jet packet, NZ/Z0 ani run authority |
| `OR-C01-RW1-CR1A-MAP-011` | `OR-C01-RW1-CR1A-PROVENANCE-010`, conditional memberwise geometry-to-stress map nad `D_CR1a` | task622 contract SHA256 `2FAE2A826EB8905920BC5E4C9DB9E51F58A5BA6E3EC00EB2194BCBCACF37E83D` zmrazuje množinu všetkých existujúcich regular `(Z,e)` s preukázaným unique pre-event `B_rec` ownerom a úplným `F_e -> Gamma_e -> C_W` lift receiptom; neprázdnosť sa nepredpokladá; WallGo v1.0.0 je iba E2 comparator, nie zdroj alebo Q1R6 supplement | `TASK622B_PHYSICAL_EOF_HANDOFF_CORRECTED / RANGE_CONDITIONAL_OPEN / LIVE_WAITING / BATCH1_1_OF_10`: mapuje iba certifikovaného člena na odvodené `q,n,dA,Gamma,C_W,T_loc,T_CT,t_CT,j_CT` a úplné geometry/source jets; current corpus nemá certifikovaného člena | nepreukazuje neprázdnosť `D_CR1a`, actual map member, common traction-current response, curve, NZ/Z0, globálny `K_bridge`, Xi/kernel/I0/PK1/E_N, WallGo-Q1R6 identitu, observable ani run authority |

## WORKING-DEV-RC-OFFICIAL — technika sa oddeľuje od dôkazu

**Prijaté používateľom:** 2026-07-29  
**Nahrádza:** audit/freeze/successor slučku po každej technickej chybe.

### A. DEV_SANDBOX

- Jeden pracovný base/runner sa opravuje na mieste.
- Povolené sú offline synthetic unit/selftest, compile a help bez reálnych
  vedeckých vstupov, siete, official outputu a fyzikálneho verdiktu.
- Bežná chyba vytvorí len jeden compact error row a regresný test.
- Nevytvára nový prereg, versioned successor, DNR, samostatný audit,
  progress review ani external package.
- Rovnaký failed candidate SHA sa bez opravy nespúšťa znova.

### B. RC_FREEZE

RC vznikne až po DEV suite PASS. Zmrazí sa finálny vedecký contract,
source/input hashe, official príkaz, prahy, absent-output guard a oddelenie
autora od auditora.

Nezávislý math/script auditor kontroluje exact RC a iba relevantné historické
error patterns. Full error ledger sa nerečíta ako rituál. Auditný blocker sa
vracia do rovnakého DEV súboru.

### C. OFFICIAL A SCIENCE AUDIT

Po statickom audite môže orchestrátor povoliť jeden bounded official run.
Technický crash/timeout/schema/dependency fail nemá fyzikálny význam.
Fyzikálny záver vznikne až z immutable rawu, frozen contractu a nezávislého
science auditu.

## WORKING-ERROR-BATCH-10 — po desiatich chybách rozhoduje autor

Každá implementačná línia vedie:

~~~text
ERROR_BATCH_INDEX
ERRORS_USED_IN_CURRENT_BATCH
CUMULATIVE_TECHNICAL_ERRORS
LAST_FAILED_CANDIDATE_SHA256
~~~

1. Jedna distinct failed candidate/test konfigurácia vyžadujúca opravu
   spotrebuje '1/10'. Viac fixtures s jednou koreňovou príčinou je jedna
   chyba.
2. DEV PASS nevynuluje dávku. Counter nevynuluje ani názov, suffix, agent,
   task alebo formálne prebalenie architektúry.
3. Pri '10/10' vznikne 'TECHNICAL_PERMISSION_GATE'. Povolená je iba stručná
   read-only diagnóza; ďalší edit alebo proces sa zastaví.
4. Pokusy 11–20 sa otvoria iba po explicitnom povolení Martina Jambora.
   Ďalšie desaťchyby rovnako potrebujú nové povolenie.
5. Official/scientific closure ukončí líniu. Nový vedecký atóm začne vlastný
   batch '0/10'; kumulatívna história ostáva.
6. Gate 10/10 nie je fyzikálny STOP a nesmie zabiť rodičovskú koľaj.

Compact error row:

~~~text
timestamp | batch/error | candidate_sha | failing_test |
root_cause_class | fix_or_next | scientific_effect
~~~

Samostatný incident audit je povinný iba ak chyba mohla zmeniť už publikovaný
raw alebo zasahuje rovnice, units, gauge, state order, prahy, provenance či
rozhodovaciu logiku. Reusable prevencia sa pridá do known patterns iba ak je
nová a všeobecná.

## WORKING-PROGRESS-MILESTONES — review iba pri informačnej zmene

'progress_goal_reviewer' sa spúšťa po:

- official výsledku alebo uzavretí vedeckej brány;
- zmene autoritatívneho blockeru, route alebo next scientific action;
- 'TECHNICAL_PERMISSION_GATE 10/10';
- explicitnom podozrení na goal drift alebo neprimeraný audit/doc churn.

Nespúšťa sa po bežnej DEV chybe, oprave, static blocker, compile/help/smoke
ani package control medzikroku. Klasifikácie zostávajú:

- 'SCIENTIFIC_GATE_PROGRESS';
- 'BOUNDARY_OR_BLOCKER_PROGRESS';
- 'TECHNICAL_ENABLEMENT_ONLY';
- 'DOCUMENTATION_OR_AUDIT_CLOSURE_ONLY';
- 'NO_INFORMATIONAL_PROGRESS';
- 'GOAL_DRIFT'.

Počet súborov, skriptov, testov alebo auditov sám nezvyšuje vedecký progress.

## WORKING-PHYSICAL-TRACK-WAIT-STATE — bez fyzikálneho dôvodu sa koľaj neuzatvára

**Rozhodnutie autora:** Martin Jambor, 2026-07-29

1. Fyzikálna koľaj sa môže uzavrieť iba pre explicitný fyzikálny dôvod
   podopretý príslušným výpočtom alebo dôkazom, nezávislým auditom a
   autoritatívnym rozhodnutím. Technický fail, vyčerpaný source loop,
   nedostupný dôkaz, timeout, evidenčný checkpoint ani koniec implementačnej
   dávky nie sú dôvodom na uzavretie fyzikálnej koľaje.
2. Ak fyzikálny PASS alebo STOP ešte neexistuje, stav koľaje je
   'WAITING_FOR_<EXACT_PHYSICAL_INPUT_OR_DERIVATION>', nie 'CLOSED'.
3. Živý plán pri čakaní presne uvedie:
   - čo fyzikálne chýba;
   - prečo je to potrebné pre ďalšiu bránu;
   - čo môže koľaj znovu aktivovať;
   - ktoré technické pomocné línie sú už terminálne a nesmú sa opakovať.
4. Technická alebo evidenčná pomocná línia môže byť označená ako terminálna,
   ale jej terminál sa nesmie preniesť na rodičovskú fyzikálnu koľaj.
5. Čakajúca koľaj ostáva 'LIVE / WAITING', zachováva doterajšie platné dôkazy
   a nesmie dostať fyzikálny STOP ani closure iba z absencie nového vstupu.

## WORKING-AUDIT-FINDING-DECISION — nález rozhoduje o návratovom bode

**Prijaté používateľom:** 2026-07-29

Interný aj externý audit používa rovnakú taxonómiu:

| Trieda | Význam |
|---|---|
| 'P0_PACKAGE_PROCESS_ONLY' | chyba control vrstvy balíka; evidence/claim nedotknuté |
| 'T1_TECHNICAL_NO_CLAIM_REACH' | technická chyba bez dosahu na vedecký claim |
| 'S1_LOCAL_CORRECTABLE_SAME_TRACK' | vedecký dosah, ale definujúca identita koľaje môže zostať |
| 'S2_TRACK_IDENTITY_AT_RISK' | oprava môže meniť definujúcu fyziku alebo filozofiu koľaje |
| 'S3_FATAL_IN_SCOPE' | invariantný rozpor v presnom scope |
| 'S4_PARENT_THEORY_IMPACT' | nález zasahuje rodičovský contract alebo viac koľají |

'P0' sa rieši novou package control revision nad byte-identickými evidence
hashmi a novým audit submissionom. Nevracia sa do DEV/RC/official.

'S1–S4' aktivuje 'CLAIM_QUARANTINE'. Historický raw sa nemaže, ale nesmie sa
používať ako prijatý vstup. Transitive descendants dostanú
'SUSPENDED_DEPENDENCY'.

### Jeden decision record a tri osi kontroly

Namiesto viacerých dokumentov vznikne jeden 'AUDIT_FINDING_DECISION_RECORD':

1. **matematika/logika** — rovnice, dôkaz, numerický contract, units,
   threshold logic, reachability a earliest invalid checkpoint;
2. **fyzika** — covariance, conservation, gauge, causality, stability,
   regularity, null limits a observables;
3. **filozofia/identita teórie** — bunková ontológia, lokálnosť a emergence,
   smer kauzality, význam stavov a vysvetľovací cieľ; oprava nesmie byť
   ad-hoc zásah len na záchranu dát.

Výstupom je 'TRACK_IDENTITY_GATE':

- 'SAME_TRACK_CONFIRMED';
- 'NEW_TRACK_REQUIRED';
- 'UNRESOLVED_AUTHOR_DECISION'.

### Návratový bod

- interpretácia -> interný science audit;
- official input/execution -> official gate po oprave upstream príčiny;
- source alebo formula transcription -> DEV a nový RC;
- contract/rovnica pri same-track identite -> contract draft;
- track-defining/fatal/parent finding -> žiadny automatický run; rozhoduje
  Martin medzi opravou rodiča, novou koľajou a ukončením.

Opakujú sa iba zneplatnený checkpoint a jeho potomkovia. Hashovo neporušené
upstream checkpointy zostávajú platné.

## WORKING-REUSABLE-AUDIT-CHECKPOINT — audit od ľubovoľného míľnika

Každý prijatý externe auditovateľný progress alebo STOP bod má canonical
checkpoint:

~~~text
CHECKPOINT_ID
PARENT_CHECKPOINT_IDS
ROUTE_AND_GATE
ACCEPTED_STATE
CONTRACT_RC_INPUT_RAW_AUDIT_SHA256
CANONICAL_PACKAGE_ID
CANONICAL_PACKAGE_MANIFEST_SHA256
CHECKPOINT_STATUS
SUPERSEDES_CHECKPOINT_ID
~~~

Jeden sealed package možno opakovane odovzdať viacerým auditorom bez zmeny
bajtov. Každé odovzdanie má vlastný 'AUDIT_SUBMISSION_ID', auditor identity,
mode, response path/hash a assessment state. Nový auditor štandardne nečíta
predošlé responses.

Checkpoint package obsahuje parent IDs a manifest hashes. Auditor si môže
vybrať, či parent claims prijme ako hash-bound assumptions, alebo si vyžiada
ich packages a prejde DAG dozadu. Potom môže pokračovať po potomkoch. Tým je
možný opakovaný audit teórie od ľubovoľného prijatého progress/STOP bodu.

Rozporné audity otvoria 'AUDIT_DISCREPANCY_REVIEW'; nerozhoduje prostá väčšina,
ale presná reprodukcia, evidence tags a argument.

## WORKING-DOCUMENTATION-MINIMUM — dokumentuje sa teória, nie debugging

Trvalá vedecká dokumentácia obsahuje:

1. cieľ a frozen contract;
2. rovnice, source lineage, units, gauge a rozhodovacie kritériá;
3. immutable raw/receipt;
4. interný science audit a autoritatívne rozhodnutie;
5. aktuálny blocker a najmenší successor.

Bežný debugging patrí do error row + regression testu. Stack traces,
jednotlivé fixture failures, premenovania lokálnych premenných a opakované
handoff narrative sa nepovyšujú na vedecké dokumenty.

Živý current/route plán nesmie obsahovať podrobnú historickú kroniku. Tá je
v 'HISTORY/' a načítava sa iba exact podľa potreby. Externý balík sa pripraví
až pre ucelený vedecký míľnik, nie pre technický fail.

Závažný finding pridá najviac jeden decision record a dve compact registry
delty: checkpoint status a audit submission. Package-process chyba nepridáva
vedecký decision record.

## WORKING-TASK-AND-AGENT-BOUNDARY

Samostatná hlavná úloha vzniká pre fyzikálne nezávislý balík, nie pre každý
suffix, mód, parameter alebo technickú opravu. V jednej úlohe zostávajú
atómy s rovnakými rovnicami, ktoré sa líšia iba módom, 'k', variantom,
toleranciou alebo supportom.

Subagenti sa používajú na ohraničené roly s jasným prechodom. Fyzikálne
odvodenie, zmena mechanizmu a autoritatívny PASS/REVIEW/STOP zostávajú na
autorovi a hlavnom orchestrátorovi podľa ich kompetencie. Writeri nesmú mať
prekrývajúce sa write scopes.

## Otvorené metodické body

- dokončiť klasifikáciu historických párov '05' bez zmeny ich obsahu;
- vyriešiť kolízie AR/Q ID podľa
  'tracks/METHODOLOGY/00_IDENTIFIER_COLLISION_LEDGER.md';
- pri Git baseline pripraviť presnú migračnú mapu;
- pred v3.18 vytvoriť jeden konsolidovaný SK/EN release register;
- po prvom vedeckom míľniku nového workflow overiť, či error rows,
  batch gate a RC audit dávajú dostatočnú auditovateľnosť bez nového churnu.
