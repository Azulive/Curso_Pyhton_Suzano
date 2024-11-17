# Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

r = float(input ('Raio: '))
Volume = (4/3) * 3.1415 * r ** 3
Area = 4 * 3.1415 * r ** 2


print(f'O volume da esfera é: {Volume:.2f}'
      f'\nA area da esfera é: {Area:.2f}')

# :.2f serve para limitar numeros