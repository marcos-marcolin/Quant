tipo_jogo = 0
global partida
global campeonato


def partida():
    
    print("")
    
    n = int(input("Quantas peças: "))
    m = int(input("Limite de peças por jogada: "))
    
    is_computer_turn = True
    
    if n%(m+1) ==0: is_computer_turn = False
            
    while n>0:
        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print ("Computador retirou {} peças. ".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou {} peças.".format(jogada))
            
        n = n-jogada
        print("Restam apenas{} peças em jogo.\n ".format(n))
        
    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0

def usuario_escolhe_jogada (n, m):
    global partida
    global campeonato
    
    print("sua vez! \n")
    
    jogada = 0
    
    while jogada == 0:
        jogada = int(input("Quabtas peças irá tirar: "))
        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0
    return jogada

def computador_escolhe_jogada (n, m):
    global partida
    global campeonato
    
    print("Vez do computador")
    quantia = n% (m+1)
    if quantia > 0:
        return quantia
    return m
        
def campeonato():
    global partida
    global campeonato

    usuario = 0
    computador = 0
    
    for _ in range(3):
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario+1
        else:
            computador = computador +1
    print("Placar final: você {} x {} Computador". format(usuario, computador))


while tipo_jogo==0:
    
    print("")
    print("Bem vindo ao NIM! Escolha dua opção: ")
    print (" ")
    print("1 - Para uma partida isolada")
    print("2 - Para jogar campeonato")
    
    tipo_jogo = int(input("Sua opção: "))
    print (" ")
    
    if tipo_jogo == 1:
        print("Você escolheu a partida isolada!")
        partida()
        break
    
    elif tipo_jogo == 2:
        print("Você escolheu um campeonato!")
        campeonato()
        break

    else:
        print("Opção Inválida")
        tipo_jogo=0
  
