# ChatGPT Baseline Reproducibility Repo — Requirements Classification (All Tasks)

This repo is a **ChatGPT-only** reproducibility package.

Unlike the earlier draft, this repo includes **all tasks** and the **actual prompt materials** (definitions + examples)
extracted into `prompts/*.txt`, then referenced from `configs/tasks.yaml`.

## Tasks included
- Functional
- Functional-PROMISE
- Quality
- Security
- NFR (multi-class)
- NFR-top (top classes)
- NFR-Hier (hierarchical)

`configs/tasks.yaml` also stores the original **Google Sheets source URLs** found in the notebook, so the runner can
download them automatically (as XLSX) if you don’t provide local files.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## API key
```bash
export OPENAI_API_KEY="YOUR_KEY"
```

## Run
```bash
python scripts/run_chatgpt.py --tasks configs/tasks.yaml
```

Outputs:
- `results/runs/<timestamp>/*_ChatGPT_Results.xlsx`
- `results/runs/<timestamp>/summary.json`

## Notes
- Prompts are stored verbatim in `prompts/` for transparency and easy edits.
- If you adjust wording, keep the output format consistent with the `parse_regex` in the config.
