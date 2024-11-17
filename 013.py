# Crie um programa que leia uma frase e mostre:
# 1 - Quantas vezes aparece a letra “a”
# 2 - Em que posição ela aparece a primeira vez
# 3 - Em que posição ela aparece na última vez

frase = input('Digite uma frase: ').strip()


print(f'Quantidade de ás {frase.count('a')}'
      f'\nPosição do primeiro a {frase.find('a') - 1}'
      f'\nUltimo á {frase.rfind('a')}')