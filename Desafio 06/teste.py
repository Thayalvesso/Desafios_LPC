
# import numpy as np

# A = np.array([[2,3], [4, -1]])
# B = np.array([8,7])

# det = np.linalg.det(A)
# print(f"Determinante de A:{det:.2f}")

# try:
#     A_inversa = np.linalg.inv(A)
#     x = np.dot(A_inversa, B)

#     print("\nSolução do sistema:")
#     print(f"x = {x[0]:.2f}")
#     print(f"y = {x[1]:.2f}")

#     print("\nVerificação:")
#     print(f"2x + 3y = 2({x[0]:.2f}) + 3({x[1]:.2f}) = {2*x[0] + 3*x[1]:.2f}")
#     print(f"4x - y = 4({x[0]:.2f}) - {x[1]:.2f} = {4*x[0] - x[1]:.2f}")
# except np.linalg.LinAlgError:
#     print("Erro: A matriz A é singular (não invertível).")

# import numpy as np
# A = np.array([[2,1,2], [1,2,3], [3,1,4]])
# B = np.array([7, 7, 11])

# det = np.linalg.det(A)
# print(f"Determinante de A: {det:.2f}")

# try:
#     X = np.linalg.solve(A, B)

#     print("\nSolução do sistema:")
#     print(f"x = {x[0]:.2f}")
#     print(f"y = {x[1]:.2f}")
#     print(f"z = {x[2]:.2f}")

#     print("\nVerificação:")
#     print(f"2x + y + 2z = 2({x[0]:.2f}) + {x[1]:.2f} + 2({x[2]:.2f}) = {2*x[0] + x[1] + 2*x[2]:.2f}")
#     print(f"x + 2y + 3z = {x[0]:.2f} + 2({x[1]:.2f}) + 3({x[2]:.2f}) = {x[0] + 2*x[1] + 3*x[2]:.2f}")
#     print(f"3x + y + 4z = 3({x[0]:.2f}) + {x[1]:.2f} + 4({x[2]:.2f}) = {3*x[0] + x[1] + 4*x[2]:.2f}")
# except np.linalg.LinAlgError:
#     print("Erro: A matriz A é singular (não invertível).")

for i in range(100):
    print(f"Teste {i+1}")
