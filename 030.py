# Escreva um programa que calcule a soma dos números de 1 a 100 usando um loop

'''
for i in range(0, 100):
    i = 1
    soma = i + 1
    print(f'{soma + i}')
'''

soma = 0
for i in range(1, 101):
    soma = soma + i
    print(f'{soma}')