from __future__ import annotations
import argparse, json, time
from pathlib import Path
import yaml
import pandas as pd
from rich import print

from src.chatgpt_rc.openai_client import OpenAISettings, ChatClient
from src.chatgpt_rc.io import read_excel_any
from src.chatgpt_rc.parse import chunked, parse_numbered_labels, default_label_line
from src.chatgpt_rc.metrics import weighted_prf

def read_prompt(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", default="configs/tasks.yaml")
    ap.add_argument("--outdir", default="results/runs")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.tasks).read_text(encoding="utf-8"))
    settings = OpenAISettings(**cfg["openai"])
    client = ChatClient(settings)

    defaults = cfg.get("defaults", {})
    stamp = time.strftime("%Y%m%d-%H%M%S")
    outdir = Path(args.outdir) / stamp
    outdir.mkdir(parents=True, exist_ok=True)

    summaries = []

    for task in cfg["tasks"]:
        df = read_excel_any(task["local_path"], task.get("source_url",""))
        text_col = task["text_col"]
        true_col = task.get("true_col","")
        batch_size = int(task.get("batch_size", defaults.get("batch_size", 10)))
        parse_regex = task.get("parse_regex", defaults.get("parse_regex"))

        system_prompt = read_prompt(task["system_prompt_file"])

        reqs = df[text_col].astype(str).str.replace("\n", " ", regex=False).tolist()
        preds = [""] * len(reqs)

        for start, batch in chunked(reqs, batch_size):
            user_prompt = "\n".join([default_label_line(start+i+1, r) for i, r in enumerate(batch)])
            resp = client.chat(system_prompt, user_prompt)
            parsed = parse_numbered_labels(resp, parse_regex)

            for i in range(len(batch)):
                idx = start + i + 1
                if idx in parsed:
                    parts = parsed[idx]
                    # label mode: first captured group is label
                    if task.get("output_mode") == "hier":
                        # expect (level1, level2)
                        if len(parts) >= 2:
                            preds[idx-1] = f"{parts[0]} --> {parts[1]}"
                        elif len(parts) == 1:
                            preds[idx-1] = parts[0]
                    else:
                        preds[idx-1] = parts[0] if parts else ""

        df["Predicted Label"] = preds

        metrics = {}
        if true_col and true_col in df.columns:
            metrics = weighted_prf(df[true_col].astype(str).tolist(), df["Predicted Label"].astype(str).tolist())

        out_xlsx = outdir / f"{task['name']}_ChatGPT_Results.xlsx"
        df.to_excel(out_xlsx, index=False)

        summaries.append({"task": task["name"], **metrics})
        print(f"[green]OK[/green] {task['name']} -> {out_xlsx} {metrics}")

    (outdir / "summary.json").write_text(json.dumps(summaries, indent=2), encoding="utf-8")
    print(f"[bold]Wrote[/bold] {outdir}")

if __name__ == "__main__":
    main()
