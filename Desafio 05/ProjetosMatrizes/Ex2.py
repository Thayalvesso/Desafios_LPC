
vendas_1 = [
    [2000, 8000, 4500],  # semana 1
    [6500, 12000, 3000], # semana 2
    [2100, 5000, 7000],  # semana 3
]

vendas_2 = [
    [1500, 9000, 4000],  # semana 1
    [7000, 11000, 3500], # semana 2 
    [2500, 4500, 8000],  # semana 3
]

C_adição = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        C_adição[i][j] = vendas_1[i][j] + vendas_2[i][j]  # Exemplo de adição (vendas + vendas)
print("Matriz resultante da adição:\n", C_adição)
sum_total = 0
for i in range(3):
    for j in range(3):
        sum_total += C_adição[i][j]
print("Soma total das vendas combinadas:", sum_total)
