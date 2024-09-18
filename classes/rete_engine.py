from dataclasses import dataclass
from typing import List
from classes.rule import Rule


@dataclass
class ReteEngine:
    rules: List[Rule]

    def match(self, enemy, items):
        matched_items = []
        for item in items:
            # Calcula a pontuação com base no número de regras que correspondem ao item
            score = sum(1 for rule in self.rules if rule.matches(enemy, item))
            if score > 0:
                matched_items.append((item, score))
        return matched_items

    def run(self, enemy, items):
        applicable_items = self.match(enemy, items)
        # Ordenar itens por maior pontuação
        applicable_items.sort(key=lambda x: x[1], reverse=True)
        # Retorna uma lista com os nomes dos itens
        recommendations = [item.name for item, score in applicable_items]
        return recommendations
