from dataclasses import dataclass
from enum import Enum

from classes.enemy import Enemy
from classes.item import Item
from classes.spell import Spell


class RuleType(Enum):
    VULNERABILITY = 0
    RESISTANCE = 1
    IMMUNITY = 2
    CONDITION_IMMUNITY = 3


@dataclass
class Rule:
    enemy_attribute: str
    item_property: str
    effect_type: RuleType

    def matches(self, enemy: Enemy, item: Item | Spell):
        if self.effect_type == RuleType.VULNERABILITY:
            return (
                self.enemy_attribute in enemy.vulnerabilities
                and self.item_property in item.properties
            )
        elif self.effect_type == RuleType.RESISTANCE:
            return (
                self.enemy_attribute in enemy.resistances
                and self.item_property in item.properties
            )
        elif self.effect_type == RuleType.IMMUNITY:
            return (
                self.enemy_attribute in enemy.immunities
                and self.item_property in item.properties
            )
        elif self.effect_type == RuleType.CONDITION_IMMUNITY:
            return (
                self.enemy_attribute in enemy.condition_immunities
                and self.item_property in item.properties
            )
        return False
