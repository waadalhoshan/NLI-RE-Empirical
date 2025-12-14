from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

@dataclass
class EmbeddingZSL:
    hf_id: str

    def __post_init__(self):
        self.enc = SentenceTransformer(self.hf_id)

    def predict(self, text: str, label_texts: List[Tuple[str,str]]) -> str:
        labels, reps = zip(*label_texts)
        v_req = self.enc.encode([text], normalize_embeddings=True)
        v_lab = self.enc.encode(list(reps), normalize_embeddings=True)
        sims = cosine_similarity(v_req, v_lab)[0]
        return labels[int(np.argmax(sims))]
