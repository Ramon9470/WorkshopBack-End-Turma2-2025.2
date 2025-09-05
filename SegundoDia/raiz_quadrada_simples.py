import math

def raiz(valor):
    resultado = math.sqrt(valor)
    return resultado

calc = float(input('Informe um valor: '))

calc2 = raiz(calc)
print(calc2)