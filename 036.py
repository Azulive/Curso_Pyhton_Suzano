# Escreva um programa que leia o peso de 7 pessoas, e no final,
# mostre qual foi o maior e o menor peso lidos


maior_peso = 0
menor_peso = 100000000000000000
#maior_peso_v2 = None
#menor_peso_v2 = None

for i in range(7):
    peso = float(input('Digite seu peso: '))

    #if i == 0
        #menor_peso_v2 = peso
        #maior_peso_v2 = peso

    if peso > maior_peso:
        maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso

print(f'O mais obeso tem {maior_peso}'
      f'\nO mais raquítico tem {menor_peso}')