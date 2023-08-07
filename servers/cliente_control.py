from sqlalchemy.orm import Session

from servers.BancoDeDados import BancoDeDados
from servers.tabelas import ClienteServer


class ClienteControl:

    def __init__(self):
        bd = BancoDeDados()
        self.session = Session(bd.engine)

    def inserir_cliente(self, cliente):
        cliente_bd = ClienteServer(
            nome=cliente.nome,
            cpf=cliente.cpf,
            rg=cliente.rg,
            data_nascimento=cliente.data_nascimento,
            cep=cliente.cep,
            logradouro=cliente.logradouro,
            complemento=cliente.complemento,
            bairro=cliente.bairro,
            cidade=cliente.cidade,
            estado=cliente.estado,
            numero_residencia=cliente.numero_residencia,
        )

        try:
            self.session.add(cliente_bd)
            self.session.commit()
            self.session.refresh(cliente_bd)

            return cliente_bd.cpf
        except Exception as err:
            return print("Não foi possível inserir: ", err)

    def alterar_cliente(self, cliente, cpf):

        try:
            cliente_bd = self.session.query(ClienteServer).filter_by(cpf=cpf).first()

            if cliente_bd:
                cliente_bd.nome = cliente.nome,
                cliente_bd.rg = cliente.rg,
                cliente_bd.data_nascimento = cliente.data_nascimento,
                cliente_bd.cep = cliente.cep,
                cliente_bd.logradouro = cliente.logradouro,
                cliente_bd.complemento = cliente.complemento,
                cliente_bd.bairro = cliente.bairro,
                cliente_bd.cidade = cliente.cidade,
                cliente_bd.estado = cliente.estado,
                cliente_bd.numero_residencia = cliente.numero_residencia,

                self.session.commit()
                self.session.refresh(cliente_bd)
                return cliente_bd.nome
            else:
                print("CPF não encontrado")

        except Exception as err:
            return print("Não foi possível alterar: ", err)

    def deletar_cliente(self, cpf):

        try:
            cliente = self.session.query(ClienteServer).filter_by(cpf=cpf).first()
            if cliente:
                self.session.delete(cliente)
                self.session.commit()
                print("Cliente deletado com sucesso.")
            else:
                print("CPF não encontrado")

        except Exception as err:
            return print("Não foi possível deletar: ", err)

    def buscar_cliente(self, cpf):

        try:
            result = self.session.query(ClienteServer).filter_by(cpf=cpf).first()

            return result
        except Exception as err:
            return print("Não foi possível buscar: ", err)

    def listar_clientes(self):

        try:
            clientes = self.session.query(ClienteServer).all()

            return clientes

        except Exception as err:
            return print("Não foi possível listar: ", err)

    def buscar_cliente_id(self, cpf):

        try:
            result = self.session.query(ClienteServer).filter_by(cpf=cpf).first()

            if result:
                return result.id
            else:
                print("Cliente não encontrado.")
        except Exception as err:
            return print("Não foi possível buscar: ", err)
