from __future__ import annotations
from typing import List, Dict
from sklearn.metrics import precision_recall_fscore_support

def weighted_prf(y_true: List[str], y_pred: List[str]) -> Dict[str, float]:
    p, r, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="weighted", zero_division=0)
    return {"wP": float(p), "wR": float(r), "wF1": float(f1)}
