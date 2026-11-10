import random #Importando uma biblioteca, ferramentas.

print('JOGO DA ALEATORIDADE')
print()
print('TENTE ACERTAR O NÚMERO DE 1 A 10... ')
print('VALENDO R$5.000,00')


tentativas  =  3 # Variavel tentativas recebe valor 3
for n in range(tentativas): #Para (For) n em uma distância (range) de tentativas (3)
    numero_maquina = random.randint(1,10) # variavel maquina recebe uma função de escolher um número de 1 a 10
    numero_usuario = int(input('SEU CHUTE VALENDO 5K!>>>> ')) #numero usuario para escolher de 1 a 10
    tentativas =  tentativas - 1 # A cada tentativa, ele perde uma
    if numero_usuario == numero_maquina: # Se numero de usuario for igual numero da maquina
        print('Você é o grande vencedor(a), você se tornou um ♥') #printar
        print('LEVE SEU 5K!!!! ;)') #printar
    else: # Caso contrário
        print('ERROU FEIO!! SEU BOSTA!!') #printar
        print('tentativas', tentativas) #mostrar tentativas que faltam
        if tentativas  == 0: # Se tentativas for igual a 0
            print('o numero da maquina é ', numero_maquina) # printar numero escolhido pela maquina
            print('Tentaivas esgotadas!!! ;P ') #printar