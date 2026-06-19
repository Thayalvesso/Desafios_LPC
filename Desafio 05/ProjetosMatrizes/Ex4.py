import numpy as np
matriz =  np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
det_matriz = np.linalg.det(matriz)
print("Determinante da matriz 3x3:", det_matriz)
if det_matriz != 0:
    inversa = np.linalg.inv(matriz)
    print("Matriz inversa:\n", inversa)
else:    
    print("A matriz não é invertível.")