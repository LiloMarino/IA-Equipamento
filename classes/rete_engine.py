from dataclasses import dataclass
from typing import List, Union

from classes.enemy import Enemy
from classes.item import Item
from classes.rule import Rule, RuleType
from classes.spell import Spell


@dataclass
class ReteEngine:
    rules: List[Rule]

    def match(self, enemy: Enemy, items: List[Union[Item, Spell]]):
        matched_items = []
        for item in items:
            score = 0
            for rule in self.rules:
                if rule.matches(enemy, item):
                    # Pontuação baseada no tipo de efeito da regra
                    if rule.effect_type == RuleType.VULNERABILITY:
                        score += 3  # Vulnerabilidade aumenta a pontuação
                    elif rule.effect_type == RuleType.RESISTANCE:
                        score -= 2  # Resistência diminui a pontuação
                    elif rule.effect_type == RuleType.IMMUNITY:
                        score -= 3  # Imunidade a dano reduz drasticamente (proporcional a vulnerabilidade)
                    elif rule.effect_type == RuleType.CONDITION_IMMUNITY:
                        score -= 1  # Imunidade a condições diminui a pontuação

            # Se o item inflige condições, aumenta a pontuação
            if hasattr(item, "conditions_inflicted"):
                for _ in item.conditions_inflicted:
                    score += 1  # Proporcional a imunidade a condições

            if score > 0:
                matched_items.append((item, score))

        return matched_items

    def run(self, enemy: Enemy, items: List[Union[Item, Spell]]):
        applicable_items = self.match(enemy, items)
        applicable_items.sort(key=lambda x: x[1], reverse=True)
        return applicable_items  # Retorna a lista ordenada de tuplas (item, score)
