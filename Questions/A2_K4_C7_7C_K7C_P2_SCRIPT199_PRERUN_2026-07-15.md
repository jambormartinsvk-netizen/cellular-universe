# SCI-A2K4-C7G5-K7C-P2-MLEDGER — predbeh skriptu 199

Dátum: 2026-07-15  
Typ: `EXPLORATORY_CAUSAL_DIAGNOSTIC`  
Skóre: `NONE`  
Stav pri zápise: skript 199 ešte neexistuje a nebol spustený

## Čo sa počíta — ľudskou rečou

Child 185 zopakuje už registrovanú najjemnejšiu NID/deep RK4 trajektóriu a
odovzdá tri stavy `x=-25,-24.875,-24.75`. Skript 199 najprv vyžaduje ich
presnú paritu so zmrazeným P1 raw JSON. Potom na každom stave rozloží
problematickú rovnicu `M'` na deväť už existujúcich sčítancov.

Cieľom je zistiť, či nekonvergenciu môže spôsobiť strata číslic pri sčítaní
veľkých protichodných členov. Nevykonáva sa nová fyzika, nemení sa RHS a
nepridáva sa ďalší integračný bod.

## Deväť nemenných členov

1. `(-q-2) M`
2. `D/2`
3. `(1.5 Ob - Wg load_fraction) Ug`
4. `(0.25 Wg inv1r - 0.5 Og) dg`
5. `-0.5 Ob db`
6. `-0.5 Oc dc`
7. `Of df`
8. `-2 On sigma_fs`
9. `(1.5 delta Of (beta_f+2) + 3 Of g) Uf`

Poradie je totožné s výrazom `M'` v skripte 197. Skript musí vyžadovať, aby
obyčajný ľavostranný súčet bol bitovo zhodný so serializovaným `rhs["M"]`
z child 185. Nezhoda je `REVIEW_PROVENANCE_OR_TERM_DECOMPOSITION`, nie dôvod
na uvoľnenie tolerancie.

## Tri súčtové cesty a doplnková referencia

1. pôvodný ľavostranný float64 súčet;
2. `math.fsum` tých istých deviatich float64 členov;
3. primárna 80-dps referencia: členy znovu vyhodnotené z toho istého
   float64 stavu, ale s registrovanými desatinnými background parametrami,
   a sčítané cez `mpmath.fsum`;
4. doplnková 80-dps referencia: iba presný súčet už vypočítaných float64
   členov. Tá izoluje čistú chybu sčítania od chyby pri tvorbe členov.

Vysoká presnosť neopravuje ani neaudituje chybu ODE stavu. Testuje len
aritmetiku `M'` na už daných float64 stavoch.

## Predregistrované rozhodovanie

Stredná očakávaná hodnota sa neurčuje. Povinné výstupy pre každý checkpoint:

- všetkých deväť členov, znamienko a absolútna veľkosť;
- obyčajný súčet, `math.fsum` a obe HP referencie;
- `sum_abs_terms/abs(full_HP_sum)`;
- absolútna chyba oboch float64 súčtov voči plnej HP referencii;
- `plain_error/fsum_error` voči plnej HP referencii;
- rovnaké chyby voči HP súčtu identických float64 členov;
- škálovaná chyba vzhľadom na integračnú mierku `M`.

Rozhodovací prah ostáva pôvodný:

- ak zlepšenie voči plnej 80-dps referencii je `>=10` na každom aktívnom
  checkpointe, smie vzniknúť samostatná K7c.3e evolučná podkoľaj;
- tento výsledok ešte nie je PASS K7c. K7c.3e musí následne zlepšiť aj
  100/200/400 konvergenciu;
- ak je faktor `<10` na ktoromkoľvek aktívnom checkpointe, jednoduché
  `math.fsum` vysvetlenie je v tomto rozsahu mŕtve;
- nefinite hodnota, timeout, iný zoznam členov, nesúlad child/P1 checkpointu
  alebo nezhoda s `rhs["M"]` znamená REVIEW bez fyzikálnej smrti K4.

## Fail-closed provenance

| Artefakt | Očakávaný SHA-256 |
|---|---|
| skript 185 | `CE75B6DB373F70701C7B35650CEB663C430197F2ED237A7346E7EBB666982686` |
| skript 183 | `90F177DCD8AC612524AB9DD3DBA4516EC7A3805F4DE46682BEBE5F9D566EA7C8` |
| skript 179 | `8F45DC698817992E4FB2B859A7CAFA49D225B4F7F5FD54B07F88CA99059BD441` |
| skript 197 | `088B4CD58F57A30BD061D30042BA3E2CB5021DF9BF320003ED8291D86FB6C022` |
| P1 raw JSON | `A5A94550BB7542090D6244237326404A5A5CD2298D4D70A53C061B2A6B791BA5` |

Child musí skončiť historicky očakávaným REVIEW výsledkom K7c.3c a exportovať
presne tri konečné checkpointy. P1 raw JSON sa nemení a používa sa iba na
paritnú kontrolu.

## Povinné limity a formálne brány

- child 185: interný limit 20 s, jeho seed source 15 s, seed child 6 s;
- subprocess limit 22 s;
- skript 199: interný limit 30 s;
- externý limit: 40 s, kontrola procesu najneskôr po 10 s;
- RHS cap zostáva v child 185;
- výsledný JSON sa zapíše fail-closed do novej cesty a nesmie prepísať
  existujúci súbor.

Pred fyzikou sú povinné: presný inventár čísla 199, kontrola neprítomnosti
markera `__K7C3D_CONTINUE__`, jediný `__main__`, `py_compile`, CLI `--help`,
JSON smoke-test bez child fyziky a kontrola všetkých hashov. Každý Python
príkaz má samostatný externý timeout.

## Ak výsledok vyjde podľa vetiev

- `>=10` všade: iba založiť a predregistrovať K7c.3e; nič ešte nevkladať do
  produkčnej RHS bez samostatného auditu.
- `<10` niekde: zdokumentovať smrť jednoduchej fsum príčiny a pokračovať
  samostatne algebraickým preusporiadaním, lokálnou tuhosťou/eigenmódmi alebo
  vyššou pracovnou presnosťou.
- technický/provenance problém: opraviť iba formálnu chybu novým číslom;
  nemeníť prah ani fyzikálnu interpretáciu.

