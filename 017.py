# Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''
letra = input('Insira uma letra: ').strip().lower()[0]     #tira os epaços, deixa minusculo e analisa a primeira string

if letra == 'a':
    print('Vogal')
elif letra == 'e':
    print('Vogal')
elif letra == 'i':
    print('Vogal')
elif letra == 'o':
    print('Vogal')
elif letra == 'u':
    print('Vogal')
else:
    print('Consoante')

#Caso 2
letra input('letra: ').strip().lower()[0]

if letra in 'aeiou':
    print('Vogal')
else:
    print('Consoante')
'''


#Caso 3

letra = input('letra: ').strip().lower()[0]

if  (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print('Vogal')
else:
    print('Consoante')