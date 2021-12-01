import pygame

pygame.init()


def update_bar(screen, point):
    # dette er bare en test for at se om det virker
    point_max = 100
    point_min = -100

    unloadedbar = pygame.image.load(
        r"C:\Users\sofus\FIRE-game\FIRE-game\Billeder\unloadedbar.png").convert_alpha()
    loadedbar = pygame.image.load(
        r"C:\Users\sofus\FIRE-game\FIRE-game\Billeder\loadedbar.png").convert_alpha()

    unloadedbar_rect = unloadedbar.get_rect()
    loadedbar_rect = loadedbar.get_rect()

    unloadedbar_rect.x = 100
    unloadedbar_rect.y = 200

    loadedbar_rect.x = 100
    loadedbar_rect.y = 200

    # set det fra dette link: https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (200, 15, 10))
    screen.blit(textsurface, (0,0))
    #if point_min >= point >= point_max():


    pygame.display.flip()
