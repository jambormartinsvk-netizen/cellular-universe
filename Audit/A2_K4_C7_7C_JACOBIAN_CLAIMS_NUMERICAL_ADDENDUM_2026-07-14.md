# A2-K4 / C7.7c — numerický dodatok k auditu Jacobianu 151/152

**Dátum:** 2026-07-14  
**Skripty:** 157 a 158  
**Typ:** nulovo-integračný krížový test; 175 RHS volaní na mód  
**Skóre pred/po:** `66.5/100`  
**A2-K4:** bez zmeny, živá; C7.7c otvorená

## 1. Vykonané kontroly

- fyzikálny Jacobian `J_y[:,j]=rhs(x,e_j)-rhs(x,0)`;
- exaktné diagonálne transformácie `J_env=S_env^-1 J_y S_env` a `J_local=S_local^-1 J_y S_local`;
- centrálne FD v envelope súradniciach s krokmi `10^-4...10^-8`;
- kontrola spektrálneho polomeru a celého zoradeného spektra;
- priama kontrola linearity RHS.

Oba behy skončili verdictom `CAPTURED_C7_7C_JACOBIAN_SPECTRAL_RADIUS_FD_AUDIT` približne za jednu sekundu vnútorného runtime.

## 2. Závislosť od škálovania

| Veličina | NID/deep | NIV/deep |
|---|---:|---:|
| fyzikálny `max|J_y|` | `43.5350` | `43.5350` |
| lokálny `max|J_local|` | `5.5594×10^23` | `9.7018×10^13` |
| obálkový `max|J_env|` | `4.1886×10^14` | `8.8471×10^10` |
| fyzikálny `sigma_max` | `43.9497` | `43.9497` |
| lokálny `sigma_max` | `7.9727×10^23` | `1.4450×10^14` |
| obálkový `sigma_max` | `6.0889×10^14` | `1.3177×10^11` |
| fyzikálny spektrálny polomer | `3.444151542625` | `3.444151542625` |
| lokálna relatívna odchýlka spektra | `3.39×10^-15` | `4.08×10^-15` |
| obálková relatívna odchýlka spektra | `4.85×10^-15` | `2.59×10^-15` |

Tým sa číselne potvrdilo:

1. `max|J|` a SVD sú dramaticky závislé od súradnicovej normy;
2. lokálna škála `max(|y_start|,10^-300)` nie je automaticky lepšia — pri tiny počiatočných komponentoch vytvorila ešte väčší scale span a väčšie maticové prvky;
3. spektrum pri exaktnom podobnostnom prepočte zostáva invariantné na úrovni floating-point chyby.

## 3. FD sweep

### Relatívna Frobeniova chyba voči priamemu `J_env`

| FD krok | NID/deep | NIV/deep |
|---:|---:|---:|
| `10^-4` | `7.20×10^-13` | `4.00×10^-13` |
| `10^-5` | `1.65×10^-12` | `5.72×10^-12` |
| `10^-6` | `6.88×10^-11` | `1.70×10^-11` |
| `10^-7` | `2.70×10^-10` | `5.64×10^-10` |
| `10^-8` | `4.06×10^-9` | `1.33×10^-9` |

Pre striktne lineárny RHS nemá centrálna diferencia truncation chybu z nelineárnych členov; pri zmenšovaní kroku preto dominuje roundoff. Z testovaných krokov bol najlepší `10^-4`. Návrh `epsilon^(1/3)` je rozumné všeobecné východisko pre nelineárny centrálno-diferenčný Jacobian, ale pri tomto lineárnom RHS je priamy bázový Jacobian presnejší a FD vôbec netreba.

### Spektrálny polomer

NID relatívna chyba spektrálneho polomeru bola od `1.8×10^-15` do `3.3×10^-11`; NIV od `9.0×10^-16` do `3.0×10^-15`. Dominantný spektrálny polomer je teda veľmi robustný.

Naproti tomu na NIV sa maximálna odchýlka párovaného zoradeného spektra pri FD krokoch pohybovala od `10^-3` po `0.32`, hoci Frobeniova chyba matice bola malá. To je prejav citlivosti nenormálneho spektra a čiastočne krehkého párovania vlastných čísel. Jednotlivé FD vlastné čísla sa nesmú používať bez pseudospektrálneho/condition auditu.

## 4. Linearita RHS

Pri teste `rhs(0.37y-0.23r) = 0.37rhs(y)-0.23rhs(r)`:

| Mód | max. absolútne rezíduum | relatívne rezíduum |
|---|---:|---:|
| NID/deep | `1.49×10^-16` | `2.25×10^-10` |
| NIV/deep | `1.16×10^-10` | `1.10×10^-16` |

RHS je algebraicky lineárny. NID relatívne číslo je horšie preto, že výsledná kombinácia je sama kompenzovaná a malá; absolútne rezíduum leží na machine-precision úrovni. To súhlasí s nezávislou condition mapou 155/156.

## 5. Konečný rozsudok o predložených tvrdeniach

1. **Veľký envelope FD krok:** všeobecná námietka je správna, ale konkrétny RHS je lineárny a bez stavových vetiev. Problémom je roundoff, nie nelineárna nelokalita.
2. **Miešanie dynamiky s headroomom:** potvrdené. `max|J|`, top couplings, SVD a `f_i/S_i` sú súradnicové diagnostiky.
3. **Condition proxy:** potvrdené ako chybný. FD chyba pri kroku `10^-7` je rádovo `10^-10`, takže cutoff `sigma_max×10^-14` ležal hlboko pod zmeranou chybovou úrovňou. Proxy zostáva stiahnutý.
4. **Lokálne škálovanie:** nie je všeobecným riešením; v tomto teste zhoršilo maticový scale span.
5. **Spektrálny polomer:** potvrdený ako robustná kontrola podobnostnej transformácie, nie ako úplný stability verdict.
6. **Existencia RHS:** námietka je uzavretá; `rhs` existuje a celý reťazec 146→151→157/158 bol spustiteľný.

## 6. Dopad na koľaje

- C7.7c-K4 a K5 ostávajú mŕtve numerické podkoľaje kvôli reálnym timeoutom, nie kvôli fyzikálne veľkému `max|J|`.
- Condition mapa 155/156 a smer K7 ostávajú platné, pretože sú založené na termových cancellation hraniciach fyzikálneho RHS.
- Skóre sa nemení.

