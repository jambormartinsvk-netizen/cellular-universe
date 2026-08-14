# Q22a/Q18 — audit existencie skorého zdroja pary ako funkcie

**Otázka:** môže existovať funkcia skorého zdroja pary, ktorá rešpektuje
zachovanie energie, dá konečný malý relikt `Delta N_eff` a po BBN už nemá
neskorú injekciu?  
**Verdikt:** `ÁNO — EXISTUJE AKO EFEKTÍVNA FLRW TRIEDA HISTÓRIÍ; LOKÁLNA KOVARIANTNÁ REALIZÁCIA EŠTE ČAKÁ NA CLOCK/REZERVOÁR`.

**Erratum rozsahu:** `Audit/ERRATUM_Q22A_EARLY_STEAM_FUNCTION_COVARIANCE_SCOPE_2026-07-16.md`.

## Konštruktívny dôkaz existencie

Použime `x=ln a` a označme relatívnu parnú hustotu `rho_s`. V homogénnom
FLRW priestore má zdrojová rovnica tvar

```text
d rho_s/dx + 4 rho_s = S_s(x),
```

kde `S_s=C_s/H`. Nech `g(x)` je ľubovoľná hladká, nezáporná funkcia s
konečnou podporou výhradne pred BBN, napríklad hladký bump s podporou
`[x_*-w,x_*+w]` a `x_*+w < x_BBN`. Definujme

```text
S_s(x) = A g(x),
A = rho_s(0) / integral_{-infinity}^0 [exp(4u) g(u) du].
```

Potom presné riešenie je

```text
rho_s(x) = exp(-4x) integral_{-infinity}^x [exp(4u) S_s(u) du].
```

Pre `g>=0` je `rho_s>=0`; po konci podpory zdroja sa para riedi presne
`a^-4`. Voľbou konečnej pozitívnej hodnoty `rho_s(0)` — tu tej, ktorá
zodpovedá registrovanému `Delta N_eff=0.0535` — teda existuje nekonečne veľa
takých funkcií.

## Kovariantný a energetický ledger

Funkcia nie je porušením GR, ak má zdrojový rezervoár `e`, definovaný lokálny
clock/stav a platí

```text
nabla_mu T_s^(mu nu) = +S_s^nu,
nabla_mu T_e^(mu nu) = -S_s^nu,
S_s^nu = C_s(x) u^nu.
```

Súčet je presne nula. Pri dostatočne pozitívnej počiatočnej energii rezervoára
zostáva aj `rho_e` kladná. V skorej fáze môže `e` znamenať iba zatiaľ
neodvodený exit/reheatingový rezervoár Q18/Q23; **nesmie** sa bez ďalšieho
dôkazu stotožniť s neskorým A1 transferom `q=lambda rho_f`.

## Čo tým bolo a nebolo dokázané

| Tvrdenie | Stav |
|---|---|
| Existuje matematicky hladký, pozitívny a skončený skorý zdroj pary | PASS — konštruktívny dôkaz |
| Dá sa napojiť na kovariantné zachovanie energie | PASS — párový štvorvektorový ledger |
| Nevytvorí M-015 neskorú kontinuálnu injekciu | PASS, ak podpora skončí pred BBN |
| Konkrétny tvar `g`, čas `x_*`, šírka `w` a rezervoár sú odvodené zo siete | OTVORENÉ |
| Ide o parameter-free predikciu `Delta N_eff` | NIE — dnešná hodnota je zatiaľ okrajová podmienka, nie odvodenie |
| Prejde BBN+CMB a poruchami | OTVORENÉ — treba Q18/Q23 a plný likelihood |

## Hranica dôkazu a ďalší krok

Toto je dôležitá odpoveď na otázku existencie: známe fyzikálne zákony samy
nezakazujú skorý ukončený zdroj. Pozorovania a ďalšie zákony môžu zúžiť jeho
triedu `g`, ale z dát bez mikrofyziky nevznikne jediná predikčná funkcia.

M0 provenance audit teraz potvrdil, že súčasná teória takú mieru udalostí a
rezervoár ešte nedefinuje. Ďalší správny krok preto nie je hľadať ľubovoľný
fit `g`, ale založiť jazvovú alebo exit/reheating koľaj s lokálnym `chi`,
`T_e^(mu nu)` a `C_s(chi,I_i)`. Až po tomto M0 prechode sa `x_*`, `w` a
amplitúda smú porovnať s BBN, CMB a `P_AB(k)`.

**Dôkaz:** `Audit/Q22A_M0_CLOCK_AND_RESERVOIR_PROVENANCE_AUDIT_2026-07-16.md`.
