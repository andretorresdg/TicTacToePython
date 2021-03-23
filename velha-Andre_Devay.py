'''
Nome: Andre Devay Torres Gomes
NUSP: 10770089

'''

#Importações necessárias
import random
import sys
import time


# Função principal que roda a interface e chama as outras funções
def main():
    global modo
    global matriz
    global historico
    matriz = [[ 1, '|', 2, '|', 3],[ 4, '|', 5,'|', 6], [ 7, '|', 8, '|', 9]]
    jogo = 4
    modo = 1
    while jogo != 1 or jogo != 0:
        print()
        print()
        jogo = int(input("Deseja jogar ? (Digite 1 para SIM ou 0 para NÃO)  "))
        print()
        if jogo == 1:
            historico = []
            modo = int(input("Digite 1 para modo Player vs. Player ou digite 2 para modo Player vs. Computador  "))
            print()
            jogar()
        elif jogo == 0:
            print("Finalizando...")
            sys.exit()


# Função que executa o jogo             
def jogar():
    global matriz
    global vez
    global modo
    rodada = 0
    vez = 1

    while ganhou() == 0:
        rodada = rodada + 1
        print(" Turno de jogador", vez)
        imprimeMatriz(matriz)
        print()
        print()
        if vez == 1:
            jogador()
            historico.append(lugar)
            print(historico)
            if len(historico) == 9:
                print()
                print()
                print('O jogo deu velha!')
                sys.exit()
            vez = 2
        elif vez == 2:
            if modo == 1:
                jogador()
            elif modo == 2:
                computador()   
            vez = 1
            historico.append(lugar)
            print(historico)
        if len(historico) == 9:
            print()
            print()
            print('O jogo deu velha!') 
            sys.exit()
        if ganhou() == 1:
            print()
            print('O jogador 1 venceu!') 
            print()
            imprimeMatriz(matriz)
            sys.exit()
        elif ganhou() == 2:
            print()
            print('O jogador 2 venceu!')  
            print()
            imprimeMatriz(matriz)
            sys.exit()
        
        
# Imprime a matriz atualizada durante o jogo
def imprimeMatriz(matriz):
    b = 0
    for linha in matriz:
        b = b + 1
        for coluna in linha:
            print(coluna,end='')
        if b != 3:
            print('\n' + '-+-+-')


# Executa o tipo de rodada em que há um Player
def jogador():
    global matriz
    global lugar
    if vez == 1:
        sinal = 'X'
    elif vez == 2:
        sinal = 'O'
    lugar = 0

    while lugar == 0:
        lugar = int(input("Digite o número do espaço em que deseja jogar  "))
        if historico.count(lugar) > 0:
            lugar = 0

        if lugar == 1:
            if matriz[0][0] == 1:
                matriz[0][0] = sinal
                

        elif lugar == 2:
            if matriz[0][2] == 2:
                matriz[0][2] = sinal


        elif lugar == 3:
            if matriz[0][4] == 3:
                matriz[0][4] = sinal
                lugar = 3

        elif lugar == 4:
            if matriz[1][0] == 4:
                matriz[1][0] = sinal
                lugar = 4

        elif lugar == 5:
            if matriz[1][2] == 5:
                matriz[1][2] = sinal
                lugar = 5

        elif lugar == 6:
            if matriz[1][4] == 6:
                matriz[1][4] = sinal
                lugar = 6

        elif lugar == 7:
            if matriz[2][0] == 7:
                matriz[2][0] = sinal
                lugar = 7

        elif lugar == 8:
            if matriz[2][2] == 8:
                matriz[2][2] = sinal
                lugar = 8

        elif lugar == 9:
            if matriz[2][4] == 9:
                matriz[2][4] = sinal
                lugar = 9

    
    return(lugar)
    

# Executa o tipo de rodada em que NÃO há um Player
def computador():
    global matriz
    global lugar
    lugar = 0 

    while lugar == 0:
        time.sleep(0.3)
        lugar = random.randint(1,9)
        if historico.count(lugar) > 0:
            lugar = 0

        if lugar == 1:
            if matriz[0][0] == 1:
                matriz[0][0] = 'O'
                lugar = 1

        elif lugar == 2:
            if matriz[0][2] == 2:
                matriz[0][2] = 'O'
                lugar = 2

        elif lugar == 3:
            if matriz[0][4] == 3:
                matriz[0][4] = 'O'
                lugar = 3

        elif lugar == 4:
            if matriz[1][0] == 4:
                matriz[1][0] = 'O'
                lugar = 4

        elif lugar == 5:
            if matriz[1][2] == 5:
                matriz[1][2] = 'O'
                lugar = 5

        elif lugar == 6:
            if matriz[1][4] == 6:
                matriz[1][4] = 'O'
                lugar = 6

        elif lugar == 7:
            if matriz[2][0] == 7:
                matriz[2][0] = 'O'
                lugar = 7

        elif lugar == 8:
            if matriz[2][2] == 8:
                matriz[2][2] = 'O'
                lugar = 8

        elif lugar == 9:
            if matriz[2][4] == 9:
                matriz[2][4] = 'O'
                lugar = 9
 
           
    return(lugar)
    

# Confere se algumas das maneiras de ganhar o jogo foi atinginda (por qualquer um dos jogadores)
def ganhou():
    global matriz
    
    if matriz[0][0] == 'X':
        if matriz[0][2] == 'X':
            if matriz[0][4] == 'X':
                return 1
        elif matriz[1][0] == 'X':
            if matriz[2][0] == 'X':
                return 1
        elif matriz[1][2] == 'X':
            if matriz[2][4] == 'X':
                return 1
    
    if matriz[0][0] == 'O':
        if matriz[0][2] == 'O':
            if matriz[0][4] == 'O':
                return 2
        elif matriz[1][0] == 'O':
            if matriz[2][0] == 'O':
                return 2
        elif matriz[1][2] == 'O':
            if matriz[2][4] == 'O':
                return 2

    if matriz[2][0] == 'X':
        if matriz[2][2] == 'X':
            if matriz[2][4] == 'X':
                return 1
    
    if matriz[2][0] == 'O':
        if matriz[2][2] == 'O':
            if matriz[2][4] == 'O':
                return 2

    if matriz[0][2] == 'X':
        if matriz[1][2] == 'X':
            if matriz[2][2] == 'X':
                return 1
    
    if matriz[0][2] == 'O':
        if matriz[1][2] == 'O':
            if matriz[2][2] == 'O':
                return 2

    if matriz[0][4] == 'X':
        if matriz[1][4] == 'X':
            if matriz[2][4] == 'X':
                return 1
    
    if matriz[0][4] == 'O':
        if matriz[1][4] == 'O':
            if matriz[2][4] == 'O':
                return 2
    
    if matriz[1][2] == 'X':
        if matriz[0][4] == 'X':
            if matriz[2][0] == 'X':
                return 1
        elif matriz[1][0] == 'X':
            if matriz[1][4] == 'X':
                return 1
    
    if matriz[1][2] == 'O':
        if matriz[0][4] == 'O':
            if matriz[2][0] == 'O':
                return 2
        elif matriz[1][0] == 'O':
            if matriz[1][4] == 'O':
                return 2

    return 0


main()
