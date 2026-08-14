#!/usr/bin/env python3
"""
check_state.py - linter autoritativneho stavu projektu Teoria/QCTS.

Kazde pravidlo tu zodpoveda JEDNEJ zdokumentovanej minulej chybe.
Pravidlo, ktore je len napisane v Markdowne, sa porusi. Pravidlo, ktore
kontroluje stroj, sa porusit neda.

Spustenie:  python check_state.py [cesta/00_STATE.json]
Exit kod:   0 = ciste, 1 = porusenia (BLOCK), 2 = len varovania (WARN)

Ziadne zavislosti. Ziadny LLM. Nedriftuje.
"""
import json
import sys
import os

RULES = []


def rule(rid, precedent, severity="BLOCK"):
    def deco(fn):
        RULES.append((rid, precedent, severity, fn))
        return fn
    return deco


# ---------------------------------------------------------------- pravidla

@rule("R01", "audit 2 V.7 - X_K nie je finitne parameterizovany, §8 nemoze skoncit")
def r01(S):
    """Ziva kolaj musi mat deklarovany konecny rez."""
    out = []
    for k in S["kolaje"]:
        if k["status"] == "UNDECIDED_INFINITE" or (
                k["status"].startswith("UNDECIDED") and not k.get("finite_cut")):
            out.append(f"{k['id']}: ziadny finite_cut -> nie je legalna kolaj, "
                       f"otazka existencie sa nesmie otvorit")
    return out


@rule("R02", "audit 2 V.6 - FS-C1 povysil vetvu lambda=0.15 na mantinel piatich kolaji")
def r02(S):
    """Hodnota z vetvy sa nesmie stat tvrdym mantinelom pre inu kolaj."""
    out = []
    hard = {m["id"]: m for m in S.get("mantinely", []) if m.get("kind") == "HARD"}
    for k in S["kolaje"]:
        for cid in k.get("hard_constraints", []):
            m = hard.get(cid)
            if m and m.get("derived_from"):
                out.append(f"{k['id']}: tvrdy mantinel {cid} je odvodeny z vetvy "
                           f"{m['derived_from']} -> vetva obmedzuje kolaj")
    return out


@rule("R03", "moje varovanie - mnozenie stanic chrani filozofiu pred smrtou")
def r03(S):
    """Kazda stanica ma vlastnu, od susedov odlisnu podmienku smrti."""
    out, seen = [], {}
    for s in S["stanice"]:
        d = (s.get("death_condition") or "").strip()
        if not d:
            out.append(f"{s['id']}: chyba death_condition -> nie je to stanica, "
                       f"je to ochranny pas")
        elif d in seen:
            out.append(f"{s['id']}: rovnaka podmienka smrti ako {seen[d]}")
        else:
            seen[d] = s["id"]
    return out


@rule("R04", "audit 2 V.8 - pat zaloznych kolaji je jeden chybajuci objekt")
def r04(S):
    """Kolaje na jednej stanici nesmu cakat na ten isty objekt bez priznania."""
    out, by = [], {}
    for k in S["kolaje"]:
        w = k.get("waiting_for")
        if w:
            by.setdefault((k["stanica"], w), []).append(k["id"])
    for (st, w), ids in by.items():
        if len(ids) > 1:
            out.append(f"{st}: {len(ids)} kolaji ({', '.join(ids)}) caka na TEN ISTY "
                       f"objekt '{w}' -> falosna pluralita, je to jedna sanca")
    return out


@rule("R05", "nova otazka - stanica so samymi 'neporusenie' kolajami je ziva ale sterilna",
      severity="WARN")
def r05(S):
    """Aspon jedna ziva kolaj na stanici ma prispievat PREPOJENIM."""
    out = []
    live = {"UNDECIDED_FINITE", "NONEMPTY_CERTIFIED"}
    for s in S["stanice"]:
        ks = [k for k in S["kolaje"] if k["stanica"] == s["id"] and k["status"] in live]
        if ks and not any(k.get("contributes") == "PREPOJENIE" for k in ks):
            out.append(f"{s['id']}: vsetky zive kolaje su IBA_NEPORUSENIE -> "
                       f"stanica nemoze zomriet, ale ani nic nevyrobi")
    return out


@rule("R06", "audit 2 V.4/VI.6 - 222 taskov, pohyb hlbky nula")
def r06(S):
    """Po N suchych behoch musi kolaj ist do DORMANT."""
    n = S.get("prahy", {}).get("dry_runs_to_dormant", 3)
    return [f"{k['id']}: {k['dry_runs']} suchych behov >= {n}, ale status je "
            f"{k['status']} -> ma byt DORMANT (odobrate zdroje, NIE smrt)"
            for k in S["kolaje"] if k.get("dry_runs", 0) >= n and k["status"] != "DORMANT"]


@rule("R07", "audit 2 V.5 - rozpocet sa obnovoval delenim problemu")
def r07(S):
    out = []
    for q in S["otazky"]:
        if q["errors_used"] > q["budget"]:
            out.append(f"{q['id']}: {q['errors_used']}/{q['budget']} prekroceny")
        elif q["errors_used"] == q["budget"] and q["status"] != "NO_GO_BY_EXHAUSTION":
            out.append(f"{q['id']}: rozpocet vycerpany -> status musi byt "
                       f"NO_GO_BY_EXHAUSTION (je to publikovatelny vysledok)")
    return out


@rule("R08", "Martinova poziadavka - nezabit nieco len preto, ze to nevieme spocitat")
def r08(S):
    """Smrt vyzaduje certifikat, nikdy nie nepritomnost."""
    out = []
    for k in S["kolaje"]:
        if k["status"] == "EMPTY_CERTIFIED" and not k.get("certificate"):
            out.append(f"{k['id']}: EMPTY_CERTIFIED bez pola 'certificate' -> "
                       f"to nie je smrt, to je nevedomost")
        if k["status"] == "EXCLUDED_BY_DATA" and not (
                k.get("measurement") and k.get("what_would_reverse")):
            out.append(f"{k['id']}: EXCLUDED_BY_DATA musi uviest meranie A co by ho "
                       f"zvratilo -> vylucenie datami je vzdy podmienene")
    return out


@rule("R09", "audit 2 III.6(d) - ladenie o 9 radov pre kazde pole nie je mechanizmus")
def r09(S):
    n = S.get("prahy", {}).get("measure_zero_tuning_orders", 3)
    out = []
    for k in S["kolaje"]:
        t = k.get("tuning_orders")
        if t is None:
            continue
        bad = t > n and not k.get("single_parameter", False)
        if bad and k["status"] != "MEASURE_ZERO":
            out.append(f"{k['id']}: {t} radov koincidencie bez jedneho parametra "
                       f"(prah {n}) -> ma byt MEASURE_ZERO")
        if not bad and k["status"] == "MEASURE_ZERO":
            out.append(f"{k['id']}: MEASURE_ZERO, ale {t} radov je pod prahom {n} "
                       f"alebo je to jeden parameter -> neopravnene zabite")
    return out


@rule("R10", "audit 2 V.10 - interne 'Neprijate' vs publikovane survival targets")
def r10(S):
    return [f"{p['id']}: interne neprijate, ale status '{p['status']}' -> "
            f"rozpor medzi internym stavom a publikovanym"
            for p in S["predikcie"]
            if not p.get("internal_accepted", True)
            and p["status"] not in ("PRE_A3_DIAGNOSTIC", "WITHDRAWN", "IDENTITY")]


@rule("R11", "audit 2 C2 - A_f = 7809.270101963506 pri vstupoch s 3-4 ciframi")
def r11(S):
    maxd = S.get("prahy", {}).get("max_significant_digits", 4)
    out = []
    for grp, key in (("vetvy", "parameter"), ("predikcie", "velicina")):
        for it in S.get(grp, []):
            v = it.get("value")
            if v is None or isinstance(v, bool):
                continue
            d = len(f"{float(v):.15g}".replace("-", "").replace(".", "")
                    .lstrip("0").rstrip("0")) or 1
            if d > maxd:
                out.append(f"{it['id']} ({it[key]}): {v} ma ~{d} platnych cifier "
                           f"> {maxd} -> falosna precizia")
    return out


@rule("R12", "moje zistenie - Dodatok A1 auditu ma preklep, lebo kod bol prepisany")
def r12(S):
    """Kazda publikovana hodnota ma mat receipt zo spusteneho skriptu."""
    return [f"{p['id']}: ma hodnotu {p['value']}, ale ziadny receipt -> "
            f"cislo bez behu nie je dohladatelne"
            for p in S["predikcie"]
            if p.get("value") is not None and not p.get("receipt")]


@rule("R13", "audit 2 VI.1/VI.2 - mrtvy git tag v3.18, README popiera release")
def r13(S):
    r, out = S.get("release", {}), []
    if not r.get("git_tag_exists"):
        out.append(f"v{r.get('version')}: git tag neexistuje -> vsetky evidence "
                   f"odkazy v release su 404, §13 citacna podmienka nesplnena")
    if not r.get("readme_matches_release"):
        out.append(f"v{r.get('version')}: README nesuhlasi s release")
    if not r.get("audit_layer_named_correctly"):
        out.append(f"v{r.get('version')}: 'external audit' pouzite pre LLM agenta -> "
                   f"materialna dezinformacia konotaciou")
    if r.get("max_significant_digits", 0) > S.get("prahy", {}).get("max_significant_digits", 4):
        out.append(f"v{r.get('version')}: publikovane cisla maju az "
                   f"{r['max_significant_digits']} cifier")
    return out


# ---------------------------------------------------------------- beh

def main(path):
    S = json.load(open(path, encoding="utf-8"))
    print(f"=== check_state.py :: {os.path.basename(path)} (stav k {S.get('updated')}) ===\n")
    nb = nw = 0
    for rid, precedent, sev, fn in RULES:
        try:
            findings = fn(S) or []
        except Exception as e:
            findings = [f"pravidlo zlyhalo: {e!r}"]
            sev = "BLOCK"
        if not findings:
            print(f"  OK    {rid}")
            continue
        print(f"  {sev:5} {rid}  ({precedent})")
        for f in findings:
            print(f"        - {f}")
        nb += len(findings) if sev == "BLOCK" else 0
        nw += len(findings) if sev == "WARN" else 0
    print(f"\n=== {nb} poruseni (BLOCK), {nw} varovani (WARN) ===")
    if nb:
        print("BLOCK znamena: tento stav sa nesmie pouzit ako vychodisko noveho vypoctu.")
    return 1 if nb else (2 if nw else 0)


if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "00_STATE.json")
    sys.exit(main(p))
