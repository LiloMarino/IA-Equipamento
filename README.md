# Sistema de Recomendação de Itens e Magias para Enfrentar Inimigos

Este projeto implementa um sistema baseado em conhecimento para recomendar itens e magias que maximizem a eficácia contra inimigos 
em um cenário fictício. Ele utiliza uma adaptação do **algoritmo Rete**, um eficiente motor de inferência para regras de produção, para fazer 
a relação de itens/magias com as vulnerabilidades, resistências e imunidades dos inimigos.

## Estrutura do Projeto

### 1. Classes Principais

- **Enemy**: Representa o inimigo, com atributos que indicam suas vulnerabilidades, resistências, imunidades e imunidades a condições.
- **Item**: Representa um item que pode ter propriedades específicas, como tipos de dano.
- **Spell**: Similar ao item, mas contém atributos relacionados a magias, como tipos de dano e condições infligidas.
- **Rule**: Define uma regra de correspondência, que associa um atributo de um inimigo (como vulnerabilidade ou resistência) a uma propriedade de um item ou magia.
- **InferenceEngine**: O motor que processa as regras e faz a correspondência entre itens/magias e as características do inimigo, aplicando pesos para vulnerabilidades, resistências e imunidades.

### 2. Motor de Inferência (InferenceEngine)

O **InferenceEngine** processa as regras associadas a cada inimigo. Ele avalia quais itens ou magias são mais apropriados para o inimigo 
selecionado, atribuindo uma pontuação com base nos seguintes critérios:

- **Vulnerabilidades**: Itens ou magias que exploram vulnerabilidades do inimigo recebem uma pontuação mais alta.
- **Resistências**: A pontuação é reduzida para itens que causam dano ao qual o inimigo é resistente.
- **Imunidades**: Se o inimigo for imune a algum dano do item, a pontuação é drasticamente reduzida.
- **Imunidades a Condições**: Se o inimigo não é imune a algum tipo de condição então ele é vulnerável a ela, e portanto, a pontuação é incrementada, caso contrário (ou seja ele é imune) esse incremento é anulado.

O agoritmo implementa o motor de regras (InferenceEngine) é progressivo, não recursivo. 
O processo de avaliação de itens segue um fluxo linear, onde:
1. O método run chama o método match para avaliar todos os itens, um por um.
2. Cada item é comparado com o inimigo, utilizando as regras fornecidas.
3. Para cada regra, é feita uma simples verificação condicional (por exemplo, se o item corresponde a uma vulnerabilidade, resistência ou imunidade).
4. Se algum item corresponde, a pontuação é ajustada e o item é adicionado à lista de correspondências.

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
3. O motor de inferência avalia os itens e magias de acordo com as regras geradas para aquele inimigo.
4. Exibir as recomendações com pontuações que indicam a eficácia.

### 6. Sistema Baseado em Conhecimento

Sistema computacional que utiliza conhecimento específico sobre um domínio para realizar inferências e tomar decisões com base em regras.

- **Base de Conhecimento:** Armazena fatos e regras sobre o domínio.
- **Motor de Inferência:** Armazena fatos e regras sobre o domínio.
- **Interface de Usuário:** Permite que o sistema interaja com o usuário para fornecer recomendações ou realizar ações.

### 6.1 Relacionando com o projeto:

- **Base de Conhecimento:** Na implementação, a classe `Enemy` contém informações sobre vulnerabilidades e imunidades dos inimigos, enquanto `Item` e `Spell` representam os objetos e habilidades que o jogador pode usar.

- **Regras de Produção:** A classe `Rule` define como as propriedades dos itens ou magias correspondem às características dos inimigos. Se um inimigo tem uma vulnerabilidade, a regra aumenta a pontuação daquele item ou magia, já se tiver alguma resistência diminui a pontuação.

- **Motor de Inferência:** O motor de inferência é implementado pela classe InferenceEngine, que recebe as regras e os itens ou magias, e avalia quais são as melhores opções com base nas características do inimigo. Ele avalia cada item e magia em relação às regras, e gera uma pontuação para cada um, ordenando-os de acordo com a eficácia contra o inimigo selecionado.

### 7. Conclusão

Este sistema demonstra a aplicação prática de um projeto usando Sistema Baseado em Conhecimento. 
O foco principal foi implementar um motor de inferência eficiente para gerenciar e aplicar regras em um sistema de combate, recomendando as melhores estratégias (itens ou magias) para enfrentar inimigos com diferentes vulnerabilidades, resistências e imunidades. A lógica implementada otimiza a tomada de decisão com base em conhecimentos previamente codificados.
