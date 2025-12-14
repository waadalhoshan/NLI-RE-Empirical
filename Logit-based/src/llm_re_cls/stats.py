from __future__ import annotations
from typing import Dict, List, Any
import itertools
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon, friedmanchisquare

def holm_adjust(pvals: List[float]) -> List[float]:
    m = len(pvals)
    order = np.argsort(pvals)
    adj = np.empty(m, dtype=float)
    for i, idx in enumerate(order):
        adj[idx] = min(1.0, (m - i) * pvals[idx])
    for i in range(1, m):
        adj[order[i]] = max(adj[order[i]], adj[order[i-1]])
    return adj.tolist()

def rq2_wilcoxon(scores_a: List[float], scores_b: List[float]) -> Dict[str, float]:
    stat, p = wilcoxon(scores_a, scores_b, zero_method="wilcox", correction=False)
    return {"W": float(stat), "p_value": float(p)}

def rq1_friedman(df_long: pd.DataFrame, block_cols: List[str], condition_col: str, metric_col: str = "wF1") -> Dict[str, Any]:
    wide = df_long.pivot_table(index=block_cols, columns=condition_col, values=metric_col, aggfunc="mean").dropna(axis=0, how="any")
    if wide.shape[1] < 3 or wide.shape[0] < 5:
        return {"status":"insufficient_data", "k": int(wide.shape[1]), "n_blocks": int(wide.shape[0])}
    chi2, p = friedmanchisquare(*[wide[c].to_numpy() for c in wide.columns])
    pairs, stats, pvals = [], [], []
    for a, b in itertools.combinations(wide.columns, 2):
        stat, pv = wilcoxon(wide[a], wide[b], zero_method="wilcox", correction=False)
        pairs.append((a,b)); stats.append(stat); pvals.append(pv)
    posthoc = pd.DataFrame({"cond_a":[x for x,_ in pairs], "cond_b":[y for _,y in pairs], "W":stats, "p_value":pvals, "p_adj":holm_adjust(pvals)})
    return {"status":"ok", "friedman":{"chi2": float(chi2), "p_value": float(p), "k": int(wide.shape[1]), "n_blocks": int(wide.shape[0])}, "posthoc": posthoc}
