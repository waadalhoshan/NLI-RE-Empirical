from __future__ import annotations
import argparse, time, json
from pathlib import Path
import yaml
import pandas as pd
from src.embedding_rc.io import read_excel_any
from src.embedding_rc.labels import load_curated_labels
from src.embedding_rc.model import EmbeddingZSL
from src.embedding_rc.hierarchy import build_hierarchy_from_dataset

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset-key", default="hierarchical_promise_xlsx")
    ap.add_argument("--datasets", default="configs/datasets.yaml")
    ap.add_argument("--experiments", default="configs/experiments.yaml")
    ap.add_argument("--labels-csv", default="data/labels/curated_label_texts.csv")
    ap.add_argument("--outdir", default="results/runs")
    args = ap.parse_args()

    ds_cfg = yaml.safe_load(Path(args.datasets).read_text(encoding="utf-8"))["datasets"][args.dataset_key]
    exp = yaml.safe_load(Path(args.experiments).read_text(encoding="utf-8"))
    task = next(t for t in exp["tasks"] if t["type"] == "hierarchical")
    task_name = task["name"]

    df = read_excel_any(ds_cfg["local_path"], ds_cfg.get("url",""))
    if ds_cfg.get("nfr_label_col") in df.columns:
        # match notebook behavior: drop Portability if desired by user later
        pass
    h = build_hierarchy_from_dataset(df, ds_cfg["fr_label_col"], ds_cfg["nfr_label_col"])

    curated = load_curated_labels(args.labels_csv).by_task
    model = EmbeddingZSL(hf_id=exp["embedding_model"]["hf_id"])

    preds=[]
    for _, r in df.iterrows():
        req = str(r[ds_cfg["text_col"]]).replace("\n"," ")
        current = h["root_labels"]
        path=[]
        while current:
            label_texts=[(lab, curated.get(task_name, {}).get(lab, lab)) for lab in current]
            pred = model.predict(req, label_texts)
            path.append(pred)
            current = h.get(pred, [])
        preds.append("/".join(path))

    df["Predicted Label"] = preds
    stamp = time.strftime("%Y%m%d-%H%M%S")
    outdir = Path(args.outdir) / f"embed_hier_{stamp}"
    outdir.mkdir(parents=True, exist_ok=True)
    df.to_excel(outdir / "predictions.xlsx", index=False)
    (outdir / "notes.txt").write_text("Metrics for hierarchical require gold labels + hierarchical metric; add if needed.", encoding="utf-8")
    print("[OK] wrote", outdir)

if __name__ == "__main__":
    main()
