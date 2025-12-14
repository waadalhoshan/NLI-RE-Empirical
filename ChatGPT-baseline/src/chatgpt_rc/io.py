from __future__ import annotations
from pathlib import Path
import re
import pandas as pd
import requests

def google_sheet_to_xlsx_url(url: str) -> str:
    # Supports typical "spreadsheets/d/<ID>/..." links
    m = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", url)
    if not m:
        return url
    sid = m.group(1)
    return f"https://docs.google.com/spreadsheets/d/{sid}/export?format=xlsx"

def ensure_excel(local_path: str, source_url: str = "") -> str:
    p = Path(local_path)
    if p.exists():
        return str(p)
    if source_url:
        p.parent.mkdir(parents=True, exist_ok=True)
        xurl = google_sheet_to_xlsx_url(source_url)
        r = requests.get(xurl, timeout=60)
        r.raise_for_status()
        p.write_bytes(r.content)
        return str(p)
    raise FileNotFoundError(f"Missing {local_path} and no source_url provided.")

def read_excel_any(local_path: str, source_url: str = "") -> pd.DataFrame:
    path = ensure_excel(local_path, source_url=source_url)
    return pd.read_excel(path)
