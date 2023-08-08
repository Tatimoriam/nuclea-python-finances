import unittest

from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import gerar_nome_fake
from utils.valida_cpf import gera_cpf, valida_cpf
from models.cliente import Cliente
from servers.cliente_control import ClienteControl
from utils.valida_rg import valida_rg


class TestCliente(unittest.TestCase):

    # Em vez de rodar a classe de teste, rodei teste por teste.
    # Com o pgAdmin ao lado, rodei os testes na orcem que os declarei
    # insirir cliente -> pega cpf pelo pgAdmin (poupar tempo)
    # na hora de rodar as outras funções utilizar o este cpf
    # preencho ele manualmente nos outros testes
    # test_listar_clientes é o único teste que não precisa input

    def test_inserir_cliente(self):
        cpf = valida_cpf(gera_cpf())

        cli = Cliente()
        cli.nome = gerar_nome_fake()
        cli.cpf = cpf
        cli.rg = valida_rg("12.345.678-x")
        cli.data_nascimento = valida_data_nascimento("12/02/2001")
        endereco = valida_cep('05003-060')
        cli.cep = endereco['CEP']
        cli.logradouro = endereco['Logradouro']
        cli.complemento = endereco['Complemento']
        cli.bairro = endereco['Bairro']
        cli.cidade = endereco['Cidade']
        cli.estado = endereco['Estado']
        cli.numero_residencia = "45"

        cli_bd = ClienteControl()
        cpf = cli_bd.inserir_cliente(cli)

        self.assertEqual(cli.cpf, cpf)

    def test_alterar_cliente(self):
        cpf = '920.303.365-30'

        cli = Cliente()
        cli.nome = gerar_nome_fake()
        cli.cpf = cpf
        cli.rg = valida_rg("12.345.678-x")
        cli.data_nascimento = valida_data_nascimento("12/02/2001")
        endereco = valida_cep('05003-060')
        cli.cep = endereco['CEP']
        cli.logradouro = endereco['Logradouro']
        cli.complemento = endereco['Complemento']
        cli.bairro = endereco['Bairro']
        cli.cidade = endereco['Cidade']
        cli.estado = endereco['Estado']
        cli.numero_residencia = "45"

        cli_bd = ClienteControl()
        nome = cli_bd.alterar_cliente(cli, cpf)
        self.assertEqual(cli.nome, nome)

    def test_buscar_cliente(self):
        cpf = '920.303.365-30'

        cli_bd = ClienteControl()

        cliente = cli_bd.buscar_cliente(cpf)

        self.assertEqual(cpf, cliente.cpf)

    def test_deletar_cliente(self):
        cpf = '920.303.365-30'

        cli_bd = ClienteControl()
        cli_bd.deletar_cliente(cpf)
        retorno = cli_bd.buscar_cliente(cpf)

        self.assertEqual(None, retorno)

    def test_listar_clientes(self):
        cli_bd = ClienteControl()
        cliente = cli_bd.listar_clientes()

        lista = []
        for c in cliente:
            lista.append(c.nome)

        self.assertEqual(type(lista), type([]))

    def test_buscar_cliente_id(self):
        cpf = '466.422.557-12'

        cli_bd = ClienteControl()

        cliente = cli_bd.buscar_cliente_id(cpf)

        print(cliente)
