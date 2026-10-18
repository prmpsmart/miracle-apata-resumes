#!/usr/bin/env python3
"""Convert the Markdown resumes into PDFs under pdfs/, using pandoc + typst.

Usage:
    python3 generate_pdfs.py

Requires:
    - pandoc  (brew install pandoc)
    - typst   (brew install typst)
"""

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
RESUMES_DIR = REPO_ROOT / "resumes"
PDF_DIR = REPO_ROOT / "pdfs"

RESUME_FILES = [
    RESUMES_DIR / "mobile-engineer.md",
    RESUMES_DIR / "backend-engineer.md",
    RESUMES_DIR / "desktop-engineer.md",
    RESUMES_DIR / "software-engineer.md",
    RESUMES_DIR / "python-engineer.md",
]

# Extra pandoc/typst styling. `margin.x`/`margin.y` use pandoc's dotted -V
# nesting to populate the typst template's `margin` dict.
PANDOC_ARGS = [
    "--pdf-engine=typst",
    "-V",
    "margin.x=1.9cm",
    "-V",
    "margin.y=1.7cm",
    "-V",
    "fontsize=10pt",
]


def convert(md_path: Path, out_path: Path) -> None:
    # cwd=REPO_ROOT so root-relative asset paths resolve the same way
    # GitHub renders them in place.
    subprocess.run(
        ["pandoc", str(md_path), "-o", str(out_path), *PANDOC_ARGS],
        check=True,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def main() -> None:
    PDF_DIR.mkdir(exist_ok=True)
    for md_path in RESUME_FILES:
        if not md_path.exists():
            print(f"skip (not found): {md_path.relative_to(REPO_ROOT)}")
            continue
        name = "-".join(w.capitalize() for w in md_path.stem.split("-"))
        out_path = PDF_DIR / f"Miracle-Apata-{name}.pdf"
        convert(md_path, out_path)
        print(f"generated: pdfs/{out_path.name}")


if __name__ == "__main__":
    main()
