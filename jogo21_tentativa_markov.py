import random
import math
import numpy as np
import pandas as pd
from scipy.linalg import eig

# Baralho de 52 cartas, para duas pessoas
cartas_iniciais = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

def valor_mao(mao):
    valor = 0
    for carta in mao:
        if carta in ["J", "Q", "K"]:
            valor += 10
        elif carta == "A":
            valor += 1
        else:
            valor += int(carta)
    return valor

def jogar_modo_2_jogadores(matriz_transicao):
    jog1 = []
    jog2 = []
    while True:
        valor_anterior_jog1 = valor_mao(jog1)
        valor_anterior_jog2 = valor_mao(jog2)
        jog1.append(cartas.pop())
        jog2.append(cartas.pop())
        valor_atual_jog1 = valor_mao(jog1)
        valor_atual_jog2 = valor_mao(jog2)
        if valor_atual_jog1 <= 21:
            matriz_transicao[valor_anterior_jog1, valor_atual_jog1] += 1
        if valor_atual_jog2 <= 21:
            matriz_transicao[valor_anterior_jog2, valor_atual_jog2] += 1
        #print("Mão jogador 1: ", jog1, " valor: ", valor_atual_jog1)
        #print("Mão jogador 2: ", jog2, " valor: ", valor_atual_jog2)
        if valor_atual_jog1 == 21 or (valor_atual_jog2 > 21 and valor_atual_jog1 < 21):
            #print("Jogador 1 venceu")
            break
        if valor_atual_jog2 == 21 or (valor_atual_jog1 > 21 and valor_atual_jog2 < 21):
            #print("Jogador 2 venceu")
            break
        if valor_atual_jog1 == valor_atual_jog2 == 21:
            #print("empate")
            break
        if len(cartas) == 0:
            #print("Fim do baralho ")
            break

if __name__ == "__main__":
    matriz_transicao = np.zeros((22, 22), dtype=int)  
    for _ in range(2000):
        random.shuffle(cartas_iniciais)
        cartas = cartas_iniciais.copy()
        jogar_modo_2_jogadores(matriz_transicao)
    df_matriz_transicao = pd.DataFrame(matriz_transicao, 
                                       columns=[str(i) for i in range(22)], 
                                       index=[str(i) for i in range(22)])
    
    print("Matriz de Transição:")
    print(df_matriz_transicao)

    matriz_probabilidade_transicao = df_matriz_transicao.div(df_matriz_transicao.sum(axis=1), axis=0).fillna(0)
    
    print("Matriz de Probabilidades de Transição:")
    print(matriz_probabilidade_transicao)

    # Calculando as probabilidades limite de transição
    matriz_limite = np.linalg.matrix_power(matriz_probabilidade_transicao.values,15)
    df_matriz_limite = pd.DataFrame(matriz_limite, 
                                    columns=[str(i) for i in range(22)], 
                                    index=[str(i) for i in range(22)])
    
    print("Matriz de Probabilidades Limite de Transição:")
    print(df_matriz_limite)
