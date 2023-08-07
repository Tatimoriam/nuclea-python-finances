from faker import Faker


def formata_texto(texto):
    nome_formatado = texto.title().strip()
    return nome_formatado


def gerar_nome_fake():
    fake = Faker()
    return fake.name()
