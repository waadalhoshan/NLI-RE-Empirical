from __future__ import annotations
from typing import Dict, List, Tuple, Set
import pandas as pd

def generate_hierarchical_labels_from_dataset_with_nfr(dataset: pd.DataFrame) -> Dict[str, List[str]]:
    hierarchical_labels: Dict[str, List[str]] = {"root_labels": []}
    hierarchical_labels["root_labels"] = dataset["FR Label"].unique().tolist()
    for root_label in hierarchical_labels["root_labels"]:
        hierarchical_labels[root_label] = []
    for _, row in dataset.iterrows():
        root_label = row["FR Label"]
        if str(root_label).lower() == "non-functional" and not pd.isna(row.get("NFR Label")):
            child_label = row["NFR Label"]
            if child_label not in hierarchical_labels[root_label]:
                hierarchical_labels[root_label].append(child_label)
    return hierarchical_labels

def generate_label_definitions_with_matching(dataset: pd.DataFrame) -> Dict[str, str]:
    label_definitions: Dict[str, str] = {}
    for _, row in dataset.iterrows():
        fr_label = row["FR Label"]
        if str(fr_label).lower() == "functional":
            label_definitions[fr_label] = row["FR/NFR Definition"]
        elif str(fr_label).lower() == "non-functional" and pd.notna(row.get("NFR Label")):
            nfr_label = row["NFR Label"]
            if fr_label not in label_definitions:
                label_definitions[fr_label] = row["FR/NFR Definition"]
            label_definitions[nfr_label] = row["NFR Label Definition"]
    return label_definitions

def get_ancestors(label: str) -> Set[str]:
    ancestors: Set[str] = set()
    parts = label.split('/')
    current = ''
    for part in parts:
        current = (current + '/' + part) if current else part
        ancestors.add(current)
    return ancestors

def hierarchical_prf(true_labels: List[str], predicted_labels: List[str]) -> Tuple[float, float, float]:
    tp = fp = fn = 0
    for t, p in zip(true_labels, predicted_labels):
        ta = get_ancestors(t)
        pa = get_ancestors(p)
        tp += len(ta & pa)
        fp += len(pa - ta)
        fn += len(ta - pa)
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (2*prec*rec)/(prec+rec) if (prec+rec) else 0.0
    return prec, rec, f1
