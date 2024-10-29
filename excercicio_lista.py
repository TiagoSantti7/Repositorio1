import os

"""
1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
"""

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Marcos', 'Tiago', 'Felipe', 'Regismar']
ano_atual_ano_nascimento = [2024, 2002]

"""
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
"""

"""for numero in numeros:
    
    print(f'{numero}')"""

"""
3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
"""

"""soma_impares = 0

for i in range(1,11,2):
    
    soma_impares += i
    print(soma_impares)"""

"""
4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
"""

"""for i in range(10, 0, -1):
    print(i)"""

"""
5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
"""

"""numero_tabuada = int(input('Informe o valor que eu digo a tabuada: '))

for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")"""

"""
6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
"""
"""lista_numeros = [12, 35, 7, 9]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
        print(f'Somando {numero}... Soma atual igual a {soma}')
    print(f'Soma total dos elemetos é igual a  {soma}')
except Exception as e:
        print(f'Ocorreu um erro: {e}')"""

"""
7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""

lista_média = [1,2,4,6,8,10]
tamanho = len(lista_média)
soma = 0

try:
    if tamanho == 0:
        raise ZeroDivisionError('A lista está vazia, não é possível calcular a média')
    for i in lista_média:
        soma += i
    media = soma / tamanho
    print(f'A média é igual a {media}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')