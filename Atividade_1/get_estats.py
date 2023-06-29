import subprocess
import os
import pandas as pd

def executar():
    csvFiles = [csvFile for csvFile in os.listdir(
    ) if 'csv' in csvFile and 'collectSample' not in csvFile]
    print(csvFiles)

    data_estats = {"file_name":[],"mean":[],"std_deviation":[]}

    for csvFile in csvFiles:
        df = pd.read_csv(csvFile)

        data_estats["file_name"].append(csvFile)
        data_estats["mean"].append(df["delta"].mean())
        data_estats["std_deviation"].append(df["delta"].std())
        
    df = pd.DataFrame(data = data_estats)

    df.to_csv("dados_atividade.csv",index = False)

executar()
