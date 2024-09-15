class ReteEngine:
    def __init__(self, rules):
        self.rules = rules

    def match(self, enemy, items):
        matched_items = []
        for item in items:
            score = sum(1 for rule in self.rules if rule.matches(enemy, item))
            if score > 0:
                matched_items.append((item, score))
        return matched_items

    def run(self, enemy, items):
        applicable_items = self.match(enemy, items)
        applicable_items.sort(
            key=lambda x: x[1], reverse=True
        )  # Ordenar por maior pontuação
        recommendations = [item.name for item, score in applicable_items]
        return recommendations
