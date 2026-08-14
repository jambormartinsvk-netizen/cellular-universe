"""Verdict-free HP-M1 plus support checkpoint for BI/k=.15.

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
from baseScripts.p5_general_synchronous import c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint as audit  # noqa: E402

if any(os.environ.get(name) != value for name, value in THREAD_ENV.items()):
    raise RuntimeError("KMPC-106 deterministic single-thread environment not active")

PRIOR_RUNNER_NAME = (
    "349_script_KMPC_105_P5_3g7_C2_BI_k0p15_HP_M1_downstream_identity_successor.py"
)
PRIOR_RUNNER_SHA256 = (
    "1AA37C77A9992424EB7878C9056DD6AF4A48609149148F4F9663CEAE9C8D146E"
)


def _load_prior_literal_contract() -> tuple[dict[str, str], dict[str, str]]:
    path = Path(__file__).resolve().with_name(PRIOR_RUNNER_NAME)
    if harness.stable.sha256_file(path) != PRIOR_RUNNER_SHA256:
        raise RuntimeError("KMPC-106 prior runner contract hash mismatch")
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    wanted = {"EXPECTED_SOURCE_HASHES", "EXPECTED_PREREQUISITES"}
    found: dict[str, dict[str, str]] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id in wanted:
            value = ast.literal_eval(node.value)
            if not isinstance(value, dict):
                raise TypeError(f"KMPC-106 {target.id} is not a literal dict")
            found[target.id] = value
    if set(found) != wanted:
        raise RuntimeError("KMPC-106 prior runner literal contract incomplete")
    return found["EXPECTED_SOURCE_HASHES"], found["EXPECTED_PREREQUISITES"]


_prior_sources, _prior_prerequisites = _load_prior_literal_contract()
EXPECTED_SOURCE_HASHES = dict(_prior_sources)
EXPECTED_SOURCE_HASHES[
    "c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint.py"
] = "301E3121DA9E260308FB46E6011A9694BA79676EE57F653DCCD3D472C4C44A78"
EXPECTED_PREREQUISITES = dict(_prior_prerequisites)
EXPECTED_PREREQUISITES[
    "RUN_KMPC_105_P5_3G7_C2_BI_K0p15_HP_M1_DOWNSTREAM_IDENTITY_SUCCESSOR_TECHNICAL_FAILURE.json"
] = "DAF1A456678310A12E3D5A3E46EECF23A4421F502384775A5099577915239EC3"

audit.configure(
    run_id="KMPC-106", mode="BI", k_mpc=0.15,
    output_name="RUN_KMPC_106_P5_3G7_C2_BI_K0p15_HP_M1_SUPPORT_CHECKPOINT.json",
    accepted=(0, 5), audit=(0, 7), m1_depth=7,
    prerequisite_name="RUN_KMPC_080_P5_3G7_C2_BI_K0p15_SAME_MATRIX_REFINEMENT.json",
    prerequisite_sha256="028BE28F8111FE6F775ACFC68A46FF51156DE0F1BD753D5A9C9CEA1CDF83DD1F",
    prerequisite_candidate="REVIEW_C2_CORE_GATE_UNCLOSED",
)

if __name__ == "__main__":
    raise SystemExit(harness.run_cli(
        run_id="KMPC-106",
        audit_module="baseScripts.p5_general_synchronous.c2_bi_k0p15_high_precision_m1_reassembly_v13_support_checkpoint",
        aggregate_name="NOT_AVAILABLE_KMPC_106.json",
        expected_source_hashes=EXPECTED_SOURCE_HASHES,
        expected_prerequisites=EXPECTED_PREREQUISITES,
        expected_harness_hash="735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5",
        expected_high_precision_harness_hash="8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D",
        script_dir=Path(__file__).resolve().parent,
    ))
