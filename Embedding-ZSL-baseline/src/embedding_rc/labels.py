from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple
from pathlib import Path
import pandas as pd

@dataclass(frozen=True)
class CuratedLabels:
    by_task: Dict[str, Dict[str, str]]
    parents: Dict[Tuple[str,str], str]

def load_curated_labels(csv_path: str) -> CuratedLabels:
    p = Path(csv_path)
    if not p.exists():
        raise FileNotFoundError(csv_path)
    df = pd.read_csv(p)
    need = {"task","label","curated_text"}
    if not need.issubset(df.columns):
        raise ValueError(f"CSV must contain {sorted(need)}")
    by_task: Dict[str, Dict[str,str]] = {}
    parents: Dict[Tuple[str,str], str] = {}
    for _, r in df.iterrows():
        t=str(r["task"]); lab=str(r["label"]); txt=str(r.get("curated_text","") or "")
        by_task.setdefault(t, {})[lab]=txt if txt else lab
        parent = str(r.get("parent_label","") or "")
        if parent:
            parents[(t,lab)] = parent
    return CuratedLabels(by_task=by_task, parents=parents)
