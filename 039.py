# Faça um programa que leia um número e retorne o fatorial !
# 4! = 4 x 3 x 2 x 1

contador = 0

numero = int(input('Digite um número: '))
if numero < 0:
    print('Não existem fatoriais de números negativos')
elif numero == 0 or numero == 1:
    print(f'O fatorial de {numero} é 1')
else:
    fatorial = 1
    contador = numero
    while contador > 1:
     fatorial *= contador
     contador -= 1
     print(f'O fatorial de {numero} é {fatorial}')