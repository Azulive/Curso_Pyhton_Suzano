# Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar
'''
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Seu número é par')
else:
    print('Seu número é impar')
'''
#Caso 2

numero = (input('Digite um número: '))

if numero[-1] == '0':
    print('É par')
elif numero[-1] == '2':
    print('É par')
elif numero[-1] == '4':
    print('É par')
elif numero[-1] == '6':
    print('É par')
elif numero[-1] == '8':
    print('É par')
else:
    print('É impar')