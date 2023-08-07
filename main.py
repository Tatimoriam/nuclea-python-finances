from datetime import datetime

from models.cliente import Cliente
from models.ordem import Ordem
from servers.cliente_control import ClienteControl
from servers.ordem_control import OrdemControl
from utils.carteira import analisar_carteira
from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto
from utils.relatorio import obter_dados_acao, obter_dados_acao2
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg


def menu_cliente():
    while True:
        print("\nMenu Cliente ")
        print("1 - Cadastrar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Buscar Cliente")
        print("4 - Deletar Cliente")
        print("5 - Listar Clientes")
        print("6 - Voltar ao menu anterior")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cli = Cliente()

            cli.nome = formata_texto(input("Nome: "))
            cli.cpf = valida_cpf(input("CPF: "))
            cli.rg = valida_rg(input("RG: "))
            cli.data_nascimento = valida_data_nascimento(input("Data de Nascimento: "))
            endereco = valida_cep(input("CEP: "))
            cli.cep = endereco['CEP']
            cli.logradouro = endereco['Logradouro']
            cli.complemento = endereco['Complemento']
            cli.bairro = endereco['Bairro']
            cli.cidade = endereco['Cidade']
            cli.estado = endereco['Estado']
            cli.numero_residencia = input("Número casa: ")

            cli_bd = ClienteControl()
            cli_bd.inserir_cliente(cli)

            print("Cliente inserido com sucesso.")
        elif opcao == "2":
            cpf = valida_cpf(input("CPF do usuário a ser alterado: "))

            cli_bd = ClienteControl()
            cliente = cli_bd.buscar_cliente(cpf)

            if cliente:

                print("Nome:", cliente.nome)
                print("CPF:", cliente.cpf)
                print("RG:", cliente.rg)
                print("Data Nascimento:", cliente.data_nascimento)
                print("CEP:", cliente.cep)
                print("Numero casa:", cliente.numero_residencia)

                print("Insira os novos dados: ")
                cli = Cliente()
                cli.nome = formata_texto(input("Nome: "))
                cli.rg = valida_rg(input("RG: "))
                cli.data_nascimento = valida_data_nascimento(input("Data de Nascimento: "))
                endereco = valida_cep(input("CEP: "))
                cli.cep = endereco['CEP']
                cli.logradouro = endereco['Logradouro']
                cli.complemento = endereco['Complemento']
                cli.bairro = endereco['Bairro']
                cli.cidade = endereco['Cidade']
                cli.estado = endereco['Estado']
                cli.numero_residencia = input("Número casa: ")

                cli_bd = ClienteControl()
                cli_bd.alterar_cliente(cli, cpf)
                print("Cliente alterado com sucesso.")
            else:
                print("Cliente não encontrado.")
        elif opcao == "3":
            cpf = valida_cpf(input("CPF: "))

            cli_bd = ClienteControl()
            cliente = cli_bd.buscar_cliente(cpf)

            if cliente:
                print("\n")
                print("Nome:", cliente.nome)
                print("CPF:", cliente.cpf)
                print("RG:", cliente.rg)
                print("Data Nascimento:", cliente.data_nascimento)
                print("CEP:", cliente.cep)
                print("Numero casa:", cliente.numero_residencia)
            else:
                print("Cliente não encontrado.")

            while True:
                voltar = input("\nDigite 'voltar' para sair ").lower()
                if voltar == "voltar":
                    break
        elif opcao == "4":
            cpf = valida_cpf(input("CPF do cliente que gostaria de deletar: "))

            cli_bd = ClienteControl()
            cli_bd.deletar_cliente(cpf)
        elif opcao == "5":
            cli_bd = ClienteControl()
            cliente = cli_bd.listar_clientes()

            print("\nClientes: ")
            for c in cliente:
                print("Nome:", c.nome,
                      "| CPF:", c.cpf,
                      "| RG:", c.rg,
                      "| Data de Nascimento:", c.data_nascimento,
                      "| CEP:", c.cep,
                      "| Número da casa:", c.numero_residencia)

            while True:
                voltar = input("\nDigite 'voltar' para sair ").lower()
                if voltar == "voltar":
                    break
        elif opcao == "6":
            break


def menu_ordem():
    while True:
        print("\nMenu Ordem ")
        print("1 - Cadastrar Ordem de Compra")
        print("2 - Alterar Ordem Adquirida")
        print("3 - Buscar Ordem Adquirida")
        print("4 - Deletar Ordem Adquirida")
        print("5 - Voltar ao menu anterior")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("Para qual cliente será registrada a ordem?\n")
            cpf = valida_cpf(input("CPF: "))

            if cpf:
                ordem = Ordem()

                print("Informações da Ação")
                ordem.nome = input("Nome: ")
                ordem.ticket = input("Ticket: ")
                ordem.valor_compra = input("Valor da Compra: ")
                ordem.quantidade_compra = input("Quantidade da Compra: ")
                ordem.data_compra = datetime.now().date()

                ordem_bd = OrdemControl()
                ordem_bd.inserir_ordem(ordem, cpf)
            else:
                print("Não há nenhum cliente com este CPF cadastrado.\n")
        elif opcao == "2":
            print("De qual cliente é a ordem?\n")
            cpf = valida_cpf(input("CPF: "))

            ticket = input("Informe o Ticket (ex: ITSA4) para alteração: ")

            ord_bd = OrdemControl()
            ordem = ord_bd.buscar_ordem(ticket, cpf)

            if ordem:
                print("\nInformações da Ação")
                print("Nome:", ordem.nome)
                print("Ticket:", ordem.ticket)
                print("Valor Compra:", ordem.valor_compra)
                print("Quantidade:", ordem.quantidade_compra)
                print("Data_compra:", ordem.data_compra)

                print("\nNovos Valores")
                ordem.nome = input("Nome: ")
                ordem.valor_compra = input("Valor da Compra: ")
                ordem.quantidade_compra = input("Quantidade da Compra: ")
                ordem.data_compra = datetime.now().date()

                ordem_bd = OrdemControl()
                ordem_bd.alterar_ordem(ordem, cpf)
                print("Ordem alterada com sucesso.\n")
            else:
                print("Não há nenhum cliente ou ticket com os valores inseridos.\n")
        elif opcao == "3":
            print("Qual cliente gostaria de verificar as ordens?\n")
            cpf = valida_cpf(input("CPF: "))

            if cpf:
                ordem_bd = OrdemControl()
                ordem = ordem_bd.lista_ordem_cliente(cpf)

                if ordem:
                    print("\nOrdens do Cliente de CPF", cpf)
                    for o in ordem:
                        print("Nome: ", o.nome,
                              "| Ticket: ", o.ticket,
                              "| Valor da Compra: ", o.valor_compra,
                              "| Quantidade: ", o.quantidade_compra,
                              "| Data da Compra: ", o.data_compra)
                else:
                    print("Nenhuma Ordem encontrada.")
            else:
                print("Não há nenhum cliente com este CPF cadastrado.\n")

            while True:
                voltar = input("\nDigite 'voltar' para sair ").lower()
                if voltar == "voltar":
                    break
        elif opcao == "4":
            print("De qual cliente é a ordem?\n")
            cpf = valida_cpf(input("CPF: "))

            if cpf:
                ticket = input("Informe o nome do Ticket que gostaria de deletar: ")

                ord_bd = OrdemControl()
                ord_bd.deletar_ordem(ticket, cpf)
            else:
                print("Não há nenhum cliente com este CPF cadastrado.\n")
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")


def analise_carteira():
    print("De qual cliente é a ordem?\n")
    cpf = valida_cpf(input("CPF: "))

    ordem_bd = OrdemControl()
    ordem = ordem_bd.lista_ordem_cliente(cpf)

    if ordem:
        lista_ordem = []

        for o in ordem:
            lista_ordem.append(o.ticket + ".SA")

        analisar_carteira(lista_ordem)
    else:
        print("Nenhuma Ordem encontrada.")


def imprimir_relatorio():
    while True:
        print("\n1 - Gerar relatório de uma ação específica.")
        print("2 - Gerar relatório de das ações do cliente.")
        print("3 - Voltar ao menu anterior")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            ticket = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
            nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()

            obter_dados_acao(ticket, nome_arquivo)
        if opcao == "2":
            print("De quem é a carteira que gostaria de gerar o relátorio?")
            cpf = valida_cpf(input("CPF: "))

            ordem_bd = OrdemControl()
            ordem = ordem_bd.lista_ordem_cliente(cpf)

            if ordem:
                lista_ordem = []

                for o in ordem:
                    lista_ordem.append(o.ticket + ".SA")

                nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()

                obter_dados_acao2(lista_ordem, nome_arquivo)
            else:
                print("Nenhuma Ordem encontrada.")
        if opcao == "3":
            break


while True:
    print(
        "Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções "
        "abaixo:")
    print("1 - Cliente")
    print("2 - Ordem")
    print("3 - Realizar análise da carteira")
    print("4 - Imprimir relatório da carteira")
    print("5 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        menu_cliente()
    elif opcao == "2":
        menu_ordem()
    elif opcao == "3":
        analise_carteira()
    elif opcao == "4":
        imprimir_relatorio()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
