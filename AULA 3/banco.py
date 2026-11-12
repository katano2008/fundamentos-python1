acesso = input('Deseja acessar o banco? [S/N]: ').lower()
c = 3
extrato = []
saldo = 2500

while acesso == 's':
    senha_acesso = input('Digite sua senha de acesso: ')
    if senha_acesso == '0506':
        
            print('''Seja bem-vindo ao Banco Nubanque''')
            menu = input('''
                    1 - saque
                    2 - deposito
                    3 - extrato
                    4 - sair
                    Digite o número: ''')
            if menu == '1':
                saque_ = float(input('R$'))
                if saque_ < saldo:
                        senha_acesso = input('Digite sua senha: ')
                        if senha_acesso == '0506':
                            saldo =- saque_
                            extrato.append(- saque_)
                            print(f'conta: {saldo}')
                            acesso = input('Deseja acessar o banco? [S/N]: ').lower()
                        else:
                            print('Senha incorreta')
                            acesso = input('Deseja acessar o banco? [S/N]: ').lower()
                else:
                    print('saldo insuficiente...')                
            elif menu == '2':
                deposito_ = float(input('R$'))
                if senha_acesso == '0506':
                    saldo += deposito_
                    extrato.append(deposito_)
                    print(f'conta: {saldo}')
                    acesso = input('Deseja acessar o banco? [S/N]: ').lower()
                else:
                    print('Senha incorreta')
                    acesso = input('Deseja acessar o banco? [S/N]: ').lower()
            elif menu == '3':
                print(extrato)
                acesso = input('Deseja acessar o banco? [S/N]: ').lower()
            else:
                print('Obrigado, volte sempre!')
                break
    else:
        c -= 1
        print(f'Senha incorreta...')
else:
    print('Sessão finalizada')