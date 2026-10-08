# Lista de Tarefas (To-Do List)

Programa de linha de comando escrito em Python puro, sem dependências externas, para organizar tarefas do dia a dia. Permite adicionar, listar, concluir e remover tarefas por meio de um menu interativo no terminal, com persistência automática em um arquivo JSON — ou seja, as tarefas continuam salvas mesmo depois que o programa é fechado.

## Funcionalidades

- **Adicionar tarefa**: cadastra uma nova tarefa com descrição, prioridade (Baixa, Média ou Alta) e um prazo opcional (data no formato `DD/MM/AAAA`).
- **Listar tarefas**: exibe todas as tarefas cadastradas, indicando número, descrição, prioridade, prazo (quando houver) e se já foi concluída.
- **Concluir tarefa**: marca uma tarefa existente como concluída, a partir do seu número.
- **Remover tarefa**: exclui uma tarefa da lista, mediante confirmação do usuário.
- **Persistência automática**: toda alteração (adicionar, concluir ou remover) é imediatamente salva no arquivo `tarefas.json`, sem necessidade de nenhum comando manual de salvar.
- **Validação de entradas**: descrições em branco, prioridades inválidas, datas em formato incorreto e números de tarefa inexistentes são tratados com mensagens claras, sem travar o programa.

## Como executar

Requisitos: **Python 3.7 ou superior** (não utiliza nenhuma biblioteca externa).

```bash
git clone https://github.com/seu-usuario/lista-de-tarefas-python.git
cd lista-de-tarefas-python
python3 lista_de_tarefas.py
```

Um arquivo `tarefas.json` será criado automaticamente na primeira vez que uma tarefa for adicionada.

## Exemplo de uso

```
========================================
           LISTA DE TAREFAS
========================================

O que você deseja fazer?
1. Adicionar tarefa
2. Listar tarefas
3. Concluir tarefa
4. Remover tarefa
5. Sair

Escolha uma opção (1-5): 1

--- Adicionar Tarefa ---
Descrição da tarefa: Estudar Python
Prioridade da tarefa:
1. Baixa
2. Média
3. Alta
Escolha a prioridade (padrão: Média): 3
Prazo (formato DD/MM/AAAA, opcional): 31/12/2026

Tarefa adicionada com sucesso! (#1)
```

## Estrutura do projeto

```
.
├── lista_de_tarefas.py      # Ponto de entrada: menu e interação com o usuário
├── gerenciador_tarefas.py   # Lógica de negócio e persistência em JSON
├── modelo_tarefa.py         # Estrutura de dados da tarefa (classe Tarefa)
└── README.md                 # Documentação do projeto
```

## Organização do código

O projeto é dividido em três módulos, cada um com uma responsabilidade bem definida:

- **`modelo_tarefa.py`**: define a classe `Tarefa`, responsável apenas por representar os dados de uma tarefa e converter esses dados entre o objeto Python e o formato de dicionário usado no JSON.
- **`gerenciador_tarefas.py`**: define a classe `GerenciadorDeTarefas`, responsável por toda a lógica de negócio — adicionar, listar, concluir, remover e, principalmente, carregar e salvar as tarefas no arquivo `tarefas.json`.
- **`lista_de_tarefas.py`**: ponto de entrada do programa. Cuida exclusivamente da interação com o usuário — exibição do menu, leitura e validação das entradas — delegando toda a lógica de dados ao `GerenciadorDeTarefas`.

Essa separação torna o código mais fácil de ler, testar e expandir, já que cada parte do programa cuida apenas de uma responsabilidade.

## Formato dos dados salvos

Cada tarefa é armazenada no `tarefas.json` como um objeto com a seguinte estrutura:

```json
{
    "identificador": 1,
    "descricao": "Estudar Python",
    "prioridade": "Alta",
    "prazo": "31/12/2026",
    "concluida": false
}
```

## Possíveis melhorias futuras

Algumas ideias para quem quiser evoluir o projeto:

- Ordenar a listagem de tarefas por prioridade ou por prazo.
- Permitir editar a descrição, a prioridade ou o prazo de uma tarefa já existente.
- Destacar tarefas com prazo vencido ou próximo do vencimento.
- Adicionar categorias ou etiquetas às tarefas (ex.: "Trabalho", "Pessoal").

## Licença

Este projeto está licenciado sob os termos da licença MIT.
