# Reproducibility Artifacts for  
**How Effective Are Generative LLMs Using Logit-Based Inference for Requirements Classification?  
An Empirical Evaluation**  

**Waad Alhoshan · Alessio Ferrari · Liping Zhao**

---

This repository page documents the **reproducibility artifacts** accompanying our empirical study on the effectiveness of **Generative Large Language Models (LLMs)** for **requirements classification**, with a particular focus on **logit-based zero-shot inference**.

To ensure clarity, modularity, and ease of reuse, we provide **three separate repositories**, each corresponding to a distinct modeling paradigm evaluated in the paper.

---

## 1️ - Logit-Based Zero-Shot Inference (Main Contribution)

**Repository:** `logit-based-requirements-classification`

This repository implements our **primary contribution**:  
**logit-based zero-shot inference using generative LLMs**, where classification decisions are derived from **model output logits**, rather than from generated labels.

### Key characteristics
- Supports **binary**, **multi-class**, and **hierarchical** requirements classification
- Uses **fixed prompt templates**; only the **label string changes**
- No fine-tuning or external training data required
- Fully deterministic scoring pipeline
- Closely aligned with the experimental design reported in the paper

**This is the main artifact for reproducing the core results of the paper.**

---

## 2- Embedding-Based Zero-Shot Baseline

**Repository:** `embedding-based-requirements-classification`

This repository implements a **standard embedding-based zero-shot classification baseline**, where:
- Requirements and **expert-curated label texts** are embedded using a sentence embedding model
- Labels are assigned via **cosine similarity**
- Hierarchical classification is performed via **top-down traversal**

### Key characteristics
- Supports **binary**, **multi-class**, and **hierarchical** settings
- Relies on **explicit label descriptions**, curated by domain experts
- Serves as a **non-generative semantic baseline** for comparison

This repository corresponds to the **embedding-based baseline** reported in the paper and allows readers to assess how much performance is gained by **logit-based inference over embedding-based similarity**.

---

## 3-  ChatGPT Prompting Baseline

**Repository:** `chatgpt-requirements-classification`

This repository provides a **ChatGPT-based classification baseline**, implemented via:
- Instruction prompting
- Batch processing of requirements
- Deterministic decoding (temperature = 0)
- Robust output parsing and evaluation

### Key characteristics
- Covers **binary**, **multi-class**, and **hierarchical** tasks
- Includes **full task definitions and examples** used in the experiments
- Reflects common practitioner-style usage of ChatGPT for classification

This repository supports the analysis of **generation-based prompting**, enabling a direct comparison with **logit-based inference**, as discussed in the paper.

---

## Relationship Between the Repositories

| Repository | Method | Role in Paper |
|----------|-------|---------------|
| Logit-based | Generative LLM + logits | **Main contribution** |
| Embedding-based | Sentence embeddings | Zero-shot baseline |
| ChatGPT | Prompted generation | Generative baseline |

Each repository is **self-contained**, but all follow:
- Consistent dataset usage
- Comparable evaluation metrics
- Transparent and reproducible workflows

---

## Citation

If you use any of these artifacts, please cite our paper:

> **How Effective Are Generative LLMs Using Logit-Based Inference for Requirements Classification?  
> An Empirical Evaluation**  
> Waad Alhoshan, Alessio Ferrari, Liping Zhao

---


