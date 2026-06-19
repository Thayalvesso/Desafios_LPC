import numpy as np
notas = np.array ([
    [8.5, 7.0, 9.0],
    [6.0, 8.5, 7.5],
])
print("Matrizes de notas:")
for linha in notas:
    print(linha)

for i, media in enumerate(np.mean(notas, axis=1)):
    print(f"Aluno {i+1}: {media:.2f}")    