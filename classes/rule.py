from dataclasses import dataclass


@dataclass
class Rule:
    enemy_attribute: str  # Pode ser vulnerabilidade, resistência ou imunidade
    item_property: str
    effect_type: str  # "vulnerability", "resistance", "immunity"

    def matches(self, enemy, item):
        if self.effect_type == "vulnerability":
            return (
                self.enemy_attribute in enemy.vulnerabilities
                and self.item_property in item.properties
            )
        elif self.effect_type == "resistance":
            return (
                self.enemy_attribute in enemy.resistances
                and self.item_property in item.properties
            )
        elif self.effect_type == "immunity":
            return (
                self.enemy_attribute in enemy.immunities
                and self.item_property in item.properties
            )
        return False
