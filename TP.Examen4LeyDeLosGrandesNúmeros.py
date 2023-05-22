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

import numpy as np

# Número de pelotas a soltar en la máquina de Galton
N = 1000000

# Array para guardar en qué casillero cae cada pelota
casilleros = np.zeros(N, dtype=int)

# Para cada pelota
for i in range(N):
    # Caída de la pelota a través de los 5 niveles de clavos
    for _ in range(5):
        # Si el número aleatorio es menor que 0.5, se mueve a la derecha (aumenta el número del casillero)
        if np.random.rand() < 0.5:
            casilleros[i] += 1

# Contar cuántas pelotas caen en cada casillero
conteo_casilleros = np.bincount(casilleros, minlength=6)

# Calcula las probabilidades dividiendo por el número total de pelotas
probabilidades = conteo_casilleros / N

# Imprime las probabilidades
for i, prob in enumerate(probabilidades):
    print(f'La probabilidad de que la pelota caiga en el casillero {i+1} es {prob:.5f}')
