from loja.produtos import listar_produtos


def calcular_venda(produto, quantidade, cliente):
    valor_bruto = produto["preco"] * quantidade
    if quantidade > 10:
        desconto = valor_bruto * 0.05
    else:
        desconto = 0
    valor_final = valor_bruto - desconto
    produto["estoque"] -= quantidade
    return {
        "cliente": cliente,
        "produto": produto,
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final,
    }


def realizar_venda(produtos, vendas):
    nome = input("Digite o nome do cliente: ")
    listar_produtos(produtos)
    try:
        escolha = int(input("Escolha o número do produto: ")) - 1
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")
        return

    if produtos[escolha]["estoque"] >= quantidade:
        venda = calcular_venda(produtos[escolha], quantidade, nome)
        vendas.append(venda)
        print(f"Venda realizada com sucesso! Valor final: R${venda['valor_final']:.2f}")
    else:
        print("Estoque insuficiente para realizar a venda.")
