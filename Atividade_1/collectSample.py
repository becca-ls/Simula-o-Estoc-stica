import subprocess
import os


def exec():
    for _ in range(2500):
        executar()


def executar():
    pyFiles = [pyFile for pyFile in os.listdir(
    ) if 'py' in pyFile and 'collectSample' not in pyFile]
    print(pyFiles)

    for pyFile in pyFiles:
        print("Running ", pyFile)
        subprocess.call(
            ['python', pyFile])

exec()
