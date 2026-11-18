def soma(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def multiplicacao():
    return a * b
def divisao(a,b):
    return a / b

def calculadora():
    continuar_ = input('Vamos começar? [S/N]: ').lower()
    if continuar_ == 's':
        while continuar_ == 's':
            n1 = float(input('Digite o número: '))
            opcao = input('( + | - | / | x ): ')
            if opcao == '+':
                n2 = float(input('Digite o outro número: '))
                print(soma(n1, n2))
                continuar_ = input('Deseja calcular novamente? [S/N]: ').lower()
            elif opcao == '-':
                n2 = float(input('Digite o outro número: '))
                print(subtracao(n1, n2))
                continuar_ = input('Deseja calcular novamente? [S/N]: ').lower()
            elif opcao == '/':
                n2 = float(input('Digite o outro número: '))
                print(divisao(n1, n2))
                continuar_ = input('Deseja calcular novamente? [S/N]: ').lower()
            elif opcao == 'x':
                n2 = float(input('Digite o outro número: '))
                print(multiplicacao(n1, n2))
                continuar_ = input('Deseja calcular novamente? [S/N]: ').lower()
            else:
                print('Opção inexistente')
        else:
            print('Encerrando calculadora...')
            print('Calculadora encerrada.')
    elif continuar_ == 'n':
        print('Encerrando sistema...')
        print('Sistema encerrado.')
calculadora()
