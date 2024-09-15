class Rule:
    def __init__(self, enemy_weakness, item_property):
        self.enemy_weakness = enemy_weakness
        self.item_property = item_property

    def matches(self, enemy, item):
        return any(weakness in item.properties for weakness in enemy.weaknesses)

    def execute(self, item):
        return item.name
