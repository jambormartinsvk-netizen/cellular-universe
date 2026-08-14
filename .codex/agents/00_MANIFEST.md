# Manifest projektových subagentov

**Snímka:** 2026-08-11  
**Workflow:** `DEV -> RC -> STATIC_MATH_AUDIT -> OFFICIAL -> SCIENCE_AUDIT
-> FINDING_TRIAGE/DECISION_GATE -> CHECKPOINT/MILESTONE`; osobitne
`FROZEN_MANUAL_ANALYTIC_RESULT -> MANUAL_ANALYTIC_RESULT_AUDIT ->
ORCHESTRATOR_DECISION` bez official runu  
**Rozsah:** projektové sekvenčné roly; bez autority fyzikálneho verdiktu

| Konfigurácia | Model/reasoning | SHA-256 |
|---|---|---|
| `physics_track_auditor.toml` | `gpt-5.6-sol / high` | `73D4DFD20EDC1C1522F7C3EE675CA93F041279F07A287F14DE4FB770B3770B11` |
| `progress_goal_reviewer.toml` | `gpt-5.6-terra / medium` | `4633466C2CDEB8E02BB2776BF98AAC214DBFF5113AA19FAFAE9B94459B2E2544` |
| `math_script_auditor.toml` | `gpt-5.6-sol / high` | `EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79` |
| `manual_analytic_result_auditor.toml` | `gpt-5.6-sol / high` | `164E156380E38335C83FC606A02FCA0B719674627CCAF7ED5EC0E3098A24B6D1` |
| `documentation_release_steward.toml` | `gpt-5.6-terra / low` | `3FEC698E98C37CBF1AB1D2E098748F658045045E29F0AD2F07E3725A9A8C7D68` |
| `python_script_author.toml` | `gpt-5.6 / high` | `86D8F4F69317276BDAB58F841400794104B9750A5A29359EAEC575E5666AB1C3` |
| `external_package_curator.toml` | `gpt-5.6-terra / medium` | `4F80AF6830969FDDCE48BA458526081CCB892AAF27CFE0BDFC08D13894191FAC` |
| `external_auditor.toml` | `gpt-5.6-sol / high` | `98E55F94679F49D4DCE08E3281AE2A38F899B896E25726F9A3C2A85A9FC997E3` |

Hashe vypočítal deterministický `Get-FileHash -Algorithm SHA256`. Nové
capsules používajú iba tieto hashe. Staré neuzavreté kapsuly s predošlým
hashom sú `SUPERSEDED_BY_PROCESS_MIGRATION` a nesmú autorizovať proces.
