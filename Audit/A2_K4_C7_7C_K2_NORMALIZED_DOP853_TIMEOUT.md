# A2-K4 C7.7c-K2 — timeout normalizovanej DOP853 koľaje

**Dátum:** 2026-07-14  
**Skripty:** 142, 143  
**Rozsudok:** `TIMEOUT_UNCLOSED`  
**K4:** živá; `66.5/100`

K2 použila predregistrované škálovanie všetkých 13 premenných podľa ich
počiatočnej analytickej amplitúdy. Syntax oboch skriptov prešla. Activity
audit však nedostal výsledný JSON do limitu 50 s a skončil exit kódom 124.

Výsledok nie je fyzikálny FAIL. Ukazuje, že explicitný DOP853 pri požiadavke
rozlíšiť amplitúdy od `10^6` po `10^-24` je v tejto normalizácii príliš
drahý. Zodpovedá to už registrovanému vysokému `nfev` hlbokého NIV behu.

Wrapper 143 mal rovnaký 50-sekundový limit ako detský beh, takže ho ukončil
na hranici bez rezervy na serializáciu. Ďalšia podkoľaj musí mať kratší
vnútorný limit než vonkajší.

## K3

C7.7c-K3 nemení rovnice, stav, scaling, toleranciu ani activity floor. Mení
iba explicitný DOP853 na implicitný `Radau`, vhodný pre možnú stiffness, a
použije limity `45 s` pre evolúciu, `50 s` pre auditný wrapper a `60 s`
zvonka.

