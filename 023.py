# Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.


palavra = input('Digite uma palavra: ').strip().lower()[0]

if palavra in 'aeiou':
    print('Começa com vogal')
else:
    print('Começa com consoante')

'''
if palavra == ('a' or palavra == 'e' or palavra == 'i' or palavra == 'o' or palavra == 'u'):
    print('Começa com vogal')
else:
    print('Começa com consoante')
'''