import numpy as np

A = np.array([[2, 3], [4, -1]])
B = np.array([8, 7])

det = np.linalg.det(A)
print(f"Determinante de A: {det:.2f}")

try:
    A_inversa = np.linalg.inv(A)
    X = np.dot(A_inversa, B)

    print("\nSolução do sistema:")
    print(f"x = {X[0]:.2f}")
    print(f"y = {X[1]:.2f}")

    print("\nVerificação:")
    print(f"2x + 3y = 2({X[0]:.2f}) + 3({X[1]:.2f}) = {2*X[0] + 3*X[1]:.2f}")
    print(f"4x - y = 4({X[0]:.2f}) - {X[1]:.2f} = {4*X[0] - X[1]:.2f}")
except np.linalg.LinAlgError:
    print("Erro: A matriz A é singular (não invertível).")