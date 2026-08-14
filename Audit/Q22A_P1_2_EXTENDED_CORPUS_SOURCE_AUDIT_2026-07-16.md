# Q22a/Q18 P1.2 — rozšírený audit zdrojov v hlavnom a nespracovanom korpuse

**Vstup:** predregistrácia
`Questions/Q22A_P1_2_EXTENDED_CORPUS_AUDIT_SCOPE_SK.md`.  
**Rozsah:** hlavný SK/EN dokument, relevantné A16 návrhy, `Nespracovane` a
staršie fyzikálne audity nájdené cieleným vyhľadávaním.  
**Verdikt:** `P1 STOP POTVRDENÝ V PREHĽADANOM RELEVANTNOM KORPUSE; ŽIADNY NOVÝ P2-READY KANDIDÁT.`

## Nález A — A12 opisuje tepelnú okrajovú podmienku, nie zdrojový operátor

Hlavný dokument A12 uvádza, že para bola pri Planckovej genéze v rovnováhe,
potom sa odpojila, a z `g*=106.75` vypočíta podmienené `Delta N_eff=0.0535`.
Uvádza aj odhad `Gamma/H=(T/T_P)^3`. Tento text nedáva:

- lokálny stav `chi` s evolučnou rovnicou;
- `C_g(T,H,...)` alebo jeho collision kernel;
- energetický rezervoár a párové `-S_g^mu/+S_g^mu`;
- mechanizmus, ktorý zdroj obnoví pri exite alebo prežije 1280 e-foldov.

Nie je teda P2-ready operátorom. Je to staršia **podmienená termodynamická
interpretácia**, platná iba ak sa zdrojová história neskôr odvodí.

Navyše `Audit/fyzikalny_audit_bunkoveho_priestoru_2026-07-13.md`, riadky
216–233, priamo ukazuje, že kúpeľ odpojený pred približne 1280 e-foldmi sa
zriedi faktorom `exp(-5120)`. Vyžaduje produkciu/retermalizáciu pri exite,
zdroj počas fázy, alebo opravu počtu e-foldov. Tým sa A12 nemôže použiť ako
dôkaz hotového dnešného reliktu.

## Nález B — A16 návrhy potvrdzujú iba existujúci `F->C` transfer

`Nespracovane/A16_K1_kovariantne_zobrazenie_SK_v3.18_NAVRH.md` explicitne
deklaruje rozsah „Q vytvára iba CDM“ a zapisuje `Q^nu=Gamma rho_f u_c^nu`.
Relativistické `r` má iba štandardné baryónovo-radiačné kolízie, nie bunkový
zdroj. Dokument navyše priznáva, že kovariancia nevysvetľuje mikroskopický
pôvod `Gamma`. Preto nepokrýva zdroj pary ani lokálny exit clock.

## Nález C — nespracované tvrdenia o zhode `N_eff` nie sú mechanizmus

`Nespracovane/sud_14_slabin_a_latex_ns.md` a `krok_D_registrovy_balik.md`
obsahujú staršie slovné obhajoby kompatibility čísla `N_eff=3.10` s dátami.
Neobsahujú však `C_g`, `T_e^(mu nu)`, dynamický exit ani párový ledger.
Nemôžu preto zmeniť P1 verdict. Ak sú v napätí s novším fyzikálnym auditom,
platí novší auditný rozsah: kompatibilita vloženého čísla nie je odvodenie
jeho pôvodu.

## Kontrolná tabuľka P1 polí

| Zdroj | Lokálny stav | Rezervoár | Evolúcia | Ledger do pary | Vypnutie | Verdikt |
|---|---|---|---|---|---|---|
| A12 Plancková genéza/`g*` | nie | nie | iba škálovací odhad `Gamma/H`, nie dynamický systém | nie | nie | `NIE P2-READY` |
| A16 `Q=Gamma rho_f` | `rho_f` áno | palivo áno | áno pre `F->C` | nie pre paru | nie pre skorý impulz | `PARTIAL; NIE P2-READY` |
| staré `N_eff` obhajoby | nie | nie | nie | nie | nie | `NIE P2-READY` |

## Záver a status starších formulácií

P1.1 neprehliadla existujúci zdrojový zákon. P1.2 potvrdzuje, že relevantné
staršie texty dávajú najviac podmienenú rovnovážnu hranicu a existujúci
neskorý `F->C` ledger. Nedávajú fundamentálnu funkciu pary.

Staršie dokumenty sa nemažú. Odteraz však veta „A12 odvodzuje dnešné
`Delta N_eff=0.0535`“ smie znamenať iba **podmienený výpočet po zadanom
vzniku/decouplingu**, nie odvodenú zdrojovú históriu. Fundamental A4 zostáva
P1 STOP, kým Q4/Q8 alebo Q23 nedodá nový explicitný mikrofyzický vstup.

