import pygame

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
executando = True
while executando:
    # Eventos do Pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

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

# Encerramento do Pygame
pygame.quit()
