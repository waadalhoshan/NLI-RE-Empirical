from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
from src.llm_re_cls.stats import rq1_friedman, rq2_wilcoxon

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Long-form CSV with columns for blocks, condition, metric")
    ap.add_argument("--mode", choices=["rq1","rq2"], required=True)
    ap.add_argument("--metric", default="wF1")
    ap.add_argument("--block-cols", default="dataset,task,block_id")
    ap.add_argument("--condition-col", default="prompt")
    ap.add_argument("--a", default="")
    ap.add_argument("--b", default="")
    ap.add_argument("--outdir", default="results/tables")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.input)

    if args.mode == "rq1":
        blocks = [c.strip() for c in args.block_cols.split(",")]
        res = rq1_friedman(df, blocks, args.condition_col, args.metric)
        (outdir / "rq1_friedman.json").write_text(pd.Series(res["friedman"]).to_json() if res.get("status")=="ok" else str(res), encoding="utf-8")
        if res.get("status")=="ok":
            res["posthoc"].to_csv(outdir / "rq1_posthoc.csv", index=False)
        print(res)
    else:
        # rq2 expects two series; here you can filter by columns a/b upstream and pass lists
        raise SystemExit("RQ2 script is a helper; please compute paired lists and call rq2_wilcoxon in code.")

if __name__ == "__main__":
    main()
