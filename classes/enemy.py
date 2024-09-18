from dataclasses import dataclass
from typing import List


@dataclass
class Enemy:
    name: str
    vulnerabilities: List[str]
    resistances: List[str]
    immunities: List[str]
    condition_immunities: List[str]
