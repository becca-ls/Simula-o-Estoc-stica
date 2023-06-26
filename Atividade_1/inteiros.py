import random

lista = []
tamanho = 10000000

for _ in range(tamanho):
    elemento = random.randint(0,1000)
    lista.append(elemento)


soma = 0
for elemento in lista:
    soma += elemento
