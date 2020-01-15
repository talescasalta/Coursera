def modo():
    valido = False
    while not valido:
        modo = int(input("Digite 1 para partida ou 2 para campeonato"))
        if modo == 1 or modo ==  2:
            valido = True
            return modo
        else:
            print("Entre um número válido")            
def computador_escolhe_jogada(n,m):
    tira = 1
    while (n - tira) % (m + 1) != 0 and tira <= m:
        tira = tira + 1
    if tira >= m:
        tira = m
    print("O computador tirou", tira, "peça(s).")
    return tira
def usuario_escolhe_jogada(n,m):
    valido = False
    while not valido:
        tira = int(input("Quantas peças você vai tirar?"))
        if 1 <= tira <= m:
            valido = True
            print("Você tirou", tira, "peça(s).")
            return tira
        else:
            print("Entre um número válido menor que", m)            
def partida():
    n = int(input("Quantas peças tem no jogo?"))
    m = int(input("Limite de peças por jogada?"))
    return n, m
def jogo():
    n, m = partida()
    if n % (m+1) ==0:
        pccomeca = False
        print("Voce começa!")
    else:
        pccomeca = True
        print("Computador começa!")
    print("o número de peças restantes é: ", n)
    while n > 0:
        if pccomeca:
            pccomeca = False
            tira = computador_escolhe_jogada(n,m)
            n = n - tira
            print("Agora resta apenas" , n , " peça(s) no tabuleiro.")
        else:
            pccomeca = True
            tira = usuario_escolhe_jogada(n,m)
            n = n - tira
            print("Agora resta apenas" , n , " peça(s) no tabuleiro.")
    if pccomeca:
        print("Fim do jogo! Você ganhou!")
        return pccomeca
    else:
        print("Fim do jogo! O computador ganhou!")
        return pccomeca
print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
if modo() == 1:
    print("Voce escolheu partida isolada")
    jogo()
else:
    print("Voce escolheu um campeonato!")
    print("**** Rodada 1 ****")
    p1 = jogo()
    print("**** Rodada 2 ****")
    p2 = jogo()
    print("**** Rodada 3 ****")
    p3 = jogo()
    voce = 0
    pc = 0
    if p1:
        voce = 1
    if p2:
        voce = voce + 1
    if p3:
       voce = voce + 1
    pc = 3 - voce
    print("Placar: Você", voce," X", pc, "Computador")
