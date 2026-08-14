# A2-K4 / C7.7c / K7c.3a — technická smrť skriptu 181

Dátum: 2026-07-15  
Stav skriptu 181: **MŔTVA TECHNICKÁ PODKOĽAJ**  
Dopad na K4: **žiadny fyzikálny verdikt**

Skript 181 mal zostaviť presný lineárny operátor bez ODE. Pri probe fyzikálnym jednotkovým vektorom `e_j` však zdedil ODE safety cap. Pre zložku s integračnou škálou rádovo `1e-23` znamená fyzikálna jednotka normalizovanú amplitúdu rádovo `1e23`, a guard preto správne skončil s `normalized safety cap exceeded` ešte pred výpočtom operátora.

Povolená oprava je presná pre lineárny systém:

```text
A[:,j] = (f(S_j e_j)-f(0))/S_j.
```

Každý probe má normalizovanú amplitúdu 1. Nejde o FD krok ani lokálnu aproximáciu; z linearity je výsledok identický s jednotkovým stĺpcom. Rovnice, integračná škála, seed a všetky diagnostické prahy ostávajú nezmenené.

