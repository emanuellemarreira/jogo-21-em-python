import random
import math
import numpy as np
#baralho de 52 cartas, pra duas pessoas
cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

def valor_mao(mao):
    valor = 0
    for carta in mao:
        if carta in ["J","Q","K"]:
            valor += 10
        elif carta == "A":
            valor += 1
        else:
            valor += int(carta)
    return valor

def jogar_modo_1(jog1, jog2, n, nl):
    p = 0
    while True:
        jog1.append(cartas.pop())
        print("mao jogador ",n,": ", jog1, " valor: ", valor_mao(jog1))
        if valor_mao(jog1) == 21:
            break
        if valor_mao(jog1) > 21:
            p = -1
            break
        resp_jog = input("deseja continuar? s/n ")
        if resp_jog == "n":
            print("fim de jogo")
            break
    if p == -1:
        print("jogador ", nl, "venceu")
    elif math.fabs((21 - valor_mao(jog1))) < math.fabs((21 - valor_mao(jog2))):
        print("jogador ",n," venceu")
    elif math.fabs((21 - valor_mao(jog1))) > math.fabs((21 - valor_mao(jog2))):
        print("jogador ",nl,"venceu")
    else:
        print("empate")
    return 0


def jogar_modo_2_jogadores():
    jog1 = []
    jog2 = []
    valor_mao_anterior = 0
    while True:
        jog1.append(cartas.pop())
        jog2.append(cartas.pop())
        print("mao jogador 1: ", jog1, " valor: ", valor_mao(jog1))
        print("mao jogador 2: ", jog2, " valor: ", valor_mao(jog2))
        if valor_mao(jog1) == 21 or (valor_mao(jog2) > 21 and valor_mao(jog1) < 21):
            print("jogador1 venceu")
            break
        if valor_mao(jog2) == 21 or (valor_mao(jog1) > 21 and valor_mao(jog2) < 21):
            print("jogador2 venceu")
            break
        resp_jog1 = input("deseja continuar? s/n ")
        resp_jog2 = input("deseja continuar? s/n ")
        if resp_jog1 == resp_jog2 == "n":
            if math.fabs((21 - valor_mao(jog1))) < math.fabs((21 - valor_mao(jog2))):
                print("jogador 1 venceu")
                break
            elif math.fabs((21 - valor_mao(jog2))) < math.fabs((21 - valor_mao(jog1))):
                print("jogador 2 venceu")
                break
            else:
                print("empate")
                break
        if resp_jog1 == "s" and resp_jog2 == "n":
            jogar_modo_1(jog1, jog2, 1, 2)
            break
        if resp_jog2 == "s" and resp_jog1 == "n":
            jogar_modo_1(jog2, jog1,2, 1)
            break
        if len(cartas) == 0:
            print("fim do baralho")
            break

if __name__ == "__main__":
    random.shuffle(cartas)
    matriz_transicao = np.zeros((21, 21), dtype=int)
    jogar_modo_2_jogadores()
