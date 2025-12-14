from __future__ import annotations
from typing import Dict, List
import pandas as pd

def build_hierarchy_from_dataset(df: pd.DataFrame, fr_col: str, nfr_col: str) -> Dict[str, List[str]]:
    h: Dict[str, List[str]] = {"root_labels": []}
    roots = df[fr_col].dropna().astype(str).unique().tolist()
    h["root_labels"] = roots
    for r in roots:
        h[r] = []
    # children under Non-Functional
    for _, row in df.iterrows():
        r = str(row.get(fr_col,""))
        if r.lower() == "non-functional":
            child = row.get(nfr_col, "")
            if pd.notna(child):
                c = str(child)
                if c not in h[r]:
                    h[r].append(c)
    return h
