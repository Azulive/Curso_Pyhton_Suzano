# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

resposta = ''
soma = 0
contador = 0
maior = None
menor = None


while resposta != 'n':
    n1 = int(input('Número: '))
    resposta = input(f'Deseja continuar? [S/N]: ').strip().lower()[0]
    contador += 1
    soma += n1

    if maior == None and menor == None:
            maior = n1
            menor = n1

    if n1 > maior:
        maior = n1

    elif n1 < menor:
        menor = n1

print(f'A média é {soma / contador}'
      f'\nO maior número foi {maior} e o menor foi {menor}')
