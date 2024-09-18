from dataclasses import dataclass
from typing import List
from classes.rule import Rule


@dataclass
class ReteEngine:
    rules: List[Rule]

    def match(self, enemy, items):
        matched_items = []
        for item in items:
            score = 0
            for rule in self.rules:
                if rule.effect_type == "vulnerability" and rule.matches(enemy, item):
                    score += 2  # Dê mais peso para vulnerabilidades
                elif rule.effect_type == "resistance" and rule.matches(enemy, item):
                    score -= 1  # Reduza a pontuação por resistências
                elif rule.effect_type == "immunity" and rule.matches(enemy, item):
                    score = 0  # Zere a pontuação se houver imunidade
            if score > 0:
                matched_items.append((item, score))
        return matched_items

    def run(self, enemy, items):
        applicable_items = self.match(enemy, items)
        applicable_items.sort(key=lambda x: x[1], reverse=True)
        recommendations = [item.name for item, score in applicable_items]
        return recommendations
