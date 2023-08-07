# nuclea-python-finances
Projeto desenvolvimento para o módulo de Programação Python do curso
oferecido pela [Ada Tech](https://www.linkedin.com/school/adatechbr/) 
em parceria com a [Núclea](https://www.linkedin.com/company/nucleabr/).

---
### Do que se trata o projeto?
O projeto foi desenvolvimento em aula junto com a turma, o objetivo
era desenvolver um CRUD simples de **cliente** e **ordens de clientes**, no
caso ações.

Um dos requisitos do projeto são validações e testes unitários.

---
### O que mais tem neste projeto?

O premissa é que o projeto inteiro seja desenvolvido utilizando 
Programação Orientada a Objetos.

---
### Rodar o Projeto
Primeiramente eu utilizei o pacote [python-dotenv](https://pypi.org/project/python-dotenv/) 
para configurar as variaveis de ambiente, crie um banco de dados PostgreSQL (banco de dados
utilizado nesta aplicação) e configure o arquivo `.env` (adicione a raiz do projeto) com os seguintes dados:
```env
user=USUARIO_DO_BANCO
password=SENHA_DO_BANCO
host=HOST_DO_BANCO
port=PORDA_DO_BANCO
database=NOME_DO_BANCO
```
Substitua os valores em caixa alta para os seus valores.
Para criar as tabelas do banco, basta rodar o arquivo `tabelas.py` dentro da pasta servers

```python
if __name__ == "__main__":
    bd = BancoDeDados()
    Base.metadata.create_all(bind=bd.engine)
```

Desta forma criará as tabelas no banco automaticamente.
Depois disto é só rodar o projeto!

---
### Versão refatorada: qual a diferença?
Esta versão é a refatorada, a desenvolvida em aula junto com o professor
se encontra no repositorio [nuclea-python-financas](https://github.com/Tatimoriam/nuclea-python-financas).

Os adendos são:
- SQLAlchemy ORM
- python-dotenv
- ~~testes menos crimonosos~~

---

[![Linkedin Badge](https://img.shields.io/badge/-Tatiane-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tatimoriam)](https://www.linkedin.com/in/tatimoriam/) 