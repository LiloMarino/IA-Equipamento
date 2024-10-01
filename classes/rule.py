from dataclasses import dataclass
from enum import Enum
from typing import Union

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

    def matches(self, enemy: Enemy, item: Union[Item, Spell]):
        # Mapeia tipos de efeito para as correspondentes propriedades de Enemy
        attribute_map = {
            RuleType.VULNERABILITY: enemy.vulnerabilities,
            RuleType.RESISTANCE: enemy.resistances,
            RuleType.IMMUNITY: enemy.immunities,
            RuleType.CONDITION_IMMUNITY: enemy.condition_immunities,
        }

        # Verifica se a propriedade do item corresponde ao atributo do inimigo para a regra
        return (
            self.enemy_attribute in attribute_map[self.effect_type]
            and self.item_property in item.properties
        )
