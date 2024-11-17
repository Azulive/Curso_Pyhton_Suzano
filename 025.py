# Crie um programa para jogar JOKEMPO, usando a função random.randint
'''
import random
jogador = int(input('Digite um número de 1 a 3, sendo que 1-Papel, 2-Pedra, 3-Tesoura: '))
pc = random.randint(1, 3)

while True:

if  jogador == 1 and pc == 1:
    print('Empate')
elif jogador == 1 and pc == 2:
    print('Papel ganha de pedra! Jogador ganhou!')
elif jogador == 1 and pc == 3:
    print('Papel perde para tesoura! Pc ganhou')
elif jogador == 2 and pc == 1:
    print('Papel ganha de pedra! Pc ganhou')
elif jogador == 2 and pc == 2:
    print('Empate')
elif jogador == 2 and pc == 3:
    print('Pedra ganha de tesoura! Jogador ganhou!')
elif jogador == 3 and pc == 1:
    print('Tesoura ganha de papel! Jogador ganhou!')
elif jogador == 3 and pc == 2:
    print('Pedra ganha de tesoura! Pc ganhou')
elif jogador == 3 and pc == 3:
    print('Empate')
'''

# Caso 2

import random
import time

pc = random.randint(1, 3)

print('Bem vindo ao JOKEMPO em Python!!!')

jogador = int(input('1 - Pedra'
                    '\n2 - Papel'
                    '\n3 - Tesoura'
                    '\n--------------> '))
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO')
time.sleep(1)
print('Pensando...')
time.sleep(2)

print('*************************************')

if jogador == pc:
    print('Empate')
elif ((jogador == 1 and pc == 3) or
      (jogador == 2 and pc == 1) or
      (jogador == 3 and pc == 2)):
       print('Você Ganhou!!!')
else:
    print('Você Perdeu!')

print('*************************************')