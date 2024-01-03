import pygame

from snake import SnakePlayer

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
snake = SnakePlayer(50, 50, screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((110, 171, 130))
    snake.update()

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
