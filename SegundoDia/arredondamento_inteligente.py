import math

def nivel_medio(numero):
    #numero = float(input('Informe um valor: '))
    chao = math.floor(numero)
    teto = math.ceil(numero)
    arrendodado = round(numero)
    return chao, teto, arrendodado
print(nivel_medio(3.4))
