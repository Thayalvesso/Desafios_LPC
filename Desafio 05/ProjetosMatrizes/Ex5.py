import numpy as np

estoque = np.array([[10, 20, 15], [5, 8, 12], [3, 6, 9]])
transposta = np.transpose(estoque)
print("Matriz original:\n", estoque)
print("Matriz transposta:\n", transposta)

precos = np.array([[2.5, 3.0, 1.5], [4.0, 2.0, 3.5], [1.0, 2.5, 4.0]])
valor_total = np.sum(np.multiply(estoque, precos))
print("Valor total do estoque:\n", valor_total)
