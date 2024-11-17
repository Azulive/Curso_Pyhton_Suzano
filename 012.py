# Crie um programa que leia um nome, e mostre o
# primeiro e o último nome
'''
nome_completo = input('Digite seu nome completo: ').strip()
primeiro_nome = nome_completo.split()[0]
ultimo_nome = nome_completo [-1]

print(f'O primeiro nome é: {primeiro_nome.split()}')
print(f'O último nome é: {ultimo_nome}')
'''

nome = input('Digite seu nome: ').strip()

primeiro_nome = nome[:nome.find(' ')]
ultimo_nome = nome[nome.rfind(' '):]

nome_em_lista = nome.split()
#primeiro_nome = nome_em_lista[0]
ultimo_nome = nome_em_lista[len(nome_em_lista) - 1]
#ultimo_nome = nome_em_lista[-1]

print(f'O primeiro nome é: {primeiro_nome}'
      f'\nO último nome é: {ultimo_nome}')
