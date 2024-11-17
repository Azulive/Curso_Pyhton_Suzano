# Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e
# continue pedindo até que o usuário acerte o número.
# E no final, retorne também a quantidade de tentativas necessárias.

'''
import random

random.randint
resposta = ' '
contador = 0
pc = random.randint(1, 10)
tentativas = 0

while resposta != pc:
    numero = int(input('Digite um número: '))
    resposta = numero
    contador += 1

    if resposta == pc:
        print('Você acertou!!!')
    else:
        print('Tente de novo!!!'
              '\n************************'
              f'\nO número gerado foi {pc}')
print(f'Foram necessárias {contador} tentativas')
'''

#Resolução professor

#gerar o aleatorio
import random
pc = random.randint(1, 10)
contador = 0

#Leitura inicial
numero = int(input('Número entre 1 e 10: '))

while numero > 10 or numero < 1:
    print('Somente entre 1 e 10')
    numero = int(input('Número entre 1 e 10: '))
    contador += 1

#Loop de repetição

while pc != numero:
    numero = int(input('Número de 1 a 10: '))
    while numero > 10 or numero < 1:
        print('Somente entre 1 e 10')
        numero = int(input('Número de 1 a 10: '))
        contador += 1

#Retorno das informações
print(f'Você acertou em {contador} tentativas')