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
            print("Restam apenas {} peças em jogo.\n ".format(n))
        
        if is_computer_turn:
            print("Você ganhou!")
            return 1
        else:
            print("O computador ganhou!")
            return 0
        
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

print("Bem vindo ao jogo do NIM! Escolha: ")
print(" ")

print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")


tipo_jogo =(input("Digite sua escolha: "))

if tipo_jogo == 1: 
            partida()
    
elif tipo_jogo == 2:
            campeonato()


def usuario_escolhe_jogada (n, m):

        print("sua vez! \n")
    
        jogada = 0
    
        while jogada == 0:
            jogada = int(input("Quantas peças irá tirar: "))
            if jogada > n or jogada < 1 or jogada > m:
                jogada = 0
                return jogada
def computador_escolhe_jogada (n, m):

        print("Vez do computador")
        quantia = n% (m+1)
        if quantia > 0:
            return quantia
        return m
        
