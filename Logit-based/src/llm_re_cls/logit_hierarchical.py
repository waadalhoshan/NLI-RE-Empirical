from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple
import torch
import pandas as pd
from .logit_flat import LogitSequenceClassifier
from .prompts import PromptTemplate
from .hierarchy import hierarchical_prf

@dataclass
class LogitHierarchicalRunner:
    clf: LogitSequenceClassifier

    def classify_one(self, req: str, hierarchy: Dict[str, List[str]], defs: Dict[str, str], prompt: PromptTemplate) -> Tuple[str, str, List[float]]:
        current = hierarchy.get("root_labels", [])
        path: List[str] = []
        last_probs: List[float] = []
        while current:
            prompts = []
            usable_labels = []
            for lab in current:
                d = defs.get(lab, "")
                prompts.append(prompt.render(req=req, label=lab, definition=d))
                usable_labels.append(lab)
            pred, probs = self.clf.predict_label(prompts, usable_labels)
            last_probs = [p[0] for p in probs]
            path.append(pred)
            current = hierarchy.get(pred, [])
        hier_label = "/".join(path)
        flat_label = path[-1] if path else ""
        return hier_label, flat_label, last_probs

    def evaluate(self, df: pd.DataFrame, hierarchy: Dict[str, List[str]], defs: Dict[str, str], prompt: PromptTemplate) -> Dict[str, float]:
        y_true = df["Label"].astype(str).tolist()
        y_pred_h = []
        y_pred_flat = []
        for _, row in df.iterrows():
            hier, flat, _ = self.classify_one(str(row["RequirementText"]), hierarchy, defs, prompt)
            y_pred_h.append(hier)
            y_pred_flat.append(flat)
        from .metrics import weighted_prf
        flat = weighted_prf(y_true, y_pred_flat)
        hP, hR, hF1 = hierarchical_prf(y_true, y_pred_h)
        return {**flat, "hP": hP, "hR": hR, "hF1": hF1}
