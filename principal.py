from random import randint
from time import sleep
from os import system
import constantes

if __name__ == '__main__':
      
    tipo_pacman = True

    pos_pacman = [randint(0, constantes.TAM_TELA - 1), randint(0, constantes.TAM_TELA - 1)]
    pos_comida = [randint(0, constantes.TAM_TELA - 1), randint(0, constantes.TAM_TELA - 1)]

    while True:
        system('cls')

        for linha in range(constantes.TAM_TELA):
            for coluna in range(constantes.TAM_TELA):
                if linha == pos_pacman[0] and coluna == pos_pacman[1]:
                    if tipo_pacman:
                        print(constantes.PACMAN[0], end='')
                    else:
                        print(constantes.PACMAN[1], end='')
                elif linha == pos_comida[0] and coluna == pos_comida[1]:
                    print(constantes.COMIDA, end='')
                else:
                    print('.', end='')
            print()

        if pos_pacman[0] < pos_comida[0]:
            pos_pacman[0] += 1
        elif pos_pacman[0] > pos_comida[0]:
            pos_pacman[0] -= 1
        elif pos_pacman[1] < pos_comida[1]:
            pos_pacman[1] += 1
        elif pos_pacman[1] > pos_comida[1]:
            pos_pacman[1] -= 1

        if pos_pacman == pos_comida:
            pos_comida = [randint(0, constantes.TAM_TELA - 1), randint(0, constantes.TAM_TELA - 1)]
        tipo_pacman = not tipo_pacman
        sleep(constantes.TEMPO)
