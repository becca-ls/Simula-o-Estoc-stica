import random
import numpy as np
import os
import datetime
import csv

csvFile = 'C:/Users/rls/Documents/estocástica/Atividade_1/executionTime_matriz.csv'

mode = 'a'  # read mode
matrizes = []
qtd_matrizes = 10000
linhas = 30
colunas = 30

if not os.path.exists(csvFile):
    mode = 'w'  # mode write if the file does not exist


def write(content: list[str], file):
    writer = csv.writer(file)
    if mode == 'w':
        writer.writerow([
            'start', 'end', 'delta'
        ])
    writer.writerow(content)

for _ in range(qtd_matrizes):
    matriz = []
    for _ in range(linhas):
        linha = []
        for _ in range (colunas):
            elemento = random.randint(0,1000)
            linha.append(elemento)
        matriz.append(linha)
    matrizes.append(matriz)

start = datetime.datetime.now()


# Multiplicação das matrizes
matriz_resultante = matrizes[0]
for matriz in matrizes[1:]:
    matriz_resultante = np.dot(matriz_resultante, matriz)

# Pos-processing

end = datetime.datetime.now()
delta = end - start

file = open(csvFile, mode)

write([str(data) for data in [start, end, delta]], file)
file.close()
