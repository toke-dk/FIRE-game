import pygame

pygame.init()


def update_bar(screen, point):
    # dette er bare en test for at se om det virker
    point_max = 100
    point_min = -100
    x_unload = 270
    y_unload = 0
    x_load = 270
    point = 100

    if point_min >= point >= point_max():
        y_load = 20 - point

    elif point_min >= point:
        y_load = 50

    elif point_max <= point:
        y_load = 0

    unloadedbar = pygame.image.load("Billeder/unloadedbar.png")
    loadedbar = pygame.image.load("Billeder/loadedbar.png")
    unloadedbar_rect = unloadedbar.get_rect()
    loadedbar_rect = loadedbar.get_rect()

    loadedbar_rect.height = 800
    loadedbar_rect.width = 400
    loadedbar = pygame.transform.scale(loadedbar, (400, 800))
    print(loadedbar.get_width())

    unloadedbar_rect.height = 800
    unloadedbar_rect.width = 400
    unloadedbar = pygame.transform.scale(unloadedbar, (400, 800))
    print(unloadedbar.get_width())

    # set det fra dette link: https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (200, 15, 10))
    screen.blit(unloadedbar, (x_unload, y_unload))
    screen.blit(loadedbar, (x_load, y_load))
    pygame.display.update()



    pygame.display.flip()
