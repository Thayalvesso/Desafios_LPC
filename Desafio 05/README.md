# Exercícios de Matrizes

Coleção de exercícios em Python sobre operações com matrizes, utilizando listas nativas e a biblioteca NumPy.

## Como executar

Certifique-se de ter o Python e o NumPy instalados. Para instalar o NumPy:

```bash
pip install numpy
```

Execute cada exercício individualmente:

```bash
python Ex1.py
python Ex2.py
python Ex3.py
python Ex4.py
python Ex5.py
```

## Exercícios

### Ex1 — Matriz Aleatória
Gera uma matriz 3x3 preenchida com números aleatórios entre 0 e 10.

**Conceitos:** list comprehension, `random.randint`, percurso com `for`.

### Ex2 — Soma de Vendas
Soma as matrizes de vendas de duas lojas ao longo de 3 semanas e calcula o total combinado.

**Conceitos:** adição de matrizes, acumulador, loops aninhados.

### Ex3 — Média de Notas
Calcula a média de notas de cada aluno a partir de uma matriz de notas com NumPy.

**Conceitos:** `np.array`, `np.mean`, `axis=1`, `enumerate`.

### Ex4 — Determinante e Inversa
Calcula o determinante de uma matriz 3x3 e, se possível, sua inversa.

**Conceitos:** `np.linalg.det`, `np.linalg.inv`, verificação de invertibilidade.

### Ex5 — Transposta e Valor do Estoque
Exibe a transposta de uma matriz de estoque e calcula o valor total multiplicando quantidade por preço.

**Conceitos:** `np.transpose`, `np.multiply`, `np.sum`.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `Ex1.py` | Matriz aleatória 3x3 |
| `Ex2.py` | Soma de matrizes de vendas |
| `Ex3.py` | Média de notas com NumPy |
| `Ex4.py` | Determinante e inversa |
| `Ex5.py` | Transposta e valor do estoque |
| `matrizes.py` | Exemplos e anotações de aula comentados |
