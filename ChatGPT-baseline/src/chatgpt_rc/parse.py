from __future__ import annotations
import re
from typing import List, Tuple, Dict

def chunked(items: List[str], size: int):
    for i in range(0, len(items), size):
        yield i, items[i:i+size]

def parse_numbered_labels(text: str, regex: str) -> Dict[int, Tuple[str,...]]:
    pat = re.compile(regex, re.IGNORECASE)
    out: Dict[int, Tuple[str,...]] = {}
    for line in text.splitlines():
        m = pat.match(line.strip())
        if not m:
            continue
        idx = int(m.group(1))
        out[idx] = tuple(g.strip() for g in m.groups()[1:])
    return out

def default_label_line(idx: int, req: str) -> str:
    return f"{idx}. {req}"
