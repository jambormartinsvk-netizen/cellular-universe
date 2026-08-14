"""Raw one-dimensional H0 residuals for audited S8/H0 toy points.

These residuals ignore model uncertainty, covariance and parameter refitting.
They are arithmetic diagnostics, not cosmological likelihood significances.
"""

from __future__ import annotations

import json


ANCHORS = {
    "SH0ES_2022": (73.04, 1.04),
    "DESI_DR2_CMB_flat_LCDM": (68.17, 0.28),
    "DESI_DR2_CMB_nonflat_LCDM": (68.50, 0.33),
}

POINTS = {
    "cellular_base": 66.3657534122467,
    "curvature_OmegaK_0p005": 68.70603442192078,
    "combined_example_OmegaK_0p002_gamma_0p015": 67.26722598075867,
    "post_data_target_calibration": 68.00000548362732,
}


def main() -> int:
    results = {}
    for point_name, h0 in POINTS.items():
        results[point_name] = {
            anchor_name: {
                "H0_point": h0,
                "H0_anchor": mean,
                "anchor_sigma": sigma,
                "raw_residual_sigma": (h0 - mean) / sigma,
            }
            for anchor_name, (mean, sigma) in ANCHORS.items()
        }

    output = {
        "results": results,
        "interpretation_limit": (
            "Raw residuals ignore model uncertainty, covariance, data overlap, "
            "and refitting. They are not likelihood significances."
        ),
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
