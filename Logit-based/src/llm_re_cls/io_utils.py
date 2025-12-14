from __future__ import annotations
from pathlib import Path
import pandas as pd

def ensure_excel(local_path: str, url: str = "") -> str:
    p = Path(local_path)
    if p.exists():
        return str(p)
    if url:
        p.parent.mkdir(parents=True, exist_ok=True)
        df = pd.read_excel(url)
        df.to_excel(p, index=False)
        return str(p)
    raise FileNotFoundError(f"Missing file: {local_path} and no url provided.")

def read_excel_any(local_path: str, url: str = "") -> pd.DataFrame:
    path = ensure_excel(local_path, url=url)
    return pd.read_excel(path)
