from __future__ import annotations
from pathlib import Path
import re
import pandas as pd
import requests

def ensure_excel(local_path: str, url: str = "") -> str:
    p = Path(local_path)
    if p.exists():
        return str(p)
    if url:
        p.parent.mkdir(parents=True, exist_ok=True)
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        p.write_bytes(r.content)
        return str(p)
    raise FileNotFoundError(f"Missing {local_path} and no url provided.")

def read_excel_any(local_path: str, url: str = "") -> pd.DataFrame:
    path = ensure_excel(local_path, url=url)
    return pd.read_excel(path)
