from dataclasses import dataclass
from typing import List, Union

from classes.item import Item
from classes.rule import Rule
from classes.spell import Spell


@dataclass
class InferenceEngine:
    rules: List[Rule]

    def match(self, items: List[Union[Item, Spell]]):
        matched_items = []
        for item in items:
            score = 0
            for rule in self.rules:
                if rule.matches(item):
                    score += rule.weight

            # Se o item inflige condições, aumenta a pontuação
            if hasattr(item, "conditions_inflicted"):
                for _ in item.conditions_inflicted:
                    score += 1  # Proporcional a imunidade a condições

            if score > 0:
                matched_items.append((item, score))

        return matched_items

    def run(self, items: List[Union[Item, Spell]]):
        applicable_items = self.match(items)
        applicable_items.sort(key=lambda x: x[1], reverse=True)
        return applicable_items  # Retorna a lista ordenada de tuplas (item, score)
