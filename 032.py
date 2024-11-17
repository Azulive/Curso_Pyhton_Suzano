# Escreva um programa que imprima todos os números pares
# entre dois números fornecidos pelo usuário.
'''
numero = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

for i in range(2):
    if numero or numero2 % 2 == 0:
       print(i)
'''

inicio = int(input('Digite um número: '))
fim = int(input('Digite um número: '))

if inicio < fim:
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            print(i)
    else:
        for i in range(fim, inicio + 1):
            if i % 2 == 0:
                print(i)