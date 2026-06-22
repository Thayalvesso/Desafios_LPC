# 📋 Sistema de Gestão de Funcionários

Sistema de linha de comando em Python para cadastrar funcionários, gerar relatórios e salvar dados em arquivo de texto.

## Funcionalidades

- Cadastrar funcionários com nome, tipo e salário
- Gerar relatório no terminal com lista de funcionários e salário médio
- Salvar o relatório em arquivo `.txt`
- Menu interativo em loop até o usuário sair

## Como usar

### Pré-requisitos

- Python 3.x instalado

### Executando o programa

```bash
python funcionarios.py
```

### Menu principal

```
===== Menu =====
1 - Cadastrar funcionário
2 - Gerar relatório
3 - Salvar relatório em arquivo
4 - Sair
```

## Exemplo de uso

**Cadastrando um funcionário:**
```
Nome do funcionário: Ana Souza
Tipo: CLT
Salário: 3500,00
Funcionário Ana Souza cadastrado com sucesso.
```

**Gerando relatório:**
```
===== Relatório de Funcionários =====
1. Nome: Ana Souza, Tipo: CLT, Salário: R$ 3500.00

Total de funcionários: 1
Salário médio: R$ 3500.00
```

**Salvando em arquivo:**
```
Nome do arquivo para salvar (ex: relatorio.txt): meus_funcionarios.txt
Relatório salvo em 'meus_funcionarios.txt'.
```

## Estrutura do código

| Função | Descrição |
|---|---|
| `cadastrar_funcionario()` | Lê nome, tipo e salário via input e adiciona à lista |
| `gerar_relatorio()` | Exibe todos os funcionários e o salário médio no terminal |
| `salvar_arquivo()` | Salva o relatório em um arquivo `.txt` escolhido pelo usuário |
| `menu()` | Controla o fluxo principal com loop e opções numeradas |

## Validações

- Nome e tipo não podem ser vazios
- Salário deve ser um valor numérico (aceita vírgula como separador decimal)
- Não é possível gerar ou salvar relatório sem funcionários cadastrados
- Nome do arquivo tem valor padrão `relatorio.txt` se deixado em branco


## Observações

- Os dados ficam armazenados apenas em memória durante a execução. Ao encerrar o programa, os dados não persistem, a menos que o relatório tenha sido salvo em arquivo.
- O arquivo de saída é salvo no mesmo diretório de execução do script.
