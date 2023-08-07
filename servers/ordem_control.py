from sqlalchemy.orm import Session

from servers.BancoDeDados import BancoDeDados
from servers.cliente_control import ClienteControl
from servers.tabelas import OrdemServer


class OrdemControl:

    def __init__(self):
        bd = BancoDeDados()
        self.session = Session(bd.engine)

    def inserir_ordem(self, ordem, cpf):
        cliente_bd = ClienteControl()
        id_cliente = cliente_bd.buscar_cliente_id(cpf)

        if id_cliente:
            ordem_bd = OrdemServer(
                nome=ordem.nome,
                ticket=ordem.ticket,
                valor_compra=ordem.valor_compra,
                quantidade_compra=ordem.quantidade_compra,
                data_compra=ordem.data_compra,
                cliente_id=id_cliente
            )
            try:
                self.session.add(ordem_bd)
                self.session.commit()
                self.session.refresh(ordem_bd)

                print("Ordem cadastrada com sucesso.\n")
                return ordem_bd.ticket
            except Exception as err:
                return print("Não foi possível inserir: ", err)
        else:
            return print("\n")

    def alterar_ordem(self, ordem, cpf):

        try:
            cliente_bd = ClienteControl()
            id_cliente = cliente_bd.buscar_cliente_id(cpf)

            if id_cliente:
                ordem_bd = self.session.query(OrdemServer).filter_by(ticket=ordem.ticket, cliente_id=id_cliente).first()

                if ordem_bd:
                    ordem_bd.nome = ordem.nome
                    ordem_bd.ticket = ordem.ticket
                    ordem_bd.valor_compra = ordem.valor_compra
                    ordem_bd.quantidade_compra = ordem.quantidade_compra
                    ordem_bd.data_compra = ordem.data_compra

                    self.session.commit()
                    self.session.refresh(ordem_bd)
                    return ordem_bd.ticket
            else:
                print("\n")

        except Exception as err:
            return print("Não foi possível alterar: ", err)

    def buscar_ordem(self, ticket, cpf):

        try:
            cliente_bd = ClienteControl()
            id_cliente = cliente_bd.buscar_cliente_id(cpf)

            if id_cliente:
                result = self.session.query(OrdemServer).filter_by(ticket=ticket, cliente_id=id_cliente).first()
                return result
            else:
                print("\n")

        except Exception as err:
            return print("Não foi possível buscar: ", err)

    def lista_ordem_cliente(self, cpf):
        try:
            cliente_bd = ClienteControl()
            id_cliente = cliente_bd.buscar_cliente_id(cpf)

            if id_cliente:
                clientes = self.session.query(OrdemServer).filter_by(cliente_id=id_cliente).all()
                return clientes
            else:
                print("CPF não encontrado")
        except Exception as err:
            return print("Não foi possível listar: ", err)

    def deletar_ordem(self, ticket, cpf):
        try:
            cliente_bd = ClienteControl()
            id_cliente = cliente_bd.buscar_cliente_id(cpf)

            if id_cliente:
                ordem = self.session.query(OrdemServer).filter_by(ticket=ticket, cliente_id=id_cliente).first()
                if ordem:
                    self.session.delete(ordem)
                    self.session.commit()
                    print("Ordem deletada com sucesso.\n")
                else:
                    print("Ticket não encontrado")

            else:
                print("CPF não encontrado")

        except Exception as err:
            return print("Não foi possível deletar: ", err)
