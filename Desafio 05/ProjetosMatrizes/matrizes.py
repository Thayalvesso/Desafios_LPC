# notas = [
#     [8.5, 7.0, 9.0],
#     [6.0, 8.5, 7.5],
# ]
# print("Matrizes de notas:")
# for linha in notas:
#     print(linha)

# for linha in notas: #percorre linha po linha da matriz
#    for nota in linha:
#        print(nota, end=" ")
#    print()

# Acessando elementos específicos
# print("Nota do primeiro aluno na primeira prova:", notas[0][0])  #Acessa a primeira linha (aluno) e a primeira coluna (prova)
# print("Nota do segundo aluno na segunda prova:", notas[1][1])  #Acessa a segunda linha (aluno) e a segunda coluna (prova)

# Acessando e Modificando Elementos
# print("Nota do aluno 1 na disciplina 2:", notas[0][1])  # Acessa a nota do aluno 1 na disciplina 2
# notas[0][1] = 9.0  # Modifica a nota do aluno 1 na disciplina 2 para 9.0
# print("Matriz atualizada:", notas)

# Calculando a média do aluno 1
# media_aluno1 = (notas [0][0] + notas[0][1] + notas[0][2]) / 3
# print("Média do aluno 1:", media_aluno1)

# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# Adição: Criando matriz C
# C_adição = [[0, 0], [0, 0]]
# for i in range(2):
#    for j in range(2):
#        C_adição[i][j] = A[i][j] + B[i][j]
# print("Matriz resultante da adição:", C_adição)

# Subtração: Criando matriz D
# D_subtração = [[0, 0], [0, 0]]
# for i in range(2):
#    for j in range(2):
#        D_subtração[i][j] = A[i][j] - B[i][j]
# print("Matriz resultante da subtração:", D_subtração)

# import numpy as np

# A_np = np.array(A)
# B_np = np.array(B)
# C_adição_np = A_np + B_np
# D_subtração_np = A_np - B_np
# print("Adição com NumPy:", C_adição_np)
# print("Subtração com NumPy:", D_subtração_np)

# import numpy as np

# # Matrizes compatíveis: A (2x3) e E (3x2)
# A = np.array([[1, 2, 3], [4, 5, 6]])
# E = np.array([[7, 8], [9, 10], [11, 12]])

# # Multiplicação: np.dot ou @
# F_multi = np.dot(A, E)
# print("Multiplicação de matrizes:\n", F_multi)

# import numpy as np
# matriz = np.array([[1, 2, 3], [4, 5, 6]])
# transposta = np.transpose(matriz) #ou matriz.t
# print("Matriz original:\n", matriz)
# print("Matriz transposta:\n", transposta)

# import numpy as np
# # A = np.array([[3, 1], [2, 4]])
# # det_A = np.linalg.det(A)
# # print("Determinante de A (2x2):", det_A)

# B = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
# det_B = np.linalg.det(B)
# print("Determinante de B (3x3):", det_B)

# import numpy as np
# A = np.array([[3, 1], [2, 4]])
# if np.linalg.det(A) !=0:
#     inversa = np.linalg.inv(A)
#     print("Matriz inversa de A:\n", inversa)
# else:    
#     print("A matriz A não é invertível.")






