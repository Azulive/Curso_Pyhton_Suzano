# Escreva um programa que leia um número n inteiro qualquer e
# mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

contador = 0
atual = ''
proximo = ''
numero = ''

numero = int(input('Digite um número: '))

atual, proximo = numero, numero + 1

print(f'Os primeiros 5 elementos da sequência de Fibonacci a partir de {numero} são: ')

while contador < 5:
    print(f'{atual}')

    atual, proximo = proximo, atual + proximo
    contador += 1

#proximo = anterior + atual
#anterior = atual
#atual = proximo

