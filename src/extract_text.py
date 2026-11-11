"""Turn deliverable files (xlsx, docx, pdf, pptx, text) into plain text a grader model can read.

Spreadsheet cells show both formula and stored value, since openpyxl-written files hold no computed values.
"""
import zipfile
from pathlib import Path

# ~100k tokens per file; a 60k cap cut large workbooks and the judge failed items whose evidence was cut
MAX_CHARS_PER_FILE = 400_000


def _xlsx(path: Path) -> str:
    import openpyxl
    wb_f = openpyxl.load_workbook(path, data_only=False)
    wb_v = openpyxl.load_workbook(path, data_only=True)
    out = []
    for ws in wb_f.worksheets:
        wv = wb_v[ws.title]
        out.append(f"## Sheet '{ws.title}' (dims {ws.dimensions})")
        for row in ws.iter_rows():
            cells = []
            for c in row:
                if c.value is None:
                    continue
                v = wv[c.coordinate].value
                if isinstance(c.value, str) and c.value.startswith("="):
                    shown = f"{c.value} -> {v!r}" if v is not None else f"{c.value} -> (not computed)"
                else:
                    shown = repr(c.value)
                cells.append(f"{c.coordinate}={shown}")
            if cells:
                out.append(" | ".join(cells))
    return "\n".join(out)


def _docx(path: Path) -> str:
    import docx
    d = docx.Document(path)
    out = []
    for p in d.paragraphs:
        if p.text.strip():
            style = p.style.name if p.style is not None else ""
            prefix = "# " if style.startswith("Heading") or style == "Title" else ""
            out.append(prefix + p.text)
    for i, t in enumerate(d.tables, 1):
        out.append(f"\n[Table {i}]")
        for r in t.rows:
            out.append(" | ".join(c.text.strip() for c in r.cells))
    return "\n".join(out)


def _pdf(path: Path) -> str:
    import pdfplumber
    out = []
    with pdfplumber.open(path) as pdf:
        out.append(f"[PDF, {len(pdf.pages)} pages]")
        for i, page in enumerate(pdf.pages, 1):
            out.append(f"\n--- page {i} ---\n{page.extract_text() or '(no extractable text)'}")
    return "\n".join(out)


def _pptx(path: Path) -> str:
    from pptx import Presentation
    prs = Presentation(path)
    out = [f"[PPTX, {len(prs.slides)} slides]"]
    for i, slide in enumerate(prs.slides, 1):
        out.append(f"\n--- slide {i} ---")
        for shape in slide.shapes:
            if shape.has_text_frame and shape.text_frame.text.strip():
                out.append(shape.text_frame.text)
            if getattr(shape, "has_table", False) and shape.has_table:
                for r in shape.table.rows:
                    out.append(" | ".join(c.text for c in r.cells))
    return "\n".join(out)


def extract(path: Path) -> str:
    ext = path.suffix.lower()
    try:
        if ext in (".xlsx", ".xlsm"):
            text = _xlsx(path)
        elif ext == ".docx":
            text = _docx(path)
        elif ext == ".pdf":
            text = _pdf(path)
        elif ext == ".pptx":
            text = _pptx(path)
        elif ext in (".txt", ".md", ".csv", ".json", ".py", ".yaml", ".html"):
            text = path.read_text(errors="replace")
        elif ext == ".zip":
            with zipfile.ZipFile(path) as z:
                text = "[ZIP contents]\n" + "\n".join(z.namelist())
        else:
            text = f"[{ext} file, {path.stat().st_size} bytes: content not extractable as text]"
    except Exception as e:  # a corrupt file is itself a finding for the grader
        text = f"[FILE COULD NOT BE OPENED: {type(e).__name__}: {e}]"
    if len(text) > MAX_CHARS_PER_FILE:
        dropped = len(text) - MAX_CHARS_PER_FILE
        text = text[:MAX_CHARS_PER_FILE] + f"\n[TRUNCATED: {dropped} more characters not shown]"
    return text


def extract_all(paths: list[Path]) -> str:
    if not paths:
        return "(no deliverable files were produced)"
    return "\n\n".join(f"===== FILE: {p.name} =====\n{extract(p)}" for p in sorted(paths))


if __name__ == "__main__":
    import sys
    print(extract_all([Path(a) for a in sys.argv[1:]]))
