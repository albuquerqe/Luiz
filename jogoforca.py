# Ana Flávia Melo Florencio 1134228
# Luiz Henrique Albuquerque 1134362


import os 

# aqui esta a funcao que acha letras na palavra
def achaletra(letra, palavra, acerto):
    retorno=[]
    indice = 0
    fezerro = True
    for let in palavra:
        if letra == let:
            retorno.append(palavra[indice])
            print("acertou: ",palavra[indice])
            fezerro = False
        else:
            retorno.append(acerto[indice])
        indice = indice + 1
    return retorno, fezerro
def exibir_menu():
    while True: 
        opcao = input("Deseja Jogar novamente? (s/n) \n")
        if opcao.upper() == "s":
            return True
        elif opcao.upper() == "n":
            return False
        else:
            print("Opção Inváilida. Tente novamente")
    

# aqui faz as entradas e inicializa variaveis
inicio = input(" Bem vindo ao Jogo da forca! ")
desafiante = input("Nome do Desafiante:")
competidor = input("Nome do Competidor:")
os.system("cls")
palavra = input("Informe a palavra chave: ")
dica = []
acerto=[]
erro=0
contdicas = 1
dica.append(input( "Informe a dica 1: "))
dica.append(input( "Informe a dica 2: "))
dica.append(input( "Informe a dica 3: "))
os.system("cls")
# aqui cria a lista das letras acertadas
tamanho = len(palavra)
for cont in palavra:
    acerto.append("*")
print("A palavra tem: " , len(palavra) * "*") 
# inicia a execucao no while
while True: 
    opcao = input("(1) Jogar | (2) Solicitar dica\n")
    if (opcao == "2"):
        if (contdicas <= 3):
            print (dica [contdicas - 1]) 
            contdicas = contdicas + 1 
        else:
            print ("Voce não tem mais dicas")
    letra = input("Informe uma letra: ")
    acerto, fezerro = achaletra(letra, palavra, acerto)
    if (fezerro):
        erro=erro+1
    if (erro==6):
            print("Desafiante",desafiante,"GANHOU")
            break
    ganhou = True
    for cont in acerto:
        if cont == "*":
            ganhou = False
    if (ganhou):
        print("Competidor",competidor,"GANHOU")
        break
    #os.system("cls")
    print(''.join(acerto))
    print("Erro:" ,erro)
jogar_novamente = exibir_menu() 
  
    



    
