# Escreva um programa que leia o
# Nome, idade e sexo de 4 pessoas. No final mostre:

# A média de idade do grupo
# Qual é o homem mais velho
# Quantas mulheres têm menos de 20 anos


soma = 0
quant_mulheres_menor_20_anos = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''

for i in range(10):
    nome = input('Digite seu nome: ').strip().lower()
    idade = int(input('Digite sua idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()[0]
    print('************************')

    #Soma das idades
    soma = soma + idade

    #Verificação do homem mais velho
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    #Verificação da quantidade de mulheres com menos de 20 anos
    if sexo == 'F' and  idade <20:
        quant_mulheres_menor_20_anos = quant_mulheres_menor_20_anos + 1


print(f'A média de idade é {soma / 10}'
      f'\nQuantidade de mulheres com menos de 20 anos é {quant_mulheres_menor_20_anos}'
      f'\nO homem mais velho é {nome_homem_mais_velho}')