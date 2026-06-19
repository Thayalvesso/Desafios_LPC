import random

num_linhas = 3
num_colunas = 3
min_valor = 0
max_valor = 10

matriz = [[0 for _ in range(num_linhas)] for _ in range(num_colunas)]

for i in range(num_linhas):
    for j in range(num_colunas):
        matriz[i][j] = random.randint(min_valor, max_valor)

for linha in matriz:
    print(linha)