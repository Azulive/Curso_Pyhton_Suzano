'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
'''

nome_completo = input('Digite seu nome completo: ')
quantidade_letras = len(nome_completo.replace(' ',''))
primeiro_nome = nome_completo.split()[0]

print(f'Nome Maiúsculo: {nome_completo.upper()}'
      f'\n Nome Minúsculo: {nome_completo.lower()}'
      f'\n Quantidade de letras: {quantidade_letras}'
      f'\n Quantas letras tem o primeiro nome: {len(primeiro_nome)}')
