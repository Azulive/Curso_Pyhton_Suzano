# Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média,
# é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
nota5 = float(input('Digite a quinta nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f'Sua média foi {media}')

if media < 6:
    print(f'Insuficiente')
elif media > 6:
    print(f'Suficiente')
elif media > 7:
    print(f'Bom')
elif media > 9:
    print(f'Excelente')