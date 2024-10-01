from dataclasses import dataclass
from enum import Enum
from typing import Union

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
    effect_type: RuleType

    def matches(self, item: Union[Item, Spell]):
        # Verifica se a propriedade do item corresponde ao atributo do inimigo para a regra
        return self.enemy_attribute in item.properties
