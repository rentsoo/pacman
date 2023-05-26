if __name__ == '__main__':
    from random import randint
    from time import sleep
    from os import system
    import constantes
    tipo_pacman = True

    pos_pacman = [randint(0, constantes.TAM_TELA - 1), randint(0, constantes.TAM_TELA - 1)]
    pos_comida = [randint(0, constantes.TAM_TELA - 1), randint(0, constantes.TAM_TELA - 1)]

    while True:
        system('cls')

        for i in range(constantes.TAM_TELA):
            for j in range(constantes.TAM_TELA):
                if i == pos_pacman[0] and j == pos_pacman[1]:
                    if tipo_pacman:
                        print(constantes.PACMAN[0], end='')
                    else:
                        print(constantes.PACMAN[1], end='')
                if i == pos_comida[0] and j == pos_comida[1]:
                    print(constantes.COMIDA, end='')
                else:
                    print('.', end='')
            print()

        if pos_pacman[0] < pos_comida[0]:
            pos_pacman[0] += 1
        if pos_pacman[0] > pos_comida[0]:
            pos_pacman[0] -= 1
        elif pos_pacman[1] < pos_comida[1]:
            pos_pacman[1] += 1
        elif pos_pacman[1] > pos_comida[1]:
            pos_pacman[1] -= 1

        if pos_pacman == pos_comida:
            pos_comida = [randint(0, constantes.TAM_TELA - 1), randint(0, constantes.TAM_TELA - 1)]
        tipo_pacman = not tipo_pacman
        sleep(constantes.TEMPO)
