# KMPC-084–086 — BI/k=.15 high-precision holdout assembly: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Interný audítor a tvorca skriptov:** Codex (OpenAI)  
**Stav:** `REVIEW_C2_BI_K0p15_EXACT_DRIVER_ASSEMBLY_REQUIRED`

KMPC-084/PF-089 a KMPC-085/PF-090 skončili v smoke pred fyzikou.
Prvé official CLI KMPC-086/PF-091 skončilo v argument garde bez `--output`;
ten istý immutable runner potom s kanonickou cestou technicky dokončil.
Raw SHA-256 je
`54F9A116EEC0EEB0EB7CEAE96A49F943F5EAE3DD63F12257155752B90B65649E`.

## Overený výsledok

| Kontrola | Výsledok |
|---|---|
| driver matica/konštanta | `FE5E5A7C...127240F`, identická s KMPC-083 |
| driver solve | jeden, 80 dps, HP replacement PASS |
| holdout zostavenie | 80 dps, `16x104`, SHA `2DE8C982...06E2DE` |
| holdout riadky vo fite | `0` |
| ostatné zmrazené brány s HP náhradami | PASS |
| `Einstein_0i[7]` absolútne rezíduum | `5.497017386772301e-17` |
| `Einstein_0i[7]` affine term norm | `1.8203510784855354e-8` |
| `Einstein_0i[7]` relatívne rezíduum | `3.0197567116259885e-9 > 1e-9`, FAIL |
| celý holdout | FAIL; worst relative `Einstein_0i[7]` |

Oproti KMPC-083 (`3.019756782389909e-9`) sa relatívna hodnota zmenila iba
o približne `7.08e-17` absolútne, teda výsledok je prakticky nezmenený.
Tým je vylúčené, že hranicu vytvorilo až posledné float64 zostavenie alebo
odčítanie holdoutu.

## Audit rozsahu a interpretácie

- binary64 upstream koeficienty boli prenesené presne cez `as_integer_ratio`;
- exact affine matica holdoutu vznikla z nulového a 104 jednotkových probe,
  nie pridaním constraintu do solve;
- PF-088 je napravený: ostatné brány sa hodnotia explicitne s HP driver
  replacementom a sú `true`;
- KMPC-086 ešte nezostavil samotnú driver maticu pri 80 dps a upstream M1,
  F0 a background koeficienty stále pochádzajú z binary64 vetvy.

Preto výsledok nie je fyzikálny STOP ani dôkaz zlej rovnice. Ďalší jediný
oprávnený krok je predregistrované 80-dps zostavenie a solve tej istej
104x104 driver matice, následne nezávislý 80-dps holdout. Rovnice, support,
prahy a non-fit status holdoutu sa nesmú zmeniť. C2 ostáva `5/10`, K4
ostáva `60/100`; active technical counter sa po vecnom úspechu resetuje na
`0/10`.
