# REGISTER 05 — SK dodatok k A2-K7.1a-K3.1-K2.1

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; existujúce pravidlá sa nemenia

## Kontrola duplicity

AR15 odlišuje rekonštrukciu od mikrofyziky, AR16 vyžaduje lokálne
`Theta`, AR17 úplnú pozitívnu Onsagerovu/noise maticu a AR18 odlišuje
maximálnu hĺbku od akceptovanej. Neurčujú však status voľného rozmerového
transportného gridu ani povinnosť vetviť fyzikálne odlišné stavy kúpeľa.
AR19 a AR20 preto nie sú duplicitné.

## AR19 — Rozmerová existencia s voľným transportným gridom nie je mikrofyzika

Kladný existenčný bod získaný voľbou rozmerových transportných
koeficientov dokazuje iba neprázdnu konzistentnú oblasť. Koeficient sa
nesmie zapísať ako predikcia ani fitovať na `S_8`, kým nie je odvodený z
collision integrálu alebo retarded spektrálneho kernelu. Ak koeficient
závisí od `H,rho` alebo iného stavu, pred lineárnou bránou musia byť určené
aj jeho poruchy.

## AR20 — Termálny, vákuový a netermálny bath sú samostatné podkoľaje

Lokálny termálny/KMS white-noise limit, vákuový kvantový farebný kernel a
netermálny farebný bath sa nesmú ticho zamieňať. Každý musí mať vlastný
retarded/noise kernel, memory rozsah a stress-energy ledger. Energia a tlak
kúpeľa musia byť zahrnuté v A1 účtovníctve alebo musí byť explicitne
dokázané, kde už sú započítané či renormalizované.

## Q47 — Prežila K3.1-K2.1 rozmerovú backgroundovú bránu?

**Stav:** `ÁNO, IBA EXISTENČNE — 39/100.`

Na 24 bodoch gridu prešlo 18. Všetky body s `ell_hat=1,10,100` mali kladný
determinant, kladnú skalárnu entalpiu, `|A|<1` a bulk korekciu pod 10 %.
Body s `ell_hat=0.1` zlyhali iba na `|A|<1`. `ell_hat`, bath, absolútny
noise a mikrofyzický kernel však odvodené neboli. Akceptované skóre K7
zostáva `30/100`; nasleduje K3.1-K2.2-K1.

