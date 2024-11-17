# Escreva um programa que execute o cálculo da Função horária da posição no MRUV,
# e retorne de acordo com o tempo informado pelo usuário

#Leitura das variaveis
posicao_inicial = float(input('Digite a posição inicial: '))
velocidade_inicial = float(input('Digite a velocidade incial: '))
tempo = float(input('Digite o tempo: '))
aceleracao = float(input('Digite a aceleração: '))

#Calculo da função Horaria do MRUV

S = posicao_inicial + velocidade_inicial * tempo + (aceleracao * tempo ** 2)/2

#Retorno das informações

print(f'A posição do objeto no tempo {tempo} é {S}')