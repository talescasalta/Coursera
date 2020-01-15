#!/usr/bin/env python
# coding: utf-8

# In[7]:


def modo():
    valido = False
    while not valido:
        modo = int(input("Digite 1 para partida ou 2 para campeonato"))
        if modo == 1 or modo ==  2:
            valido = True
            return modo
        else:
            print("Entre um número válido")


# In[8]:


def computador_escolhe_jogada(n,m):
    tira = 1
    while (n - tira) % (m + 1) != 0 and tira <= m:
        tira = tira + 1
    if tira >= m:
        tira = m
    return tira


# In[9]:


def usuario_escolhe_jogada(n,m):
    valido = False
    while not valido:
        tira = int(input("Quantas peças você vai tirar?"))
        if 1 <= tira <= m:
            valido = True
            return tira
        else:
            print("Entre um número válido menor que", m)


# In[10]:


def partida():
    n = int(input("Quantas peças tem no jogo?"))
    m = int(input("Limite de peças por jogada?"))
    return n, m


# In[11]:


print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
if modo() == 1:
    print("Voce escolheu partida isolada")
else:
    print("Voce escolheu um campeonato!")
n, m = partida()
if n % (m+1) ==0:
    pccomeca = False
    print("Voce começa!")
else:
    pccomeca = True
    print("Computador começa!")
if pccomeca:
    computador_escolhe_jogada(n,m)
else:
    usuario_escolhe_jogada(n,m)


# In[ ]:




