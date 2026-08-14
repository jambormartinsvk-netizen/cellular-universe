"""Render selected PDF pages to PNG with a cooperative runtime limit.

Page numbers supplied on the command line are one-based, matching printed PDF
page references used in audit documents. An outer process timeout is required in
addition to the cooperative deadline for third-party parser safety.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import fitz


def parse_pages(value: str) -> list[int]:
    pages = sorted({int(item.strip()) for item in value.split(",") if item.strip()})
    if not pages or pages[0] < 1:
        raise argparse.ArgumentTypeError("pages must be positive one-based integers")
    return pages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--pages", required=True, type=parse_pages)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--dpi", type=float, default=144.0)
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.dpi <= 0 or args.max_runtime_seconds <= 0:
        raise ValueError("dpi and max runtime must be positive")

    started = time.monotonic()
    input_path = args.input.resolve(strict=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    document = fitz.open(input_path)
    matrix = fitz.Matrix(args.dpi / 72.0, args.dpi / 72.0)
    outputs: list[str] = []

    try:
        for page_number in args.pages:
            if time.monotonic() - started > args.max_runtime_seconds:
                raise TimeoutError("cooperative PDF render deadline exceeded")
            if page_number > document.page_count:
                raise IndexError(
                    f"page {page_number} exceeds document length {document.page_count}"
                )
            page = document.load_page(page_number - 1)
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)
            output = args.output_dir / f"{input_path.stem}_page_{page_number:03d}.png"
            pixmap.save(output)
            outputs.append(str(output.resolve()))
    finally:
        document.close()

    print(
        json.dumps(
            {
                "status": "PASS",
                "input": str(input_path),
                "pages": args.pages,
                "outputs": outputs,
                "runtime_seconds": time.monotonic() - started,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
