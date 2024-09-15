from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    name: str
    properties: List[str]
