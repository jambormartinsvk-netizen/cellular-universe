# A2-K12 — re-entry audit po zavedení pravidla momentov produkcie

## Rozsudok

**Bez postupu v sekvenčnej hĺbke. Rodič K12 zostáva živý cez K12-K2/K3 na 10,0/100 = G1.**

- K12-K1 zostáva mŕtva M-016.
- K12-K2 zostáva otvorená, ale červená.
- K12-K3 zostáva aktívna hypotéza a preferovaná dcéra.

## Čo potvrdzuje starý audit

Skript 65 a zachovaný audit ukázali:

- presne symetrické opačné konformné náboje bez produkčného operátora dávajú nulový čistý skalárny tok;
- celkový lineárny gravitačný mód zostáva GR-like;
- nábojovo-separačný mód má vlastnú nenulovú odozvu;
- jednoduchá symetria preto sama nereprodukuje A1 tok ani automaticky neznižuje `S8`.

Tieto výsledky a M-016 sa nemenia.

## Nové obmedzenie po K8.1

Návrh K12-K3 používa samostatnú párovú produkciu

```text
fuel -> c+ + c-,
S_+=S_->0,
m_+=m_-=constant.
```

Na backgrounde možno zvoliť

```text
m_+ S_+ + m_- S_-=Gamma rho_f,
```

a tým reprodukovať A1 energetický tok bez čistého skalárneho náboja. To je životaschopná backgroundová myšlienka.

Podľa AR46 však dva skalárne zdroje `S_+`, `S_-` neurčujú dva štvorvektory `Q_+^mu`, `Q_-^mu`, pôrodné rámce, tlakové momenty ani korelovaný šum páru. K12-K3 preto stále neprešla úplný G2 ledger.

## Prečo opačný náboj problém automaticky nerieši

Presné zrušenie sily platí pre center-of-mass mód iba na symetrickej podvariete. Rozdiel

```text
Delta_sep = delta_+ - delta_-
```

je samostatný fyzický separačný mód. Opačné sily naň pôsobia s opačnými znamienkami a môžu ho zosilniť aj vtedy, keď celková hustota vyzerá zdravo. Preto treba testovať celú dvojzložkovú bázu, nie iba súčet `delta_+ + delta_-`.

## Stav dcér

| Dcéra | Stav | Dôvod |
|---|---|---|
| K12-K1 | `MŔTVA M-016` | presná symetria bez produkcie ruší tok; skript a dôkaz sa zachovávajú |
| K12-K2 | `OTVORENÁ — ČERVENÁ` | asymetria obnoví tok, ale aj netienenú silu a potenciálne segregation/isocurvature |
| K12-K3 | `AKTÍVNA HYPOTÉZA` | párová produkcia môže niesť energiu nezávisle od náboja, ale chýba úplný collision kernel |

## Čo musí priniesť K12-K3.1

1. lokálny párový kernel s presným prahom a sadzbou;
2. nultý aj prvý moment pre `c+` a `c-`;
3. spoločnú spätnú reakciu paliva a presnú celkovú konzerváciu;
4. tlak, anizotropný stres a korelovaný shot noise páru;
5. akčnú maticu opačných síl bez ghosta a gradientovej nestability;
6. pravidelný center-of-mass aj separačný superhorizontový mód;
7. nulový limit náboja, v ktorom zostane čistá párová produkcia.

Bez týchto položiek nemá zmysel opakovať kozmologický rastový výpočet.

## Rozhodnutie o priorite

K12-K3 je fyzikálne konkrétnejšia než rodičia K8/K9, ale stále vyžaduje nový mikrofyzický kernel. Nie je preto lacnejšou okamžitou cestou než návrat ku K4. Zostáva v mikrofyzickom backlogu spolu s K8-Fkin a K9.

