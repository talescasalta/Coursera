#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# definicao de constantes
CAP_MIN = 10
CAP_MAX = 51 # ja ajustado ao random
VOL_MIN = 1
VOL_MAX = 11 # ja ajustado ao random

def main():
    semente = int(input("Digite a semente para gerar numeros pseudo-aleatorios: "))
    jogo    = Simulador(semente)

    fim = False
    while not fim:
        jogo.sorteia()
        opcao = input("Deseja utilizar o volume sorteado? (s/n): ")
        if opcao == 's':
            fim = jogo.deposita()  # retorna True caso o balde fique cheio
        else:
            fim = True
    jogo.finaliza()

class Simulador:
    def __init__(self, semente):
        random.seed(semente)
        capacidade = random.randrange(CAP_MIN, CAP_MAX)
        self.bal = Balde(capacidade)
        self.vol = 0
        self.avisou = False

    def sorteia(self):
        self.vol = random.randrange(VOL_MIN, VOL_MAX)
        print("Volume sorteado: ", self.vol)
        return self.vol

    def deposita(self):
        deposita = self.bal.deposita(self.vol)
        if self.avisou == False:
            if self.bal.volume >= (self.bal.capacidade / 2):
                self.avisou = True
        print(self.bal)
        return deposita

    def finaliza(self):
        print("Fim da simulação\n",
             "Capacidade do balde :%s"%(self.bal.capacidade), "\n",
              "volume final :%d"%(self.bal.volume))
        if self.bal.cheio:
            print("O balde está cheio e derramou %d volumes"%(self.bal.derramado))
        else:
            print("O balde não encheu")
        return

class Balde:
    def __init__(self, cap):
        self.capacidade = cap
        self.volume     = 0
        self.derramado  = 0
        self.cheio      = False

    def __str__(self):
        # remova a linha abaixo e escreva o seu codigo para esse metodo
        if self.volume < (self.capacidade / 2):
            b = "Volume abaixo da metade"
        elif self.volume >= (self.capacidade / 2) and self.volume < self.capacidade:
            b = "A metade da capacidade já foi atingida"
        elif self.volume == self.capacidade:
            b = "O balde encheu"
        else:
            b = "O balde derramou %d"%(self.derramado)
        return b

    def deposita(self, vol):
        # remova a linha abaixo e escreva o seu codigo para esse metodo
        self.volume += vol
        if self.volume >= self.capacidade:
            self.cheio = True
            if self.volume > self.capacidade:
                self.derramado = self.volume - self.capacidade
                self.volume = self.capacidade
        return self.cheio

main()


# In[ ]:




