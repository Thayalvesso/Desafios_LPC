def executar():
    numeros = [5, 2, 8, 1, 9]

    print("Tamanho:", len(numeros))
    print("Tem 8?", 8 in numeros)

    numeros.sort()
    print("Ordenado:", numeros)

    numeros.reverse()
    print("Invertido:", numeros)
