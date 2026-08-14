# A3/Q20 — stav a akčný plán po smrti A2-K6

**Dátum:** 2026-07-13  
**Kanonický stavový dokument od M-013**  
**Nahrádza pre budúce riadenie:**
`Questions/A3_STAV_A_AKCNY_PLAN_KANONICKE_CISLOVANIE.md`  
**Starší súbor sa nemaže; zachováva stav pred K6.1.**

## 1. Aktuálny stav koľají

| Koľaj | Stav | Rozhodujúci dôvod |
|---|---|---|
| A2-K1 | `MŔTVA M-009` | superhorizontový relatívny mód približne `2.014e5` |
| A2-K2 | `MŔTVA M-008` | záporné barotropické `c_s^2` |
| A2-K3 | `MŔTVA M-010` | relatívny mód `448.789` |
| A2-K4 | `MŔTVA M-011` | kladný relatívny eigenmód každého dvojfluidného energy-frame |
| A2-K5 | `MŔTVA M-012` | povinná príťažlivá sila, `S8=0.9836–1.0063` |
| **A2-K6** | **`MŔTVA M-013`** | `mu_cc>1` pre celé `eta>=0`; rast s `eta` silnie |
| **A2-K7** | **`AKTÍVNA — čaká K7.0`** | konečno-entalpický dynamický mediátor |
| A2-K8 | `ČAKÁ` | produkcia počtu konštantne hmotných častíc |
| A2-K9 | `ČAKÁ` | jeden produkčno-rozptylový operátor |
| A1-K2/A2-K10 | `ČAKÁ` | samostatná backgroundová prahová/fázová vetva |

## 2. Čo M-013 zakazuje opakovať

Za novú koľaj sa nesmie vyhlásiť:

- iný grid tej istej kladnej `eta Z^2` väzby;
- porovnanie papierového `G_cc` bez prepočtu z `rho_c` na `rho_c_hat`;
- ponechanie momentum tlmenia pri vymazaní akciou vynútenej sily;
- tvrdenie, že väčšie `eta` môže pomôcť bez vyvrátenia spojitej
  lineárno-frakčnej vety M-013;
- návrat k machine-labelu `FAIL` nulového limitu zo skriptu 48; ten bol
  numerickým artefaktom a skript 49 ho auditne opravil.

## 3. Aktívny krok A2-K7.0 — dokument problému a výber akcie

**Cieľ:** zaviesť skutočný tretí dynamický komponent `M`, ktorý má vlastný
`T_M^{mu nu}`, kladnú entalpiu a konečný relaxačný čas, aby recoil nebol
delený near-vacuum entalpiou paliva a popol po prenose nemusel niesť trvalý
skalárny náboj.

Najprv sa musí uzavrieť ledger

```text
dot(rho_f)+3H(rho_f+p_f) = -Q_fM,
dot(rho_M)+3H(rho_M+p_M) =  Q_fM-Q_Mc,
dot(rho_c)+3H rho_c      =  Q_Mc,
sum_A Q_A^mu             = 0.
```

Mediátor sa nesmie „integrovať preč“ pred kontrolou jeho energie a hybnosti.

## 4. Poradie brán K7

### K7.0 — akcia a ledger

1. založiť samostatný dokument problému K7 a uviesť, ktorú príčinu
   `C1/C4/C5` mechanizmus odstraňuje;
2. ako prvú realizáciu s najväčšou šancou preveriť kanonický masívny
   skalárny mediátor s kladnou kinetikou a konečnou dobou života;
3. zapísať lokálnu akciu vrátane interakcie `palivo-M` a `M-popol`, nie iba
   fenomenologické dve `Q`;
4. ak sa objavia fyzikálne odlišné realizácie, použiť AR10 a vytvoriť nové
   rovnocenné koľaje; neukrývať skalár, vektor a otvorený kinetický systém
   pod jedným fitom.

**Kill brána:** bez lokálnej akcie alebo uzavretého stress-energy ledgera je
K7 mŕtva ešte pred numerikou.

### K7.1 — background

1. reprodukovať celkovú A1 históriu bez tichého zahodenia `rho_M`;
2. explicitne určiť, či `rho_M` patrí do registrovaného `rho_f`, alebo je
   novou kozmologickou zložkou;
3. skontrolovať `rho_M>=0`, `rho_M+p_M>0` a limit nulovej väzby;
4. samostatne vykázať odchýlku `H(z)` a ranný podiel mediátora.

**Kill brána:** nepriznaná zmena A1 alebo potreba záporného energetického
podielu.

### K7.2 — lineárna stabilita

1. odvodiť úplné gauge-invariantné kontinuity, Eulerove rovnice a
   Einsteinove constrainty troch dynamických zložiek;
2. vypočítať kinetickú a gradientovú maticu z akcie;
3. overiť adiabaticitu a relatívne rýchlostné módy na superhorizonte;
4. dokázať, že eliminácia mediátora nevracia zosilnenie `Gamma/delta`;
5. skontrolovať nulový limit proti už známym mŕtvym K1/K3/K4.

**Kill brána:** duch, `c_s^2<0`, pól, alebo rastúci relatívny mód.

### K7.3 — rast a dáta

1. až po K7.2 odvodiť presné `G_ij`, trenie a scale dependence;
2. spustiť spoločnú CMB-normalizovanú Boltzmannovu implementáciu;
3. vyhodnotiť, či mechanizmus znižuje `S8` bez neprípustného ISW,
   lensingu alebo zmeny ranej fyziky;
4. nový parameter neprispôsobovať po výsledku bez uvedenia penalizácie.

## 5. Dokumentačný paralelný krok

Pred GitHub/Zenodo vydaním:

1. rozdeliť dokumenty do logických adresárov `Audit`, `Questions`,
   `theory/SK`, `theory/EN`, `scripts` a neskôr `results` bez straty aliasov;
2. vytvoriť mapu presunov a nemenný manifest SHA-256;
3. zachovať všetky M-008 až M-013 skripty, výstupy a dôvody smrti;
4. commitnúť GitHub pred Zenodo;
5. k publikovanej verzii pridať changelog; pri nezmenenom fundamente zostať
   vo vetve v3.18, pri zmene fundamentu použiť verziu 4.

## 6. Nasledujúci vykonateľný krok

`A2-K7.0a`: napísať konkrétnu lokálnu akciu prvého masívneho skalárneho
mediátora, odvodiť jeho stress-energy ledger a ešte pred fitovaním rozhodnúť,
či vôbec môže presne reprodukovať A1 s konečnou kladnou `rho_M`.

