# Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal,
# acima ou abaixo do IMC ideal.

'''
print('Vamos calcular seu IMC!!!')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** altura)

if  imc == 19.60:
    print('Seu IMC está ideal!')
elif imc > 19.60:
    print('Acima do peso!')
elif imc < 19.60:
    print('Parece que tá passando fome!')
'''

peso = float(input('Peso: '))
altura = float(input('Altura: '))

IMC = peso / (altura ** 2)

if  IMC > 30:
    print('Obesidade')
elif IMC < 18:
    print('Abaixo do Peso')
else:
    print('Tudo OK')