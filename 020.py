# Crie um programa que verifica se uma pessoa pode ser doadora de
# sangue, considerando a idade e os critérios de saúde.

'''
paciente = input('Nome do paciente: ').strip()
idade = int(input('Digite sua idade: '))
fumante = input('Você fuma? ')
peso = float(input('Digite seu peso: '))

if fumante == 'nao' or fumante == 'não':
    print(' ')
elif idade >=18:
    print(' ')
elif peso <= 76.5:
    print(' ')
else:
    print('Inapto')

#Caso 1

idade = int(input('Digite a sua idade: '))
peso = float(input('Digite seu peso: '))
horas_sono = int(input('Digite a quantidade de horas de sono: '))
bebida = input('Ingeriu bebida alcoolica? [S - sim / N - não]: ').strip().upper()

if  (idade > 16 and idade < 69) and peso > 50 and horas_sono > 6 and bebida == 'N':
    print('Pode doar')
else:
    print('Não pode')
'''

idade = int(input('Digite a sua idade: '))
if  idade > 16 and idade < 69:
    peso = float(input('Digite seu peso: '))
    if peso > 50:
        horas_sono = int(input('Digite a quantidade de horas de sono: '))
        if  horas_sono > 6:
            bebida = input('Ingeriu bebida alcoolica? [S - sim / N - não]: ').strip().upper()
            if bebida == 'N':
                print('Pode doar')
            else:
                print('Quantidade de horas entre bebidas inválida')
        else:
            print('Horas de sono insuficiente')
    else:
        print('Peso inválido')
else:
    print('Idade inválida')