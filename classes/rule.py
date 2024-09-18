from dataclasses import dataclass


@dataclass
class Rule:
    enemy_weakness: str
    item_property: str

    def matches(self, enemy, item):
        # Verifica se uma fraqueza específica do inimigo corresponde à propriedade do item
        return self.enemy_weakness in item.properties
