# A2-K4 / K7c P2 — konečný audit M-prime term ledgeru

Dátum: 2026-07-15  
Stabilné ID: `SCI-A2K4-C7G5-K7C-P2-MLEDGER`  
Skript: 199  
Verdikt P2: **STOP jednoduchého `math.fsum` vysvetlenia v testovanom rozsahu**  
A2-K4: **ŽIVÁ, 66.5/100**  
K7c: **REVIEW**  
Score effect: **NONE**

## Výsledok ľudskou rečou

Obyčajné ľavostranné float64 sčítanie a `math.fsum` dali na všetkých troch
checkpointoch rovnaký výsledok. Zlepšenie voči plnej 80-dps referencii bolo
presne `1×`, nie požadovaných najmenej `10×`. Cancellation condition celého
deväťčlenného súčtu bola iba približne 2, takže nejde o katastrofické
vyrušenie veľkých členov na úrovni finálneho súčtu.

Jednoduché nahradenie posledného sčítania funkciou `math.fsum` preto nemôže
vysvetliť ani opraviť ne-RK4 pomer. Rezervovaná evolučná podkoľaj K7c.3e sa
nezaloží.

## Provenance a rozsah

- child 185 skončil očakávaným historickým REVIEW exitom;
- všetky dependency hashe 185/183/179/197 a P1 raw hash prešli;
- tri child checkpointy boli bitovo zhodné s P1 raw stavmi aj RHS;
- checkpointy: `x=-25,-24.875,-24.75`;
- na každom bolo presne deväť konečných členov;
- obyčajný súčet bol bitovo zhodný s child `rhs["M"]`;
- žiadna nová ODE ani náhrada RHS sa nevykonala;
- runtime: `8.344 s`, pod všetkými limitmi.

## Číselný výsledok

| x | cancellation condition | plain chyba voči full HP | fsum chyba voči full HP | zlepšenie | K7c.3e kvalifikácia |
|---:|---:|---:|---:|---:|---|
| `-25` | `2.00000006086` | `3.90741019959705e-17` | `3.90741019959705e-17` | `1` | nie |
| `-24.875` | `2.00010458078` | `3.90741019959697e-17` | `3.90741019959697e-17` | `1` | nie |
| `-24.75` | `1.99942339769` | `5.14184881288809e-32` | `5.14184881288809e-32` | `1` | nie |

Aj 80-dps súčet už vypočítaných float64 členov dal pre `math.fsum` faktor
`1×` na všetkých checkpointoch. To nezávisle potvrdzuje, že finálne poradie
sčítania nie je príčina.

## Skutočný numerický zdroj odhalený P2

Najväčší rozdiel voči plnej HP referencii nevzniká v súčte deviatich členov,
ale už pri zostavení dvoch koeficientov:

| Člen | float64 pri `x=-25` | 80-dps hodnota |
|---|---:|---:|
| `(1.5 Ob-Wg load) Ug` | `+2.91124749316e-25` | približne `5.53e-90` |
| `(0.25 Wg inv1r-0.5 Og) dg` | `-3.90741022871e-17` | približne `-3.71e-82` |

Pri `x=-24.875` má druhý artefakt opačné znamienko
`+3.90741022871e-17`; pri `x=-24.75` sa v danej float64 evaluácii náhodou
zaokrúhli presne na nulu. To vysvetľuje, prečo rozdiel nie je stabilný pri
zjemnení mriežky.

## Exaktná algebraická identita

Označme baryónové loading číslo `R`. Z registrovaného backgroundu:

\[
\frac{\Omega_b}{\Omega_\gamma}=\frac{4R}{3},
\qquad
W_\gamma=2\Omega_\gamma+\frac32\Omega_b
             =2\Omega_\gamma(1+R).
\]

Keďže `load_fraction=R/(1+R)` a `inv1r=1/(1+R)`, presne platí

\[
\frac32\Omega_b-W_\gamma\frac{R}{1+R}=0,
\]

\[
\frac14W_\gamma\frac{1}{1+R}-\frac12\Omega_\gamma=0.
\]

Float64 výraz odčítava dve takmer rovnaké hodnoty a vytvára neexistujúci
reziduálny zdroj. Toto je algebraická cancellation chyba koeficientu, nie
nová fyzika ani finálna summation chyba.

## Rozhodnutie o koľajach

- jednoduchá `fsum` koľaj: **MŔTVA PRED EVOLÚCIOU**; dôvod a JSON sa zachovajú;
- K7c.3e rezervovaná pre `fsum` evolúciu: **NOT_CREATED / DISQUALIFIED BY P2**;
- nová prvá alternatíva: algebraická identity koľaj, samostatne a bez zmeny
  iných členov;
- tuhosť/eigenmódy a vyššia pracovná presnosť ostávajú oddelené neskoršie
  alternatívy, ak algebraická koľaj nepomôže.

## Dôkazy

| Artefakt | SHA-256 |
|---|---|
| `scripts/199_script_A2_K4_C7_7c_K7c_P2_Mprime_term_ledger.py` | `911F7DDBDC6B41C019CD041FC024A2B8FAF9CF2A27A1F35686ECB6649BAD8DF9` |
| `Audit/A2_K4_K7C_P2_MLEDGER_RAW_2026-07-15.json` | `C268A63CE34888744E48A8BD784651C75B243B25705E74C301299DA69499FA5C` |
| `scripts/200_script_python_corpus_status_audit_after_K7c_P2_script199.py` | `77829D7737334289A0E4A984956714D200F1DAE303C0C248C817395F2A595412` |
| `Audit/A2_K4_K7C_P2_CORPUS_CHECKER_200_2026-07-15.json` | `C261E23CEB06338C4BB142A9EFD332D5DFF852A7BE720A1629E0C14198B6BDCE` |

## Nasledujúci krok

Najprv bez ODE auditovať exaktné identity na všetkých troch checkpointoch a
na deep/shallow backgroundových plochách. Až po PASS môže samostatný
evolučný skript nahradiť iba dva identicky nulové koeficienty ich exaktnou
hodnotou a zopakovať 100/200/400. Prah RK4 `8–32` a rozdiel `<1e-6` sa
nesmú meniť.

