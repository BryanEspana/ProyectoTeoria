import numpy as np

# Matriz de transición
T = np.array([
    [0.5, 0.5, 0,   0,   0,   0],
    [0,   0.5, 0.5, 0,   0,   0],
    [0,   0,   0.5, 0.5, 0,   0],
    [0,   0,   0,   0.5, 0.5, 0],
    [0,   0,   0,   0,   0.5, 0.5],
    [0,   0,   0,   0,   0,   1]
])

# Distribución de probabilidad inicial
p = np.array([1, 0, 0, 0, 0, 0])

# Multiplica la distribución de probabilidad por la matriz de transición 5 veces
for _ in range(5):
    p = p @ T

# Imprime las probabilidades
for i, prob in enumerate(p):
    print(f'La probabilidad de que la pelota caiga en el casillero {i+1} es {prob:.5f}')
