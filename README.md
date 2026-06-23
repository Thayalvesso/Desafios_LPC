# Desafios L.P.C. — Lógica e Programação de Computadores

Repositório com os desafios práticos da disciplina L.P.C. do curso de Sistemas de Informação. Cada desafio explora um conjunto de conceitos em Python, organizados em pastas separadas.

## Estrutura do Repositório

Desafios/
├── Desafio 01/
│   ├── main.py
│   └── README.md
├── Desafio 03/
│   ├── listas/
│   │   ├── criacao_listas.py
│   │   ├── acesso_elementos.py
│   │   ├── iteracao_listas.py
│   │   ├── operacoes_listas.py
│   │   ├── pilha.py
│   │   ├── funcoes_listas.py
│   │   ├── listas_aninhadas.py
│   │   └── list_comprehension.py
│   ├── main.py
│   └── README.md
├── Desafio 04/
│   ├── loja/
│   │   ├── produtos.py
│   │   ├── vendas.py
│   │   └── relatorio.py
│   ├── main.py
│   └── README.md
├── Desafio 05/
│   └── ProjetosMatrizes/
│       ├── Ex1.py
│       ├── Ex2.py
│       ├── Ex3.py
│       ├── Ex4.py
│       ├── Ex5.py
│       ├── matrizes.py
│       └── README.md
├── Desafio 06/
│   ├── numpy/
│   │   ├── ex1_sistema_2x2.py
│   │   ├── ex2_fabrica_3x3.py
│   │   ├── ex3_desafio_usuario.py
│   │   ├── ex4_fabrica_2_recursos.py
│   │   ├── ex5_fabrica_3_recursos.py
│   │   ├── ex6_padaria.py
│   │   └── ex7_mistura_quimica.py
│   ├── random/
│   │   └── ex1_matriz_aleatoria.py
│   └── README.md
└── README.md


## Desafio 01 — Sistema de Gestão de Funcionários

Sistema de linha de comando para cadastrar funcionários, gerar relatórios e salvar dados em arquivo `.txt`.

**Funcionalidades:**
- Cadastrar funcionários com nome, tipo e salário
- Gerar relatório no terminal com salário médio
- Salvar relatório em arquivo `.txt`
- Menu interativo em loop

**Conceitos:** funções, dicionários, listas, `try-except`, leitura e escrita de arquivos, `f-strings`.

**Como rodar:**
```bash
python "Desafio 01/main.py"
```

## Desafio 03 — Listas em Python

Projeto modular para praticar o uso de listas em Python, com exemplos organizados em módulos separados e executados por um `main.py` central.

**Módulos:**
- Criação de listas
- Acesso a elementos
- Iteração
- Operações com listas
- Pilha
- Funções de listas
- Listas aninhadas
- List comprehension

**Conceitos:** listas, módulos, `__init__.py`, importações, list comprehension, pilha.

**Como rodar:**
```bash
python "Desafio 03/main.py"
```

## Desafio 04 — Sistema de Loja Simples

Programa que simula uma loja com cadastro de produtos, realização de vendas e geração de relatórios, organizado em módulos dentro da pasta `loja/`.

**Funcionalidades:**
- Cadastrar produtos
- Realizar vendas com cálculo de desconto
- Gerar relatório de vendas no terminal
- Salvar relatório em arquivo `.txt`

**Conceitos:** módulos, importações, dicionários, listas, desconto, leitura e escrita de arquivos.

**Como rodar:**
```bash
python "Desafio 04/main.py"
```

## Desafio 05 — Matrizes em Python

Exercícios práticos sobre operações com matrizes, usando listas nativas e a biblioteca NumPy.

| Arquivo | Descrição |
|---|---|
| `Ex1.py` | Matriz aleatória 3x3 com `random` |
| `Ex2.py` | Soma de matrizes de vendas de duas lojas |
| `Ex3.py` | Média de notas por aluno com NumPy |
| `Ex4.py` | Determinante e matriz inversa |
| `Ex5.py` | Transposta e valor total do estoque |
| `matrizes.py` | Exemplos e anotações de aula comentados |

**Conceitos:** listas 2D, `random.randint`, `numpy.array`, `np.mean`, `np.linalg.det`, `np.linalg.inv`, `np.transpose`, `np.multiply`.

**Como rodar:**
```bash
python "Desafio 05/ProjetosMatrizes/Ex1.py"
python "Desafio 05/ProjetosMatrizes/Ex2.py"
# ... e assim por diante
```

## Desafio 06 — Resolução de Sistemas Lineares com Matrizes

Exercícios de resolução de sistemas de equações lineares na forma matricial **AX = B**, organizados em duas pastas conforme a biblioteca utilizada.

**numpy/** — Sistemas lineares com NumPy

| Arquivo | Descrição |
|---|---|
| `ex1_sistema_2x2.py` | Sistema 2x2 com inversão de matriz |
| `ex2_fabrica_3x3.py` | Fábrica com 3 recursos (sistema 3x3) |
| `ex3_desafio_usuario.py` | Sistema 3x3 com entrada do usuário |
| `ex4_fabrica_2_recursos.py` | Fábrica com 2 recursos (sistema 2x2) |
| `ex5_fabrica_3_recursos.py` | Fábrica com 3 recursos (versão expandida) |
| `ex6_padaria.py` | Produção de pães e bolos (farinha e açúcar) |
| `ex7_mistura_quimica.py` | Mistura de compostos químicos |

**random/** — Matriz aleatória

| Arquivo | Descrição |
|---|---|
| `ex1_matriz_aleatoria.py` | Matriz 3x3 com números aleatórios |

**Conceitos:** `np.linalg.solve`, `np.linalg.inv`, `np.linalg.det`, `np.dot`, `try-except`, `random.randint`.

**Como rodar:**
```bash
python "Desafio 06/numpy/ex1_sistema_2x2.py"
python "Desafio 06/random/ex1_matriz_aleatoria.py"
# ... e assim por diante
```

## Pré-requisitos Gerais

- Python 3.x instalado
- NumPy instalado (necessário para os Desafios 05 e 06):

```bash
pip install numpy
```

## Observações

- Os dados dos programas ficam em memória durante a execução. Salve os relatórios em arquivo quando necessário.
- Cada desafio possui seu próprio `README.md` com detalhes específicos.
