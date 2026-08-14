"""Exact M3 driver/holdout resume from the KMPC-108/109 checkpoint pair.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

import ast
import os

THREAD_ENV = {"OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1",
              "MKL_NUM_THREADS": "1", "NUMEXPR_NUM_THREADS": "1"}
for _name, _value in THREAD_ENV.items():
    os.environ[_name] = _value

from pathlib import Path  # noqa: E402
from baseScripts.p5_general_synchronous import c2_high_precision_runner_harness as harness  # noqa: E402
from baseScripts.p5_general_synchronous import c2_bi_k0p15_high_precision_m1_reassembly_v17_exact_resume as audit  # noqa: E402

if any(os.environ.get(name) != value for name, value in THREAD_ENV.items()):
    raise RuntimeError("KMPC-110 deterministic single-thread environment not active")

PRIOR_RUNNER_NAME = (
    "353_script_KMPC_109_P5_3g7_C2_BI_k0p15_HP_M1_support_checkpoint_read_only_receipt.py"
)
PRIOR_RUNNER_SHA256 = (
    "A390718F258FE47408888EFD6A825A5387D5C6573E8B66FF1AF5E81B2D3CAE57"
)
LITERAL_ANCESTOR_NAME = (
    "346_script_KMPC_102_P5_3g7_C2_BI_k0p15_native_HP_M1_CPQR_routing_successor.py"
)
LITERAL_ANCESTOR_SHA256 = (
    "5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB"
)


def _load_literal_ancestor_contract() -> tuple[dict[str, str], dict[str, str]]:
    here = Path(__file__).resolve().parent
    if harness.stable.sha256_file(here / PRIOR_RUNNER_NAME) != PRIOR_RUNNER_SHA256:
        raise RuntimeError("KMPC-110 prior-runner lineage hash mismatch")
    path = here / LITERAL_ANCESTOR_NAME
    if harness.stable.sha256_file(path) != LITERAL_ANCESTOR_SHA256:
        raise RuntimeError("KMPC-110 literal ancestor hash mismatch")
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    wanted = {"EXPECTED_SOURCE_HASHES", "EXPECTED_PREREQUISITES"}
    found: dict[str, dict[str, str]] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name) or target.id not in wanted:
            continue
        if not isinstance(node.value, ast.Dict):
            raise TypeError(f"KMPC-110 {target.id} ancestor is not a literal dict")
        value = ast.literal_eval(node.value)
        if not isinstance(value, dict):
            raise TypeError(f"KMPC-110 {target.id} is not a literal dict")
        found[target.id] = value
    if set(found) != wanted:
        raise RuntimeError("KMPC-110 literal ancestor contract incomplete")
    return found["EXPECTED_SOURCE_HASHES"], found["EXPECTED_PREREQUISITES"]


_ancestor_sources, _ancestor_prerequisites = _load_literal_ancestor_contract()
EXPECTED_SOURCE_HASHES = dict(_ancestor_sources)
EXPECTED_SOURCE_HASHES.update({
    "c2_bi_k0p15_high_precision_m1_reassembly_v11_downstream_insertion.py":
        "28B5FD79225BD06D8CB762BA9960EFFB1AE82E9E84F05E0FCCBFC77429B4B573",
    "c2_bi_k0p15_high_precision_m1_reassembly_v12_downstream_identity_successor.py":
        "479EEFD9BFDBF6E663BF6C6941444AB347C1CF9B54EBC522A3E82601D9C615F3",
    "c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint.py":
        "301E3121DA9E260308FB46E6011A9694BA79676EE57F653DCCD3D472C4C44A78",
    "c2_bi_k0p15_high_precision_m1_reassembly_v14_checkpoint_identity_successor.py":
        "0ED499BFBBD6E6D7FC2640FE13BDAF67CE0C31C1B9AE593648BC2FEB3934733A",
    "c2_bi_k0p15_high_precision_m1_reassembly_v15_checkpoint_json_successor.py":
        "0818D47F50A99C4EDE4FD5320F9A39E4FA0B6134A95FC1027D6FF7AB57A5362B",
    "c2_bi_k0p15_high_precision_m1_reassembly_v16_checkpoint_receipt.py":
        "96B95FF8E43F782494ED4B50C2A03A0856810C03297ED760991F4AF393CB7484",
    "c2_bi_k0p15_high_precision_m1_reassembly_v17_exact_resume.py":
        "1EC7DF765617A978940105129D74F02C1419B726CC023977F4DB426DDA5A33C4",
})
EXPECTED_PREREQUISITES = dict(_ancestor_prerequisites)
EXPECTED_PREREQUISITES.update({
    "RUN_KMPC_102_P5_3G7_C2_BI_K0p15_NATIVE_HP_M1_CPQR_ROUTING_SUCCESSOR.json":
        "49187BB85B8C59559A23EF6741DFB64F0015C2F0CC458D5C9D284FF2CECDE0CB",
    "RUN_KMPC_105_P5_3G7_C2_BI_K0p15_HP_M1_DOWNSTREAM_IDENTITY_SUCCESSOR_TECHNICAL_FAILURE.json":
        "DAF1A456678310A12E3D5A3E46EECF23A4421F502384775A5099577915239EC3",
    "RUN_KMPC_107_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_ROUTING_SUCCESSOR_TECHNICAL_FAILURE.json":
        "ADB8D2A1669E4C6E0C07C4A3E2C0E3B8809A4514C4F32E26CF76684FAA92F89C",
    "RUN_KMPC_108_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_JSON_SUCCESSOR.json":
        "683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995",
    "RUN_KMPC_109_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT_READ_ONLY_RECEIPT.json":
        "21EF9A9BF8D6E437CC848BD76EC026C5621534F35C0D88F99D2BFAFAD28118F9",
})

audit.configure(
    run_id="KMPC-110", mode="BI", k_mpc=0.15,
    output_name="RUN_KMPC_110_P5_3G7_C2_BI_K0p15_HP_M1_CHECKPOINT_EXACT_RESUME.json",
    accepted=(0, 5), audit=(0, 7), m1_depth=7,
    prerequisite_name="RUN_KMPC_080_P5_3G7_C2_BI_K0p15_SAME_MATRIX_REFINEMENT.json",
    prerequisite_sha256="028BE28F8111FE6F775ACFC68A46FF51156DE0F1BD753D5A9C9CEA1CDF83DD1F",
    prerequisite_candidate="REVIEW_C2_CORE_GATE_UNCLOSED",
)

if __name__ == "__main__":
    raise SystemExit(harness.run_cli(
        run_id="KMPC-110",
        audit_module="baseScripts.p5_general_synchronous.c2_bi_k0p15_high_precision_m1_reassembly_v17_exact_resume",
        aggregate_name="NOT_AVAILABLE_KMPC_110.json",
        expected_source_hashes=EXPECTED_SOURCE_HASHES,
        expected_prerequisites=EXPECTED_PREREQUISITES,
        expected_harness_hash="735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5",
        expected_high_precision_harness_hash="8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D",
        script_dir=Path(__file__).resolve().parent,
    ))
