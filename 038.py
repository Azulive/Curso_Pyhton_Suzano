#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa
'''
contador = 0
resposta = ' '
maior_numero = ' '

n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))

while resposta != '5':


    resposta = input('1. Somar'
                     '\n2. Multiplicar'
                     '\n3. Maior'
                     '\n4. Novos Números'
                     '\n5 Sair do programa ------------------> ')
    if resposta == '1':
        print(f'A soma é {n1 + n2 + n3}')
    elif resposta == '2':
        print(f'A multiplicação é {n1 * n2 * n3}')
    elif resposta == '3':
        if n1 > n2 and n1 > n3:
            print(f'{n1} é o maior')
        elif n2 > n1 and n2 > n3:
            print(f'{n2} é o maior')
        elif n3 > n1 and n3 > n2:
            print(f'{n3} é o maior')
    elif resposta == '4':
            n1 = int(input('N1: '))
            n2 = int(input('N2: '))
            n3 = int(input('N3: '))
    elif resposta == '5':
            print('Até logo!')
    else:
            print('Entrada inválida')

'''
n1 = int(input('Número: '))
n2 = int(input('Número: '))
n3 = int(input('Número: '))

opcao = ''

while opcao != '5':
    opcao = input('1. Somar'
                  '\n2. Multiplicar'
                  '\n3. Maior'
                  '\n4. Novos Números'
                  '\n5. Sair')
    
    if opcao == '1':
        print(f'A some é {n1 + n2 + n3}')
    elif opcao == '2':
        print(f'A multiplicação é {n1 * n2 * n3}')
    elif opcao == '3':
        if n1 > n2 and n1 > n3:
            print(f'{n1} é o maior')
        elif n2 > n3:
            print(f'{n2} é o maior')
        else:
            print(f'{n3} é o maior')
    elif opcao == '4':
        n1 = int(input('Número: '))
        n2 = int(input('Número: '))
        n3 = int(input('Número: '))
    elif opcao == '5':
        print('Até breve!')
    else:
        print('Entrada inválida')