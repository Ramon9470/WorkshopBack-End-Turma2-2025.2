import math
import sys

class Figura_Gerometrica:

    @staticmethod
    def area_circulo(raio):
        circulo = math.pi * math.pow(raio, 2)
        return circulo

    @staticmethod
    def area_triagulo(base, altura):
        return (base * altura) / 2

    @staticmethod
    def hipotenusa(cateto1, cateto2):
        # Correct formula should be addition, not multiplication
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))

    @staticmethod
    def menu():
        print('======== MENU ======== ')
        print('1 - A área de um círculo, dado o raio')
        print('2 - A área de um triângulo, dados base e altura')
        print('3 - A hipotenusa de um triângulo retângulo, dados os catetos')
        print('4 - Sair')

    @staticmethod
    def main():
        while True:
            Figura_Gerometrica.menu()

            opcao = input('Escolha uma opção entre de (1 a 4): ')

            if opcao == '1':
                raio = float(input("Informe o raio: "))
                area = Figura_Gerometrica.area_circulo(raio)
                print(f"A área do círculo é: {area:.2f}")

            elif opcao == '2':
                base = float(input("Informe a base: "))
                altura = float(input("Informe a altura: "))
                area = Figura_Gerometrica.area_triagulo(base, altura)
                print(f"A área do triângulo é: {area:.2f}")

            elif opcao == '3':
                cateto1 = float(input("Informe o cateto 1: "))
                cateto2 = float(input("Informe o cateto 2: "))
                hip = Figura_Gerometrica.hipotenusa(cateto1, cateto2)
                print(f"A hipotenusa é: {hip:.2f}")

            elif opcao == '4':
                print("Saindo...")
                sys.exit()

            else:
                print("Opção inválida. Tente novamente.")

Figura_Gerometrica.main()