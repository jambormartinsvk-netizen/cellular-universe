# A2-K4.3b-RG BR3B-2f-5 — dodatok stability voči odrezaniu

Dátum: 2026-07-14  
Nadväzuje na: `A2_K4_3B_RG_BR3B2F5_FULL_MIXED_CHAIN_AUDIT.md`  
Rozsudok: **PASS POTVRDENÝ**

Tento dodatok vznikol samostatne, pretože Windows patch helper odmietol
bezpečné doplnenie už vytvoreného hlavného auditu. Hlavný audit sa nemení.

Ten istý skript 124 bol samostatne spustený s `standard-order=4`, `5` a `6`.
Všetky tri behy skončili `PASS_FULL_MIXED_CHAIN_THROUGH_COMMON_FUEL`, vždy
s `26/26` kontrolami a hodnosťou `36/36` pre NID aj NIV.

| Odrez | NID škálované rezíduum | NIV škálované rezíduum |
|---:|---:|---:|
| 4 | `1.553e-15` | `9.564e-16` |
| 5 | `1.695e-15` | `7.149e-16` |
| 6 | `1.384e-15` | `9.173e-16` |

Maximálna absolútna zmena ľubovoľného common-fuel koeficientu voči odrezu 4:

| Mód | `order 4` vs `5` | `order 4` vs `6` |
|---|---:|---:|
| NID | `4.265e-16` | `1.874e-16` |
| NIV | `2.300e-16` | `2.822e-16` |

Rozdiel je na úrovni numerického zaokrúhlenia. BR3B-2f-5 PASS preto nie je
artefaktom najnižšieho povoleného odrezu. Stav A2-K4 ostáva **ŽIVÁ**, skóre
ostáva **60/100 = G6** a nasleduje BR3B-2g.

