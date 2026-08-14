# Akčný plán v3.18 — po PASS C7.7c-K7b

Dátum: 2026-07-15  
Aktívna koľaj: **A2-K4**  
Jemná hĺbka: **66.5/100**  
Stav: **K7a PASS, K7b PASS, K7c nasleduje**

## Dokončené

1. K7a — algebraická a Jacobiánová transformácia projektovaných `D,M`.
2. K7b.1/K7b.2 — štvorpovrchový coefficient/constraint audit a identifikácia NID flooru.
3. K7b.3a — mŕtva mäkká HP podkoľaj; dôvod zachovaný.
4. K7b.3b.1 — tvrdo viazaný fyzikálny `mu` register prešiel NID deep/shallow.
5. Skript 176 — konečný NID/NIV deep/shallow PASS bez ODE.

## Bezprostredný postup

1. **K7c.1:** preregistrovať presnú 13-zložkovú projektovanú bázu a jej obojsmerné mapovanie na druhový stav.
2. **K7c.2:** overiť počet stupňov voľnosti, determinant/rank transformácie a počiatočný round-trip na štyroch plochách.
3. **K7c.3:** zaviesť krátku jednosegmentovú ODE iba na NID/deep s checkpointmi, constraint ledgerom a pevnými vnútornými/vonkajšími limitmi.
4. **K7c.4:** ak NID/deep prejde, zopakovať NID/shallow, potom NIV/deep a NIV/shallow.
5. **K7c.5:** až po štvorpovrchovom evolučnom PASS overiť step/tolerance convergence a deep/shallow endpoint agreement.
6. **K7d:** úplný 13-komponentový activity verdikt; iba úplný PASS môže zvýšiť jemnú hĺbku z `66.5` na `66.7/100`.

## Stop pravidlá

- Prvý fyzikálny alebo numerický neúspech zastaví ďalšie povrchy a vytvorí zdokumentovanú podkoľaj.
- Timeout/parser/solver failure je REVIEW, nie smrť K4.
- Smrť vyžaduje reprodukovateľný rovnicový alebo fyzikálny rozpor pri nezmenených preregistrovaných prahoch.
- Všetky skripty a podprocesy musia mať časové limity.

## Neskorší release postup

Po uzavretí zvoleného rozsahu K4 nasleduje upratanie dokumentácie do logických adresárov, kontrola SK/EN, manifesty a SHA-256, commit na GitHub a až potom Zenodo balík s changelogom podľa existujúcich publikačných kritérií.
