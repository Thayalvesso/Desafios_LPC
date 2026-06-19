def executar():
    frutas = ["maçã", "banana", "laranja"]

    frutas.append("morango")
    print("Após append:", frutas)

    frutas.remove("banana")
    print("Após remove:", frutas)

    frutas[1] = "kiwi"
    print("Após modificação:", frutas)

    nova_lista = frutas + ["uva", "manga"]
    print("Concatenação:", nova_lista)
