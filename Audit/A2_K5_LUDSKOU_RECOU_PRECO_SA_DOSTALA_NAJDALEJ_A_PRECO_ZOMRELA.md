# A2-K5 ľudskou rečou — prečo sa dostala najďalej a prečo zomrela

**Dátum:** 2026-07-14  
**Kanonický názov:** A2-K5  
**Historické označenie konkrétnej realizácie:** A2-K5/K1  
**Stav:** `MŔTVA M-012`  
**Max. hĺbka:** `75/100`

## 1. Základná predstava

V tejto koľaji už „palivo“ nebolo iba tekutinou, ktorej sme ručne
predpísali, kam má odovzdávať energiu. Palivo bolo opísané ako skutočné
skalárne pole `phi`, ktoré vypĺňa priestor. Popol, teda tmavá hmota, bol
opísaný ako častice, ktorých hmotnosť závisí od lokálnej hodnoty tohto poľa.

Zjednodušený obraz:

> Priestor je vyplnený poľom paliva. Častice popola sú na toto pole
> pripojené tak, že pri zmene poľa sa mení ich hmotnosť. Keď hmotnosť
> častíc rastie, energia, ktorú získali, ubudla z poľa paliva.

Matematicky:

```text
rho_c = m_c(phi) n_c,
beta(phi) = d ln m_c / d(phi/M_Pl).
```

Počet častíc `n_c` sa v tejto realizácii nemení. Mení sa ich hmotnosť
`m_c(phi)`. Tým vznikne požadovaný tok energie

```text
palivo -> popol,
Q = Gamma rho_f,
Gamma = lambda H0.
```

Nebolo to už iba účtovnícke pravidlo. Tok vyšiel z jednej lokálnej akcie a
celková energia a hybnosť sa zachovávali.

## 2. Analógia s lanom

Predstavme si pole paliva a popol ako dva objekty spojené jedným lanom.

- Ťahanie lana mení energiu a hmotnosť popola. To je požadovaný metabolizmus.
- To isté lano však prenáša aj silu medzi časticami popola.

Nemožno povedať:

> Lano bude prenášať energiu, ale nebude prenášať silu.

V jednej konzistentnej akcii sú obe vlastnosti spojené tou istou väzbou
`beta`. Keby sme silu z rovníc odstránili, už by sme neriešili tú istú
teóriu.

## 3. Prečo bola K5 oveľa lepšia než K1–K4

K1–K4 opisovali palivo ako tekutinu veľmi blízku vákuu. Jej inerciálna
hustota bola iba

```text
rho_f+p_f=(1+w_f)rho_f=delta rho_f,
delta=0.02297.
```

Pri prenose hybnosti sa preto objavoval nebezpečný faktor `1/delta`.
Relatívne rýchlosti sa rozbiehali alebo barotropická verzia dostala zápornú
zvukovú rýchlosť.

K5 tento problém odstránila tým, že začala od zdravej akcie:

1. skalár mal kladný kinetický člen;
2. jeho fyzikálna zvuková rýchlosť bola `c_s^2=1`;
3. nevznikol ghost ani gradientová nestabilita;
4. rekonštruované hmotnostné členy boli kladné;
5. nulový limit bez väzby bol regulárny;
6. Einsteinove constrainty boli numericky zachované;
7. superhorizontový relatívny mód neexplodoval;
8. existoval regulárny adiabatický počiatočný mód.

Preto sa K5 dostala až na `75/100`. Nezomrela na algebraickej chybe,
nesprávnom znamienku ani na nestabilite raného vesmíru. Zomrela až pri
neskorom raste štruktúr.

## 4. Kde vznikol problém piatej sily

Keď hmotnosť častice závisí od poľa, častica cíti rozdiely poľa v priestore.
Prehustenie popola zmení skalárne pole a toto pole začne priťahovať ďalší
popol. Popri obyčajnej gravitácii tak vznikne ďalšia príťažlivá sila.

V kvázistatickom limite má približný tvar

```text
G_eff/G = 1 + 2 beta^2 F(k,a),
0 <= F <= 1.
```

Rekonštrukcia požadovaného toku energie dala dnes

```text
beta_0 = 1.52883.
```

V nescreenovanej limite by to znamenalo

```text
1 + 2 beta_0^2 = 5.67466.
```

Skalár má konečnú hmotnosť, takže sila nie je rovnako veľká na každej
mierke. Na testovaných lineárnych mierkach však zostala dostatočne silná na
zvýšenie rastu.

## 5. Prečo nepomohlo „trenie“

Meniaca sa hmotnosť vytvorila v Eulerovej rovnici aj člen podobný treniu.
Samostatne by mierne spomaľoval pohyb popola:

```text
friction-only rast / GR-like rast approximately 0.989.
```

To je približne jednopercentné potlačenie. Piata sila však pôsobila opačným
smerom a bola silnejšia. Po zahrnutí všetkých členov vyšiel rast CDM väčší
približne o šesť percent a hustotne vážený rast všetkej hmoty väčší o

```text
5.196 % až 5.305 %.
```

Teda:

> Trenie trochu brzdilo, ale povinná príťažlivá sila ťahala výrazne
> silnejšie. Výsledkom bolo rýchlejšie, nie pomalšie zhlukovanie.

Nie je dovolené ponechať v rovniciach iba priaznivé trenie. Trenie aj sila
pochádzajú z tej istej akcie.

## 6. Prečo je to opačný smer, než potrebujeme

Cieľom bolo znížiť zhlukovanie približne

```text
S8: 0.87 -> 0.82.
```

K5 však pridala príťažlivú silu a posunula rast nahor. Prvý diagnostický
odhad zo starého základu dal približne

```text
S8 approximately 0.920.
```

Toto číslo nebolo plnou CMB-normalizovanou predikciou. Preto koľaj ešte
nebola zabitá a pokračovala do hlbšej brány.

Konzervatívny CMB-kotvený hybridný screen následne dal

```text
S8 = 0.983642 až 1.006266.
```

Tieto hodnoty tiež nie sú výsledkom plnej vlastnej K5 Boltzmannovej a KiDS
likelihood. CAMB vytvoril CMB-normalizované referenčné spektrum a naň sa
aplikoval akciou odvodený neskorý rast K5. Výpočet bol zámerne nastavený v
prospech koľaje: pod `k=0.01 h/Mpc` sa dodatočný rast vypol.

Aj tak oba výsledky prekročili predregistrovanú screeningovú hranicu

```text
S8_screen = 0.863.
```

## 7. Prečo sa výsledok nedal zachrániť menšou počiatočnou amplitúdou

Pri pevnom transfere približne platí

```text
S8 proportional sqrt(A_s).
```

Na stlačenie výsledku iba po hranicu `0.863` by bolo potrebné znížiť
primordiálnu amplitúdu `A_s` o

```text
23.0 % až 26.4 %.
```

To nie je malá korekcia. Väzba K5 bola pri rekombinácii zanedbateľná, takže
model nemal vlastný mechanizmus, ktorým by primárna CMB amplitúda klesla o
štvrtinu. Pridať nový parameter iba na zrušenie piatej sily alebo zníženie
`A_s` po zhliadnutí výsledku by znamenalo založiť novú koľaj.

## 8. Presný dôvod smrti M-012

A2-K5 zomrela preto, že v konkrétnej registrovanej akcii platilo súčasne:

1. požadovaný tok `palivo -> popol` určoval veľkosť väzby `beta`;
2. tá istá väzba nevyhnutne vytvorila príťažlivú piatu silu;
3. sila prekonala priaznivý trecí účinok;
4. rast hmoty sa zvýšil namiesto požadovaného zníženia;
5. CMB-kotvený konzervatívny screen skončil ďaleko nad registrovanou hranou;
6. záchrana vyžadovala veľký neodvodený posun primordiálnej amplitúdy alebo
   nový rušiaci parameter.

Preto je presný rozsudok:

> **MŔTVA M-012: konkrétna kanonická skalárna akcia s konformne meniacou sa
> hmotnosťou popola pri registrovaných parametroch vytvára povinnú
> príťažlivú silu a príliš veľký neskorý rast štruktúr.**

## 9. Čo M-012 nezakazuje

M-012 neznamená, že:

- každé skalárne pole je mŕtve;
- každá piata sila je zakázaná;
- každá lokálna akcia pre palivo a popol je nemožná;
- backgroundový tok A1 je automaticky chybný;
- tmavá hmota nesmie mať žiadnu mikrofyzickú interakciu.

M-012 zabíja iba mechanizmus, v ktorom sa registrovaný tok realizuje zmenou
hmotnosti popola cez túto konkrétnu konformnú väzbu. Mechanizmus založený na
produkcii počtu častíc, konečno-entalpickom mediátore alebo inom odvodenom
operátore je nová koľaj a musí mať vlastné testy.

Historická `K5/K3a` nebola živou dcérou tejto K5. Taxonomické erratum ju
prečíslovalo na samostatnú A2-K6, pretože zmenila akciu a fyzikálny
mechanizmus.

## 10. Jednovetové zhrnutie

> K5 sa dostala najďalej, pretože po prvýkrát nahradila ručne zvolený tok
> energie zdravou lokálnou akciou; zomrela preto, že tá istá väzba, ktorá
> úspešne premieňala palivo na hmotnosť popola, nevyhnutne vytvorila ešte
> silnejšiu príťažlivosť popola a zvýšila `S8` presne opačným smerom, než
> teória potrebovala.

## 11. Reprodukčné podklady

- `Audit/A2_K5_00_canonical_scalar_action_reconstruction_and_growth_risk.md`
- `Audit/A2_K5_1_uplne_relativisticke_perturbacie_a_superhorizontovy_test.md`
- `Audit/A3_K5_K1_MRTVA_CMB_normalizovana_rastova_brana_M012.md`
- `Audit/REGISTER_MRTVYCH_KOLAJI_A_DOKAZOV_v3.18_ADDENDUM_A3.md`
- `Audit/ERRATUM_taxonomie_novych_A2_kolaji_po_M012.md`
- `scripts/32_script_A2_K5_K1_canonical_scalar_reconstruction.py`
- `scripts/33_script_A2_K5_K1_quasistatic_growth_gate.py`
- `scripts/36_script_A2_K5_K1_weighted_matter_growth_and_S8_projection_corrected_labels.py`
- `scripts/37--44` pre úplné rovnice a superhorizontové brány
- `scripts/45_script_A3_K5_K1_CAMB_anchor_and_growth_bound.py`
- `scripts/46_script_A3_K5_K1_required_primordial_amplitude.py`

