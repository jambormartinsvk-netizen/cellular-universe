# Q22a-S2 — preregistrácia sita priamej pary iba v rozpočte `Delta N_eff`

**Stav pred behom:** `PRIPRAVENÉ; bez fyzikálneho skóre`  
**Cieľ:** sprísniť S1 tým, že priamy produkt môže vstúpiť iba do parnej
reliktn ej zložky, nie nahradiť štandardné fotóny ani neutrína.

## Rozklad dnešnej radiácie

Pri zmrazených A1 vstupoch sa radiačný obsah rozdelí na

```text
X_r,std = omega_gamma [1+0.2271 N_eff,std]/h^2,
X_s      = omega_gamma [0.2271 Delta N_eff]/h^2,
X_r = X_r,std + X_s.
```

`X_r,std` má pevné štandardné riedenie `a^-4`. Iba para `X_s` dostane priamy
zdroj `f_R q`; ostatný transfer ide do popola. Pri dnešnej `Delta N_eff=0.0535`
je parná rezerva o viac než dva rády menšia než celý radiačný rozpočet.

## Očakávanie

K1 (`f_R=0`) zostane pozitívna. K2 (`f_R=1`) musí pri spätnom behu zlyhať
prakticky okamžite. Horná hranica `f_R,max,steam` bude výrazne pod S1
`0.0043831`; nepredstavuje fit, iba nutnú podmienku kladnosti registrovanej
parnej hustoty až po rekombináciu.

## PASS / STOP

* **PASS sita:** rozklad sa algebraicky sčíta na pôvodné `X_r`, K1 je
  pozitívna, K2 zlyhá a hranica je nájdená.
* **K2 STOP v A1:** neprejde, ak kontinuálne priamo produkuje voľnú paru.
* **K3:** priamy parný podiel je len prísne obmedzený; to ešte neurčuje
  mikrofyzický podiel ani nevykonáva BBN/CMB likelihood.

## Limity

Interný limit 4.5 s, vonkajší limit 10 s, najviac 200 000 RK4 krokov na
trajektóriu. Po prvom behu sa urobí samostatne preregistrovaná konvergencia.
