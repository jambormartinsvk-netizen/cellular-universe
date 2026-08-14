"""BI/k=.15 HP-M1 downstream F0/M3/non-fit holdout insertion.

Theory author: Martin Jambor. Script creator: Codex (OpenAI).
"""

import importlib.util
import os

THREAD_ENV = {"OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1",
              "MKL_NUM_THREADS": "1", "NUMEXPR_NUM_THREADS": "1"}
for _name, _value in THREAD_ENV.items():
    os.environ[_name] = _value

from pathlib import Path  # noqa: E402
from baseScripts.p5_general_synchronous import c2_high_precision_runner_harness as harness  # noqa: E402
from baseScripts.p5_general_synchronous import c2_bi_k0p15_high_precision_m1_reassembly_v11_downstream_insertion as audit  # noqa: E402

if any(os.environ.get(name) != value for name, value in THREAD_ENV.items()):
    raise RuntimeError("KMPC-103 deterministic single-thread environment not active")

PRIOR_RUNNER_NAME = (
    "346_script_KMPC_102_P5_3g7_C2_BI_k0p15_native_HP_M1_CPQR_routing_successor.py"
)
PRIOR_RUNNER_SHA256 = (
    "5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB"
)


def _load_prior_contract():
    path = Path(__file__).resolve().with_name(PRIOR_RUNNER_NAME)
    if harness.stable.sha256_file(path) != PRIOR_RUNNER_SHA256:
        raise RuntimeError("KMPC-103 prior runner contract hash mismatch")
    spec = importlib.util.spec_from_file_location("_kmpc102_frozen_contract", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("KMPC-103 cannot load prior runner contract")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_prior = _load_prior_contract()
EXPECTED_SOURCE_HASHES = dict(_prior.EXPECTED_SOURCE_HASHES)
EXPECTED_SOURCE_HASHES[
    "c2_bi_k0p15_high_precision_m1_reassembly_v11_downstream_insertion.py"
] = "28B5FD79225BD06D8CB762BA9960EFFB1AE82E9E84F05E0FCCBFC77429B4B573"
EXPECTED_PREREQUISITES = dict(_prior.EXPECTED_PREREQUISITES)
EXPECTED_PREREQUISITES[
    "RUN_KMPC_102_P5_3G7_C2_BI_K0p15_NATIVE_HP_M1_CPQR_ROUTING_SUCCESSOR.json"
] = "49187BB85B8C59559A23EF6741DFB64F0015C2F0CC458D5C9D284FF2CECDE0CB"

audit.configure(
    run_id="KMPC-103", mode="BI", k_mpc=0.15,
    output_name="RUN_KMPC_103_P5_3G7_C2_BI_K0p15_HP_M1_DOWNSTREAM_INSERTION.json",
    accepted=(0, 5), audit=(0, 7), m1_depth=7,
    prerequisite_name="RUN_KMPC_080_P5_3G7_C2_BI_K0p15_SAME_MATRIX_REFINEMENT.json",
    prerequisite_sha256="028BE28F8111FE6F775ACFC68A46FF51156DE0F1BD753D5A9C9CEA1CDF83DD1F",
    prerequisite_candidate="REVIEW_C2_CORE_GATE_UNCLOSED",
)

if __name__ == "__main__":
    raise SystemExit(harness.run_cli(
        run_id="KMPC-103",
        audit_module="baseScripts.p5_general_synchronous.c2_bi_k0p15_high_precision_m1_reassembly_v11_downstream_insertion",
        aggregate_name="NOT_AVAILABLE_KMPC_103.json",
        expected_source_hashes=EXPECTED_SOURCE_HASHES,
        expected_prerequisites=EXPECTED_PREREQUISITES,
        expected_harness_hash="735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5",
        expected_high_precision_harness_hash="8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D",
        script_dir=Path(__file__).resolve().parent,
    ))
