import numpy as np
A = []
B = []

print("Digite os coeficientes da matriz A (3x3):")
for i in range(3):
    linha = []
    for j in range(3):
    valor = float(input(f"A[{i}][{j}]: "))
    linha.append(valor)
    A.append(linha)

print("Digite os termos independentes (3 valores):")
for i in range(3):
    valor = float(input(f"B[{i}]: "))
    B.append(valor)