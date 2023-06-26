import random
import numpy as np

matrizes = []
qtd_matrizes = 10000
linhas = 30
colunas = 30

for _ in range(qtd_matrizes):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range (colunas):
            elemento = random.randint(0,1000)
            linha.append(elemento)
        matriz.append(linha)
    matrizes.append(matriz)


# Multiplicação das matrizes
matriz_resultante = matrizes[0]
for matriz in matrizes[1:]:
    matriz_resultante = np.dot(matriz_resultante, matriz)
