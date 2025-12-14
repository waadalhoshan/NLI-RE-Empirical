from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional
import pandas as pd

@dataclass(frozen=True)
class HierDatasetConfig:
    local_path: str
    text_col: str
    fr_label_col: str
    nfr_label_col: str
    fr_def_col: str
    nfr_def_col: str

def load_excel(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Missing file: {path}. Put it under data/raw/ or update configs/datasets.yaml")
    return pd.read_excel(p)

def load_hierarchical_dataset(cfg: Dict) -> pd.DataFrame:
    ds = HierDatasetConfig(**cfg)
    df = load_excel(ds.local_path)
    return df
