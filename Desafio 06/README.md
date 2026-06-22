## Resolução de Sistemas Lineares com Matrizes em Python

Coleção de exercícios práticos sobre resolução de sistemas de equações lineares usando matrizes em Python, organizados em duas pastas: numpy e random.


## Pré-requisitos


Python 3.x instalado
NumPy instalado:


bashpip install numpy


## Estrutura

numpy/
    ex1_sistema_2x2.py
    ex2_fabrica_3x3.py
    ex3_desafio_usuario.py
    ex4_fabrica_2_recursos.py
    ex5_fabrica_3_recursos.py
    ex6_padaria.py
    ex7_mistura_quimica.py

   random/
    ex1_matriz_aleatoria.py


## numpy/

Exercícios de resolução de sistemas lineares na forma matricial AX = B, usando numpy.linalg.solve e numpy.linalg.inv.

ex1_sistema_2x2.py — Sistema 2x2

Resolve o sistema 2x + 3y = 8 e 4x - y = 7 usando inversão de matriz (numpy.linalg.inv) e multiplicação (numpy.dot). Exibe a solução e verificação.

Conceitos: np.linalg.inv, np.dot, try-except.


ex2_fabrica_3x3.py — Fábrica com 3 Recursos

Uma fábrica produz itens usando trabalhadores, máquinas e horas de operação. Resolve um sistema 3x3 para determinar a taxa de produção por cada recurso.

Conceitos: np.linalg.solve, sistema 3x3, verificação de solução.


ex3_desafio_usuario.py — Sistema 3x3 com Entrada do Usuário

O usuário digita os coeficientes da matriz A (3x3) e o vetor B. O programa valida se a matriz é invertível e exibe a solução.

Conceitos: input, np.linalg.det, np.linalg.solve, tratamento de erros.


ex4_fabrica_2_recursos.py — Fábrica com 2 Recursos

Com 5 trabalhadores e 3 máquinas a fábrica produz 110 itens; com 8 e 2 produz 100. Resolve o sistema 2x2 e calcula a produção para uma nova combinação.

Conceitos: np.linalg.solve, sistema 2x2.


ex5_fabrica_3_recursos.py — Fábrica com 3 Recursos (expandido)

Versão expandida com 3 recursos (trabalhadores, máquinas e horas). Exibe a matriz A, o vetor B, as taxas de produção e a verificação completa.

Conceitos: np.linalg.det, np.linalg.solve, exibição formatada de matriz.


ex6_padaria.py — Padaria

Uma padaria usa farinha e açúcar para produzir pães e bolos. Resolve o sistema para determinar a quantidade de cada ingrediente por unidade produzida.

Conceitos: np.linalg.solve, sistema 2x2, contexto de produção alimentar.


ex7_mistura_quimica.py — Mistura Química

Uma empresa usa dois compostos (A e B) para produzir uma mistura com ingredientes ativos. Resolve o sistema para determinar a quantidade de ingrediente X por litro de cada composto.

Conceitos: np.linalg.solve, sistema 2x2, verificação de determinante.


 ## random/

ex1_matriz_aleatoria.py — Matriz Aleatória

Gera e exibe uma matriz 3x3 preenchida com números inteiros aleatórios entre 0 e 10.

Conceitos: random.randint, list comprehension, loops aninhados.


## Como executar

Execute cada arquivo individualmente pelo terminal:

bashpython numpy/ex1_sistema_2x2.py
python numpy/ex2_fabrica_3x3.py
python numpy/ex3_desafio_usuario.py
python numpy/ex4_fabrica_2_recursos.py
python numpy/ex5_fabrica_3_recursos.py
python numpy/ex6_padaria.py
python numpy/ex7_mistura_quimica.py
python random/ex1_matriz_aleatoria.py


## Conceitos Abordados

ConceitoArquivosInversão de matrizex1_sistema_2x2.pyResolução direta com np.linalg.solveex2 ao ex7Verificação de determinanteex3, ex5, ex6, ex7Entrada do usuárioex3_desafio_usuario.pyMatriz aleatória com randomex1_matriz_aleatoria.py