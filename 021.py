# Escreva um programa que peça ao usuário um número de 1 a 7 e imprima
# o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.)

numero = int(input('Digite um número: '))

if numero == 1:
    print('Segunda-feira')
elif numero == 2:
    print('Terça-feira')
elif numero == 3:
    print('Quarta-feira')
elif numero == 4:
    print('Quinta-feira')
elif numero == 5:
    print('Sexta-feira')
elif numero == 6:
    print('Sábado')
elif numero == 7:
    print('Domingo')
else:
    print('Número invalido!')