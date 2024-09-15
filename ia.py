import json
from classes.enemy import Enemy
from classes.item import Item
from classes.rule import Rule
from classes.rete_engine import ReteEngine


def load_data(file_path):
    """Carregar dados de um arquivo JSON."""
    with open(file_path, "r") as file:
        return json.load(file)


def create_enemies(data):
    """Criar objetos Enemy a partir dos dados carregados."""
    enemies = []
    for enemy_data in data:
        enemy = Enemy(enemy_data["name"], enemy_data["weaknesses"])
        enemies.append(enemy)
    return enemies


def create_items(data):
    """Criar objetos Item a partir dos dados carregados."""
    items = []
    for item_data in data:
        item = Item(item_data["name"], item_data["properties"])
        items.append(item)
    return items


def create_rules(enemy):
    """Criar regras de correspondência entre fraquezas e itens."""
    rules = []
    for weakness in enemy.weaknesses:
        rule = Rule(enemy_weakness=weakness, item_property=weakness)
        rules.append(rule)
    return rules


def main():
    # Carregar os dados de inimigos e itens a partir dos arquivos JSON
    enemies_data = load_data("data/enemies.json")
    items_data = load_data("data/items.json")

    # Criar objetos Enemy e Item
    enemies = create_enemies(enemies_data)
    items = create_items(items_data)

    # Exemplo: Selecionar o primeiro inimigo para demonstração (Dragon)
    selected_enemy = enemies[1]

    # Criar as regras com base nas fraquezas do inimigo
    rules = create_rules(selected_enemy)

    # Inicializar o motor de inferência
    rete_engine = ReteEngine(rules)

    # Executar o motor de inferência para recomendar itens contra o inimigo
    recommendations = rete_engine.run(selected_enemy, items)

    # Exibir as recomendações
    print(f"Recommended Equipment against {selected_enemy.name}: {recommendations}")


if __name__ == "__main__":
    main()
