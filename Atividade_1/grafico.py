import pygame
import os
import datetime
import csv

csvFile = 'C:/Users/rls/Documents/estocástica/Atividade_1/executionTime_operacao_grafica.csv'
mode = 'a'  # read mode

if not os.path.exists(csvFile):
    mode = 'w'  # mode write if the file does not exist

def write(content: list[str], file):
    writer = csv.writer(file)
    if mode == 'w':
        writer.writerow([
            'start', 'end', 'delta'
        ])
    writer.writerow(content)

start = datetime.datetime.now()
# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movendo Imagem")

# Carregamento da imagem
imagem = pygame.image.load("C:/Users/rls/Documents/estocástica/Atividade_1/img.png")
posicao_x = 0
posicao_y = 0

# Loop principal do jogo
executando = 100
while executando:
    # Movimento da imagem
    posicao_x += 0.1
    posicao_y += 0.1
    if(posicao_x >500):
        posicao_x -= 600
        posicao_y -= 500
    if(posicao_y >500):
        posicao_x -= 500
        posicao_y -= 600

    # Preenchimento da tela com cor de fundo
    tela.fill((255, 255, 255))

    # Desenho da imagem na tela
    tela.blit(imagem, (posicao_x, posicao_y))

    # Atualização da tela
    pygame.display.flip()
    executando -=1

# Encerramento do Pygame
pygame.quit()

# Pos-processing

end = datetime.datetime.now()
delta = end - start

file = open(csvFile, mode)

write([str(data) for data in [start, end, delta]], file)
file.close()
