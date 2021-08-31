import pygame as pygame
import pygame.display as display
import pygame.event as event
import pygame.draw as draw

# Constantes
SCREEN_SIZE = (640,480)
AMARELO = (255,255,0)
ESP = 10

# Variáveis

# Inicializa o construtor
pygame.init()

# Define configurações da tela.
tela = display.set_mode(size=SCREEN_SIZE, flags=0, depth=0, display=0, vsync=0)

# Métodos
def cria_elemento():
    draw.line(tela, AMARELO, (320, 0), (600, 240), ESP)
    draw.line(tela, AMARELO, (320, 0), (40, 240), ESP)
    draw.rect(tela, AMARELO, ((40, 240), (560, 200)), ESP)
    display.update()

# Laço do jogo
while True:
    # 1 passo - Calcula as regras.

    # 2 passo - Pinta os elementos, faz o print.
    cria_elemento()


    # 3 passo controla os eventos.
    for e in event.get():
        if e.type == pygame.QUIT:
            exit()