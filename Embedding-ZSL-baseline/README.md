# Embedding-based Zero-shot Baseline — Requirements Classification (Flat + Hierarchical)

This repository contains an **embedding-based** zero-shot baseline for requirements classification:

- **Flat tasks** (binary + multi-class): choose label whose *curated label text* is closest to the requirement text in embedding space.
- **Hierarchical task**: greedy top-down traversal (root → child) using the same embedding similarity.

## Key input you will edit
`data/labels/curated_label_texts.csv`  
One row per **task × label** with a `curated_text` string.

A starter version is included and **pre-filled** with expert-curated label texts extracted from your hierarchical notebook export (FR/NFR + NFR subclasses).

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Data
Put Excel files under `data/raw/` and configure them in `configs/datasets.yaml`.

## Run
Flat tasks:
```bash
python scripts/run_embedding_flat.py --dataset-key functional
python scripts/run_embedding_flat.py --dataset-key nfr_multi
```

Hierarchical:
```bash
python scripts/run_embedding_hierarchical.py
```

Outputs are written to `results/runs/<timestamp>/`.
