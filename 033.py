# Escreva um programa que calcule a soma de todos os números múltiplos de 4
# que são encontrados entre 1 até 500
'''
soma = 0

for i in range(1, 500):
    if soma % 4 + i:
        print(i)


# Caso 1
soma = 0
for i in range(501):
    if i % 4 == 0:
      soma = soma + i
print(soma)
'''
# Caso 2

soma = 0
for i in range(0, 501, 4):
    soma = soma + i
print(soma)