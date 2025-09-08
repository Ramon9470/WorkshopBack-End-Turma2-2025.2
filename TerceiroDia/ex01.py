#Indentificando e correingindo erros de sintaxe

#print('Olá, Mundo!' #Faltando fechar os parênteses
print('Olá, Mundo!') #Corrigido, fechando os parênteses

#print(nome) #Variável 'nome' não foi definida
print('nome') #Corrigido, colocando 'nome' entre aspas para imprimir como string

def somar(a, b):
    return a + b

#resultado = somar(10, "5") #Argumento '5' está como string
resultado = somar(10, 5) #Corrigido, passando ambos os argumentos
print(resultado) #Corrigido, convertendo '5' para inteiro


#Feito o tratamento de exceções com try e except
numeros = [10, 20, 30]
try:
    indice = int(input('Digite um índice para acessar a lista: '))
    print(numeros[indice])
except ValueError:
    print('Favor, digite um número válido.')
except IndexError:
    print('Índice fora do intervalo da lista.')

def dividir(a, b):
    return a / b

#Feito o tratamento de exceções com try e except
try:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    if int(num2) == 0:
        raise ValueError('Divisão por zero não é permitida.')
except ValueError as e:
    print(f'Erro: {e}')
    num2 = input('Por favor, digite um número diferente de zero para o segundo número: ')

resultado = dividir(int(num1), int(num2))
print(f'Resultado: {resultado}')

#Feito o tratamento de exceções com try e except em um dicionário
dados = {
    'nome': 'Isaac',
    'idade': 25,
    'cidade': 'São Paulo'
}

try:
    chave = input('Digite a chave que deseja acessar: ')
    print(f"O valor da chave '{chave}' é: {dados[chave]}")
except KeyError:
    print(f"A chave '{chave}' não existe no dicionário.")

#chave = input('Digite a chave que deseja acessar: ')
#print(f"O valor da chave '{chave}' é: {dados[chave]}") #Pode gerar KeyError se a chave não existir

#Feito o tratamento de exceções com try e except
def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError('A idade deve estar entre 0 e 120 anos!') #Erro personalizado
try:
    idade = int(input('Digite sua idade: '))
    #print(validar_idade(idade)) #Pode gerar ValueError se a idade for inválida
    print(validar_idade(idade)) #Corrigido, adicionando tratamento de exceção
except ValueError as e:
    print(f'Erro: {e}')

#Feito o tratamento de exceções com try e except
def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

try:
    notas = [8, 9, "10", 7]
    media = calcular_media(notas)
    print(f'Média: {media:.2f}')
except TypeError:
    print('Erro: Todas as notas devem ser números.')

#notas = [8, 9, "10", 7]
#media = calcular_media(notas)
#print(f'Média: {media:.2f}') #Pode gerar TypeError se houver um valor não numérico na lista