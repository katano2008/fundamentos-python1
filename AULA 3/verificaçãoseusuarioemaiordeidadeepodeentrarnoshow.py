verificacao = input('Deseja fazer a verificação? [S/N]').lower()

while verificacao == 's':
    nome = input('Qual seu nome? ')
    idade = int(input(f'Olá {nome}, quantos anos você tem? '))
    
    if idade < 0:
        print('erro...')
    elif idade < 18:
        print('Acesso Negado...')
    elif idade <= 60:
        print(f'Acesso liberado, Seja Bem-vindo {nome}!')
    else:
        print('Calma, algo está errado...')
    verificacao = input('Deseja refazer? [S/N]').lower()