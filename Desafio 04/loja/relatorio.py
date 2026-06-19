def gerar_relatorio(vendas):
    for venda in vendas:
        print(f"Cliente: {venda['cliente']}")
        print(f"Produto: {venda['produto']['nome']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Valor Bruto: R${venda['valor_bruto']:.2f}")
        print(f"Desconto: R${venda['desconto']:.2f}")
        print(f"Valor Final: R${venda['valor_final']:.2f}")
        print("-" * 30)
    total = 0
    for venda in vendas:
        total += venda["valor_final"]
    print(f"Total de vendas: R${total:.2f}")


def salvar_relatorio(vendas):
    try:
        with open("relatorio_vendas.txt", "w") as file:
            for venda in vendas:
                file.write(f"Cliente: {venda['cliente']}\n")
                file.write(f"Produto: {venda['produto']['nome']}\n")
                file.write(f"Quantidade: {venda['quantidade']}\n")
                file.write(f"Valor Bruto: R${venda['valor_bruto']:.2f}\n")
                file.write(f"Desconto: R${venda['desconto']:.2f}\n")
                file.write(f"Valor Final: R${venda['valor_final']:.2f}\n")
                file.write("-" * 30 + "\n")
            total = sum(venda["valor_final"] for venda in vendas)
            file.write(f"Total de vendas: R${total:.2f}\n")
        print("Relatório salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
