from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass(frozen=True)
class PromptTemplate:
    name: str
    template: str

    def render(self, req: str, label: str, definition: str = "") -> str:
        return self.template.format(req=req, label=label, definition=definition)

def load_prompts(prompts_cfg: Dict) -> Dict[str, PromptTemplate]:
    patterns = prompts_cfg.get("patterns", {})
    return {k: PromptTemplate(k, v) for k, v in patterns.items()}
