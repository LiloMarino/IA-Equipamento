# Sistema de Recomendação de Itens e Magias para Enfrentar Inimigos

Este projeto implementa um sistema baseado em conhecimento para recomendar itens e magias que maximizem a eficácia contra inimigos 
em um cenário fictício. Ele utiliza o **algoritmo Rete**, um eficiente motor de inferência para regras de produção, para fazer 
o casamento de itens/magias com as vulnerabilidades, resistências e imunidades dos inimigos.

## Estrutura do Projeto

### 1. Classes Principais

- **Enemy**: Representa o inimigo, com atributos que indicam suas vulnerabilidades, resistências, imunidades e imunidades a condições.
- **Item**: Representa um item que pode ter propriedades específicas, como tipos de dano.
- **Spell**: Similar ao item, mas contém atributos relacionados a magias, como tipos de dano e condições infligidas.
- **Rule**: Define uma regra de correspondência, que associa um atributo de um inimigo (como vulnerabilidade ou resistência) a uma propriedade de um item ou magia.
- **ReteEngine**: O motor que processa as regras e faz a correspondência entre itens/magias e as características do inimigo, aplicando pesos para vulnerabilidades, resistências e imunidades.

### 2. Motor de Inferência (ReteEngine)

O **ReteEngine** processa as regras associadas a cada inimigo. Ele avalia quais itens ou magias são mais apropriados para o inimigo 
selecionado, atribuindo uma pontuação com base nos seguintes critérios:

- **Vulnerabilidades**: Itens ou magias que exploram vulnerabilidades do inimigo recebem uma pontuação mais alta.
- **Resistências**: A pontuação é reduzida para itens que causam dano ao qual o inimigo é resistente.
- **Imunidades**: Se o inimigo for imune ao efeito do item, a pontuação é zerada.
- **Imunidades a Condições**: Regras especiais são aplicadas para magias que infligem condições nas quais o inimigo é imune.

O algoritmo Rete permite a correspondência eficiente de regras, otimizando o processo de inferência ao evitar a repetição desnecessária de verificações.

### 3. Interface CLI com `curses`

O sistema inclui uma interface de linha de comando (CLI) interativa, implementada com a biblioteca `curses`, que permite ao usuário 
navegar pelos inimigos e receber recomendações de itens ou magias de acordo com as características do inimigo selecionado. 
A navegação inclui paginação, seleção de itens e magias recomendadas, e exibição de pontuações de eficácia.

### 4. Funcionalidades

- **Carregar Dados**: O sistema carrega os dados de inimigos, itens e magias a partir de arquivos JSON.
- **Regras Dinâmicas**: Para cada inimigo, o sistema gera regras dinamicamente, levando em conta suas vulnerabilidades, resistências, imunidades e imunidades a condições.
- **Recomendações**: O sistema avalia itens e magias com base nas regras geradas e os classifica conforme sua eficácia contra o inimigo.
- **Navegação Interativa**: O usuário pode navegar pelos inimigos e visualizar itens ou magias recomendadas, com base nas características do inimigo.

### 5. Exemplo de Uso

O fluxo típico de uso inclui:
1. Carregar os dados de inimigos e itens/magias.
2. Selecionar um inimigo.
3. O motor de inferência (Rete) avalia os itens e magias de acordo com as regras geradas para aquele inimigo.
4. Exibir as recomendações com pontuações que indicam a eficácia.

### 6. Algoritmo Rete

O **algoritmo Rete** é usado como motor de inferência para otimizar a aplicação de regras. Ele reduz o custo computacional de verificar 
regras múltiplas e complexas ao compartilhar subexpressões comuns entre regras. A lógica deste sistema segue o modelo dos 
Sistemas Baseados em Conhecimento (SBC), onde o conhecimento (regras e fatos) é separado do motor de inferência. 
Este último processa as regras para tomar decisões informadas.

- **Combinação de Padrões**: Rete cria um grafo que representa as regras como nós, permitindo um casamento eficiente entre as condições dos itens/magias e as vulnerabilidades do inimigo.
- **Otimização**: Rete elimina a necessidade de reavaliar todas as regras do sistema a cada interação, resultando em um processo de inferência mais rápido.

### 7. Conclusão

Este sistema demonstra a aplicação prática do algoritmo Rete dentro de um Sistema Baseado em Conhecimento. 
O foco principal foi implementar um motor de inferência eficiente com o algoritmo Rete para gerenciar e aplicar regras em um 
sistema de combate, recomendando as melhores estratégias (itens ou magias) para enfrentar inimigos com diferentes vulnerabilidades, 
resistências e imunidades. A lógica implementada otimiza a tomada de decisão com base em conhecimentos previamente codificados.
