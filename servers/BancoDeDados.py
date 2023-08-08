from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()


class BancoDeDados:

    def __init__(self):
        par = self.retorna_parametros_conexao_banco_de_dados()
        self.engine = create_engine(f"postgresql+psycopg2://"
                                    f"{par['user']}:{par['password']}@{par['host']}"
                                    f":{par['port']}/{par['database']}")

    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            "user": os.getenv('user'),
            "password": os.getenv('password'),
            "host": os.getenv('host'),
            "port": os.getenv('port'),
            "database": os.getenv('database')
        }
        return parametros_conexao
