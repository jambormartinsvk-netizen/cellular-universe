# Erratum importu medzi skriptmi 12 a 13

**Dátum:** 2026-07-13  
**Stav:** implementačná chyba skriptu 12, fyzikálny výpočet sa nespustil

## Chyba

Skript `12_script_A1_K1_cdm_background_audit_exact_zstar.py` načítaval skript 11 cez `importlib.util`. Vytvorený modul však pred vykonaním nezaregistroval v `sys.modules`.

Python 3.11 potrebuje túto registráciu pri spracovaní dekorátora `@dataclass`. Skript preto skončil chybou:

```text
AttributeError: 'NoneType' object has no attribute '__dict__'
```

Chyba nastala počas importu. Žiadna integračná ani fyzikálna kontrola neprebehla.

## Oprava

Skript `13_script_A1_K1_cdm_background_audit_exact_zstar.py` pred `exec_module` vykoná:

```python
sys.modules[SPEC.name] = BASE
```

Iné časti skriptu 12 sa nemenia. Skript 12 zostáva uložený ako reprodukovateľná stopa chybného importu.

## Spustenie

```powershell
python scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py
```
