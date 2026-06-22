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

print("\nDigite os termos independentes (B):")
for i in range(3):
    valor = float(input(f"B[{i}]: "))
    B.append(valor)

A = np.array(A)
B = np.array(B)

try:
    if np.abs(np.linalg.det(A)) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante zero). O sistema não tem solução única.")
    else:
        X = np.linalg.solve(A, B)

        print("\nMatriz A:")
        for i in range(3):
            for j in range(3):
                print(f"{A[i][j]:.0f}", end=" ")
            print()

        print("\nVetor B:")
        print(B)

        print("\nSolução:")
        print(f"x = {X[0]:.2f}")
        print(f"y = {X[1]:.2f}")
        print(f"z = {X[2]:.2f}")
except np.linalg.LinAlgError:
    print("Erro: Não foi possível resolver o sistema (matriz singular ou mal-condicionada).")
