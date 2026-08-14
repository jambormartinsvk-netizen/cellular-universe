# A2-K4 / C7.7c-K7a — predregistrácia projected-Jacobian brány

**Dátum:** 2026-07-14  
**Skóre:** `66.5/100`, bez možného prírastku v tejto bráne  
**Zákaz:** žiadna ODE evolúcia pred úplným PASS.

## 1. Povinné poradie

1. zostaviť priamy fyzikálny `A_y` bázovými vektormi;
2. zostaviť `T,T'` z analytických `Omega_A'`;
3. overiť `T'` centrálnym backgroundovým rozdielom s krokmi `10^-4,10^-5,10^-6`;
4. zostaviť `A_proj=(T'+T A_y)T^-1`;
5. nezávisle zostaviť explicitný projected RHS z odvodených rovníc `D',M'` a jeho bázový Jacobian;
6. porovnať oba projected Jacobiany;
7. až potom vyhodnotiť conditioning a radiačný nulový limit.

## 2. Brány

- `Omega_fs>0` na každom povrchu;
- konečné `T,T',T^-1,A_y,A_proj`;
- `cond_2(T)<10^4`;
- relatívna chyba analytickej `T'` proti najlepšiemu FD kroku `<10^-8`;
- relatívna Frobeniova chyba explicitného a transformačného `A_proj <10^-12`;
- maximálna absolútna chyba týchto matíc `<10^-10`;
- spektrum zmrazenej časti `T A_y T^-1` súhlasí s `A_y` relatívne `<10^-12`;
- `max|A_proj|<10^4` ako numerická safety brána, nie fyzikálny invariant;
- radiačný nulový limit má maximálne koeficientové rezíduum `<10^-14`.

## 3. Interpretácia spektra

Rovnosť spektra sa vyžaduje iba pre zmrazenú podobnostnú časť. Úplný `A_proj` obsahuje `T'T^-1`; jeho okamžité spektrum sa nesmie porovnávať s `A_y` ako invariant ani používať ako samostatný stability verdict.

## 4. Povrchy

Brána sa vykoná pre `NID/NIV × deep/shallow`. Keďže Jacobian závisí od backgroundu a nie od amplitúdy lineárneho módu, NID/NIV na rovnakom povrchu musia dať rovnaké `A_y,T,A_proj` v rámci roundoff chyby. Nezhoda znamená chybu implementácie.

## 5. Stop pravidlo

Prvý FAIL zastavuje postup k evolúcii. Oprava znamienka, `T'`, rekonštrukcie alebo backgroundovej derivácie musí byť zdokumentovaná ako nová revízia skriptu; prahy sa po výsledku nemenia.
