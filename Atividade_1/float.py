import random

lista = []
tamanho = 10000000

for _ in range(tamanho):
    elemento = round(random.uniform(1.0, 10000.0), 3)
    lista.append(elemento)


soma = 0
for elemento in lista:
    soma += elemento
