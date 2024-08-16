import pygame
from pygame.locals import *

# inicializar pygame
pygame.init()

# configurar la resolución de pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('juego de prueba pproyecto')

# colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


# posición y tamaño del jugador
posicion = [10, 300]
player_size = 40

# velocidad del jugadorr
player_speed = 0.5


# posición y tamaño del enemigo
enemy_pos = [300, 0]
enemy_size = 80
enemy_speed = 1


# puntos del jugador
player_points = 10
font = pygame.font.SysFont("monospace", 12)

cross_points = 0

# estados del juego
running = True















# bucle principal del juego
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    # rellenar la pantalla con color blanco
    screen.fill(white)



    # obtener la tecla presionada
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and posicion[0] > 0:
        posicion[0] -= player_speed
    if keys[K_RIGHT] and posicion[0] < 800 - player_size:
        posicion[0] += player_speed
    if keys[K_UP] and posicion[1] > 0:
        posicion[1] -= player_speed
    if keys[K_DOWN] and posicion[1] < 600 - player_size:
        posicion[1] += player_speed




    # mover el enemigo
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > 600:
        enemy_pos[1] = 0



    # detectar colisión
    player_rect = pygame.Rect(posicion[0], posicion[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
    if player_rect.colliderect(enemy_rect):
        player_points -= 1
        enemy_pos[1] = 0  # reiniciar la posición del enemigo


    x = posicion[0]
    y = posicion[1]
    j = 800 - player_size




    # sistema de puntaje por cruzar de lado a lado
    if x >= j:
        cross_points += 1
        posicion[0] = 10  # reiniciar la posición del jugador
        posicion[1] = 300







   # dibujar el jugador
    pygame.draw.rect(screen, black, (posicion[0], posicion[1], player_size, player_size))


    # dibujar el enemigo
    pygame.draw.rect(screen, red, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))



 




    # mostrar los puntos
    points_text = font.render(f"Puntos: {player_points}", True, black)
    screen.blit(points_text, (10, 10))


    cross_points_text = font.render(f"Cruces: {cross_points}", True, black)
    screen.blit(cross_points_text, (10, 50))


    pos = "x=" + str(posicion[0]) + " y=" + str(posicion[1]) + " j=" + str(800 - player_size)
    posicion_jugador = font.render(f"pos_jugador: {pos}", True, black)
    screen.blit(posicion_jugador, (10, 90))


  

   # actualizar la pantalla
    pygame.display.flip()







# salir de pygame
pygame.quit()
