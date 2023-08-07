from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy import Integer, String, Date, ForeignKey, Numeric

from servers.BancoDeDados import BancoDeDados


class Base(DeclarativeBase):
    pass


class ClienteServer(Base):
    __tablename__ = "cliente"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    cpf = mapped_column(String(14), nullable=False, unique=True)
    rg = mapped_column(String(20), nullable=False)
    data_nascimento = mapped_column(Date, nullable=False)
    cep = mapped_column(String(10), nullable=False)
    logradouro = mapped_column(String(50), nullable=False)
    complemento = mapped_column(String(20), nullable=False)
    bairro = mapped_column(String(20), nullable=False)
    cidade = mapped_column(String(30), nullable=False)
    estado = mapped_column(String(2), nullable=False)
    numero_residencia = mapped_column(String(10), nullable=False)
    ordem = relationship('OrdemServer', cascade="all, delete-orphan")


class OrdemServer(Base):
    __tablename__ = "ordem"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    ticket = mapped_column(String(10), nullable=False)
    valor_compra = mapped_column(Numeric(10), nullable=False)
    quantidade_compra = mapped_column(Numeric(5), nullable=False)
    data_compra = mapped_column(Date, nullable=False)
    cliente_id = mapped_column(ForeignKey("cliente.id", ondelete='CASCADE'))


# cria tabelas
if __name__ == "__main__":
    bd = BancoDeDados()
    Base.metadata.create_all(bind=bd.engine)
