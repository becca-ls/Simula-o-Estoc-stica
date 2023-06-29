import random
import os
import datetime
import csv

csvFile = 'C:/Users/rls/Documents/estocástica/Atividade_1/executionTime_disco.csv'
mode = 'a'

def algorithm():

    frase = 'Este eh um arquivo de exemplo.'
    qtd = 500

    for _ in range(qtd):
        arquivo = open('C:/Users/rls/Documents/estocástica/Atividade_1/arquivo.txt', 'w')
        arquivo.write(frase+'\n')
        arquivo.close()

def write(content: list[str], file):
    writer = csv.writer(file)
    if mode == 'w':
        writer.writerow([
            'start', 'end', 'delta'
        ])
    writer.writerow(content)


def check_file():
    global mode
    if not os.path.exists(csvFile):
        mode = 'w'  # mode write if the file does not exist


def collect_sample():
    check_file()
    start = datetime.datetime.now()
    # Algorithm
    algorithm()
    # Pos-processing

    end = datetime.datetime.now()
    delta = end - start

    file = open(csvFile, mode)

    write([str(data) for data in [start, end, delta]], file)
    file.close()


collect_sample()
