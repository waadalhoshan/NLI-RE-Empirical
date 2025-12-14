from __future__ import annotations
import argparse
from pathlib import Path
import yaml
from src.embedding_rc.labels import load_curated_labels

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--experiments", default="configs/experiments.yaml")
    ap.add_argument("--csv", default="data/labels/curated_label_texts.csv")
    args = ap.parse_args()

    exp = yaml.safe_load(Path(args.experiments).read_text(encoding="utf-8"))
    curated = load_curated_labels(args.csv).by_task

    ok=True
    for t in exp["tasks"]:
        tname=t["name"]
        labels = t.get("labels") or (t.get("root_labels") or [])
        if tname not in curated:
            print("[MISSING TASK]", tname); ok=False; continue
        miss=[l for l in labels if l not in curated[tname]]
        if miss:
            print("[MISSING LABELS]", tname, miss); ok=False
    if ok:
        print("[OK] curated labels cover all configured tasks")

if __name__ == "__main__":
    main()
