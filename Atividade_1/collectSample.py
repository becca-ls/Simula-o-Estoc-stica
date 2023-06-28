import subprocess

def executar():
    subprocess.call(['python', 'C:/Users/rls/Documents/estocástica/Atividade_1/inteiros.py'])

# Executa o script "inteiros.py" 2500 vezes
for _ in range(50):
    executar()
