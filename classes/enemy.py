from dataclasses import dataclass
from typing import List


@dataclass
class Enemy:
    name: str
    weaknesses: List[str]
