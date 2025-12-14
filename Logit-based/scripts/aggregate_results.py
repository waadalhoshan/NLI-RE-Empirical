from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="results/runs")
    ap.add_argument("--out", default="results/summary.csv")
    args = ap.parse_args()

    rows = []
    for d in Path(args.runs).glob("*"):
        if not d.is_dir():
            continue
        for f in d.glob("*.json"):
            try:
                obj = json.loads(f.read_text(encoding="utf-8"))
            except Exception:
                continue
            if isinstance(obj, list):
                for r in obj:
                    rows.append({"run": d.name, "file": f.name, **r})
            elif isinstance(obj, dict):
                rows.append({"run": d.name, "file": f.name, **obj})
    df = pd.DataFrame(rows)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out, index=False)
    print("[OK] wrote", args.out)

if __name__ == "__main__":
    main()
