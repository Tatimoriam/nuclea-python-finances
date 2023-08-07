import re

from validate_docbr import CPF


def valida_cpf(cpf):
    cpf_validador = CPF()

    while True:
        resultado_validacao = cpf_validador.validate(cpf)

        cpf = re.sub("[-.]", "", cpf)

        if resultado_validacao:
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            return cpf_formatado
        else:
            cpf = input("CPF inválido, digite novamente: ")


def gera_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate()
    return cpf_gerado
