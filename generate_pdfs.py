#!/usr/bin/env python3
"""Convert the Markdown resumes into PDFs under pdfs/, using headless Chrome.

Usage:
    python3 generate_pdfs.py

Requires:
    - Python `markdown` package (pip install markdown)
    - Google Chrome installed at the default macOS path
"""

import subprocess
import tempfile
from pathlib import Path

import markdown

REPO_ROOT = Path(__file__).resolve().parent
RESUMES_DIR = REPO_ROOT / "resumes"
PDF_DIR = REPO_ROOT / "pdfs"

RESUME_FILES = [
    REPO_ROOT / "README.md",
    RESUMES_DIR / "mobile-engineer.md",
    RESUMES_DIR / "backend-engineer.md",
    RESUMES_DIR / "desktop-engineer.md",
    RESUMES_DIR / "software-engineer.md",
    RESUMES_DIR / "python-engineer.md",
]

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

HTML_TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<base href="file://{base_dir}/">
<style>
  body {{
    font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
    max-width: 820px;
    margin: 40px auto;
    padding: 0 24px;
    line-height: 1.5;
    color: #1a1a1a;
  }}
  h1 {{ font-size: 26px; border-bottom: 2px solid #ddd; padding-bottom: 8px; }}
  h2 {{ font-size: 19px; margin-top: 28px; border-bottom: 1px solid #eee; padding-bottom: 4px; }}
  h3 {{ font-size: 16px; margin-top: 18px; }}
  h4 {{ font-size: 14px; margin-top: 12px; }}
  a {{ color: #0969da; text-decoration: none; }}
  code {{ background: #f6f8fa; padding: 1px 5px; border-radius: 4px; font-size: 0.9em; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 0.95em; }}
  th, td {{ border: 1px solid #ddd; padding: 6px 10px; text-align: left; }}
  blockquote {{ border-left: 3px solid #ddd; margin: 8px 0; padding: 2px 16px; color: #555; }}
  img {{ max-width: 100%; }}
  hr {{ border: none; border-top: 1px solid #ddd; margin: 20px 0; }}
</style>
</head>
<body>
{content}
</body>
</html>
"""


def convert(md_path: Path, out_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        text, extensions=["tables", "fenced_code", "sane_lists", "nl2br"]
    )
    # Base href is the repo root (not the md file's own folder) so that
    # root-relative asset paths like `images/...` resolve the same way
    # they do when GitHub renders the file in place.
    html = HTML_TEMPLATE.format(base_dir=REPO_ROOT, content=html_body)

    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", delete=False, encoding="utf-8"
    ) as f:
        f.write(html)
        html_file = f.name

    try:
        subprocess.run(
            [
                CHROME_PATH,
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                f"--print-to-pdf={out_path}",
                "--print-to-pdf-no-header",
                html_file,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    finally:
        Path(html_file).unlink(missing_ok=True)


def main() -> None:
    PDF_DIR.mkdir(exist_ok=True)
    for md_path in RESUME_FILES:
        if not md_path.exists():
            print(f"skip (not found): {md_path.relative_to(REPO_ROOT)}")
            continue
        out_path = PDF_DIR / (md_path.stem + ".pdf")
        convert(md_path, out_path)
        print(f"generated: pdfs/{out_path.name}")


if __name__ == "__main__":
    main()
