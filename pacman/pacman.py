import pygame
import pygame.display as display
import pygame.event as event
import pygame.draw as draw

# Constantes
SCREEN_SIZE = (1280,768)
AMARELO = (255,255,0)
PRETO = (0,0,0)
VELOCIDADE = 1
RAIO = 30


# Variáveis
x = 10
y = 10
vel_x = VELOCIDADE
vel_y = VELOCIDADE


# Inicializa o construtor
pygame.init()

# Define configurações da tela.
tela = display.set_mode(size=SCREEN_SIZE, flags=1, depth=0, display=0, vsync=0)

# Laço do jogo
while True:
    # 1 passo - Calcula as regras.
    x += vel_x
    y += vel_y

    if x + RAIO > 1280:
        vel_x = -VELOCIDADE
    elif x - RAIO < 0: 
        vel_x = VELOCIDADE
    
    if y + RAIO > 768:
        vel_y = -VELOCIDADE
    elif y - RAIO < 0: 
        vel_y = VELOCIDADE


    # 2 passo - Pinta os elementos, faz o print.
    tela.fill(PRETO)
    draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)
    display.update()


    # 3 passo controla os eventos.
    for e in event.get():
        if e.type == pygame.QUIT:
            exit()