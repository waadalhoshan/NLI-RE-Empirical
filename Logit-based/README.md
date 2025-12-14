# Reproducibility Package — Logit-based Zero-Shot Requirements Classification (Logit-only)

This repository contains the **logit-based** zero-shot classification implementation (our approach),
supporting:

- **Binary** classification tasks
- **Multi-class** classification tasks
- **Hierarchical** classification tasks

Prompt templates are aligned with `notebooks/logit.txt` (6 prompt patterns).

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Data

Place your datasets under `data/raw/` and configure paths in `configs/datasets.yaml`.

## Run (flat tasks: binary/multi-class)

```bash
python scripts/run_logit_flat.py --dataset-key functional
python scripts/run_logit_flat.py --dataset-key nfr_multi
```

## Run (hierarchical)

```bash
python scripts/run_logit_hierarchical.py
```

## Outputs

Each run writes to `results/runs/<run_name_timestamp>/`:
- `metrics.json`
- `predictions.csv` (flat tasks)

## Statistics
`scripts/stats.py` + `src/llm_re_cls/stats.py` include RQ1/RQ2 utilities (non-parametric tests).
