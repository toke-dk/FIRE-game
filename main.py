import pygame

(width, height) = (1000, 1000)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('FIRE spillet')

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
