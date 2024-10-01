from dataclasses import dataclass
from typing import List

from classes.enemy import Enemy
from classes.item import Item
from classes.rule import Rule, RuleType
from classes.spell import Spell


@dataclass
class ReteEngine:
    rules: List[Rule]

    def match(self, enemy: Enemy, items: list[Item | Spell]):
        matched_items = []
        for item in items:
            score = 0
            for rule in self.rules:
                if rule.effect_type == RuleType.VULNERABILITY and rule.matches(
                    enemy, item
                ):
                    score += 3  # Dê mais peso para vulnerabilidades
                elif rule.effect_type == RuleType.RESISTANCE and rule.matches(
                    enemy, item
                ):
                    score -= 2  # Reduza a pontuação por resistências ou imunidade a condições
                elif rule.effect_type == RuleType.IMMUNITY and rule.matches(
                    enemy, item
                ):
                    score -= 3  # Reduza drasticamente se houver imunidade a algum dano
                elif rule.effect_type == RuleType.CONDITION_IMMUNITY and rule.matches(
                    enemy, item
                ):
                    score -= 1  # Reduza a pontuação por imunidade a condições

            # Aumente a pontuação dos items que infligem condições aos monstros
            if hasattr(item, "conditions_inflicted"):
                for _ in item.conditions_inflicted:
                    score += 1
            if score > 0:
                matched_items.append((item, score))
        return matched_items

    def run(self, enemy, items):
        applicable_items = self.match(enemy, items)
        applicable_items.sort(key=lambda x: x[1], reverse=True)
        # Agora retorna uma lista de tuplas (item, score)
        return applicable_items
