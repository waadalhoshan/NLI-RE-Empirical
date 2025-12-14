from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple, Dict
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

@dataclass
class LogitSequenceClassifier:
    hf_id: str
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    use_auth_token: bool = False

    def __post_init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained(self.hf_id, use_auth_token=self.use_auth_token)
        self.tokenizer = AutoTokenizer.from_pretrained(self.hf_id)
        self.model.to(self.device)
        self.model.eval()
        # pad token
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model.config.pad_token_id = self.tokenizer.pad_token_id

    @torch.no_grad()
    def predict_label(self, prompts: List[str], labels: List[str]) -> Tuple[str, List[List[float]]]:
        encoded = self.tokenizer(prompts, padding=True, truncation=True, return_tensors="pt").to(self.device)
        out = self.model(**encoded)
        logits = out.logits
        if len(labels) > 2:
            log_probs = torch.nn.functional.log_softmax(logits, dim=1)
            probs = torch.exp(log_probs)
        else:
            probs = torch.sigmoid(logits)
        probs_list = probs.detach().cpu().tolist()
        # follow notebook logic: choose candidate with max first element
        max_idx = max(range(len(probs_list)), key=lambda i: probs_list[i][0])
        return labels[max_idx], probs_list
