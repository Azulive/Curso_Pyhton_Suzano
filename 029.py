# Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

'''
print('VAMOS FAZER CONTAS!!!')
print('***************************')
tabuada = 0
x = 2
for i in range(1, 11):
    tabuada = int(input('Digite um número: '))
    tabuada = tabuada * (x)
    print(f'3x1 = {tabuada} or \n3x2 = {tabuada * (x)} or \n3x3 = {tabuada * (x)}'
          f'\n3x4 = {tabuada * (x)}')

print('*******************')
'''
print('VAMOS FAZER CONTAS!!!')
print('***************************')

numero = int(input('Digite um número: '))

for i in range(11):
    print(f'{numero} x {i} = {numero * i}')

