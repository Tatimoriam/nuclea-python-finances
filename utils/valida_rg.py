import re


def valida_rg(rg):
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

    while True:
        rg = re.sub("[-.]", "", rg)

        rg = f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}"

        if re.match(padrao_rg, rg):
            return rg
        else:
            rg = input("RG inválido. Tente novamente: ")
