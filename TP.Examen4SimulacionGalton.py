"""
Universidad del Valle de Guatemala
Teoría de Probabilidades
Examen #4
Problema #3

Bryan Carlos Roberto España Machorro - 21550
Javier Alejandro Prado Ramirez  - 21486
Joaquín André Puente Grajeda - 22296
Roberto Francisco Rios Morales - 20979
Alejandro José Martínez León- 21430
"""

from random import randint

def galton(h, b):
    """
    h: niveles del tablero
    b: cantidad de pelotas
    """
    containers = [0] * (h + 1)
    for _ in range(b):
        pos = 0
        for i in range(0, h):
            turn = randint(0, 1)
            if turn == 1:
                pos += 1
        containers[pos] = containers[pos] + 1

    return containers


def curva(containers):
    for val in containers:
        for _ in range(0, val):
            print('.', end='')
        print(val)




for i in range(10):
    containers = galton(h=5, b=100)
    print("\n")
    print(containers)
    curva(containers)
    print("\n")
