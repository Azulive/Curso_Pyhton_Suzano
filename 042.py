# Simulação de um Caixa Eletrônico
# Este programa simula um caixa eletrônico, permitindo que o usuário faça depósitos,
# saques e consulte o saldo da conta, e sair

contador = 0
opcao = ''
valor_deposito = ''
valor_saque = ''
saldo = ''
saque = ''

print('********************************************')

print(f'BEM VINDO AO SEU BANCO!!!')

print('********************************************')

while opcao != '4':
    opcao = input('1. Depósito'
                  '\n2. Saque'
                  '\n3. Saldo'
                  '\n4. Sair------------------> ')

    if opcao == '1':
        deposito = float(input(f'Qual valor deseja depositar?: '))
        valor_deposito = deposito
        saldo = valor_deposito
        print(f'Seu depósito de R$ {valor_deposito} foi efetuado com sucesso!')
        print(f'Seu novo saldo é de R$ {saldo}')

        print('********************************************')

    elif opcao == '2':
        valor_saque = float(input(f'Qual valor deseja sacar?: '))

        saldo = saldo - valor_saque
        print(f'O saque de {valor_saque} foi efetuado com sucesso!')
        print(f'Seu novo saldo é de {saldo}')

        print('********************************************')

    elif opcao == '3':
        print(f'Seu saldo é de R$ {saldo}')

        print('********************************************')

    elif opcao == '4':
        print('Volte sempre!')

        print('********************************************')