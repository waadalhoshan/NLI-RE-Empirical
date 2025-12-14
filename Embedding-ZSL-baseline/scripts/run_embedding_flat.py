from __future__ import annotations
import argparse, time, json
from pathlib import Path
import yaml
import pandas as pd
from src.embedding_rc.io import read_excel_any
from src.embedding_rc.labels import load_curated_labels
from src.embedding_rc.model import EmbeddingZSL
from src.embedding_rc.metrics import weighted_prf

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset-key", required=True)
    ap.add_argument("--datasets", default="configs/datasets.yaml")
    ap.add_argument("--experiments", default="configs/experiments.yaml")
    ap.add_argument("--labels-csv", default="data/labels/curated_label_texts.csv")
    ap.add_argument("--outdir", default="results/runs")
    args = ap.parse_args()

    ds_cfg = yaml.safe_load(Path(args.datasets).read_text(encoding="utf-8"))["datasets"][args.dataset_key]
    exp = yaml.safe_load(Path(args.experiments).read_text(encoding="utf-8"))
    task_name = ds_cfg["task"]
    task = next(t for t in exp["tasks"] if t["name"] == task_name)
    labels = task["labels"]

    curated = load_curated_labels(args.labels_csv).by_task
    label_texts = [(lab, curated[task_name].get(lab, lab)) for lab in labels]

    df = read_excel_any(ds_cfg["local_path"], ds_cfg.get("url",""))
    df = df.dropna(subset=[ds_cfg["text_col"], ds_cfg["label_col"]]).copy()
    df["text"] = df[ds_cfg["text_col"]].astype(str).str.replace("\n"," ", regex=False)
    df["true"] = df[ds_cfg["label_col"]].astype(str)

    mcfg = exp["embedding_model"]
    model = EmbeddingZSL(hf_id=mcfg["hf_id"])

    y_true, y_pred = [], []
    for _, r in df.iterrows():
        pred = model.predict(r["text"], label_texts)
        y_true.append(r["true"]); y_pred.append(pred)

    metrics = weighted_prf(y_true, y_pred)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    outdir = Path(args.outdir) / f"embed_flat_{args.dataset_key}_{stamp}"
    outdir.mkdir(parents=True, exist_ok=True)
    df["Predicted Label"] = y_pred
    df.to_excel(outdir / "predictions.xlsx", index=False)
    (outdir / "metrics.json").write_text(json.dumps({"dataset": args.dataset_key, "task": task_name, **metrics}, indent=2), encoding="utf-8")
    print(metrics)
    print("[OK] wrote", outdir)

if __name__ == "__main__":
    main()
