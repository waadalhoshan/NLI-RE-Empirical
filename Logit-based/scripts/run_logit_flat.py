from __future__ import annotations
import argparse, time, json
from pathlib import Path
import yaml
import pandas as pd

from src.llm_re_cls.io_utils import read_excel_any
from src.llm_re_cls.prompts import load_prompts
from src.llm_re_cls.logit_flat import LogitSequenceClassifier
from src.llm_re_cls.metrics import weighted_prf

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/experiments.yaml")
    ap.add_argument("--datasets", default="configs/datasets.yaml")
    ap.add_argument("--dataset-key", required=True, help="Key under configs/datasets.yaml")
    ap.add_argument("--prompt", default="assertion_is_about")
    ap.add_argument("--outdir", default="results/runs")
    args = ap.parse_args()

    exp = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    ds_cfg = yaml.safe_load(Path(args.datasets).read_text(encoding="utf-8"))["datasets"][args.dataset_key]
    prompts_cfg = yaml.safe_load(Path("configs/prompts.yaml").read_text(encoding="utf-8"))
    prompts = load_prompts(prompts_cfg)

    task_name = ds_cfg["task"]
    task = next(t for t in exp["tasks"] if t["name"] == task_name)
    labels = task["labels"]

    df = read_excel_any(ds_cfg["local_path"], ds_cfg.get("url",""))
    df = df.dropna(subset=[ds_cfg["text_col"], ds_cfg["label_col"]]).copy()
    df["text"] = df[ds_cfg["text_col"]].astype(str).str.replace("\n"," ", regex=False)
    df["label"] = df[ds_cfg["label_col"]].astype(str)

    mcfg = exp["models"]["logit_models"][0]
    clf = LogitSequenceClassifier(hf_id=mcfg["hf_id"], use_auth_token=bool(mcfg.get("requires_auth", False)))

    spec = prompts[args.prompt]

    y_true, y_pred = [], []
    rows = []
    for _, r in df.iterrows():
        req = r["text"]
        cand_prompts = [spec.render(req=req, label=lab, definition="") for lab in labels]
        pred, probs = clf.predict_label(cand_prompts, labels)
        y_true.append(r["label"]); y_pred.append(pred)
        rows.append({"Requirement": req, "True Label": r["label"], "Predicted Label": pred, "Scores": json.dumps(probs)})

    metrics = weighted_prf(y_true, y_pred)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    outdir = Path(args.outdir) / f"logit_flat_{args.dataset_key}_{stamp}"
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "metrics.json").write_text(json.dumps({"dataset": args.dataset_key, "task": task_name, "prompt": args.prompt, **metrics}, indent=2), encoding="utf-8")
    pd.DataFrame(rows).to_csv(outdir / "predictions.csv", index=False)
    print(metrics)
    print("[OK] wrote", outdir)

if __name__ == "__main__":
    main()
