# Metodické pravidlá a register otázok — verziované checkery a segmentované dôkazy (SK)

Dátum: 2026-07-15  
Rozsah: dodatok; staršie pravidlá sa nemenia

## AR56 — Korpusový checker je nemenný číslovaný snapshot

Očakávaný počet súborov a karanténny slovník patria ku konkrétnej hash revízii checkeru. Po vedomom pridaní skriptov sa starý checker ticho neprepisuje: dostane stav `SUPERSEDED`, zachová sa jeho dôvod a hash a vytvorí sa nový číslovaný nástupca. `NOT_IN_QUARANTINE` nie je technický ani fyzikálny PASS.

## AR57 — Nezávislé prípady sa checkpointujú pred ďalším prípadom

Ak monolitický agregátor obsahuje viac nezávislých vedeckých alebo negatívnych prípadov a timeout by zahodil už hotové dôkazy, každý prípad sa spustí s vlastným interným aj externým limitom a jeho nemenný výstup, exit a hash sa uložia pred ďalším prípadom. Konečné spojenie vykoná offline agregátor bez child procesov. Timeout jedného prípadu je REVIEW iba daného prípadu a nemaže hotové výsledky ostatných.

## Q81 — Ktorý korpusový checker je aktuálny po K7b P0?

**Odpoveď:** skript 196. Auditoval 200 ostatných Python súborov, eviduje 68 karanténnych položiek, syntaxové chyby iba 118/119, neúplný vstup iba 186 a nespustil žiadny cieľový skript. Staršie 188, 191 a 194 sú reprodukovateľné snapshoty so stavom `SUPERSEDED`.

## AR58 — Relevantný error-ledger preflight je povinný pred každým príkazom

Pred zostavením alebo spustením Python či shell príkazu sa musia podľa jeho syntaxe a účelu aktívne vyhľadať relevantné riadky v `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md` a ich prevencia sa musí premietnuť do príkazu. Nestačí ledger doplniť až po chybe. Opakovanie známej chyby dostane nový riadok s odkazom na pôvodnú chybu a žiadny fyzikálny verdikt. Pre PowerShell `foreach` sa výstup najprv uloží do premennej a až potom pipuje; pri číslovaných skriptoch sa presná cesta získava filtrovaným inventárom `.py` bez `__pycache__`.

## Q82 — Čo presne dokázal K7c P1 a čo ostáva otvorené?

**Odpoveď:** čistý skript 197 bez legacy adaptívneho bloku reprodukoval 100/200 rozdiel `1.44327268769215e-6`, 200/400 rozdiel `3.93123964056996e-6`, pomer `0.367129155088317` a dominanciu `M`. Reprodukcia je PASS, ale fyzikálna konvergencia je REVIEW, pretože rozdiel neklesol pod `1e-6` a RK4 pomer nie je v `8–32`. K4 ostáva živá na `66.5/100`; otvorenou otázkou P2 je, či nekonvergenciu spôsobuje sčítanie členov `M'`, algebraická kondícia, tuhosť alebo pracovná presnosť. Checker 198 je aktuálny snapshot: 202 ostatných `.py`, 69 karanténnych položiek.

## AR59 — Stanice, route prefixy a viac-kolové audity sa nesmú zamieňať

A1, A2, A3, ... sú spoločné kontrolné stanice. Koľaj je voľba mechanizmu na konkrétnej stanici a route prefix je usporiadaná cesta už zvolených koľají. Výsledok závislý od predchádzajúcej koľaje patrí do svojho route prefixu a nesmie sa bez nového auditu zovšeobecniť na rovnako pomenovanú koľaj na inom backgrounde. PASS jednej koľaje umožňuje prechod na ďalšiu stanicu; STOP jednej koľaje nezabíja stanicu, kým žije iná koľaj. Ak všetky koľaje na stanici zomrú, route prefix končí s presne uvedenou poslednou dosiahnutou stanicou.

Auditná diskusia je nemenný viac-kolový thread. Pôvodný audit a odpoveď sa neprepisujú; ďalšia námietka, odpoveď, dôkaz alebo reaudit dostanú nové číslo kola. Konfliktné audity ostávajú zachované a riešia sa samostatným adjudikačným threadom. Aktuálny súhrn odkazuje na nemenné kolá a na posledné platné rozhodnutie.

## Q83 — Aký adresárový model je autoritatívny pre budúce stanice a audity?

**Odpoveď:** primárny strom je vnorená cesta `A1/A1Kx/A2/A2Ky/A3/...`; vnútorné podkoľaje zostávajú v `SUBTRACKS` pri stanici, na ktorej sa testujú. Každá stanica, koľaj a podkoľaj má `PASS`, `REVIEW`, `STOP`, `HISTORY`, `AUDIT_THREADS` a `ARTIFACTS`. Každý auditný thread uchováva kolá `audit → response → evidence → open points → reaudit`. Podrobný návrh je `Questions/DIRECTORY_STRUCTURE_AND_MIGRATION_PROPOSAL_V2_STATIONS_ROUTES_AND_AUDIT_THREADS_2026-07-15.md`; fyzická migrácia sa začne až po path/SHA manifeste a Git baseline.

## AR60 — Váha výsledku sa zmrazí pred behom a korelované kontroly sa nezdvojujú

Každý vedecký výsledok sa pred spustením priradí jednej verziovanej gate s
fyzikálnou váhou. Váhy jedného scorecardu majú súčet 100. Po výsledku sa
nesmú meniť bez novej verzie, dôvodu a prepočtu všetkých súrodencov. Viac
riadkov, monitorov alebo reprodukčných kontrol toho istého claimu nemôže
získať viacnásobnú váhu. Scorecard oddelene uvádza validovanú podporu PASS,
blokujúcu evidenciu FAIL, otvorenú alebo technickú váhu a auditované pokrytie
PASS+FAIL. FAIL dôležitej brány má vysokú rozhodovaciu hodnotu, ale nepridáva
podporu teórii. Skóre nie je pravdepodobnosť pravdivosti.

## AR61 — HISTORY je povinný append-only event ledger

Každá stanica, koľaj, podkoľaj, auditný thread a verzia spoločného jadra má
HISTORY/00_EVENT_LEDGER.md. Zmena stavu, skóre, rozsahu, cesty, názvu,
obmedzenia alebo supersession dostane novú nemennú udalosť so starou a novou
hodnotou, dôvodom, spúšťacím auditom, dotknutými claimami a hashmi dôkazov.
Staršia udalosť sa neprepisuje; oprava používa väzbu CORRECTS. Navigačný
aktuálny súhrn môže ukazovať posledný stav, ale nenahrádza historický dôkaz.

## AR62 — Spoločné Python jadro je verziované a výsledok pinne presnú verziu

Zdieľaná fyzika, numerika a auditné brány sa môžu extrahovať do
scripts/baseScripts/vNNN, ale autoritatívna verzia sa po použití nemení.
Každý run manifest uvádza verziu a SHA-256 importovaných modulov. Oprava
vytvorí novú verziu, changelog, nový výsledok a rozdielový audit; starý
výsledok sa označí LIMITED alebo SUPERSEDED, nikdy sa ticho neprepíše.
Spoločné jadro nesmie preniesť PASS medzi rozdielnymi backgroundmi bez
samostatného route-conditioned auditu.

## Q84 — Prečo sme na K7c a prečo nemáme K1c?

**Odpoveď:** K1 až K6 boli alternatívne numerické formulácie tej istej C7.7c
brány, nie jednotné etapy a/b/c. Až siedma formulácia bola rozdelená na K7a
(projektovaná algebra/Jacobián), K7b (počiatočné koeficienty a constrainty
bez ODE), K7c (evolúcia a konvergencia) a plánovanú K7d (úplná
aktivita/constrainty). K1 sa zastavila na 28 nerozlíšených activity
kontrolách pred týmto členením. Jednotné gate ID C7-G0 až G9 odteraz
explicitne označia aj nedosiahnuté testy; historické názvy sa nemenia.

## Q85 — Akú váhu má aktuálny výsledok K7c P1?

**Odpoveď:** v scorecarde C7-W1 má K7 konzervatívne validovanú podporu 40/100
(G0 až G3), blokujúcu evidenciu 20/100 (G5 konvergencia), otvorenú váhu
40/100 a auditované pokrytie 60/100. Ľudské „8 z 10 PASS“ nie je 80 %, pretože
viaceré riadky reprodukovali ten istý claim alebo boli iba monitory. C7
scorecard sa nesčítava s historickou hĺbkou celej A2-K4 66.5/100.

## Q86 — Ako sa bude externe auditovať neúspešný RK4 pomer?

**Odpoveď:** route-conditioned balík zmrazí skript 197, checkpointy
100/200/400, rovnice a konvencie, normu, predbehové očakávania, raw výstup,
dependency a SHA manifest, známe obmedzenia a otvorené otázky. Audit má
preveriť orientáciu pomeru, asymptotický režim, vhodnosť normy, grid closure,
dominanciu M, netautologické constrainty a nezávislú implementáciu. Diskusia
pokračuje v nemenných kolách audit → response → evidence → reaudit.
## AR63 — Lokálne P0/P1/P2 musí mať v centrálnom registri namespaced ID

Krátke označenie P0, P1 alebo P2 sa smie použiť iba v dokumente, ktorého
hlavička jednoznačne určuje route a uzol. Centrálny plán, route register,
externý audit a HISTORY používajú prefix účelu: SCI vedecký výpočet, ORG
organizácia, BASE spoločné jadro, AUD audit a ZEN publikovanie. Historické
vedecké P2 K7c má stabilné ID SCI-A2K4-C7G5-K7C-P2-MLEDGER; organizačné
ORG-V2-P2 ho nesmie nahradiť ani zmeniť.

## Q87 — Kde je autoritatívny register skratiek a identifikátorov?

**Odpoveď:** slovenský register je
Questions/00_ABBREVIATION_AND_IDENTIFIER_REGISTER_SK.md a anglické zrkadlo
Questions/00_ABBREVIATION_AND_IDENTIFIER_REGISTER_EN.md. Vysvetľujú stanice,
route prefixy, K1–K7/K7a–d, C7-G0 až G9, P0/P1/P2 namespace, fyzikálne a
numerické skratky aj stavové kódy. Pri konflikte s presným fyzikálnym
odvodením má prednosť odvodenie; glossary je navigačný register.

## Q88 — Zmenila reorganizácia staré vedecké P2?

**Odpoveď:** nie. SCI-A2K4-C7G5-K7C-P2-MLEDGER zostáva nový číslovaný iba
diagnostický rozklad deviatich členov M-prime na identických uložených
checkpointoch, s porovnaním pôvodného float64 súčtu, math.fsum a 80-dps
referencie, bez zmeny RHS a bez bodov. Skript 186 ostáva
DO_NOT_RUN_TECHNICAL. Scope a SHA zdrojov sú v
Questions/A2_K4_K7C_P2_SCOPE_FREEZE_AND_ORG_NAMESPACE_2026-07-15.md.
## AR64 — Presná algebraická identita má prednosť pred numerickým rezíduom

Pred fyzikálnou interpretáciou malého alebo rastúceho numerického zvyšku sa
musí overiť, či príslušný koeficient nie je z registrovaných definícií
algebraicky identicky nulový. Float64 zvyšok vzniknutý odčítaním členov,
ktoré sa majú presne rušiť, nie je nový fyzikálny efekt. Oprava smie nahradiť
výraz presnou nulou iba po samostatnom symbolickom, provenance a
vysokopresnom audite; následná evolúcia musí zostať samostatnou bránou so
všetkými pôvodnými prahmi. Mŕtva summation vetva sa tým neoživuje.

## Q89 — Čo uzavrelo K7c P2?

**Odpoveď:** skript 199 zachoval bitovú paritu P1 stavov a RHS a zistil, že
`math.fsum` zlepšilo všetky tri checkpointy iba `1×`. Preto je
`K7c.3e fsum-only` mŕtva. P2 zároveň lokalizovalo problém do dvoch
koeficientov, ktoré majú byť podľa backgroundových definícií presne nulové.
K4 ostáva REVIEW na `66.5/100`; P2 nemá skórový účinok.

## Q90 — Aký je povolený krok po P2?

**Odpoveď:** iba P3a-A bez ODE: presný algebraický dôkaz, 80-dps numerická
kontrola a provenance audit oboch koeficientov. Až PASS povoľuje P3a-B,
ktorá zmení iba tieto dve identity na nulu a zopakuje RK4 100/200/400 s
nezmenenými bránami `8–32` a `diff200/400 < 1e-6`.

## Q91 — Aký je výsledok P3a-A a P3b?

**Odpoveď:** P3a-A dokázala obe koeficientové identity presne racionálne a
pri 80 dps s maximálnym normalizovaným rezíduom `2.5069e-81`. P3b po
source-delta dôkaze jedinej povolenej zmeny dosiahla `diff200/400 =
3.0308221211e-14` a klasický RK4 pomer `16.004121`. Obe predregistrované
krokové brány prešli. Hĺbka ostáva `66.5/100` a celý C7-G5 ostáva PARTIAL
PASS/REVIEW, pretože neprebehla metódová ani tolerančná konvergencia.

## Q92 — Ktoré staršie tvrdenie P3b obmedzila a čo je ďalší povolený krok?

**Odpoveď:** P1 zostáva platnou reprodukciou legacy float64 zápisu, ale už
nie je dôkazom fyzikálnej nekonvergencie kanonických rovníc. Fsum-only vetva
zostáva mŕtva. Ďalej sa smie iba po novej preregistrácii dokončiť metódová a
tolerančná časť G5, potom netautologická G4 a napokon NID/NIV × deep/shallow
G6. P3b sama nepovoľuje CMB/S8 ani pridelenie celej váhy G5.

## Q93 — Čo je P4a a aký je jej aktuálny stav?

**Odpoveď:** P4a je preregistrovaná, ale ešte nespustená metódová a
tolerančná časť C7-G5. Oddelene porovná DOP853 pri dvoch toleranciách a
Radau s P3b RK4-grid400; štyri rozdiely musia byť `<=1e-8`. Každý prípad má
vlastný limit a JSON, agregát je offline. Pred fyzikou musia prejsť
source-delta 210, formálny preflight a versioned corpus checker 211.

## AR65 — Aktívna route musí mať konečnú finish line a rozpočet iterácií

Každá aktívna koľaj musí uvádzať konečný zoznam zostávajúcich brán,
pracovný progress oddelený od vedeckého score a maximálny počet technických
opráv na bránu. Technická chyba nevytvára nové centrálne Q ani novú
fyzikálnu podkoľaj. Po prvej implementácii a najviac dvoch technických
opravách sa vydá PASS, fyzikálny STOP alebo REVIEW_BLOCKED s architektonickým
rozhodnutím. Zmena finish line, script/Q stropu alebo rozpočtu vyžaduje nový
dodatok a HISTORY; nesmie vzniknúť tichým pridávaním prípon.

## Q94 — Ako ďaleko je A2-K4 od dokončenia?

**Odpoveď:** jemná hĺbka je `66.5/100`, strict support C7-W1 `40/100` a
pracovný WBS-1 progress `48/100`. Zostáva šesť balíkov: dokončenie G5,
potom G4, G6, G7, G8 a G9. Realistický odhad je 25–40 pracovných dní,
optimistický 15–20 a rizikový 2–3 mesiace. Aktuálne existuje najviac skript
208; 209–212 sú iba plán. Q99 a flat script 240 sú stropy aktuálnej A2-K4
bez samostatnej revízie alebo novej fyzikálnej vetvy.
