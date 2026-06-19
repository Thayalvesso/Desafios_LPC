from loja.produtos import cadastrar_produto
from loja.vendas import realizar_venda
from loja.relatorio import gerar_relatorio, salvar_relatorio

produtos = []
vendas = []


def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Cadastrar Produto")
        print("2. Realizar Venda")
        print("3. Gerar Relatório")
        print("4. Salvar Relatório")
        print("5. Encerrar Programa")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_produto(produtos)
        elif escolha == "2":
            realizar_venda(produtos, vendas)
        elif escolha == "3":
            gerar_relatorio(vendas)
        elif escolha == "4":
            salvar_relatorio(vendas)
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    menu_principal()
