# REGISTER 05 — SK aktualizácia po A3/M-012 a K3a.0

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; staršie pravidlá AR1–AR7 sa nemenia

## Kontrola duplicity

AR8 pridáva fyzikálne pravidlo pre povinnú piatu silu; AR6 už oddeľuje
úrovne dôkazu, ale neurčuje zaobchádzanie s akciou vynútenou silou. AR9
pridáva GitHub -> Zenodo reťazec a bezpečnú migráciu dokumentácie; AR5 už
chráni nemennosť publikovanej verzie, ale neobsahuje Git commit/tag ani mapu
presunov. Nové pravidlá preto AR1–AR7 neduplikujú.

## AR8 — Povinná sila sa nemaže, neodvodená sila nenesie výsledok sama

Ak lokálna akcia alebo zákon zachovania vynúti piatu silu, musí byť zahrnutá
v backgrounde aj perturbáciách so správnym znamienkom. Jej existencia nie je
automatický dôvod smrti. Koľaj však nesmie prežiť vymazaním povinného člena,
ani rušením nezávislou post-data brzdou. Alternatívny momentum transfer musí
pochádzať z jednej kovariantnej akcie, prejsť nulovým limitom, stabilitou a
ukázať `G_eff` pred fitom `S8`. Kým jeho veľkosť neodvodí mikrofyzika, je to
priznaný parameter/lešenie, nie predikcia.

## AR9 — Git commit je povinný predchodca Zenodo vydania

Pred každým novým Zenodo vydaním musí existovať skontrolovaný Git commit a
release tag v kanonickom repozitári. Manifest vydania obsahuje commit, tag,
changelog a SHA-256. Dokumenty sa nepresúvajú bez inventára, mapy stará cesta
-> nová cesta a kontroly odkazov. Generované cache a lokálne závislosti sa
necommitujú. Git história ani Zenodo záznam sa neprepisujú silou.

## Aktualizácia otázok

| ID | Otázka | Stav |
|---|---|---|
| Q20 | Aký je úplný perturbatívny uzáver toku A1? | `OTVORENÁ V NOVOM TVARE.` K5/K1 je mŕtva M-012. K3a.0 prešla akciou, backgroundom a high-k stabilitou; K3a.1 musí odvodiť plné rovnice a `G_eff`. |
| Q35 | Prežila K5/K1 CMB-normalizovanú A3 rastovú bránu? | `NIE — MŔTVA M-012.` Konzervatívne hybridné `S8=0.9836–1.0063`; záchrana vyžaduje pokles `A_s` o 23–26 %. Nejde o tvrdenie plnej vlastnej likelihood. |
| Q36 | Existuje zdravá energy+momentum akcia bez úplnej závislosti od K5/K1 sily? | `ČIASTOČNE ÁNO.` `f=-f1(phi)rho_c+eta Z^2` presne reprodukuje A1 a pre `eta>=0` prešla prvou stabilitou. `G_eff<=G` ešte nebolo dokázané. |
| Q37 | Ako sa dokumentácia napojí na GitHub a Zenodo? | `NAPLÁNOVANÉ.` Najprv inventár a mapa presunov, potom bezpečný Git staging, validácia, commit/tag a až následne Zenodo s changelogom. |

## Neskorším auditom obmedzené staršie formulácie

- `PREŽÍVA A2-K5.1 — 60/100; A3 červená` bol správny predbežný stav. Po
  CMB-normalizovanej rastovej bráne ho nahrádza `MŔTVA M-012`.
- Tvrdenie, že `f2=eta Z^2` automaticky dáva slabú gravitáciu, platí v
  jednoduchej literárnej limite `f1=0`. Naša A1 reprodukcia má `f1!=0`, preto
  musí K3a.1 odvodiť spoločné `G_eff`; prenos jednoduchého vzorca by bol
  neplatný.
- Požiadavka „bez povinnej piatej sily“ sa spresňuje: piata sila je prípustná,
  ak ju vynúti mikrofyzika; model nemá byť úplne závislý od neodvodeného
  člena a nesmie ho post-data rušiť.

Podrobnosti: `Audit/A3_K5_K1_MRTVA_CMB_normalizovana_rastova_brana_M012.md`
a `Audit/A2_K5_K3a_0_akcna_backgroundova_stabilitna_brana.md`.
