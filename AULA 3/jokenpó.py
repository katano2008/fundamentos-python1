import random

opcao_maquina = ['pedra', 'papel', 'tesoura']
pontuacaoJogador = 0
pontuacaoMaquina = 0

rodadas = int(input('Quantas rodadas: '))
jogar_ = input('Deseja jogar: [S/N]').lower()

while jogar_ == 's': # Enquanto jogar_ for igual s
    for n in range(rodadas): # para n em uma distância da variavel rodadas
        jogador = input(f'Escolha {opcao_maquina}: ') #Jogador escolhe alguma opção da lista
        escolha_maquina = random.choice(opcao_maquina) #maquina escolhe alguma string da lista opcao_maquina
        
        if escolha_maquina == jogador:
            print('EMPATE')
            print(f'''

            Escolha da máquina: {escolha_maquina}
            Escolha do Jogador: {jogador}
            
            ''')
        elif escolha_maquina == 'pedra' and jogador == 'tesoura':
            print('Máquina ganhou')
            pontuacaoMaquina += 1 #Máquina ganhou 1 ponto
            print(f'''

            Escolha da máquina: {escolha_maquina}
            Escolha do Jogador: {jogador}
            
            ''')
        elif escolha_maquina == 'tesoura' and jogador == 'papel':
            print('Máquina ganhou')
            pontuacaoMaquina += 1 #Máquina ganhou 1 ponto
            print(f'''

            Escolha da máquina: {escolha_maquina}
            Escolha do Jogador: {jogador}
            
            ''')
        elif escolha_maquina == 'papel' and jogador == 'pedra':
            print('Máquina ganhou')
            pontuacaoMaquina += 1 #Máquina ganhou 1 ponto
            print(f'''

            Escolha da máquina: {escolha_maquina}
            Escolha do Jogador: {jogador}
            
            ''')
        else:
            print('Jogador ganhou')
            pontuacaoJogador += 1 #Jogador ganhou 1 ponto
            print(f'''

            Escolha da máquina: {escolha_maquina}
            Escolha do Jogador: {jogador}
            
            ''')
    print('PONTUAÇÃO GERAL')
    print('Pontuação do Jogador: ', pontuacaoJogador)
    print('Pontuação da Máquina: ', pontuacaoMaquina)
    jogar_ = input('Deseja continuar? ').lower() #Pergunta se deseja continuar para analisar se recomeça a repetição while ou não

if pontuacaoMaquina > pontuacaoJogador: #Se pontuação da máquina for maior que a pontuação do jogador
    print('PERDEU!!!! APOSENTA --- Máquina Venceu') #printar
elif pontuacaoMaquina == pontuacaoJogador: # Senão pontuação da máquina for igual a pontuação do jogador
    print('EMPATE...') #printar
else: # caso contrário
     print('Putz, ganhou... parabéns mr. ♥ --- Jogador Venceu') #printar