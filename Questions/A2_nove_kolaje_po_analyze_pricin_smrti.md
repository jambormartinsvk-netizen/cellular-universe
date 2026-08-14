# A2/Q20 — nové a spresnené koľaje po analýze príčin smrti

**Dátum:** 2026-07-13  
**Vstup:** `Audit/A2_analyza_hlavnych_pricin_smrti_kolaji.md`  
**Pravidlo:** žiadna koľaj nesmie iba premenovať mŕtvy fenomenologický `Q^mu`

## 1. Rozlíšenie nových a spresnených smerov

Tri staršie čakajúce smery K5/K2–K5/K4 sa nemažú ani neduplikujú. Na základe
pitvy dostávajú presnejšie podkoľaje. Dve ďalšie vetvy sú skutočne nové, ale
jedna z nich mení background a preto nepatrí pod čisté A2 dokončenie A1-K1.

## 2. Poradie podľa šance na úspech

| Poradie | Koľaj | Konštrukcia | Ktoré príčiny odstraňuje | Stav |
|---:|---|---|---|---|
| 1 | **A2-K5/K3a** | lokálna `f(n_c,phi,X,Z)` akcia s `Z=u_c^mu partial_mu phi`; súčasný energy+momentum transfer navrhnutý pre `G_eff<=G` | C1, C2, C4, C5 | **PRVÁ NOVÁ KOĽAJ NA TEST** |
| 2 | **A2-K5/K4a** | konečno-entalpický mediátor `M`: palivo -> M -> popol; `T_M^mu nu` sa nezahadzuje | C1, C2, C4, C5 | `ČAKÁ` |
| 3 | **A2-K5/K2a** | produkcia počtu častíc popola s konštantnou konečnou hmotnosťou; tok cez `n_c`, nie `m_c(phi)` | C1, C2, C5 | `ČAKÁ` |
| 4 | **A2-K5/K6** | jeden mikrofyzický operátor viaže produkciu konštantnej hmoty s elastickým momentum transferom, ktorý tlmí rast | C1, C2, C5 | `ČAKÁ`; bez spoločného operátora neprípustné dva fit parametre |
| 5 | **A1-K2/A2-K6a** | prahový alebo nukleačný `Gamma_eff(a)`, ktorý sa vypne pred neskorým rastom | C1, C3, C5 | `NOVÁ BACKGROUNDOVÁ VETVA`; pravdepodobne v4 |

## 3. A2-K5/K3a — derivatívna weak-gravity koľaj

### Hypotéza

Použiť všeobecnú lokálnu akciu CDM prúdu a skalára

```text
S_int = integral sqrt(-g) f(n_c,phi,X,Z),
X=-(partial phi)^2/2,
Z=u_c^mu partial_mu phi.
```

`Z`-závislosť poskytne fyzikálny momentum transfer, ktorý nie je určený iba
gradientom hmotnosti. Primárne práce ukazujú, že zdravé podtriedy môžu mať
`G_eff,c<G`, pričom obsahujú energiu aj hybnosť.

### Povinné brány pred numerikou

1. presná reprodukcia alebo jasne kvantifikovaná odchýlka od A1-K1;
2. nulový tlak CDM a zachovaný počet častíc;
3. kladná kinetická matica a gradienty;
4. žiadny `1/delta` pól v kanonických premenných;
5. `G_eff,c<=G` na škálach `q=30–300` bez post-data rušenia dvoch nezávislých
   veľkých členov;
6. superhorizontové testy skriptov 39/41 zopakované pre novú akciu.

### Prečo je prvá

Je to jediná aktuálna akčná trieda s publikovaným mechanizmom, v ktorom
momentum exchange môže vytvoriť slabšiu gravitáciu namiesto povinnej
príťažlivej sily K5/K1. Ide o spresnenie staršej K5/K3, nie jej duplikát.

## 4. A2-K5/K4a — konečno-entalpický mediátor

### Hypotéza

Zaviesť pole alebo prúd `M` s

```text
rho_M+p_M >= epsilon_M rho_M >0,
c_s,M^2>=0,
Q_f->M + Q_M->c + Q_total = 0.
```

Palivo neodovzdáva hybnosť priamo prachu. Mediátor nesie vlastnú hybnosť,
relaxuje a až potom vytvára konštantne hmotný popol.

### Stena

Ak sa `M` algebraicky integruje von a znovu vznikne člen `Gamma/delta`, koľaj
je iba prezlečená K1–K4 a okamžite zomiera. Ak `rho_M` nie je zanedbateľná,
musí sa prepočítať background.

## 5. A2-K5/K2a — produkcia počtu konštantne hmotného popola

### Hypotéza

```text
nabla_mu(n_c u_c^mu)=S_n,
m_c=konštanta,
Q_c=m_c S_n,
```

pričom `S_n` vznikne z lokálneho rozpadového alebo neadiabatického
produkčného operátora. Po produkcii popol nemá skalárny náboj, takže nevznikne
`1+2 beta^2`.

### Povinné doplnky

- spätná reakcia na palivo;
- creation pressure a entropia;
- fluktuačno-disipačný šum, ak ide o otvorený systém;
- dôkaz, že `Q` má správny časový profil pri `w_f približne -1`.

Bez týchto členov by išlo iba o fenomenologický zdroj a koľaj by zopakovala
chybu C4.

## 6. A2-K5/K6 — produkcia plus elastický momentum transfer

Táto koľaj kombinuje konštantne hmotnú produkciu s elastickou výmenou hybnosti,
ktorá môže tlmiť neskoré zhlukovanie bez zmeny backgroundu na prvej úrovni.
Je prípustná iba vtedy, ak jedna bunková mikrofyzika odvodí produkčný aj
rozptylový koeficient. Dva nezávisle fitované koeficienty po zhliadnutí `S8`
by boli neprípustné lešenie.

## 7. A1-K2/A2-K6a — prahový tok

Mikrofyzický prah, fázový prechod alebo nukleácia môže dať `Gamma_eff`, ktoré
je veľké iba v obmedzenom intervale a pred neskorým rastom sa vypne. Tým sa
odstráni integrovaný constant-`Gamma` problém aj dnešná veľká väzba.

Táto koľaj však nereprodukuje presne A1-K1 s `Gamma=lambda H0` pre všetky
časy. Musí sa preto založiť už na backgroundovej úrovni ako A1-K2 a pri
fundamentálnej zmene patrí do verzie 4.

## 8. Predregistrované poradie práce

1. dokončiť A3 pre aktuálne živú K5/K1, aby sa rozhodlo M-012;
2. bez ohľadu na výsledok pripraviť akčný ansatz a kinetickú maticu K5/K3a;
3. ak K5/K3a zomrie, pokračovať K5/K4a;
4. potom K5/K2a;
5. K5/K6 iba s odvodenou väzbou oboch sadzieb;
6. A1-K2/A2-K6a otvoriť iba ako explicitnú novú backgroundovú vetvu.

## 9. Primárne opory

- [Kase a Tsujikawa — všeobecné `f(n_c,phi,X,Z)` interakcie](https://arxiv.org/abs/2005.13809).
- [Amendola a Tsujikawa — energy+momentum coupling a slabšia gravitácia](https://arxiv.org/abs/2003.02686).
- [Pourtsidou, Skordis a Copeland — akčné triedy couplingov](https://arxiv.org/abs/1307.0458).
- [Beltrán Jiménez et al. — elastický dark-sector momentum transfer a `S8`](https://arxiv.org/abs/2106.11222).
