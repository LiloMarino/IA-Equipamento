import json
import curses
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
        enemy = Enemy(
            enemy_data["Name"],
            enemy_data["Damage Vulnerabilities"],
            enemy_data["Damage Resistances"],
            enemy_data["Damage Immunities"],
            enemy_data["Condition Immunities"],
        )
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
    """Criar regras de correspondência entre vulnerabilidades, fraquezas, resistência e itens."""
    rules = []
    # Criar regras para vulnerabilidades
    for vulnerability in enemy.vulnerabilities:
        rules.append(
            Rule(
                enemy_attribute=vulnerability,
                item_property=vulnerability,
                effect_type="vulnerability",
            )
        )

    # Criar regras para resistências
    for resistance in enemy.resistances:
        rules.append(
            Rule(
                enemy_attribute=resistance,
                item_property=resistance,
                effect_type="resistance",
            )
        )

    # Criar regras para imunidades
    for immunity in enemy.immunities:
        rules.append(
            Rule(
                enemy_attribute=immunity, item_property=immunity, effect_type="immunity"
            )
        )

    return rules


def curses_menu(stdscr, enemies, items):
    """Função para criar a CLI interativa com curses"""
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Selecione um inimigo (Use as setas e aperte Enter):")

        # Exibir lista de inimigos, destacando o selecionado
        for idx, enemy in enumerate(enemies):
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))  # Destacar a linha selecionada
                stdscr.addstr(idx + 1, 0, enemy.name)
                stdscr.attroff(curses.color_pair(1))  # Remover o destaque
            else:
                stdscr.addstr(idx + 1, 0, enemy.name)

        # Obter a tecla pressionada
        key = stdscr.getch()
        if key == 450 and current_row > 0:  # KEY UP
            current_row -= 1
        elif key == 456 and current_row < len(enemies) - 1:  # KEY DOWN
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            selected_enemy = enemies[current_row]
            stdscr.clear()
            stdscr.addstr(0, 0, f"Inimigo selecionado: {selected_enemy.name}")
            stdscr.addstr(1, 0, "Itens recomendados:")

            # Criar as regras e executar o motor de inferência
            rules = create_rules(selected_enemy)
            rete_engine = ReteEngine(rules)
            recommendations = rete_engine.run(selected_enemy, items)

            # Exibir os itens recomendados
            for idx, recommendation in enumerate(recommendations):
                stdscr.addstr(idx + 2, 0, f"{idx + 1}. {recommendation}")

            stdscr.addstr(len(recommendations) + 3, 0, "Aperte ESC para voltar")
            stdscr.refresh()

            # Esperar o usuário apertar ESC para voltar
            while True:
                key = stdscr.getch()
                if key == 27:  # Tecla ESC
                    break
        elif key == 27:  # Tecla ESC para encerrar o programa
            break

        stdscr.refresh()


def main(stdscr):
    # Configurações de cores
    curses.start_color()
    curses.init_pair(
        1, curses.COLOR_GREEN, curses.COLOR_BLACK
    )  # Destaque (fundo branco e texto preto)

    # Carregar os dados de inimigos e itens a partir dos arquivos JSON
    enemies_data = load_data("data/enemies.json")
    items_data = load_data("data/items.json")

    # Criar objetos Enemy e Item
    enemies = create_enemies(enemies_data)
    items = create_items(items_data)

    # Executar a interface CLI interativa
    curses_menu(stdscr, enemies, items)


if __name__ == "__main__":
    curses.wrapper(main)
