def cadastrar_funcionario(funcionarios):
    nome = input("Nome do funcionário: ").strip()
    if not nome:
        print("Nome inválido. Tente novamente.")
        return

    tipo = input("Tipo: ").strip()
    if not tipo:
        print("Tipo inválido. Tente novamente.")
        return

    try:
        salario = float(input("Salário: ").strip().replace(',', '.'))
    except ValueError:
        print("Salário inválido. Informe um valor numérico.")
        return

    funcionario = {
        "nome": nome,
        "tipo": tipo,
        "salario": salario,
    }
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso.")


def gerar_relatorio(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    print("\n===== Relatório de Funcionários =====")
    for index, funcionario in enumerate(funcionarios, start=1):
        print(
            f"{index}. Nome: {funcionario['nome']}, Tipo: {funcionario['tipo']}, Salário: R$ {funcionario['salario']:.2f}"
        )

    media_salario = sum(f["salario"] for f in funcionarios) / len(funcionarios)
    print(f"\nTotal de funcionários: {len(funcionarios)}")
    print(f"Salário médio: R$ {media_salario:.2f}")


def salvar_arquivo(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado para salvar.")
        return

    nome_arquivo = input("Nome do arquivo para salvar (ex: relatorio.txt): ").strip()
    if not nome_arquivo:
        nome_arquivo = "relatorio.txt"

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("===== Relatório de Funcionários =====\n")
            for index, funcionario in enumerate(funcionarios, start=1):
                arquivo.write(
                    f"{index}. Nome: {funcionario['nome']}, Tipo: {funcionario['tipo']}, Salário: R$ {funcionario['salario']:.2f}\n"
                )

            media_salario = sum(f["salario"] for f in funcionarios) / len(funcionarios)
            arquivo.write(f"\nTotal de funcionários: {len(funcionarios)}\n")
            arquivo.write(f"Salário médio: R$ {media_salario:.2f}\n")

        print(f"Relatório salvo em '{nome_arquivo}'.")
    except OSError as erro:
        print(f"Erro ao salvar o arquivo: {erro}")


def menu():
    funcionarios = []

    while True:
        print("\n===== Menu =====")
        print("1 - Cadastrar funcionário")
        print("2 - Gerar relatório")
        print("3 - Salvar relatório em arquivo")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_funcionario(funcionarios)
        elif opcao == "2":
            gerar_relatorio(funcionarios)
        elif opcao == "3":
            salvar_arquivo(funcionarios)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()


