import unittest
from datetime import datetime

from models.ordem import Ordem
from servers.cliente_control import ClienteControl
from servers.ordem_control import OrdemControl


class TestCliente(unittest.TestCase):

    # Em vez de rodar a classe de teste, rodei teste por teste.
    # Com o pgAdmin ao lado, rodei os testes na orcem que os declarei
    # com um cliente existente, pego seu CPF pelo pgAdmin
    # (ou roda a aplicação pra listar os clientes cadastrados e pegar um cpf aleatório)
    # informo manualmente o CPF em insirir ordem
    # e uso esse mesmo cpf e ordem para executar os outros testes
    # preencho ele manualmente nos testes

    def test_inserir_ordem(self):
        cpf = '466.422.557-12'

        ordem = Ordem()
        ordem.nome = "Itaúsa2"
        ordem.ticket = "ITSA4"
        ordem.valor_compra = 9.76
        ordem.quantidade_compra = 1
        ordem.data_compra = datetime.now().date()

        ordem_bd = OrdemControl()
        ticket = ordem_bd.inserir_ordem(ordem, cpf)

        self.assertEqual(ordem.ticket, ticket)

    def test_alterar_ordem(self):
        cpf = '466.422.557-12'

        ordem = Ordem()
        ordem.nome = "Itaúsa A"
        ordem.ticket = "ITSA4"
        ordem.valor_compra = 9.76
        ordem.quantidade_compra = 1
        ordem.data_compra = datetime.now().date()

        ordem_bd = OrdemControl()
        ticket = ordem_bd.alterar_ordem(ordem, cpf)
        self.assertEqual(ordem.ticket, ticket)

    def test_buscar_ordem(self):
        cpf = '466.422.557-12'
        ticket = "ITSA4"

        ordem_bd = OrdemControl()
        ordem = ordem_bd.buscar_ordem(ticket, cpf)

        self.assertEqual(ticket, ordem.ticket)

    def test_lista_ordem_cliente(self):
        cpf = '466.422.557-12'

        ordem_bd = OrdemControl()
        ordem = ordem_bd.lista_ordem_cliente(cpf)

        lista = []
        for o in ordem:
            lista.append(o.nome)

        self.assertEqual(type(lista), type([]))

    def test_deletar_ordem(self):
        cpf = '466.422.557-12'
        ticket = "ITSA4"

        ordem_bd = OrdemControl()
        ordem_bd.deletar_ordem(ticket, cpf)

        retorno = ordem_bd.buscar_ordem(ticket, cpf)

        self.assertEqual(None, retorno)

