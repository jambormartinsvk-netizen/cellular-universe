# A2 — kanonický stav, skóre a dôvod smrti K1 až K11

**Dátum:** 2026-07-13  
**Nahrádza iba stavové tabuľky, nie historické odvodenia.**

## Význam skóre

Skóre `N/100` je **hĺbka najvzdialenejšej preukázateľne absolvovanej
auditnej brány**, nie pravdepodobnosť pravdivosti. Mŕtva koľaj si ponecháva
maximálne dosiahnuté skóre, aby bolo vidieť, ako blízko sa dostala pred
rozhodujúcou stenou. Smrť má vždy prednosť pred číslom.

| Rozsah | Najvyššia zdokumentovaná úroveň |
|---:|---|
| `0–9` | iba opísaná hypotéza |
| `10–19` | konkrétny kovariantný ansatz alebo operátor |
| `20–29` | background/ledger alebo prvá analytická lokálna brána |
| `30–39` | akčná/kolízna a základná stabilitná brána |
| `40–49` | úplné lineárne rovnice, znamienka a nulové limity |
| `50–59` | superhorizont a high-k systém |
| `60–69` | presný efektívny rast alebo `G_ij` |
| `70–79` | CMB-normalizovaná rastová brána |
| `80–89` | plný Boltzmann/likelihood |
| `90–99` | systematiky, nelinearity a nezávislé predikcie |
| `100` | všetky predregistrované brány pre verziu prešli |

## Úplná stavová tabuľka

| Koľaj | Stav | Max. hĺbka | Základ koľaje | Dôvod smrti alebo aktuálna stena |
|---|---|---:|---|---|
| A2-K1 | `MŔTVA M-009` | `45/100` | `Q_c^mu=Gamma rho_f u_c^mu`; energetický tok bez kopanca CDM | recoil paliva delený `delta rho_f`; gauge-invariantný relatívny mód zosilnel `2.014e5` |
| A2-K2 | `MŔTVA M-008` | `25/100` | striktne barotropické palivo | `c_s^2=w=-0.97703<0`; analytická high-k gradientová nestabilita |
| A2-K3 | `MŔTVA M-010` | `45/100` | energetický tok v pokoji paliva, `Q_c^mu || u_f^mu` | superhorizontový relatívny mód zosilnel `448.789` kvôli `Gamma/delta` |
| A2-K4 | `MŔTVA M-011` | `50/100` | entalpicky vážený energy-frame dvoch tekutín | kladný fyzikálny relatívny eigenmód pre každý kladný pomer hustôt; plný zisk `1.08028e5` |
| A2-K5 | `MŔTVA M-012` | `75/100` | kanonický skalár + konformne meniaca sa hmotnosť CDM | akciou povinná príťažlivá piata sila; CMB-normalizovaná projekcia `S8=0.9836–1.0063` |
| A2-K6 | `MŔTVA M-013` | `60/100` | derivatívna energy+momentum akcia `-f1 rho_c+eta Z^2` | v celom zdravom intervale `eta>=0` ostalo `mu_cc>1`; spojitý no-go pred Boltzmannom |
| A2-K7 | `PREŽÍVA K7.0` | `30/100` | skutočný konečno-entalpický mediátor `palivo -> M -> popol` | **nie je mŕtva**; chýba pôvod `Q1,Q2`, `delta Q`, šum/pamäť a úplný superhorizont/high-k test; collision-only tlmenie popola je iba `0.9100` |
| A2-K8 | `ČAKÁ` | `5/100` | produkcia počtu konštantne hmotných častíc | **nie je mŕtva**; chýba lokálna akcia, creation pressure, entropia a šum |
| A2-K9 | `ČAKÁ` | `5/100` | jeden operátor pre produkciu aj elastický rozptyl | **nie je mŕtva**; chýba operátor spájajúci obe sadzby bez dvoch post-data parametrov |
| A1-K2/A2-K10 | `ČAKÁ` | `5/100` | prahový/fázový tok meniaci časový profil backgroundu | **nie je mŕtva**; najprv musí prejsť novou A1, BBN a CMB históriou; zmena fundamentu znamená verziu 4 |
| A2-K11 | `PREŽÍVA IBA FORMULAČNÚ BRÁNU` | `15/100` | A1-K1 energetický tok plus nový ortogonálny elastický momentum transfer | **nie je mŕtva**; skript 45 má neplatný `PASS`, predložené znamienko je anti-drag, chýba pravidelný lokálny operátor a rozlíšený constraint-preserving test |

## Dôvody smrti po jednej vete

- **K1:** near-vacuum recoil vytvoril obrovský `1/delta` rast.
- **K2:** záporná barotropická zvuková rýchlosť vytvorila high-k rast.
- **K3:** zmena bezmomentového rámca zmenšila, ale neodstránila
  `Gamma/delta` nestabilitu.
- **K4:** algebraický priemer rýchlostí nevytvoril nový nosič a zachoval
  kladný relatívny eigenmód.
- **K5:** zdravá akcia odstránila fluidný pól, ale vynútila príliš silnú
  príťažlivú piatu silu.
- **K6:** derivatívny operátor nemenil znamienko efektívnej gravitácie v
  zdravom intervale; `mu_cc` zostalo nad jednotkou.

K7–K11 nemajú „dôvod smrti“, pretože ešte neboli vyhlásené za mŕtve. Tabuľka
preto namiesto prázdneho poľa uvádza ich aktuálnu stenu. Ak niektorá zomrie,
jej riadok sa nezmaže; doplní sa kód, presná nerovnosť, skript a výstup.

## Obmedzenia starších stavov

- starý katalógový stav K6 `PREŽÍVA 40/100` bol neskôr obmedzený rozsudkom
  M-013;
- starý stav K7 `ČAKÁ` bol neskôr obmedzený výsledkom
  `PREŽÍVA K7.0 — 30/100`;
- všetky `PASS` tvrdenia skriptu 45 sú od tohto auditu obmedzené na
  „program dobehol“ a nesmú sa citovať ako fyzikálny prechod bránou;
- podrobné fyzikálne základy K1–K10 zostávajú v
  `Audit/A2_KATALOG_KOLAJI_K1_AZ_K10_ZROZUMITELNY_SUMAR.md`.

