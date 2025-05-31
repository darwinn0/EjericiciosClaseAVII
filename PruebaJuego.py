import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 600
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa la Figura")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Fuente
fuente = pygame.font.SysFont(None, 48)

# Jugador (canasta)
jugador = pygame.Rect(250, 750, 100, 20)
velocidad_jugador = 10

# Figuras (objetos a atrapar)
figuras = []
velocidad_figura = 5

def nueva_figura():
    x = random.randint(0, ANCHO - 30)
    color = random.choice([ROJO, VERDE, AZUL])
    rect = pygame.Rect(x, 0, 30, 30)
    return (rect, color)

# Contador de puntos
puntaje = 0

# Generar primera figura
figuras.append(nueva_figura())

# Loop principal
corriendo = True
while corriendo:
    reloj.tick(60)
    VENTANA.fill(BLANCO)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += velocidad_jugador

    # Mover y dibujar figuras
    for figura in figuras[:]:
        rect, color = figura
        rect.y += velocidad_figura
        pygame.draw.rect(VENTANA, color, rect)

        # Colisión
        if rect.colliderect(jugador):
            figuras.remove(figura)
            puntaje += 1

        # Fuera de la pantalla
        elif rect.top > ALTO:
            figuras.remove(figura)

    # Añadir nuevas figuras de forma aleatoria
    if random.randint(1, 60) == 1:
        figuras.append(nueva_figura())

    # Dibujar jugador
    pygame.draw.rect(VENTANA, NEGRO, jugador)

    # Mostrar puntaje
    texto = fuente.render(f"Puntos: {puntaje}", True, NEGRO)
    VENTANA.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()