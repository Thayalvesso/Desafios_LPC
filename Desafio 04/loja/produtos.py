def cadastrar_produto(produtos):
    try:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$"))
        estoque = int(input("Digite a quantidade em estoque: "))
        produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
        print("Produto cadastrado com sucesso!")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos para o preço e o estoque.")


def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for i, produto in enumerate(produtos):
            print(
                f"{i + 1}. {produto['nome']} - R${produto['preco']:.2f} - Estoque: {produto['estoque']}"
            )
