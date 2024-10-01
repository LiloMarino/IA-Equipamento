from dataclasses import dataclass
from typing import List


@dataclass
class Spell:
    name: str
    damage_types: List[str]
    conditions_inflicted: List[str]

    @property
    def properties(self):
        return self.damage_types + self.conditions_inflicted
