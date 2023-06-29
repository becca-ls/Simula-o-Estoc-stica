import subprocess
import os
import pandas as pd


def exec():
    for _ in range(50):
        executar()



def executar():
    csvFiles = [csvFile for csvFile in os.listdir(
    ) if 'csv' in csvFile and 'collectSample' not in csvFile]
    print(csvFiles)


    for csvFile in csvFiles:
        df = pd.read_csv(csvFile)

        data_estats = {}

        data_estats["mean"] = df["delta"].mean()
        data_estats["std_deviation"] = df["delta"].std()
        
        df = pd.DataFrame(data = data_estats,index = [0])

        df.to_csv("dados_atividade.csv",index = false)

exec()
