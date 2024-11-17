# Escreva um programa que verifique se uma palavra é um palíndromo.

palavra = input('Digite uma palavra: ').strip()

compatibilidade = 0

for i in range(0, len(palavra)):
    if palavra[i] == palavra[-i - 1]:
        compatibilidade = compatibilidade + 1

if compatibilidade == len(palavra):
    print('É palíndromo')
else:
    print('Não é')

'''
if palavra == palavra[::-1]:
    print('É palíndromo')
else:
    print('Não é')
'''