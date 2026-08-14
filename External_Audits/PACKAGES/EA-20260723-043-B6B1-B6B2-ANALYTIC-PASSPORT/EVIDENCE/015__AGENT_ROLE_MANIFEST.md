# Manifest projektových subagentov

**Snímka:** 2026-07-23  
**Rozsah:** projektové sekvenčné roly; bez autority fyzikálneho verdiktu

| Konfigurácia | Model/reasoning | SHA-256 |
|---|---|---|
| `physics_track_auditor.toml` | `gpt-5.6 / high` | `9A1E91215069253B022941DD45F9F52F6058D8CF0AB8F2C46719774EA3B1353F` |
| `progress_goal_reviewer.toml` | `gpt-5.6-terra / medium` | `07F89EA93DACA42EA3F6B4E93AEDE08FC23B44CAE7F3A2E74A8B8D29511750F1` |
| `math_script_auditor.toml` | `gpt-5.6 / high` | `7B5DAEE0C7AA658D8ADC25FB79C1E4F25A909619B697359C615B13A986F9E7DE` |
| `documentation_release_steward.toml` | `gpt-5.6-terra / low` | `035FEDFB8D248BEF556BC75FE51E935B56190C1B7FB4087F074929F67C187DE7` |
| `python_script_author.toml` | `gpt-5.6 / high` | `F73A4EF2401D1675FD8677BC44A3863805A35828B05945AF944E9314B33DE98E` |
| `external_package_curator.toml` | `gpt-5.6-terra / medium` | `26CAB7693DBB372C4FAEEFBACF9101CD2C1BA3F40E628CB20E6514EA8A906AE1` |
| `external_auditor.toml` | `gpt-5.6 / high` | `6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14` |

Hashe vypočítal deterministický `Get-FileHash -Algorithm SHA256`; model ich
nevytváral. Konfigurácie sa uplatnia na nové subagent sessions. Každý task
capsule nesie hash použitej konfigurácie. Ak sa zmení model, sandbox alebo
inštrukcie, najprv sa aktualizuje tento manifest a vykoná read-only
compliance smoke bez fyzikálneho verdiktu.
