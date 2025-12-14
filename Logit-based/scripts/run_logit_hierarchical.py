from __future__ import annotations
import argparse, time, json
from pathlib import Path
import yaml
import pandas as pd

from src.llm_re_cls.datasets import load_excel
from src.llm_re_cls.prompts import load_prompts
from src.llm_re_cls.hierarchy import generate_hierarchical_labels_from_dataset_with_nfr, generate_label_definitions_with_matching
from src.llm_re_cls.logit_flat import LogitSequenceClassifier
from src.llm_re_cls.logit_hierarchical import LogitHierarchicalRunner

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/experiments.yaml")
    ap.add_argument("--dataset", default="configs/datasets.yaml:hierarchical_promise_xlsx")
    ap.add_argument("--outdir", default="results/runs")
    args = ap.parse_args()

    exp = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    prompts_cfg = yaml.safe_load(Path("configs/prompts.yaml").read_text(encoding="utf-8"))
    prompts = load_prompts(prompts_cfg)

    ds_yaml, ds_key = args.dataset.split(":")
    ds_all = yaml.safe_load(Path(ds_yaml).read_text(encoding="utf-8"))
    ds = ds_all["datasets"][ds_key]

    df = load_excel(ds["local_path"])
    # remove Portability as in notebook
    if "NFR Label" in df.columns:
        df = df[df["NFR Label"] != "Portability"]

    # build hierarchical label path
    df["Label"] = df.apply(lambda r: r["FR Label"] if r["FR Label"] == "Functional" else "Non-Functional/"+str(r["NFR Label"]), axis=1)

    hierarchy = generate_hierarchical_labels_from_dataset_with_nfr(df)
    defs = generate_label_definitions_with_matching(df)

    mcfg = exp["models"]["logit_models"][0]
    clf = LogitSequenceClassifier(hf_id=mcfg["hf_id"], use_auth_token=bool(mcfg.get("requires_auth", False)))
    runner = LogitHierarchicalRunner(clf)

    stamp = time.strftime("%Y%m%d-%H%M%S")
    outdir = Path(args.outdir) / f"logit_hier_{stamp}"
    outdir.mkdir(parents=True, exist_ok=True)

    results = []
    for pname in exp["prompt_patterns"]:
        metrics = runner.evaluate(df, hierarchy, defs, prompts[pname])
        rec = {"prompt": pname, **metrics}
        results.append(rec)
        print(rec)

    (outdir / "metrics.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("[OK] wrote", outdir)

if __name__ == "__main__":
    main()
