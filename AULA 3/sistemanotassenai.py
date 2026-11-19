def acesso(senha): #Função com uma condição de senha
    if senha  == '123':
        return 'Acesso autorizado'

def inserir_nota(nome, quantidade): # Função para inserir a nota em uma lista
    lista = [] #LISTA VAZIA
    print('aluno: ', nome) #Print o nome do aluno
    for n in range(quantidade): #Para n em uma distância da quantidade
        nota1 = float(input('1 >>')) # nota
        lista.extend([nota1]) #Insere a nota na lista
        
    return [lista, nome] # retorna primeiro lista e depois nome
    
    

def media(lista): # Função para calculo de média escolar
    return sum(lista) /len(lista)
    
def system(): # Sistema
    
    acesso_ = input('Deseja acessar: ')
    while acesso_ == 'sim': # Enquanto acesso_ for igual a 'sim'
          senha = input('Digite a senha: ') #digitar senha
          print(acesso(senha)) #printa a função nomeada como senha onde está integrado a condição que retorna uma string / acesso(senha) = 'Acesso autorizado'
          if acesso(senha) == 'Acesso autorizado': # Condição: Se acesso(senha) for igual 'Acesso autorizado', ele continua. caso contrário não
               print('Registre as notas: ')
               nome =  input('Nome: ')
               q = int(input('Quantidade Notas'))
               dados = inserir_nota(nome, q) # variavel que guarda a função inserir_nota com 2 parametros (nome, q)
               print(dados[0]) # printa o primeiro parametro de dados que seria a var. nome
               media_  =  media(dados[0]) # variavel guarda função
               print('Media: ', media_, 'aluno(a)',dados[1]) #printa a media
               
    
system()
